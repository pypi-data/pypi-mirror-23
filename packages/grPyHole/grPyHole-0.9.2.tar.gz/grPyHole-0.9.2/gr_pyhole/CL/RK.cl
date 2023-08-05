/*
   Copyright 2015 - 2016 Alexander Wittig, Jai Grover

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

// RK device code specific header
#include "RK.h"
// load the available RK implementations
#include "RKF23.h"
#include "RKF45.h"
#include "RKF56.h"
#include "RKF67.h"
#include "RKF78.h"
#include "RKF89.h"

// load the right hand side (coordinate dependent) code
// this code also includes the user defined metric code (METRIC_CL) in the right place
#include RK_INCLUDE(RHS_CL)

// kernel to get the size (with padding) of an RKstate structure on this device. Also tests various RK settings for sanity. Used for host side sanity checking
kernel void RKtest( global int* restrict result )
{
    RKstate st;
    const ulong s = (long)&st;
    result[0] = sizeof(RKstate);
    result[1] = ((ulong)&st.err - s) + sizeof(st.err);
    result[2] = sizeof(RKstate) - result[1];
    result[3] = (RK_fmin >  0.0) && (RK_fmin <= 1.0);
    result[4] = (RK_fmax >= 1.0);
    result[5] = (RK_hmin >  0.0) && (RK_hmin <= RK_hmax);
    result[6] = (RK_terr >  0.0) && (RK_terr <= RK_merr);
    result[7] = (RK_bsf  >  0.0) && (RK_bsf < 1.0);
    result[8] = all( RK_errw >= (real)0.0 );
}

// kernel to set up the initial conditions in *states based on viewing directions
// states[].x is assumed to be a 6 component vector with the spherical position plus the alpha and beta viewing angles
// tf and hh are the maximum integration time and initial step size guess
kernel __attribute__((vec_type_hint(realV))) void RKinit( global RKstate* restrict states, real tf, real hh USER_ARGS_DEF )
{
    const int igid = get_global_id( 0 );

    states[igid].x = getMomenta( states[igid].x USER_ARGS );
    states[igid].t = 0.0;
    states[igid].tf = tf;
    states[igid].err = 0.0;
    states[igid].h = fabs(hh);
}

// kernel to step the integrator forward by (at most) RK_nsteps
kernel __attribute__((vec_type_hint(realV))) void RKsteps( global RKstate* restrict states, global int* restrict idx USER_ARGS_DEF )
{
    const int igid = idx[get_global_id( 0 )];
    if( igid < 0 ) return;
    realV x = states[igid].x;
    real t = states[igid].t;
    const real tf = states[igid].tf;
    real toterr = states[igid].err;
    float f_max = RK_fmax;
    bool done = false;
    bool RHSerror = false;
    bool finishing = false;
    real hh = clamp( fabs( states[igid].h ), RK_hmin, RK_hmax );               // Reinitialize with last step size
    real h = clamp( tf-t, -hh, hh );                // first step is always a full step for the moment

    uint ns;
    for( ns = RK_nsteps; !done && (ns > 0); ns-- )
//    for( uint ns = RK_nsteps; !done && (ns > 0); ns-- )
    {
        realV k[RK_stages];
        RHSerror = RHS( t, x, &k[0] USER_ARGS );
        k[0] *= h;
        realV x1 = RK_b1[0]*k[0];
        realV xerr = RK_d[0]*k[0];

        // Manual loop unrolling is ugly but saves a whooping factor of 2 in computation speed
        // With this, all branches are eliminated in the assembly of AMDAPP 3.0
        #define RKSTEPLOOP(i) \
        { \
            realV xx = x + RK_a[ib++]*k[0]; \
            for( uint j = 1; j < i; j++ ) \
                xx += RK_a[ib++]*k[j]; \
            RHSerror = RHS( t + h*RK_c[i], xx, &k[i] USER_ARGS ) || RHSerror; \
            k[i] *= h; \
            x1 += RK_b1[i]*k[i]; \
            xerr += RK_d[i]*k[i]; \
        }
        {
            uint ib = 0;
            REPEAT( RKSTEPLOOP, RK_stages )
        }

        const real err = RK_ERROR( xerr, x1, x );
        const bool success = (err < RK_merr) && !RHSerror;    // was this a successful step
        const bool accept = success || ((hh <= RK_hmin) && !RHSerror);       // is this step accepted
        x += accept ? x1 : (realV)(0.0);
        t += accept ? h : (real)(0.0);
        toterr += accept ? err : (real)(0.0);
        //x += accept*x1;       // this causes newer AMD graphics drivers to hard-fail with
                                // Error in hsa_code section, at offset 35000:
                                // Instruction has invalid rounding (default), expected: none
                                // LLVM ERROR:
                                // Brig container validation has failed in BRIGAsmPrinter.cpp
        //t += accept*h;
        //toterr += ((uint)accept)*err;

        // hack to count pr turning points
//        RHS( t, x, &k[1] USER_ARGS );
//        x.sd += (accept && (k[0].s1*h*k[1].s1)<=0.0) ? 1.0 : 0.0;

        // compute next step
        const float fact = success ? clamp( rootn( RK_terr/(float)err, RK_order ), RK_fmin, f_max ) : RK_bsf;
        f_max = success ? fmin( f_max*1.2f, RK_fmax ) : 1.0f;   // relax restriction on stepsize increase, but if backstep force back to no increase
        hh = clamp( hh*fact, RK_hmin, RK_hmax ); // new absolute maximum step size

        // actual new stepsize ("if" here to avoid calling RHS all the time)
        if( finishing || RADIUS(x) > 0.95*RSKY )
        {
            finishing = true;
            realV y;
            done = RHS( t, x, &y USER_ARGS );      // if there's an error in RHS here, we're done.
            RHSerror = RHSerror || done;
            h = 0.95*(RSKY - RADIUS( x ))/RADIAL_VELOCITY( x, y );
        }
        else
        {
            h = tf-t;
        }
        h = clamp( h, -hh, hh );

        // We're done if there was an error, or if we're close enough to the celestial sphere, or if we're out of time
        done = done || RHSerror || (fabs( RSKY - RADIUS( x ) ) < (real)1e-2) || (fabs( tf-t ) <= EPS);
    }

    const real nc = getNullCondition( x USER_ARGS );     // compute null condition for this state
#if DIM>8
    x.sf = nc;
//    x.se += RK_nsteps-ns;
#endif

    const bool ncbad = fabs(nc) > NCMAX;    // was the null condition violated?
    done = done || ncbad;                   // if null condition violation is too large, we're done
    states[igid].x = x;
    states[igid].t = t;
    states[igid].err = toterr;
    states[igid].h = RHSerror ? -1.0 : (fabs( tf-t ) <= EPS ? -2.0 : (ncbad ? -3.0 : hh));	// reason for finishing: -1 = RHSerror, -2 = out of time, -3 = integrator error (i.e. null condition too large), otherwise step size limit hh
    idx[get_global_id( 0 )] = done ? -igid-1 : igid;    // flip sign and subtract one if we are done
}

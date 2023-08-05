/* Spherical metric in Herdeiro-Radu form. */

// The user arguments to be passed down from the kernel
// Note that the leading comma is absolutely required!
// USER_ARGS_DEF must be such that:
// void func( int x, int g USER_ARGS_DEF )
// expands to a valid function definition
#define USER_ARGS_DEF , read_only image2d_t img, read_only image2d_t dX_img, read_only image2d_t dth_img
// USER_ARGS must be such that:
// func( 1, 2 USER_ARGS )
// expands to a valid function call when used inside a function with USER_ARGS_DEF in its function list
#define USER_ARGS , img, dX_img, dth_img


// declare the sampler used for the interpolation (must be done in program scope according to OpenCL 2.0 Spec pg. 51)
#if FIX_SAMPLER==1
// Implement our own linear interpolation sampler. This works around broken implementations in various GPUs and CPUs.
constant sampler_t sampler = CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST | CLK_NORMALIZED_COORDS_FALSE;

inline float4 my_read_imagef( read_only image2d_t img, const sampler_t sampler, float2 x_img )
{
    x_img -= 0.5f;
    const float2 i0 = floor( x_img );
    const float2 a = x_img - i0;
    return (1.0f - a.x)*(1.0f - a.y)*read_imagef( img, sampler, i0 )
         + a.x*(1.0f - a.y)*read_imagef( img, sampler, i0+(float2)(1.0, 0.0) )
         + (1.0f - a.x)*a.y*read_imagef( img, sampler, i0+(float2)(0.0, 1.0) )
         + a.x*a.y*read_imagef( img, sampler, i0+(float2)(1.0, 1.0) );
}
#else
// use built in linear interpolation
constant sampler_t sampler = CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_LINEAR | CLK_NORMALIZED_COORDS_FALSE;
#define my_read_imagef( img, sampler, x_img ) read_imagef( img, sampler, x_img )
#endif

// Convert radius r into rescaled variable X used in the interpolation function and its derivative dX/dr.
inline real2 getX( const real r )
{
    const real xx = sqrt( r*r - EH*EH );
    const real tmp = xx + 1.0;
    return (real2)(xx/tmp, r/(xx*tmp*tmp));
}

// Compute the components of the metric at x and store them in the metric g.
bool updateMetric( const realV x, metric* restrict g USER_ARGS_DEF )
{
    // ugly but ~2% faster than using "const real r = x.s1;" etc. instead of define
    #define r (x.s1)
    const real theta = maxmag( x.s2, (real)1e-7 );     // prevent coordinate singularity
    //#define theta (x.s2)

    // interpolate and take derivatives
    const real2 XX = getX( r );
    #define X (XX.s0)
    #define dr (XX.s1)
    const float2 x_img = (float2)((NX-1)*X, (NTHETA-1)/PI*theta)+0.5f;    // for normalized coordinates add /NX and /NTHETA

    const real4 pnt = convert_real4( my_read_imagef( img, sampler, x_img ) );
    #define F0 (pnt.s0)
    #define F1 (pnt.s1)
    #define F2 (pnt.s2)
    #define W  (pnt.s3)

    const real4 dr_pnt = dr*convert_real4( my_read_imagef( dX_img, sampler, x_img ) );
    #define dr_F0 (dr_pnt.s0)
    #define dr_F1 (dr_pnt.s1)
    #define dr_F2 (dr_pnt.s2)
    #define dr_W  (dr_pnt.s3)

    const real4 dth_pnt = convert_real4( my_read_imagef( dth_img, sampler, x_img ) );
    #define dth_F0 (dth_pnt.s0)
    #define dth_F1 (dth_pnt.s1)
    #define dth_F2 (dth_pnt.s2)
    #define dth_W  (dth_pnt.s3)

    // some common terms for reuse
    const real3 expvec = exp( ((real)(-2.0))*pnt.s012 );  // vectorized exponentiation
    #define eF0 (expvec.s0)
    #define eF1 (expvec.s1)
    #define eF2 (expvec.s2)

    const real r_inv = 1.0/r;
    const real r2_inv = r_inv*r_inv;
    const real N = 1.0 - EH*r_inv;
    const real dr_N_Ninv = r2_inv*EH/N;

    const real t1 = eF0/N;
    real cost;
    const real sint_inv = 1.0/sincos( theta, &cost );
    const real t2 = r2_inv*eF2*sint_inv*sint_inv;
    const real t3 = r2_inv*eF1;

    // calculate actual contravariant metric
    g->tt = -t1;
    g->rr = N*eF1;
    g->thth = t3;
    g->pp = t2 - W*W*t1;
    g->tp = -W*t1;

    g->dr_tt = (2.0*dr_F0 + dr_N_Ninv)*t1;
    g->dr_rr = (r2_inv*EH - 2.0*dr_F1*N)*eF1;
    g->dr_thth = -2.0*(r_inv + dr_F1)*t3;
    g->dr_pp = -2.0*((dr_F2 + r_inv)*t2 - (dr_F0*W - dr_W)*W*t1) + dr_N_Ninv*W*W*t1;
    g->dr_tp = ((2.0*dr_F0  + dr_N_Ninv)*W - dr_W)*t1;

    g->dth_tt = 2.0*dth_F0*t1;
    g->dth_rr = -2.0*dth_F1*N*eF1;
    g->dth_thth = -2.0*dth_F1*t3;
    g->dth_pp = -2.0*((dth_F2 + cost*sint_inv)*t2 + (dth_W - dth_F0*W)*W*t1);
    g->dth_tp = (2.0*dth_F0*W - dth_W)*t1;

    // check if fallen in.
    return r<RCUTOFF;

    #undef r
    //#undef theta
    #undef X
    #undef dr
    #undef F0
    #undef F1
    #undef F2
    #undef W
    #undef dr_F0
    #undef dr_F1
    #undef dr_F2
    #undef dr_W
    #undef dth_F0
    #undef dth_F1
    #undef dth_F2
    #undef dth_W
    #undef eF0
    #undef eF1
    #undef eF2
}

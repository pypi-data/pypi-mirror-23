// structure to hold components of the spherical metric
// must be defined before including the user defined metric
typedef struct _metric {
    real tt;
    real rr;
    real thth;
    real pp;
    real tp;

    real dr_tt;
    real dr_rr;
    real dr_thth;
    real dr_pp;
    real dr_tp;

    real dth_tt;
    real dth_rr;
    real dth_thth;
    real dth_pp;
    real dth_tp;
} metric;

// include the user defined metric function which also sets the additional user
// arguments etc. used below
#include RK_INCLUDE(METRIC_CL)

// check if the metric didn't define any user arguments and set them to empty (i.e. none)
#ifndef USER_ARGS
#define USER_ARGS
#endif

#ifndef USER_ARGS_DEF
#define USER_ARGS_DEF
#endif

// Compute the momenta from a viewing direction
inline realV getMomenta( const realV x USER_ARGS_DEF )
{
    metric g;
    updateMetric( x, &g USER_ARGS );    // result is ignored
    const real sa = sin( x.s4 );
    const real ca = cos( x.s4 );
    const real sb = sin( x.s5 );
    const real cb = cos( x.s5 );

    // covariant
    const real det = 1.0/(g.tt*g.pp-g.tp*g.tp);      // covariant determinant
    const real g_rr = 1.0/g.rr;
    const real g_thth = 1.0/g.thth;
    const real g_pp = det*g.tt;
    const real g_tp = -det*g.tp;

    realV res = (realV)(0.0);
    res.s0123 = x.s0123;    // first 4 components are the same
    res.s4 = -sqrt(-det/g_pp) - sa*cb*g_tp/sqrt(g_pp);
    res.s5 = ca*sqrt(g_rr);
    res.s6 = -sa*sb*sqrt(g_thth);
    res.s7 = -sa*cb*sqrt(g_pp);

    return res;
}

// compute the radius from a given state x
#define RADIUS(x) (x.s1)

// compute the radial velocity at state x and y=RHS(x)
#define RADIAL_VELOCITY(x, y) (y.s1)

/* Right hand side of the ODE for propagation.

   :param t: Independent integration variable (lambda).
   :param x: Point where to evaluate the RHS.
   :param y: Pointer to the result of the RHS evaluation.
   :param : Any user defined extra function arguments
   :return: error status that is true if there has been an error.
*/
inline bool RHS( const real t, const realV x, realV* restrict y USER_ARGS_DEF )
{
    metric g;
    const bool error = updateMetric( x, &g USER_ARGS );

    *y = (realV)(0.0);
    (*y).s0 = x.s4*g.tt+x.s7*g.tp;      // ugly (*y). notation is because AMD OpenCL doesn't like y->
    (*y).s1 = x.s5*g.rr;
    (*y).s2 = x.s6*g.thth;
    (*y).s3 = x.s7*g.pp+x.s4*g.tp;
    //(*y).s4 = 0.0;         // already initialized to zero
    (*y).s5 = -0.5*(x.s4*x.s4*g.dr_tt +x.s5*x.s5*g.dr_rr +x.s6*x.s6*g.dr_thth +x.s7*x.s7*g.dr_pp) -x.s4*x.s7*g.dr_tp;
    (*y).s6 = -0.5*(x.s4*x.s4*g.dth_tt+x.s5*x.s5*g.dth_rr+x.s6*x.s6*g.dth_thth+x.s7*x.s7*g.dth_pp)-x.s4*x.s7*g.dth_tp;
    //(*y).s7 = 0.0;
#if DIM>8
    (*y).s8 = (*y).s3;
    (*y).s9 = fabs( (*y).s3 );
#endif
    return error;
}

// Compute the null condition (i.e. g_ij * p^i * p^j)
inline real getNullCondition( const realV x USER_ARGS_DEF )
{
    metric g;
    const bool error = updateMetric( x, &g USER_ARGS );
    return error ? NAN : 0.5*(x.s4*x.s4*g.tt+x.s5*x.s5*g.rr+x.s6*x.s6*g.thth+x.s7*x.s7*g.pp)+x.s4*x.s7*g.tp;
}

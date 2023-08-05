// structure to hold components of the spherical metric
// must be defined before including the user defined metric
typedef struct _metric {
    real tt;
    real tx;
    real ty;
    real xx;
    real xy;
    real xz;
    real yy;
    real yz;
    real zz;

    real dx_tt;
    real dx_tx;
    real dx_ty;
    real dx_xx;
    real dx_xy;
    real dx_xz;
    real dx_yy;
    real dx_yz;
    real dx_zz;

    real dy_tt;
    real dy_tx;
    real dy_ty;
    real dy_xx;
    real dy_xy;
    real dy_xz;
    real dy_yy;
    real dy_yz;
    real dy_zz;

    real dz_tt;
    real dz_tx;
    real dz_ty;
    real dz_xx;
    real dz_xy;
    real dz_xz;
    real dz_yy;
    real dz_yz;
    real dz_zz;
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
    const real st = sin( x.s2 );
    const real ct = cos( x.s2 );
    const real sp = sin( x.s3 );
    const real cp = cos( x.s3 );
    const real sa = sin( x.s4 );
    const real ca = cos( x.s4 );
    const real sb = sin( x.s5 );
    const real cb = cos( x.s5 );
    const real r = x.s1;

    realV res = (realV)(0.0);
    res.s0123 = (real4)(x.s0, st*cp*r, st*sp*r, ct*r);

    metric g;
    const bool error = updateMetric( res, &g USER_ARGS );

    // get contravariant spherical (hat) from contravariant cartesian
    const real gtt = g.tt;
    const real gtp = -sp*g.tx + cp*g.ty;        // wiggle
    const real grr = st*st*cp*cp*g.xx + st*st*sp*sp*g.yy + ct*ct*g.zz + 2.0*st*st*sp*cp*g.xy + 2.0*st*ct*cp*g.xz + 2.0*st*ct*sp*g.yz;
    const real gthth = (ct*ct*cp*cp*g.xx + ct*ct*sp*sp*g.yy + st*st*g.zz + 2.0*ct*ct*sp*cp*g.xy - 2.0*st*ct*cp*g.xz - 2.0*st*ct*sp*g.yz)/(r*r);
    const real gpp = sp*sp*g.xx+cp*cp*g.yy-2.0*sp*cp*g.xy;       // wiggle
    const real det = 1.0/(gtt*gpp-gtp*gtp);     // wiggle, covariant determinant
    // compute momenta
    res.s4 = -1.0/sqrt(-gtt) + sa*cb*gtp/sqrt(det/gtt);
    res.s5 = st*cp*ca/sqrt(grr) + sp*sa*cb*sqrt(gtt*det) - ct*cp*sa*sb/(r*sqrt(gthth));
    res.s6 = st*sp*ca/sqrt(grr) + cp*sa*cb*sqrt(gtt*det) - ct*sp*sa*sb/(r*sqrt(gthth));
    res.s7 = ct*ca/sqrt(grr) + st*sa*sb/(r*sqrt(gthth));

    return res;
}

// compute the radius from a given state x
#define RADIUS(x) (length(x.s123))

// compute the radial velocity at state x and y=RHS(x)
#define RADIAL_VELOCITY(x, y) (dot(normalize(x.s123),y.s123))

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
    (*y).s0 = g.tt*x.s4 + g.tx*x.s5 + g.ty*x.s6;
    (*y).s1 = g.tx*x.s4 + g.xx*x.s5 + g.xy*x.s6 + g.xz*x.s7;
    (*y).s2 = g.ty*x.s4 + g.xy*x.s5 + g.yy*x.s6 + g.yz*x.s7;
    (*y).s3 = g.xz*x.s5 + g.yz*x.s6 + g.zz*x.s7;
    //(*y).s4 = 0.0;
    (*y).s5 = -0.5*(g.dx_tt*x.s4*x.s4 + 2.0*g.dx_tx*x.s4*x.s5 + 2.0*g.dx_ty*x.s4*x.s6 + g.dx_xx*x.s5*x.s5 + g.dx_yy*x.s6*x.s6 + g.dx_zz*x.s7*x.s7 + 2.0*g.dx_xy*x.s5*x.s6 + 2.0*g.dx_xz*x.s5*x.s7 + 2.0*g.dx_yz*x.s6*x.s7);
    (*y).s6 = -0.5*(g.dy_tt*x.s4*x.s4 + 2.0*g.dy_tx*x.s4*x.s5 + 2.0*g.dy_ty*x.s4*x.s6 + g.dy_xx*x.s5*x.s5 + g.dy_yy*x.s6*x.s6 + g.dy_zz*x.s7*x.s7 + 2.0*g.dy_xy*x.s5*x.s6 + 2.0*g.dy_xz*x.s5*x.s7 + 2.0*g.dy_yz*x.s6*x.s7);
    (*y).s7 = -0.5*(g.dz_tt*x.s4*x.s4 + 2.0*g.dz_tx*x.s4*x.s5 + 2.0*g.dz_ty*x.s4*x.s6 + g.dz_xx*x.s5*x.s5 + g.dz_yy*x.s6*x.s6 + g.dz_zz*x.s7*x.s7 + 2.0*g.dz_xy*x.s5*x.s6 + 2.0*g.dz_xz*x.s5*x.s7 + 2.0*g.dz_yz*x.s6*x.s7);
#if DIM>8
    (*y).s8 = ((*y).s2*x.s1-(*y).s1*x.s2)/fmax( (real)0.01, x.s1*x.s1+x.s2*x.s2 );      // dphi/dlambda, with protection to prevent divisions by small numbers (when closer than 0.01 to axis)
    (*y).s9 = fabs( (*y).s8 );     // |dphi/dlambda|
#endif

    return error;
}

// Compute the null condition (i.e. g_ij * p^i * p^j)
inline real getNullCondition( const realV x USER_ARGS_DEF )
{
    metric g;
    bool error = updateMetric( x, &g USER_ARGS );
    return error ? NAN : 0.5*g.tt*x.s4*x.s4 + g.tx*x.s4*x.s5 + g.ty*x.s4*x.s6 + 0.5*g.xx*x.s5*x.s5 + 0.5*g.yy*x.s6*x.s6 + 0.5*g.zz*x.s7*x.s7 + g.xy*x.s5*x.s6 + g.xz*x.s5*x.s7 + g.yz*x.s6*x.s7;
}

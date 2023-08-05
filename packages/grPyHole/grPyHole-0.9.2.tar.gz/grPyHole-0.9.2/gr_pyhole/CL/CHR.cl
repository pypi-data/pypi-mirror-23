/* Cartesian metric in Herdeiro-Radu form. */

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
bool updateMetric( const realV xx, metric* restrict g USER_ARGS_DEF )
{
    // calculate actual contravariant metric
    #define x (xx.s1)
    #define y (xx.s2)
    #define z (xx.s3)
    const real3 xyz2 = xx.s123*xx.s123;
    #define x2 (xyz2.s0)
    #define y2 (xyz2.s1)
    #define z2 (xyz2.s2)
    const real r2 = x2+y2+z2;
    const real r = sqrt( r2 );
    const real rp2 = x2+y2;
    const real rp4 = rp2*rp2;
    const real rp = sqrt( rp2 );
    const real theta = acos( z/r );

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
    const real3 expvec = exp( ((real)(2.0))*pnt.s012 );  // vectorized exponentiation
    #define eF0 (expvec.s0)
    #define eF1 (expvec.s1)
    #define eF2 (expvec.s2)

    // partials for coordinate change in derivative
    const real3 drdxyz = xx.s123/r;
    #define drdx (drdxyz.s0)
    #define drdy (drdxyz.s1)
    #define drdz (drdxyz.s2)
    const bool cond = rp < EPS_RP;
    const real dthdx = cond ? 0.0 : z*x/(r2*rp);
    const real dthdy = cond ? 0.0 : z*y/(r2*rp);
    const real rp2inv = cond ? 0.0 : 1.0/rp2;        // we adjust explicitly in the equations below where the limit of terms involving rp2inv or rp4inv is non-zero
    const real rp4inv = cond ? 0.0 : 1.0/rp4;
    const real dthdz = -rp/r2;
    const real3 dthdxyz = (real3)(dthdx, dthdy, dthdz);

    // change derivatives wrt (x, y, z)
    const real3 dxyz_F0 = drdxyz*dr_F0 + dthdxyz*dth_F0;
    #define dx_F0 (dxyz_F0.s0)
    #define dy_F0 (dxyz_F0.s1)
    #define dz_F0 (dxyz_F0.s2)
    const real3 dxyz_F1 = drdxyz*dr_F1 + dthdxyz*dth_F1;
    #define dx_F1 (dxyz_F1.s0)
    #define dy_F1 (dxyz_F1.s1)
    #define dz_F1 (dxyz_F1.s2)
    const real3 dxyz_F2 = drdxyz*dr_F2 + dthdxyz*dth_F2;
    #define dx_F2 (dxyz_F2.s0)
    #define dy_F2 (dxyz_F2.s1)
    #define dz_F2 (dxyz_F2.s2)
    const real3 dxyz_W = drdxyz*dr_W + dthdxyz*dth_W;
    #define dx_W (dxyz_W.s0)
    #define dy_W (dxyz_W.s1)
    #define dz_W (dxyz_W.s2)

    // more useful constants
    const real N = 1.0 - EH/r;
    const real N2 = N*N;
    const real W2 = W*W;
    const real dr_N = EH/r2;
    const real3 dxyz_N = drdxyz*dr_N;
    #define dx_N (dxyz_N.s0)
    #define dy_N (dxyz_N.s1)
    #define dz_N (dxyz_N.s2)

    // calculate actual contravariant metric
    g->tt = -1.0/(eF0*N);
    g->tx = (y*W)/(eF0*N);
    g->ty = -(x*W)/(eF0*N);
    g->xx = (x2/eF1 + y2/eF2)*rp2inv + (x2*(-1.0 + N))/(eF1*r2) - (y2*W2)/(eF0*N);
    g->yy = (x2/eF2 + y2/eF1)*rp2inv + (y2*(-1.0 + N))/(eF1*r2) - (x2*W2)/(eF0*N);
    g->xy = ((1.0/eF1 - 1.0/eF2)*x*y)*rp2inv + (x*y*(-1.0 + N))/(eF1*r2) + (x*y*W2)/(eF0*N);
    // adjust for missing limit involving rp2inv in expressions above
    g->xx += cond ? 1.0/eF1 : 0.0;
    g->yy += cond ? 1.0/eF1 : 0.0;
    g->zz = 1.0/eF1 + (z2*(-1.0 + N))/(eF1*r2);
    g->xz = (x*z*(-1.0 + N))/(eF1*r2);
    g->yz = (y*z*(-1.0 + N))/(eF1*r2);

    g->dx_tt = (2.0*dx_F0)/(eF0*N) + dx_N/(eF0*N2);
    g->dx_tx = (-2.0*y*W*dx_F0)/(eF0*N) - (y*W*dx_N)/(eF0*N2) + (y*dx_W)/(eF0*N);
    g->dx_ty = -(W/(eF0*N)) + (2.0*x*W*dx_F0)/(eF0*N) + (x*W*dx_N)/(eF0*N2) - (x*dx_W)/(eF0*N);
    g->dx_xx = (x2*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (-2.0*x*(x2/eF1 + y2/eF2))*rp4inv + (2.0*x*(-1.0 + N))/(eF1*r2) + (2.0*y2*W2*dx_F0)/(eF0*N) - (2.0*x2*(-1.0 + N)*dx_F1)/(eF1*r2) + ((2.0*x)/eF1 - (2.0*x2*dx_F1)/eF1 - (2.0*y2*dx_F2)/eF2)*rp2inv + (x2*dx_N)/(eF1*r2) + (y2*W2*dx_N)/(eF0*N2) - (2.0*y2*W*dx_W)/(eF0*N);
    g->dx_yy = (y2*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (-2.0*x*(x2/eF2 + y2/eF1))*rp4inv - (2.0*x*W2)/(eF0*N) + (2.0*x2*W2*dx_F0)/(eF0*N) - (2.0*y2*(-1.0 + N)*dx_F1)/(eF1*r2) + ((2.0*x)/eF2 - (2.0*y2*dx_F1)/eF1 - (2.0*x2*dx_F2)/eF2)*rp2inv + (y2*dx_N)/(eF1*r2) + (x2*W2*dx_N)/(eF0*N2) - (2.0*x2*W*dx_W)/(eF0*N);
    g->dx_xy = (x*y*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (-2.0*(1.0/eF1 - 1.0/eF2)*x2*y)*rp4inv + ((1.0/eF1 - 1.0/eF2)*y)*rp2inv + (y*(-1.0 + N))/(eF1*r2) + (y*W2)/(eF0*N) - (2.0*x*y*W2*dx_F0)/(eF0*N) - (2.0*x*y*(-1.0 + N)*dx_F1)/(eF1*r2) + (x*y*((-2.0*dx_F1)/eF1 + (2.0*dx_F2)/eF2))*rp2inv + (x*y*dx_N)/(eF1*r2) - (x*y*W2*dx_N)/(eF0*N2) + (2.0*x*y*W*dx_W)/(eF0*N);
    g->dx_zz = (z2*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (-2.0*dx_F1)/eF1 - (2.0*z2*(-1.0 + N)*dx_F1)/(eF1*r2) + (z2*dx_N)/(eF1*r2);
    g->dx_xz = (x*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (z*(-1.0 + N))/(eF1*r2) - (2.0*x*z*(-1.0 + N)*dx_F1)/(eF1*r2) + (x*z*dx_N)/(eF1*r2);
    g->dx_yz = (y*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdx/r) + (-2.0*y*z*(-1.0 + N)*dx_F1)/(eF1*r2) + (y*z*dx_N)/(eF1*r2);

    g->dy_tt = (2.0*dy_F0)/(eF0*N) + dy_N/(eF0*N2);
    g->dy_tx = W/(eF0*N) - (2.0*y*W*dy_F0)/(eF0*N) - (y*W*dy_N)/(eF0*N2) + (y*dy_W)/(eF0*N);
    g->dy_ty = (2.0*x*W*dy_F0)/(eF0*N) + (x*W*dy_N)/(eF0*N2) - (x*dy_W)/(eF0*N);
    g->dy_xx = (x2*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (-2.0*y*(x2/eF1 + y2/eF2))*rp4inv - (2.0*y*W2)/(eF0*N) + (2.0*y2*W2*dy_F0)/(eF0*N) - (2.0*x2*(-1.0 + N)*dy_F1)/(eF1*r2) + ((2.0*y)/eF2 - (2.0*x2*dy_F1)/eF1 - (2.0*y2*dy_F2)/eF2)*rp2inv + (x2*dy_N)/(eF1*r2) + (y2*W2*dy_N)/(eF0*N2) - (2.0*y2*W*dy_W)/(eF0*N);
    g->dy_yy = (y2*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (-2.0*y*(x2/eF2 + y2/eF1))*rp4inv + (2.0*y*(-1.0 + N))/(eF1*r2) + (2.0*x2*W2*dy_F0)/(eF0*N) - (2.0*y2*(-1.0 + N)*dy_F1)/(eF1*r2) + ((2.0*y)/eF1 - (2.0*y2*dy_F1)/eF1 - (2.0*x2*dy_F2)/eF2)*rp2inv + (y2*dy_N)/(eF1*r2) + (x2*W2*dy_N)/(eF0*N2) - (2.0*x2*W*dy_W)/(eF0*N);
    g->dy_xy = (x*y*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (-2.0*(1.0/eF1 - 1.0/eF2)*x*y2)*rp4inv + ((1.0/eF1 - 1.0/eF2)*x)*rp2inv + (x*(-1.0 + N))/(eF1*r2) + (x*W2)/(eF0*N) - (2.0*x*y*W2*dy_F0)/(eF0*N) - (2.0*x*y*(-1.0 + N)*dy_F1)/(eF1*r2) + (x*y*((-2.0*dy_F1)/eF1 + (2.0*dy_F2)/eF2))*rp2inv + (x*y*dy_N)/(eF1*r2) - (x*y*W2*dy_N)/(eF0*N2) + (2.0*x*y*W*dy_W)/(eF0*N);
    g->dy_zz = (z2*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (-2.0*dy_F1)/eF1 - (2.0*z2*(-1.0 + N)*dy_F1)/(eF1*r2) + (z2*dy_N)/(eF1*r2);
    g->dy_xz = (x*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (-2.0*x*z*(-1.0 + N)*dy_F1)/(eF1*r2) + (x*z*dy_N)/(eF1*r2);
    g->dy_yz = (y*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdy/r) + (z*(-1.0 + N))/(eF1*r2) - (2.0*y*z*(-1.0 + N)*dy_F1)/(eF1*r2) + (y*z*dy_N)/(eF1*r2);

    g->dz_tt = (2.0*dz_F0)/(eF0*N) + dz_N/(eF0*N2);
    g->dz_tx = (-2.0*y*W*dz_F0)/(eF0*N) - (y*W*dz_N)/(eF0*N2) + (y*dz_W)/(eF0*N);
    g->dz_ty = (2.0*x*W*dz_F0)/(eF0*N) + (x*W*dz_N)/(eF0*N2) - (x*dz_W)/(eF0*N);
    g->dz_xx = (x2*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (2.0*y2*W2*dz_F0)/(eF0*N) - (2.0*x2*(-1.0 + N)*dz_F1)/(eF1*r2) + ((-2.0*x2*dz_F1)/eF1 - (2.0*y2*dz_F2)/eF2)*rp2inv + (x2*dz_N)/(eF1*r2) + (y2*W2*dz_N)/(eF0*N2) - (2.0*y2*W*dz_W)/(eF0*N);
    g->dz_yy = (y2*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (2.0*x2*W2*dz_F0)/(eF0*N) - (2.0*y2*(-1.0 + N)*dz_F1)/(eF1*r2) + ((-2.0*y2*dz_F1)/eF1 - (2.0*x2*dz_F2)/eF2)*rp2inv + (y2*dz_N)/(eF1*r2) + (x2*W2*dz_N)/(eF0*N2) - (2.0*x2*W*dz_W)/(eF0*N);
    g->dz_xy = (x*y*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (-2.0*x*y*W2*dz_F0)/(eF0*N) - (2.0*x*y*(-1.0 + N)*dz_F1)/(eF1*r2) + (x*y*((-2.0*dz_F1)/eF1 + (2.0*dz_F2)/eF2))*rp2inv + (x*y*dz_N)/(eF1*r2) - (x*y*W2*dz_N)/(eF0*N2) + (2.0*x*y*W*dz_W)/(eF0*N);
    // adjust for missing limit involving rp2inv in expressions above
    g->dz_xx += cond ? -2.0*dz_F1/eF1 : 0.0;
    g->dz_yy += cond ? -2.0*dz_F1/eF1 : 0.0;
    g->dz_zz = (z2*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (2.0*z*(-1.0 + N))/(eF1*r2) - (2.0*dz_F1)/eF1 - (2.0*z2*(-1.0 + N)*dz_F1)/(eF1*r2) + (z2*dz_N)/(eF1*r2);
    g->dz_xz = (x*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (x*(-1.0 + N))/(eF1*r2) - (2.0*x*z*(-1.0 + N)*dz_F1)/(eF1*r2) + (x*z*dz_N)/(eF1*r2);
    g->dz_yz = (y*z*(-1.0 + N))/(eF1*r2)*(-2.0*drdz/r) + (y*(-1.0 + N))/(eF1*r2) - (2.0*y*z*(-1.0 + N)*dz_F1)/(eF1*r2) + (y*z*dz_N)/(eF1*r2);

    // check if fallen in.
    return r<RCUTOFF;

    #undef x
    #undef y
    #undef z
    #undef x2
    #undef y2
    #undef z2
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
    #undef dx_F0
    #undef dy_F0
    #undef dz_F0
    #undef dx_F1
    #undef dy_F1
    #undef dz_F1
    #undef dx_F2
    #undef dy_F2
    #undef dz_F2
    #undef dx_W
    #undef dy_W
    #undef dz_W
    #undef eF0
    #undef eF1
    #undef eF2
    #undef drdx
    #undef drdy
    #undef drdz
    #undef dx_N
    #undef dy_N
    #undef dz_N
}

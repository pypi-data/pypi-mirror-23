/* Flat metric in spherical coordinates. */

// No user arguments to be passed down from the kernel (you can remove these two lines and the USER_ARGS_DEF in line 9 if you don't use them)
#define USER_ARGS_DEF
#define USER_ARGS


// Compute the components of the metric at x and store them in the metric g.
bool updateMetric( const realV x, metric* restrict g USER_ARGS_DEF )
{
    const real r = x.s1;
    const real theta = maxmag( x.s2, (real)1e-12 );     // prevent coordinate singularity
    const real s = sin(theta);
    const real c = cos(theta);

    g->tt = -1.0;
    g->rr = 1.0;
    g->thth = 1.0/(r*r);
    g->pp = 1.0/(r*r*s*s);
    g->tp = 0.0;

    g->dr_tt = 0.0;
    g->dr_rr = 0.0;
    g->dr_thth = -2.0/(r*r*r);
    g->dr_pp = -2.0/(r*r*r*s*s);
    g->dr_tp = 0.0;

    g->dth_tt = 0.0;
    g->dth_rr = 0.0;
    g->dth_thth = 0.0;
    g->dth_pp = -2.0*c/(r*r*s*s*s);
    g->dth_tp = 0.0;

    return false;
}

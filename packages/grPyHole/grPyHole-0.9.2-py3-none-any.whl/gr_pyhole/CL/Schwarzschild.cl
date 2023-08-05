/* Schwarzschild metric in spherical coordinates. */

// Compute the components of the metric at x and store them in the metric g.
bool updateMetric( const realV x, metric* restrict g )
{
    const real r = x.s1;
    const real theta = maxmag( x.s2, (real)1e-7 );     // prevent coordinate singularity
    const real st = sin(theta);
    const real ct = cos(theta);
    const real rsr = CONST_RS/r;

    g->tt = -1.0/(1.0-rsr);
    g->rr = 1.0-rsr;
    g->thth = 1.0/(r*r);
    g->pp = 1.0/(r*r*st*st);
    g->tp = 0.0;

    g->dr_tt = rsr/((1.0-rsr)*(1.0-rsr)*r);
    g->dr_rr = rsr/r;
    g->dr_thth = -2.0/(r*r*r);
    g->dr_pp = -2.0/(r*r*r*st*st);
    g->dr_tp = 0.0;

    g->dth_tt = 0.0;
    g->dth_rr = 0.0;
    g->dth_thth = 0.0;
    g->dth_pp = -2.0*ct/(r*r*st*st*st);
    g->dth_tp = 0.0;

    return r<RCUTOFF;
}

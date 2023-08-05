/* Kerr metric in spherical coordinates. */

// Compute the components of the metric at x and store them in the metric g.
bool updateMetric( const realV x, metric* restrict g )
{
    const real r = x.s1;
    const real theta = maxmag( x.s2, (real)1e-7 );     // prevent coordinate singularity
    const real s = sin(theta);
    const real c = cos(theta);
    const real s2 = s*s;
    const real c2 = c*c;
    const real r2 = r*r;
    const real rho2 = r2 + CONST_A*CONST_A*c2;
    const real rho4 = rho2*rho2;
    const real Delta = r2 - CONST_RS*r + CONST_A*CONST_A;

    g->tt = -(r2 + CONST_A*CONST_A + CONST_RS*r*CONST_A*CONST_A*s2/rho2 )/Delta;
    g->rr = Delta/rho2;
    g->thth = 1.0/rho2;
    g->pp = (Delta-CONST_A*CONST_A*s2)/(rho2*Delta*s2);
    g->tp = -CONST_RS*r*CONST_A/(rho2*Delta);

    const real Delta_r = 2.0*r-CONST_RS;
    const real rho2_r = 2.0*r;
    const real rho2_th = -2.0*CONST_A*CONST_A*c*s;
    g->dr_tt = -(g->tt*Delta_r+2.0*r+(rho2-rho2_r*r)*CONST_RS*CONST_A*CONST_A*s2/rho4)/Delta;
    g->dr_rr = (Delta_r-rho2_r*g->rr)/rho2;
    g->dr_thth = -rho2_r/rho4;
    g->dr_pp = (Delta_r-g->pp*(rho2_r*Delta+rho2*Delta_r)*s2)/(rho2*Delta*s2);
    g->dr_tp = -(CONST_RS*CONST_A+g->tp*(rho2_r*Delta+rho2*Delta_r))/(rho2*Delta);

    g->dth_tt = -CONST_RS*CONST_A*r*2.0*s*c*(r2+CONST_A*CONST_A)/(Delta*rho4);
    g->dth_rr = -Delta*rho2_th/rho4;
    g->dth_thth = -rho2_th/rho4;
    g->dth_pp = (-2.0*CONST_A*CONST_A*c - Delta*g->pp*(rho2_th*s+2.0*rho2*c))/(rho2*Delta*s);
    g->dth_tp = CONST_RS*r*CONST_A*rho2_th/(Delta*rho4);

    return r<RCUTOFF;
}

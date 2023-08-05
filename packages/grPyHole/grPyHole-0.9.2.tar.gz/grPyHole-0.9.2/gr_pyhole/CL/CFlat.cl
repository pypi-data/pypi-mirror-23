/* Flat metric in Cartesian coordinates. */

// No user arguments to be passed down from the kernel (you can remove these two lines and the USER_ARGS_DEF in line 9 if you don't use them)
#define USER_ARGS_DEF
#define USER_ARGS


// Compute the components of the metric at x and store them in the metric g.
bool updateMetric( const realV x, metric* restrict g USER_ARGS_DEF )
{
    // contravariant form
    g->tt = -1.0;
    g->tx = 0.0;
    g->ty = 0.0;
    g->xx = 1.0;
    g->yy = 1.0;
    g->zz = 1.0;
    g->xy = 0.0;
    g->xz = 0.0;
    g->yz = 0.0;

    g->dx_tt = 0.0;
    g->dx_tx = 0.0;
    g->dx_ty = 0.0;
    g->dx_xx = 0.0;
    g->dx_yy = 0.0;
    g->dx_zz = 0.0;
    g->dx_xy = 0.0;
    g->dx_xz = 0.0;
    g->dx_yz = 0.0;

    g->dy_tt = 0.0;
    g->dy_tx = 0.0;
    g->dy_ty = 0.0;
    g->dy_xx = 0.0;
    g->dy_yy = 0.0;
    g->dy_zz = 0.0;
    g->dy_xy = 0.0;
    g->dy_xz = 0.0;
    g->dy_yz = 0.0;

    g->dz_tt = 0.0;
    g->dz_tx = 0.0;
    g->dz_ty = 0.0;
    g->dz_xx = 0.0;
    g->dz_yy = 0.0;
    g->dz_zz = 0.0;
    g->dz_xy = 0.0;
    g->dz_xz = 0.0;
    g->dz_yz = 0.0;

    return false;
}

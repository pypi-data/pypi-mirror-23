// Bogacki–Shampine
#define RKF23 1
#if RK == 1     // only load if required
#define RKF23_stages 4       // Must be compile time constant in array allocation and manual loop unrolling, hence the #define instead of constant
constant int RKF23_order = 2;        // order of lower order solution
constant real RKF23_a[]  = {
    1.0 / 2.0,
    0.0,
    3.0 / 4.0,
    2.0 / 9.0,
    1.0 / 3.0,
    4.0 / 9.0
}; // butcher table omitting upper and diagonal zeros
constant real RKF23_b1[] = {
    2.0 / 9.0,
    1.0 / 3.0,
    4.0 / 9.0,
    0.0
}; // higher order solution
//constant real RKF23_b2[] = {
//    7.0 / 24.0,
//    1.0 / 4.0,
//    1.0 / 3.0,
//    1.0 / 8.0
//}; // lower order solution
constant real RKF23_d[]  = {
    -5.0 / 72.0,
    1.0 / 12.0,
    1.0 / 9.0,
    -1.0 / 8.0
}; // difference b1-b2
constant real RKF23_c[]  = {
    0.0,
    1.0 / 2.0,
    3.0 / 4.0,
    1.0
}; // time step factors
#endif
#undef RKF23

// The classical explicit RKF45
#define RKF45 1
#if RK == 1     // only load if required
#define RKF45_stages 6       // Must be compile time constant in array allocation and manual loop unrolling, hence the #define instead of constant
constant int RKF45_order = 4;        // order of lower order solution
constant real RKF45_a[]  = {  1.0 / 4.0,
                              3.0 / 32.0,       9.0 / 32.0,
                              1932.0 / 2197.0, -7200.0 / 2197.0,  7296.0 / 2197.0,
                              439.0 / 216.0,   -8.0,              3680.0 / 513.0,   -845.0 / 4104.0,
                             -8.0 / 27.0,       2.0,             -3544.0 / 2565.0,   1859.0 / 4104.0,   -11.0 / 40.0             }; // butcher table omitting upper and diagonal zeros
constant real RKF45_b1[] = {  16.0 / 135.0,     0.0,              6656.0 / 12825.0,  28561.0 / 56430.0, -9.0 / 50.0,  2.0 / 55.0 }; // higher order solution
//constant real RKF45_b2[] = {  25.0 / 216.0,     0.0,              1408.0 / 2565.0,   2197.0 / 4104.0,   -1.0 / 5.0,   0.0        }; // lower order solution
constant real RKF45_d[]  = {  1.0 / 360.0,      0.0,             -128.0 / 4275.0,   -2197.0 / 75240.0,   1.0 / 50.0,  2.0 / 55.0 }; // difference b1-b2
constant real RKF45_c[]  = {  0.0,              1.0 / 4.0,        3.0 / 8.0,         12.0 / 13.0,        1.0,         1.0 / 2.0  }; // time step factors
#endif
#undef RKF45

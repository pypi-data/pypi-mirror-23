#ifndef _RK_H_
#define _RK_H_

/*
   Copyright 2015 - 2016 Alexander Wittig, Jai Grover

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

// Dimension of the problem (we have more than 8 states, so we have to round up to 16 here)
#ifndef DIM
#define DIM 16
#endif

// C preprocessor shenanigans
#define RK_CONCATENATE_HELPER(a,b) a ## b
#define RK_CONCATENATE(a,b) RK_CONCATENATE_HELPER(a,b)
#define RK_STRINGIFY(x) #x
#define RK_INCLUDE(x) RK_STRINGIFY(x)

// Determine FP bits from setting of real type (why does the C preprocessor not have string comparisons?)
#define RK_REAL_BITSdouble 64
#define RK_REAL_BITSfloat 32
#define RK_REAL_BITShalf 16
#define RK_REAL_BITS RK_CONCATENATE(RK_REAL_BITS,real)

#if RK_REAL_BITS == 64
    #if __OPENCL_VERSION__ < 120
        #pragma OPENCL EXTENSION cl_khr_fp64 : enable
    #endif

    // math constants
    #define EPS DBL_EPSILON
    #define PI M_PI

    // OpenCL C "real" vector types (realV is the one for ODE dimension)
    #define realV RK_CONCATENATE(double,DIM)
    #define real2 double2
    #define real3 double3
    #define real4 double4
    #define real8 double8
    #define real16 double16

    // OpenCL "real" type conversion functions
    #define convert_real(x) convert_double(x)
    #define convert_real2(x) convert_double2(x)
    #define convert_real3(x) convert_double3(x)
    #define convert_real4(x) convert_double4(x)
    #define convert_real8(x) convert_double8(x)
    #define convert_real16(x) convert_double16(x)
#elif RK_REAL_BITS == 32
    // math constants
    #define EPS FLT_EPSILON
    #define PI M_PI_F

    // OpenCL C "real" vector types (realV is the one for ODE dimension)
    #define realV RK_CONCATENATE(float,DIM)
    #define real2 float2
    #define real3 float3
    #define real4 float4
    #define real8 float8
    #define real16 float16

    // OpenCL "real" type conversion functions
    #define convert_real(x) convert_float(x)
    #define convert_real2(x) convert_float2(x)
    #define convert_real3(x) convert_float3(x)
    #define convert_real4(x) convert_float4(x)
    #define convert_real8(x) convert_float8(x)
    #define convert_real16(x) convert_float16(x)
#elif RK_REAL_BITS == 16
    #pragma OPENCL EXTENSION cl_khr_fp16 : enable

    // math constants
    #define EPS HALF_EPSILON
    #define PI M_PI_H

    // OpenCL C "real" vector types (realV is the one for ODE dimension)
    #define realV RK_CONCATENATE(half,DIM)
    #define real2 half2
    #define real3 half3
    #define real4 half4
    #define real8 half8
    #define real16 half16

    // OpenCL "real" type conversion functions
    #define convert_real(x) convert_half(x)
    #define convert_real2(x) convert_half2(x)
    #define convert_real3(x) convert_half3(x)
    #define convert_real4(x) convert_half4(x)
    #define convert_real8(x) convert_half8(x)
    #define convert_real16(x) convert_half16(x)
#else
    #error Real data type specified incorrectly!
#endif

typedef struct _RKstate {
    realV x;
    real t;
    real tf;
    real err;
    real h;
} RKstate;

// alias the selected RK to generic RK_ names
#define RK_order RK_CONCATENATE(RK,_order)
#define RK_a RK_CONCATENATE(RK,_a)
#define RK_b1 RK_CONCATENATE(RK,_b1)
#define RK_b2 RK_CONCATENATE(RK,_b2)
#define RK_c RK_CONCATENATE(RK,_c)
#define RK_d RK_CONCATENATE(RK,_d)
#define RK_stages RK_CONCATENATE(RK,_stages)

// set some default values for user defined inputs of RK algorithm if not specified earlier
#ifndef RK
    #define RK RKF78
#endif
#ifndef NSTEPS
    #define NSTEPS 10000
#endif
#ifndef HMIN
    #define HMIN 0.0001
#endif
#ifndef HMAX
    #define HMAX 0.1
#endif
#ifndef FMIN
    #define FMIN 0.01
#endif
#ifndef FMAX
    #define FMAX 10.0
#endif
#ifndef TERR
    #define TERR  (1000.0*EPS)
#endif
#ifndef MERR
    #define MERR (10.0*TERR)
#endif
#ifndef BSFACT
    #define BSFACT 0.5
#endif
#ifndef RK_ERROR
    #define RK_ERROR ERROR_MAX
#endif
#ifndef ERRWEIGHTS
    #define ERRWEIGHTS (realV)(1.0)
#endif

// vector maximum component function for ODE dimension
#define VMAX(x) RK_CONCATENATE(vmax,DIM)(x)

// various ways of measuring errors
#define ERROR_MAX(xerr, xstep, x) VMAX( fabs( xerr ) )                // maximum unweighted error
#define ERROR_MAXW(xerr, xstep, x) VMAX( fabs( RK_errw*xerr ) )       // maximum weighted error
#define ERROR_LENGTH(xerr, xstep, x) length( xerr )                   // length of unweighted error
#define ERROR_LENGTHW(xerr, xstep, x) length( RK_errw*xerr )          // length of weighted error
#define ERROR_SUM(xerr, xstep, x) dot( (realV)(1.0), fabs( xerr ) )   // sum of unweighted errors
#define ERROR_SUMW(xerr, xstep, x) dot( RK_errw, fabs( xerr ) )       // sum of weighted errors

// particular macros to unroll loops that run from i=1 to i=N-1 (defined up to N=31)
#define REPEAT(F,N) RK_CONCATENATE(REPEAT_,N)(F)
#define REPEAT_1(F) {}
#define REPEAT_2(F)  REPEAT_1(F)  F(1)
#define REPEAT_3(F)  REPEAT_2(F)  F(2)
#define REPEAT_4(F)  REPEAT_3(F)  F(3)
#define REPEAT_5(F)  REPEAT_4(F)  F(4)
#define REPEAT_6(F)  REPEAT_5(F)  F(5)
#define REPEAT_7(F)  REPEAT_6(F)  F(6)
#define REPEAT_8(F)  REPEAT_7(F)  F(7)
#define REPEAT_9(F)  REPEAT_8(F)  F(8)
#define REPEAT_10(F) REPEAT_9(F)  F(9)
#define REPEAT_11(F) REPEAT_10(F) F(10)
#define REPEAT_12(F) REPEAT_11(F) F(11)
#define REPEAT_13(F) REPEAT_12(F) F(12)
#define REPEAT_14(F) REPEAT_13(F) F(13)
#define REPEAT_15(F) REPEAT_14(F) F(14)
#define REPEAT_16(F) REPEAT_15(F) F(15)
#define REPEAT_17(F) REPEAT_16(F) F(16)
#define REPEAT_18(F) REPEAT_17(F) F(17)
#define REPEAT_19(F) REPEAT_18(F) F(18)
#define REPEAT_20(F) REPEAT_19(F) F(19)
#define REPEAT_21(F) REPEAT_20(F) F(20)
#define REPEAT_22(F) REPEAT_21(F) F(21)
#define REPEAT_23(F) REPEAT_22(F) F(22)
#define REPEAT_24(F) REPEAT_23(F) F(23)
#define REPEAT_25(F) REPEAT_24(F) F(24)
#define REPEAT_26(F) REPEAT_25(F) F(25)
#define REPEAT_27(F) REPEAT_26(F) F(26)
#define REPEAT_28(F) REPEAT_27(F) F(27)
#define REPEAT_29(F) REPEAT_28(F) F(28)
#define REPEAT_30(F) REPEAT_29(F) F(29)
#define REPEAT_31(F) REPEAT_30(F) F(30)

// Maximum component of vector functions
// Real overloading would be nice but seems not portable between OpenCL compilers.
inline real vmax2( const real2 x )
{
    return fmax( x.lo, x.hi );
}

inline real vmax3( const real3 x )
{
    return fmax( fmax( x.s0, x.s1 ), x.s2 );    // special handling
}

inline real vmax4( const real4 x )
{
    return vmax2( fmax( x.lo, x.hi ) );
}

inline real vmax8( const real8 x )
{
    return vmax4( fmax( x.lo, x.hi ) );
}

inline real vmax16( const real16 x )
{
    return vmax8( fmax( x.lo, x.hi ) );
}

// Global RK constants derived from user defined input
constant uint  RK_nsteps = NSTEPS;
constant real  RK_hmin   = HMIN;
constant real  RK_hmax   = HMAX;
constant real  RK_merr   = MERR;
constant realV RK_errw   = ERRWEIGHTS;
constant float RK_fmin   = FMIN;    // float because only used in step size estimation
constant float RK_fmax   = FMAX;    // float because only used in step size estimation
constant float RK_terr   = TERR;    // float because only used in step size estimation
constant float RK_bsf    = BSFACT;  // float because only used in step size estimation

#endif

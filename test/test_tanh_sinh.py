# -*- coding: utf-8 -*-
#
from mpmath import mp
import pytest
import quadpy
import sympy

mp.dps = 50


@pytest.mark.parametrize(
    'f, a, b, exact',
    [({
        0: lambda t: 1,
        1: lambda t: 0,
        2: lambda t: 0
        }, -1, +1, 2)]
    + [({
        0: lambda t: 1,
        1: lambda t: 0,
        2: lambda t: 0
        }, 0, +1, 1)]
    + [({
        0: lambda t: t,
        1: lambda t: 1,
        2: lambda t: 0,
        }, -0, +1, sympy.Rational(1, 2))]
    + [({
        0: lambda t: t**2,
        1: lambda t: 2*t,
        2: lambda t: 2,
        }, -1, +1, sympy.Rational(2, 3))]
    )
def test_tanh_sinh_good_estimate(f, a, b, exact):
    # test fine error estimate
    tol = 10**(-mp.dps)
    value, _ = quadpy.line_segment.tanh_sinh_regular(
                f[0], a, b, tol,
                f_derivatives={1: f[1], 2: f[2]}
                )
    assert abs(value - exact) < tol
    return


@pytest.mark.parametrize(
    'f, a, b, exact',
    [(lambda t: mp.exp(t) / mp.sqrt(1-t**2),
      0, 1, mp.pi/2 * (mp.besseli(0, 1) + mp.struvel(0, 1))
      )]
    # Some test problems from
    # <http://crd-legacy.lbl.gov/~dhbailey/dhbpapers/quadrature.pdf>
    # Test problem 1:
    + [(lambda t: t * mp.log(1+t), 0, +1, sympy.Rational(1, 4))]
    # Test problem 2:
    + [(lambda t: t**2 * mp.atan(t), 0, 1, (sympy.pi - 2 + 2*sympy.log(2))/12)]
    # Test problem 3:
    + [(lambda t: mp.exp(t) * mp.cos(t), 0, mp.pi/2, (mp.exp(mp.pi/2) - 1)/2)]
    # # Test problem 4:
    + [(
        lambda t: mp.atan(mp.sqrt(2 + t**2)) / (1+t**2) / mp.sqrt(2+t**2),
        0, 1, 5*mp.pi**2/96
      )]
    # Test problem 5:
    + [(lambda t: mp.sqrt(t) * mp.log(t), 0, 1, -sympy.Rational(4, 9))]
    # Test problem 6:
    + [(lambda t: mp.sqrt(1 - t**2), 0, 1, sympy.pi/4)]
    # Test problem 7:
    # + [(lambda t: mp.sqrt(t / (1 - t**2)),
    #     0, 1,
    #     2 * sympy.sqrt(sympy.pi)
    #     * sympy.gamma(sympy.Rational(3, 4))/sympy.gamma(sympy.Rational(1, 4))
    #     )]
    # # Test problem 8:
    # + [(lambda t: mp.log(t)**2, 0, 1, 2)]
    # Test problem 9:
    + [(lambda t: mp.log(mp.cos(t)), 0, mp.pi/2, -sympy.pi*sympy.log(2)/2)]
    # Test problem 10:
    # + [(lambda t: mp.sqrt(mp.tan(t)), 0, mp.pi/2, sympy.pi/sympy.sqrt(2))]
    # Test problem 11:
    + [(lambda t: 1/(1 - 2*t + 2*t**2), 0, 1, sympy.pi/2)]
    # Test problem 12:
    # + [(
    #     lambda t: mp.exp(1 - 1/t) / mp.sqrt(t**3 - t**4),
    #     0, 1, sympy.sqrt(sympy.pi)
    #     )]
    # Test problem 13:
    # + [(
    #     lambda t: mp.exp(-(1/t - 1)**2 / 2) / t**2,
    #     0, 1, sympy.sqrt(sympy.pi/2)
    #     )]
    # Test problem 14:
    # + [(
    #     lambda t: mp.exp(1 - 1/t) * mp.cos(1/t - 1) / t**2,
    #     0, 1, sympy.Rational(1, 2)
    #     )]
    )
def test_tanh_sinh_crude_estimate(f, a, b, exact):
    tol = 10**(-mp.dps)
    value, _ = quadpy.line_segment.tanh_sinh_regular(f, a, b, tol)
    tol2 = 10**(-mp.dps+2)
    assert abs(value - sympy.N(exact, mp.dps)) < tol2
    return


if __name__ == '__main__':
    test_tanh_sinh_good_estimate(
        # {
        #     0: lambda t: 1,
        #     1: lambda t: 0,
        #     2: lambda t: 0,
        # }, 0, 1, sympy.Rational(1, 2)
        # {
        #     0: lambda t: t**2,
        #     1: lambda t: 2*t,
        #     2: lambda t: 2,
        # }, 0, 1, sympy.Rational(1, 3)
        # {
        #     0: lambda t: t**3,
        #     1: lambda t: 3*t**2,
        #     2: lambda t: 6*t,
        # }, 0, 1, sympy.Rational(1, 4)
        # {
        #     0: lambda t: t * mp.log(1+t),
        #     1: lambda t: t / (t+1) + mp.log(t+1),
        #     2: lambda t: (t+2) / (t+1)**2,
        # }, 0, 1, sympy.Rational(1, 4)
        # {
        #     0: lambda t: 1,
        #     1: lambda t: 0,
        #     2: lambda t: 0,
        # }, 0, 5, 5
        # {
        #     0: lambda t: t,
        #     1: lambda t: 1,
        #     2: lambda t: 0,
        # }, 0, 5, mp.mpf(25)/2
        {
            0: lambda t: mp.exp(t) * mp.cos(t),
            1: lambda t: mp.exp(t) * (mp.cos(t) - mp.sin(t)),
            2: lambda t: -2*mp.exp(t) * mp.sin(t),
        }, 0, mp.pi/2, (sympy.exp(sympy.pi/2) - 1)/2
        )
    # test_tanh_sinh_crude_estimate(
    #     # lambda t: 1, 0, 1, sympy.Rational(1, 2)
    #     #
    #     # lambda t: t**2, 0, 1, sympy.Rational(1, 3)
    #     #
    #     # lambda t: t * mp.log(1+t), 0, 1, sympy.Rational(1, 4)
    #     #
    #     lambda t: mp.exp(t) * mp.cos(t),
    #     0, mp.pi/2, (sympy.exp(sympy.pi/2) - 1)/2
    #     #
    #     # lambda t: mp.sqrt(t) * mp.log(t), 0, 1, -sympy.Rational(4, 9)
    #     #
    #     # lambda t: mp.exp(t) / mp.sqrt(1-t**2),
    #     # 0, 1, mp.pi/2 * (mp.besseli(0, 1) + mp.struvel(0, 1))
    #     #
    #     # lambda t: mp.exp(1-t) / mp.sqrt(2*t-t**2),
    #     # 0, 1, mp.pi/2 * (mp.besseli(0, 1) + mp.struvel(0, 1)),
    #     # '1-s'
    #     #
    #     # lambda t: 1/mp.sqrt(t), 0, 1, 2
    #     )

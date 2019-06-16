# -*- coding: utf-8 -*-
#
"""
Carlos Felippa,
A compendium of FEM integration formulas for symbolic work,
Engineering Computation,
Volume 21, Number 8, 2004, pages 867-890.

<https://people.sc.fsu.edu/~jburkardt/datasets/quadrature_rules_wedge/quadrature_rules_wedge.html>
"""
from __future__ import division

import numpy
import sympy

from ..helpers import untangle
from .helpers import WedgeScheme


def felippa_1(symbolic=False):
    data = [(1, _s3(symbolic))]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 1", 1, weights, points)


def felippa_2(symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

    data = [(frac(1, 6), _s21_z(frac(1, 6), sqrt(frac(1, 3))))]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 2", 2, weights, points)


def felippa_3(symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

    data = [(frac(1, 6), _s21_z(frac(1, 2), sqrt(frac(1, 3))))]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 3", 2, weights, points)


def felippa_4(symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

    # roots of  135 x^4 - 240 x^3 + 120 x^2 - 20 x + 1
    a1, a2 = [
        (40 - 5 * sqrt(10) - i * sqrt(950 - 220 * sqrt(10))) / 90 for i in [+1, -1]
    ]
    data = [
        (0.6205044157722541e-01, _s21_z(a2, sqrt(frac(3, 5)))),
        (0.3054215101536719e-01, _s21_z(a1, sqrt(frac(3, 5)))),
        (0.9928070652356065e-01, _s21(a2)),
        (0.4886744162458750e-01, _s21(a1)),
    ]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 4", 4, weights, points)


def felippa_5(symbolic=False):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    sqrt = numpy.vectorize(sympy.sqrt) if symbolic else numpy.sqrt

    a1, a2 = [(6 - i * sqrt(15)) / 21 for i in [+1, -1]]
    data = [
        (0.3498310570689643e-01, _s21_z(a1, sqrt(frac(3, 5)))),
        (0.3677615355236283e-01, _s21_z(a2, sqrt(frac(3, 5)))),
        (frac(1, 16), _s3_z(sqrt(frac(3, 5)), symbolic)),
        (0.5597296913103428e-01, _s21(a1)),
        (0.5884184568378053e-01, _s21(a2)),
        (frac(1, 10), _s3(symbolic)),
    ]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 5", 5, weights, points)


def felippa_6():
    data = [
        (0.8843323515718317e-02, _s21_z(0.6308901449150223e-01, -0.8611363115940526)),
        (0.2031233592848984e-01, _s21_z(0.2492867451709104, -0.8611363115940526)),
        (
            0.1441007403935041e-01,
            _s111_z(0.5314504984481695e-01, 0.3103524510337844, 0.8611363115940526),
        ),
        (0.1657912966938509e-01, _s21_z(0.6308901449150223e-01, 0.3399810435848563)),
        (0.3808080193469984e-01, _s21_z(0.2492867451709104, 0.3399810435848563)),
        (
            0.2701546376983638e-01,
            _s111_z(0.5314504984481695e-01, 0.3103524510337844, 0.3399810435848563),
        ),
    ]
    points, weights = untangle(data)
    return WedgeScheme("Felippa 6", 6, weights, points)


def _s3(symbolic):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    return [[frac(1, 3), frac(1, 3), 0]]


def _s3_z(z, symbolic):
    frac = sympy.Rational if symbolic else lambda x, y: x / y
    return [[frac(1, 3), frac(1, 3), +z], [frac(1, 3), frac(1, 3), -z]]


def _s21(a):
    b = 1 - 2 * a
    return [[a, b, 0], [b, a, 0], [a, a, 0]]


def _s21_z(a, z):
    b = 1 - 2 * a
    return [[a, b, +z], [b, a, +z], [a, a, +z], [a, b, -z], [b, a, -z], [a, a, -z]]


def _s111_z(a, b, z):
    c = 1 - a - b
    return [
        [b, c, +z],
        [a, b, +z],
        [c, a, +z],
        [c, b, +z],
        [a, c, +z],
        [b, a, +z],
        [b, c, -z],
        [a, b, -z],
        [c, a, -z],
        [c, b, -z],
        [a, c, -z],
        [b, a, -z],
    ]


Felippa = {
    1: felippa_1,
    2: felippa_2,
    3: felippa_3,
    4: felippa_4,
    5: felippa_5,
    6: felippa_6,
}

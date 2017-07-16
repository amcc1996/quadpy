# -*- coding: utf-8 -*-
#
import numpy

from .helpers import _s4, _s31, _s22, _s211


class BeckersHaegemans(object):
    '''
    M. Beckers and A. Haegemans,
    The construction of cubature formulae for the tetrahedron,
    Report TW 128, Dept. of Computer Science, K.U. Leuven, 1990,
    <https://lirias.kuleuven.be/handle/123456789/132648>.
    '''
    def __init__(self, index):
        self.name = 'BH({})'.format(index)
        if index == 8:
            self.degree = 8
            self.weights = 6 * numpy.concatenate([
                numpy.full(1, -0.020500188658639915),
                numpy.full(4, 0.014250305822866901),
                numpy.full(4, 1.9670333131339009e-3),
                numpy.full(4, 1.6983410909288737e-4),
                numpy.full(6, 4.5796838244672818e-3),
                numpy.full(12, 5.7044858086819185e-3),
                numpy.full(12, 2.1405191411620925e-3),
                ])
            bary = numpy.concatenate([
                _s4(),
                _s31(0.20682993161067320),
                _s31(0.082103588310546723),
                _s31(5.7819505051979972e-3),
                _s22(0.44946725998110577),
                _s211(0.22906653611681113, 0.506227344977843697),
                _s211(0.036607749553197423, 0.19048604193463345),
                ])
        else:
            assert index == 9
            self.degree = 9
            self.weights = 6 * numpy.concatenate([
                numpy.full(1, -0.13779903832610864),
                numpy.full(4, 1.8653365690852895e-3),
                numpy.full(4, 4.3094239694934006e-3),
                numpy.full(4, -0.090184766481201525),
                numpy.full(4, 0.044672576202511444),
                numpy.full(12, 0.034700405884550761),
                numpy.full(12, 3.3525839026606469e-3),
                numpy.full(12, 4.3162887555699692e-4),
                ])
            bary = numpy.concatenate([
                _s4(),
                _s31(0.048351038549736740),
                _s31(0.32457928011788236),
                _s31(0.11461654022399521),
                _s31(0.22548995191151391),
                _s211(0.13162780924686980, 0.083664701617184967),
                _s211(0.43395146141140677, 0.10776985954942861),
                _s211(-1.3762773181382007e-3, 0.27655347263680734),
                ])

        self.points = bary[:, 1:]
        return

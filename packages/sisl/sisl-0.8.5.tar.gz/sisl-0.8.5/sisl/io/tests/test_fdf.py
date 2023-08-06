from __future__ import print_function, division

from nose.tools import *

from tempfile import mkstemp, mkdtemp

from sisl import Geometry, Atom
from sisl.io import fdfSileSiesta

import os.path as osp
import math as m
import numpy as np

import common as tc


class TestFDF(object):
    # Base test class for MaskedArrays.

    setUp = tc.setUp
    tearDown = tc.tearDown

    def test_fdf1(self):
        f = osp.join(self.d, 'gr.fdf')
        self.g.write(fdfSileSiesta(f, 'w'))

        fdf = fdfSileSiesta(f)
        with fdf:

            fdf.readline()

            # Be sure that we can read it in a loop
            assert_true(fdf.get('LatticeConstant') > 0.)
            assert_true(fdf.get('LatticeConstant') > 0.)
            assert_true(fdf.get('LatticeConstant') > 0.)

            fdf.read_supercell()
            fdf.read_geometry()

    def test_fdf2(self):
        f = osp.join(self.d, 'gr.fdf')
        self.g.write(fdfSileSiesta(f, 'w'))
        g = fdfSileSiesta(f).read_geometry()

        # Assert they are the same
        assert_true(np.allclose(g.cell, self.g.cell))
        assert_true(np.allclose(g.xyz, self.g.xyz))
        for ia in g:
            assert_true(g.atom[ia].Z == self.g.atom[ia].Z)
            assert_true(g.atom[ia].tag == self.g.atom[ia].tag)

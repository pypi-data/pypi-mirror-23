from __future__ import print_function, division

from nose.tools import *

from sisl import Geometry, Atom, Hamiltonian
from sisl.io.siesta import *

import os.path as osp
import math as m
import numpy as np

import common as tc


class TestSIESTAnc(object):
    # Base test class for MaskedArrays.

    setUp = tc.setUp
    tearDown = tc.tearDown

    def test_nc1(self):
        f = osp.join(self.d, 'gr.nc')
        tb = Hamiltonian(self.gtb)
        tb.construct([self.R, self.t])
        tb.write(ncSileSiesta(f, 'w'))

        ntb = ncSileSiesta(f).read_hamiltonian()

        # Assert they are the same
        assert_true(np.allclose(tb.cell, ntb.cell))
        assert_true(np.allclose(tb.xyz, ntb.xyz))
        assert_true(np.allclose(tb._csr._D[:, 0], ntb._csr._D[:, 0]))
        assert_true(self.g.atom.equal(ntb.atom, R=False))

    def test_nc2(self):
        f = osp.join(self.d, 'gr.dH.nc')
        H = Hamiltonian(self.gtb)
        H.construct([self.R, self.t])

        # annoyingly this has to be performed like this...
        sile = dHncSileSiesta(f, 'w')
        H.geom.write(sile)
        sile = dHncSileSiesta(f, 'a')

        # Write to level-1
        H.write(sile)
        # Write to level-2
        H.write(sile, k=[0, 0, .5])
        # Write to level-3
        H.write(sile, E=0.1)
        # Write to level-4
        H.write(sile, k=[0, 0, .5], E=0.1)

    def test_nc3(self):
        f = osp.join(self.d, 'grS.nc')
        tb = Hamiltonian(self.gtb, orthogonal=False)
        tb.construct([self.R, self.tS])
        tb.write(ncSileSiesta(f, 'w'))

        ntb = ncSileSiesta(f).read_hamiltonian()

        # Assert they are the same
        assert_true(np.allclose(tb.cell, ntb.cell))
        assert_true(np.allclose(tb.xyz, ntb.xyz))
        assert_true(np.allclose(tb._csr._D, ntb._csr._D))
        assert_true(self.g.atom.equal(ntb.atom, R=False))

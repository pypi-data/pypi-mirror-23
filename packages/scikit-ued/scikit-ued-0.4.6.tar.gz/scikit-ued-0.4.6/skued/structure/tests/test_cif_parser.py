# -*- coding: utf-8 -*-
import os
import unittest
from warnings import filterwarnings

import numpy as np

from .. import Crystal, graphite
from ... import transform
from ..cif_parser import CIFParser

filterwarnings('ignore', category = UserWarning)

class TestCIRParser(unittest.TestCase):
    """ Test the CIFParser on all CIF files stored herein """

    def _cif_files(self):
        """ Yields cif files included in scikit-ued """
        for root, _, files in os.walk(os.path.join('skued', 'structure')):
            for name in filter(lambda path: path.endswith('.cif'), files):
                yield os.path.join(root, name)

    def test_compatibility(self):
        """ Test the CIFParser on all CIF files stored herein to check build errors"""
        for name in self._cif_files():
            with self.subTest(name.split('\\')[-1]):
                c = Crystal.from_cif(name)
    
    def test_symmetry_operators(self):
        """ Test that the non-translation part of the symmetry_operators is an invertible
        matrix of determinant 1 | -1 """
        for name in self._cif_files():
            with self.subTest(name.split('\\')[-1]):
                with CIFParser(name) as p:
                    for sym_op in p.symmetry_operators():
                        t = sym_op[:3,:3]
                        self.assertAlmostEqual(abs(np.linalg.det(t)), 1)
    
    def test_graphite(self):
        """ Test CIFParser on C.cif and compare to built-in graphite """
        C_path = os.path.join('skued', 'structure', 'cifs', 'C.cif')
        c = Crystal.from_cif(C_path)
        
        self.assertEqual(len(c), len(graphite))
        self.assertAlmostEqual(c.volume, graphite.volume, places = -1)
    
    def test_silicon(self):
        """ Test CIFParser on Si.cif (diamond structure) """
        Si_path = os.path.join('skued', 'structure', 'cifs', 'Si.cif')
        si = Crystal.from_cif(Si_path)

        self.assertEqual(len(si), 8)
    
    def test_vo2(self):
        """ Test CIFParser on vo2.cif (monoclinic M1) """
        VO2_path = os.path.join('skued', 'structure', 'cifs', 'vo2.cif')
        vo2 = Crystal.from_cif(VO2_path)

        self.assertEqual(len(vo2), 12)
        self.assertSequenceEqual(vo2.lattice_parameters, 
                                 (5.7430000000000003, 4.5170000000000003, 5.375, 90.0, 122.60000000000001, 90.0))
        self.assertAlmostEqual(vo2.volume, 117.4661530) # from cif2cell

if __name__ == '__main__':
    unittest.main()

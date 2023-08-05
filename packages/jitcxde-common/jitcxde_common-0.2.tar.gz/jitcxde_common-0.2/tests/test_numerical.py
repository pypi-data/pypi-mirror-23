#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.testing import assert_allclose
import unittest
from jitcxde_common.numerical import random_direction, orthonormalise

class RandomDirectionTest(unittest.TestCase):
	def test_random_direction(self):
		d = 10
		n = 100000
		n_vectors = np.vstack(random_direction(d) for i in range(n))
		average = np.average(n_vectors, axis=0)
		assert_allclose( average, np.zeros(d), rtol=0, atol=0.01 )

class OrthonormaliseTest(unittest.TestCase):
	def test_orthonormalise_1(self):
		vectors = [ np.array([3.0,4.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([0.6,0.8]) )
		assert_allclose( norms, np.array([5]) )
	
	def test_orthonormalise_2(self):
		vectors = [ np.array([1.0,0.0]), np.array([0.0,1.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([1.0,0.0]) )
		assert_allclose( vectors[1], np.array([0.0,1.0]) )
		assert_allclose( norms, np.array([1.0,1.0]) )
	
	def test_orthonormalise_3(self):
		vectors = [ np.array([1.0,0.0]), np.array([1.0,1.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([1.0,0.0]) )
		assert_allclose( vectors[1], np.array([0.0,1.0]) )
		assert_allclose( norms, np.array([1.0,1.0]) )
	
	def test_orthonormalise_4(self):
		vectors = [ np.array([1.0,1.0]), np.array([1.0,1.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([np.sqrt(0.5),np.sqrt(0.5)]) )
		assert_allclose( norms, np.array([np.sqrt(2),0.0]) , atol = 1e-10 )
	
	def test_orthonormalise_5(self):
		vectors = [ np.array([1.0,1.0]), np.array([1.0,-1.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([np.sqrt(0.5),np.sqrt(0.5)]) )
		assert_allclose( vectors[1], np.array([np.sqrt(0.5),-np.sqrt(0.5)]) )
		assert_allclose( norms, np.array([np.sqrt(2),np.sqrt(2)]) )
	
	def test_orthonormalise_6(self):
		vectors = [ np.array([1.0,1.0]), np.array([1.0,0.0]) ]
		norms = orthonormalise(vectors)
		assert_allclose( vectors[0], np.array([np.sqrt(0.5),np.sqrt(0.5)]) )
		assert_allclose( vectors[1], np.array([np.sqrt(0.5),-np.sqrt(0.5)]) )
		assert_allclose( norms, np.array([np.sqrt(2),np.sqrt(0.5)]) )

if __name__ == "__main__":
	unittest.main(buffer=True)

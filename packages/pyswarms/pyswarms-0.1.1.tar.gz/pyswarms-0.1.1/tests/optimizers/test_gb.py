#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit testing for pyswarms.single.GBestPSO"""

# Import modules
import unittest
import numpy as np

# Import from package
from pyswarms.single import GBestPSO
from pyswarms.utils.functions.single_obj import sphere_func

class Base(unittest.TestCase):
    """Base class for tests

    This class defines a common `setUp` method that defines attributes
    which are used in the various tests.
    """
    def setUp(self):
        """Set up test fixtures"""
        self.options = {'c1':0.5, 'c2':0.7, 'm':0.5}
        self.safe_bounds = (np.array([-5,-5]), np.array([5,5]))

class Instantiation(Base):
    """Tests all aspects of instantiation

    Tests include: instantiation with args of wrong type, instantiation
    with input values outside constraints, etc.
    """
    def test_keyword_check_fail(self):
        """Tests if exceptions are thrown when keywords are missing"""
        check_c1 = {'c2':0.7, 'm':0.5}
        check_c2 = {'c1':0.5, 'm':0.5}
        check_m = {'c1':0.5, 'c2':0.7}
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2,**check_c1)
            optimizer = GBestPSO(5,2,**check_c2)
            optimizer = GBestPSO(5,2,**check_m)

    def test_bound_size_fail(self):
        """Tests if exception is thrown when bound length is not 2"""
        bounds = (np.array([-5,-5]))
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2, bounds, **self.options)

    def test_bound_type_fail(self):
        """Tests if exception is thrown when bound type is not tuple"""
        bounds = [np.array([-5,-5]), np.array([5,5])]
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2, bounds, **self.options)

    def test_bound_maxmin_fail(self):
        """Tests if exception is thrown when min max of the bound is
        wrong."""
        bounds_1 = (np.array([5,5]), np.array([-5,-5]))
        bounds_2 = (np.array([5,-5]), np.array([-5,5]))
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2, bounds_1, **self.options)
            optimizer = GBestPSO(5,2, bounds_2, **self.options)

    def test_bound_shapes_fail(self):
        """Tests if exception is thrown when bounds are of unequal 
        shapes."""
        bounds = (np.array([-5,-5,-5]), np.array([5,5]))
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2, bounds, **self.options)

    def test_bound_shape_dims_fail(self):
        """Tests if exception is thrown when bound shape is not equal
        to dims."""
        bounds = (np.array([-5,-5,-5]), np.array([5,5,5]))
        with self.assertRaises(AssertionError):
            optimizer = GBestPSO(5,2, bounds, **self.options)

class Methods(Base):
    """Tests all aspects of the class methods

    Tests include: wrong inputs of methods, wrong return types,
    unexpected attribute setting, and etc.
    """

    def test_reset(self):
        """Tests if the reset method resets the attributes required"""
        # Perform a simple optimization
        optimizer = GBestPSO(5,2, **self.options)
        optimizer.optimize(sphere_func, 100, verbose=0)
        # Reset the attributes
        optimizer.reset()
        # Perform testing
        self.assertEqual(optimizer.gbest_cost, np.inf)
        self.assertIsNone(optimizer.gbest_pos)

if __name__ == '__main__':
    unittest.main()
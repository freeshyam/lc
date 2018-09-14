#!/usr/bin/env python

import unittest
import random

def dutch_flag_partition(arr):
    """
    invariant:
    """

class UT1(unittest.TestCase):
    def setUp(self):
        self.f = dutch_flag_partition

    def test_base(self):
        arr = [random.randint(0, 2) for _ in range(10000)]
        sorted_arr = sorted(arr)
        self.f(arr)
        self.assertEqual(arr, sorted_arr)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

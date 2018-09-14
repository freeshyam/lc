#!/usr/bin/env python

import unittest

def binary_search(arr, target):
    """
    Args:
        arr: a sorted (in ascending order) list of numbers
        target: a number to look for in arr

    Returns:
        True if target exists in arr, otherwise False
    """

    i, j = 0, len(arr) - 1

    while i <= j:
        mid_idx = (i + j) // 2

        if arr[mid_idx] == target:
            return True
        # search right half of subarray
        elif arr[mid_idx] < target:
            i = mid_idx + 1
        # search left half of subarray
        else:
            j = mid_idx - 1

    return False

class UT1(unittest.TestCase):
    def setUp(self):
        pass

    def test_base(self):
        l = [2, 8, 13, 15, 39, 51, 66]

        self.assertEqual(binary_search(l, 2), True)
        self.assertEqual(binary_search(l, 8), True)
        self.assertEqual(binary_search(l, 13), True)
        self.assertEqual(binary_search(l, 15), True)
        self.assertEqual(binary_search(l, 39), True)
        self.assertEqual(binary_search(l, 51), True)
        self.assertEqual(binary_search(l, 66), True)

        self.assertEqual(binary_search(l, 0), False)
        self.assertEqual(binary_search(l, 5), False)
        self.assertEqual(binary_search(l, 10), False)
        self.assertEqual(binary_search(l, 14), False)
        self.assertEqual(binary_search(l, 17), False)
        self.assertEqual(binary_search(l, 42), False)
        self.assertEqual(binary_search(l, 60), False)
        self.assertEqual(binary_search(l, 99), False)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

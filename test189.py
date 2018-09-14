#!/usr/bin/env python

import unittest

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pass

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.rotate

    def test_base(self):
        t1 = [1, 2, 3, 4, 5, 6, 7]
        o1 = [7, 1, 2, 3, 4, 5, 6]

        self.f(t1, 1)
        self.assertEqual(t1, o1)

        t2 = [1, 2, 3, 4, 5, 6, 7]
        o2 = [5, 6, 7, 1, 2, 3, 4]
        self.f(t2, 3)
        self.assertEqual(t2, o2)

        t3 = [1, 2, 3, 4, 5, 6, 7]
        o3 = [1, 2, 3, 4, 5, 6, 7]
        self.f(t3, 7)
        self.assertEqual(t3, o3)
        self.f(t3, 14)
        self.assertEqual(t3, o3)

        t4 = [1, 2, 3, 4, 5, 6]
        o4 = [5, 6, 1, 2, 3, 4]
        self.f(t4, 2)
        self.assertEqual(t4, o4)

        t5 = [1, 2, 3, 4, 5, 6]
        o5 = [4, 5, 6, 1, 2, 3]
        self.f(t5, 3)
        self.assertEqual(t5, o5)

        t6 = [1, 2]
        o6 = [2, 1]
        self.f(t6, 1)
        self.assertEqual(t6, o6)


def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

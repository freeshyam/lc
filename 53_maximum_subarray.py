#!/usr/bin/env python

import unittest

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = nums[0]
        for n in nums[1:]:
            max_ending_here = max(n, max_ending_here + n)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.maxSubArray

    def test_base(self):
        self.assertEqual(self.f([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

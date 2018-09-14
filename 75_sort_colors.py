#!/usr/bin/env python

import unittest

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        nums[:i] -> 0
        nums[i:j] -> 1
        nums[j:k] -> unknown
        nums[k:] -> 2
        """
        i = j = 0
        k = len(nums)

        while j < k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1
            elif nums[j] == 1:
                j += 1
            elif nums[j] == 2:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.sortColors

    def test_base(self):
        x1 = [2, 0, 2, 1, 1, 0]
        self.f(x1)
        self.assertEqual(x1, [0, 0, 1, 1, 2, 2])

        x2 = [0, 0, 2, 0, 0, 0, 0, 2, 0, 1]
        self.f(x2)
        self.assertEqual(x2, [0, 0, 0, 0, 0, 0, 0, 1, 2, 2])

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

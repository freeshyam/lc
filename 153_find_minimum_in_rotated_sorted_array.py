#!/usr/bin/env python

import unittest

"""
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while True:
            if left == right or nums[left] < nums[right]:
                return nums[left]

            mid = left + (right - left) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[left] >= nums[mid] <= nums[right]:
                right = mid - 1
            elif nums[left] <= nums[mid] >= nums[right]:
                left = mid + 1
"""

class Solution:
    def findMin(self, nums):
        pass

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.findMin

    def test_base(self):
        self.assertEqual(self.f([1, 0]), 0)
        self.assertEqual(self.f([0, 1, 2, 3, 4, 5, 6]), 0)
        self.assertEqual(self.f([6, 0, 1, 2, 3, 4, 5]), 0)
        self.assertEqual(self.f([5, 6, 0, 1, 2, 3, 4]), 0)
        self.assertEqual(self.f([4, 5, 6, 0, 1, 2, 3]), 0)
        self.assertEqual(self.f([3, 4, 5, 6, 0, 1, 2]), 0)
        self.assertEqual(self.f([2, 3, 4, 5, 6, 0, 1]), 0)
        self.assertEqual(self.f([1, 2, 3, 4, 5, 6, 0]), 0)


def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

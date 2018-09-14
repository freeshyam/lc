#!/usr/bin/env python

import unittest

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        right = 1
        for j in range(len(nums) - 2, -1, -1):
            right *= nums[j + 1]
            ans[j] *= right

        return ans

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.productExceptSelf

    def test_standard(self):
        self.assertEqual(self.f([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(self.f([2, 3, 4, 5]), [60, 40, 30, 24])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

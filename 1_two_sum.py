#!/usr/bin/env python

import unittest

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [i, d[num]]
            d[target - num] = i

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.twoSum([], 0), None)
        self.assertEqual(self.s.twoSum([1], 0), None)

    def test_standard(self):
        self.assertEqual(sorted(self.s.twoSum([2, 7, 11, 15], 9)), [0, 1])
        self.assertEqual(sorted(self.s.twoSum([2, 7, 11, 15], 18)), [1, 2])
        self.assertEqual(sorted(self.s.twoSum([2, 7, 11, 15], 17)), [0, 3])
        self.assertEqual(sorted(self.s.twoSum([2, -15, 11, 21], 6)), [1, 3])
        self.assertEqual(sorted(self.s.twoSum([2, 5, 5, 11], 10)), [1, 2])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

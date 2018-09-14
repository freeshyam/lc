#!/usr/bin/env python

import unittest


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_arr = sorted(nums)

        l = len(sorted_arr)
        even_indices = map(lambda x: x * 2, range(l / 2))

        return sum([sorted_arr[i] for i in even_indices])

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_standard(self):
        self.assertEqual(self.s.arrayPairSum([0, 1, 4, 5, 6, 7, 8, 9]), 18)
        self.assertEqual(self.s.arrayPairSum([1, 4, 3, 2]), 4)
        self.assertEqual(self.s.arrayPairSum([1, 2]), 1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

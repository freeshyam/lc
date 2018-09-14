#!/usr/bin/env python
from __future__ import print_function

import unittest
import collections

"""
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

# 1  2   7  8    9  10
# 6 ints

# 5 1 4 2 3
#
#

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




def perms(arr):
    if len(arr) == 1:
        return [arr]
    return [[arr[i]] + perm for i in range(len(arr)) for perm in perms(arr[:i] + arr[i+1:])]

class UT1(unittest.TestCase):
    def setUp(self):
        s = Solution()
        self.f = s.longestConsecutive

    def test_base(self):
        print(self.f([3, 4, 5, 100]))

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

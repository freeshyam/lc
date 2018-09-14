#!/usr/bin/env python

import unittest

def isBadVersion(version):
    badversions = [1, 2]
    if version in badversions:
        return True
    return False

class Solution(object):
    @staticmethod
    def foo(c, low, high):
        if low > high:
            return c

        m = low + (high - low) / 2

        if isBadVersion(m):
            return Solution.foo(m, low, m - 1)
        else:
            return Solution.foo(c, m + 1, high)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Solution.foo(None, 1, n)


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_standard(self):
        self.assertEqual(self.s.firstBadVersion(2), 1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

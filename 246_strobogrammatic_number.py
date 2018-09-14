#!/usr/bin/env python3

import unittest

class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        never_strobo = {'2', '3', '4', '5', '7'}
        strobo_solo = {'0', '1', '8'}
        d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        if any(digit in num for digit in never_strobo):
            return False

        i, j = 0, len(num) - 1
        while i <= j:
            if ((i == j and num[i] not in strobo_solo)
                or
                num[i] != d[num[j]]):
                return False
            i, j = i + 1, j - 1

        return True

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.isStrobogrammatic

    def test_standard(self):
        self.assertEqual(self.f('69'), True)
        self.assertEqual(self.f('88'), True)
        self.assertEqual(self.f('962'), False)
        self.assertEqual(self.f('609'), True)
        self.assertEqual(self.f('619'), True)
        self.assertEqual(self.f('689'), True)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

"""
def strobo_helper(s):
    if not s or (len(s) == 1 and s in strobo_solo):
        return True
    elif len(s) > 1:
        return s[0] == d[s[-1]] and strobo_helper(s[1:-1])
"""
#return strobo_helper(num)

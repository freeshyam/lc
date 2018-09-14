#!/usr/bin/env python

import unittest

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a

        s = a ^ b
        carry = (a & b) << 1
        return self.getSum(s, carry)

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.getSum(0, 0), 0)

    def test_standard(self):
        self.assertEqual(self.s.getSum(1, 1), 2)
        self.assertEqual(self.s.getSum(1, 2), 3)
        self.assertEqual(self.s.getSum(-9, 9), 0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

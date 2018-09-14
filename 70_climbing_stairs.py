#!/usr/bin/env python

import unittest

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        input: 1
        output: 1
        1

        input: 2
        output: 2
        1, 1
        2

        input: 3
        output: 3
        1, 1, 1
        1, 2
        2, 1

        input: 4
        output: 5
        1, 1, 1, 1
        2, 2
        1, 1, 2
        1, 2, 1
        2, 1, 1
        """

        if n < 3:
            return n

        a = 1
        b = 2
        for _ in range(2, n):
            a, b = b, a + b

        return b

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.climbStairs

    def test_base(self):
        self.assertEqual(self.f(1), 1)
        self.assertEqual(self.f(2), 2)
        self.assertEqual(self.f(3), 3)
        self.assertEqual(self.f(4), 5)
        self.assertEqual(self.f(5), 8)
        self.assertEqual(self.f(6), 13)
        self.assertEqual(self.f(7), 21)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

#!/usr/bin/env python

import unittest

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hw = 0

        while n > 0:
            hw += n & 1
            n = n >> 1

        return hw

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.hammingWeight(0), 0)

    def test_standard(self):
        # binary    decimal  number_of_ones
        # 00000000  0        0
        # 00000001  1        1
        # 00000010  2        1
        # 00000011  3        2
        # 00000100  4        1
        # 00000101  5        2
        # 00000110  6        2
        # 00000111  7        3
        # 00001000  8        1
        # 00001001  9        2
        # 00001010  10       2
        # 00001011  11       3
        # 00001100  12       2
        # 00001101  13       3
        # 00001110  14       3
        # 00001111  15       4
        # 00010000  16       1
        self.assertEqual(self.s.hammingWeight(1), 1)
        self.assertEqual(self.s.hammingWeight(2), 1)
        self.assertEqual(self.s.hammingWeight(3), 2)
        self.assertEqual(self.s.hammingWeight(4), 1)
        self.assertEqual(self.s.hammingWeight(5), 2)
        self.assertEqual(self.s.hammingWeight(6), 2)
        self.assertEqual(self.s.hammingWeight(7), 3)
        self.assertEqual(self.s.hammingWeight(8), 1)
        self.assertEqual(self.s.hammingWeight(9), 2)
        self.assertEqual(self.s.hammingWeight(10), 2)
        self.assertEqual(self.s.hammingWeight(11), 3)
        self.assertEqual(self.s.hammingWeight(12), 2)
        self.assertEqual(self.s.hammingWeight(13), 3)
        self.assertEqual(self.s.hammingWeight(14), 3)
        self.assertEqual(self.s.hammingWeight(15), 4)
        self.assertEqual(self.s.hammingWeight(16), 1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

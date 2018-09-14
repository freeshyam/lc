#!/usr/bin/env python

import unittest

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        output = [0] * (num + 1)

        for i in range(1, num + 1):
            #output[i] = output[i / 2] + (i % 2)
            output[i] = output[i >> 1] + (i & 1)

        return output

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.countBits(0), [0])

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
        self.assertEqual(self.s.countBits(16),
                         [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

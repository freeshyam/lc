#!/usr/bin/env python3

import unittest

class Solution:
    def findStrobogrammatic(self, n):
        strobo = []
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

        if n == 0:
            return strobo

        if n % 2 == 0:
            strobo.extend([''])
            k = 2 # start at 0 + 2
        else:
            strobo.extend(['0', '1', '8'])
            k = 3 # start at 1 + 2

        for i in range(k, n + 1, 2):
            pairs_to_use = pairs if i < n else pairs[1:]
            strobo = [head + base + tail for base in strobo
                      for head, tail in pairs_to_use]

        return strobo

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.findStrobogrammatic

    def test_standard(self):
        self.assertEqual(sorted(self.f(1)), sorted(['0', '1', '8']))
        self.assertEqual(sorted(self.f(2)), sorted(['11', '69', '88', '96']))
        self.assertEqual(sorted(self.f(3)), sorted(['101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986']))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

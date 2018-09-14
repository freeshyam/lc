#!/usr/bin/env python

import unittest

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value_seen = float('inf')
        max_profit_total = float('-inf')

        for price in prices:
            min_value_seen = min(min_value_seen, price)
            max_profit_total = max(max_profit_total, price - min_value_seen)

        return max_profit_total if max_profit_total > 0 else 0

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.maxProfit

    def test_base(self):
        self.assertEqual(self.f([7,1,5,3,6,4]), 5)
        self.assertEqual(self.f([7,6,4,3,1]), 0)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

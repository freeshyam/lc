#!/usr/bin/env python
from __future__ import print_function
import unittest

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAXVAL = float('inf')
        min_coins = [0] + [MAXVAL] * amount

        for target_amount in range(1, amount + 1):
            candidate_mins = []
            for coin in coins:
                if coin <= target_amount:
                    candidate_mins.append(min_coins[target_amount - coin] + 1)
            min_coins[target_amount] = min(candidate_mins) if candidate_mins else MAXVAL

        if min_coins[amount] != MAXVAL:
            return min_coins[amount]
        return -1

def coin_change_v2(coins, amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    coin_used = [0] * (amount + 1)

    for target_amount in range(1, amount + 1):
        for coin in (x for x in coins if x <= target_amount):
            c = min_coins[target_amount - coin]
            if c != float('inf'):

                if c + 1 < min_coins[target_amount]:
                    coin_used[target_amount] = coin

                min_coins[target_amount] = min(min_coins[target_amount], c + 1)

    if min_coins[amount] != float('inf'):
        x = amount
        coin_list = []

        while x > 0:
            coin_list.append(coin_used[x])
            x -= coin_used[x]

        return (min_coins[amount], coin_list)
    return (-1, None)

def report(coins, amount):
    print("coin =", coins, "amount =", amount)
    min_num_coins, coin_list = coin_change_v2(coins, amount)
    if min_num_coins != -1:
        print("minimum # of coins needed =", min_num_coins)
        print("coins used =", coin_list)
    else:
        print("no combination of coins {} can make {}"
              .format(coins, amount))
    print()

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.coinChange

    def test_standard(self):
        self.assertEqual(self.f([1, 2, 5], 11), 3)
        self.assertEqual(self.f([2], 3), -1)
        self.assertEqual(self.f([77, 82, 84, 80, 398, 286, 40, 136, 162], 9794), 26)
        self.assertEqual(self.f([342,268,284,65,217,461,245,249,106], 9278), 22)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    """
    report([1, 2, 5], 11)
    report([1, 2, 5], 88)
    report([1, 2, 5], 99)
    report([77,82,84,80,398,286,40,136,162], 9794)
    report([342,268,284,65,217,461,245,249,106], 9278)
    """

#!/usr/bin/env python
from __future__ import print_function

import unittest
import collections

def num_decodings_without_memoization(s):
    """
    :type s: str
    :rtype: int
    """
    def solve(start_idx, substr_len):
        if start_idx + substr_len - 1 < len(s):
            n = int(s[start_idx:start_idx+substr_len])
            if substr_len == 2 and n > 0 and n <= 9:
                return 0
            if n > 0 and n <= 26:
                if start_idx + substr_len == len(s):
                    return 1
                else:
                    return solve(start_idx + substr_len, 1) + solve(start_idx + substr_len, 2)
        return 0

    return solve(0, 1) + solve(0, 2)


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def solve(start_idx, substr_len):
            if (start_idx, substr_len) in d:
                return d[(start_idx, substr_len)]

            if start_idx + substr_len - 1 < len(s):
                n = int(s[start_idx:start_idx+substr_len])
                if substr_len == 2 and n > 0 and n <= 9:
                    d[(start_idx, substr_len)] = 0
                    return d[(start_idx, substr_len)]
                if n > 0 and n <= 26:
                    if start_idx + substr_len == len(s):
                        d[(start_idx, substr_len)] = 1
                        return d[(start_idx, substr_len)]
                    else:
                        d[(start_idx + substr_len, 1)] = solve(start_idx + substr_len, 1)
                        d[(start_idx + substr_len, 2)] = solve(start_idx + substr_len, 2)
                        return d[(start_idx + substr_len, 1)] + d[(start_idx + substr_len, 2)]

            d[(start_idx, substr_len)] = 0
            return d[(start_idx, substr_len)]

        d = {}
        return solve(0, 1) + solve(0, 2)

"""
0, 1
    1, 1
        2, 1
            3, 1
            3, 2
        2, 2
            4, 1
            4, 2
    1, 2
        3, 1
            4, 1
            4, 2
        3, 2
            5, 1
            5, 2
0, 2
    2, 1
        3, 1
            4, 1
            4, 2
        3, 2
            5, 1
            5, 2
    2, 2
        4, 1
            5, 1
            5, 2
        4, 2
            6, 1
            6, 2
"""

class UT1(unittest.TestCase):
    def setUp(self):
        s = Solution()
        self.f = s.numDecodings

    def test_base(self):
        self.assertEqual(self.f('0'), 0)
        self.assertEqual(self.f('01'), 0)
        self.assertEqual(self.f('12'), 2)
        self.assertEqual(self.f('226'), 3)
        self.assertEqual(self.f('3132946387264382619476912360'), 0)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    #unit_test(UT1)

    s = Solution()
    #print(s.numDecodings('236346126136213234141123134'))
    print(s.numDecodings('21212121212121427282193728378473819123484937432121212122121212121212142728219372837847381912348493743212121212121214272821937283784738191234849374321212121212121427282193728378473819123484937432121212121212142728219372837847381912348493743121214272821937283784738191234849374321212121212121427282193728378473819123484937432121212121212142728219372837847381912348493743'))

    #print(num_decodings_without_memoization('23634612613621323414114141123134'))
    #print(num_decodings_without_memoization('21212121212121427282193728378473819123484937432121212122121212121212142728219372837847381912348493743212121212121214272821937283784738191234849374321212121212121427282193728378473819123484937432121212121212142728219372837847381912348493743121214272821937283784738191234849374321212121212121427282193728378473819123484937432121212121212142728219372837847381912348493743'))

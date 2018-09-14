#!/usr/bin/env python

import unittest

class Solution:
    def num_inner_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        def dfs(r, c):
            if r < 0 or r == num_rows or c < 0 or c == num_cols:
                return False
            if grid[r][c] == '0':
                return True

            grid[r][c] = '0'

            res_left = dfs(r, c - 1)
            res_up = dfs(r - 1, c)
            res_right = dfs(r, c + 1)
            res_down = dfs(r + 1, c)

            return res_left and res_up and res_right and res_down

        num_rows = len(grid)
        num_cols = len(grid[0])

        inner_island_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1' and dfs(i, j):
                    inner_island_count += 1

        return inner_island_count


class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.num_inner_islands

    def test_base(self):
        m1 = self.s2g("""
            11110
            11010
            11000
            00000
            """)
        self.assertEqual(self.f(m1), 0)

        m2 = self.s2g("""
            11000
            11000
            00100
            00011
            """)
        self.assertEqual(self.f(m2), 1)

        m3 = self.s2g("""
            11000001100
            11000101100
            00111000000
            00011001100
            10000011001
            """)
        self.assertEqual(self.f(m3), 2)

        m4 = self.s2g("""
            11111111111
            00000000000
            11111111111
            00000000000
            11111111111
            00000000000
            11111111111
            """)
        self.assertEqual(self.f(m4), 0)

        m5 = self.s2g("""
            1000000001
            0111001110
            0110000110
            0001111000
            0001111000
            0001111000
            0001111000
            0110000110
            0111001110
            1000000001
            """)
        self.assertEqual(self.f(m5), 5)

        m6 = self.s2g("""
            11111111111
            00000100000
            11111111111
            00000100000
            11111111111
            00000100000
            11111111111
            """)
        self.assertEqual(self.f(m6), 0)

        m7 = self.s2g("""
            00000000000
            00000000000
            00000000000
            00000000000
            00000000000
            00000000000
            00000000000
            """)
        self.assertEqual(self.f(m7), 0)

    def test_edge(self):
        self.assertEqual(self.f([]), 0)
        self.assertEqual(self.f([[]]), 0)

        m1 = self.s2g("""
            0
            """)
        self.assertEqual(self.f(m1), 0)

        m2 = self.s2g("""
            1
            """)
        self.assertEqual(self.f(m2), 0)

        m3 = self.s2g("""
            01101101100
            """)
        self.assertEqual(self.f(m3), 0)

        m4 = self.s2g("""
            1
            0
            1
            1
            0
            1
            0
            1
            1
            1
            0
            """)
        self.assertEqual(self.f(m4), 0)

        m5 = self.s2g("""
            1111111111
            0000000001
            1111111101
            1000000101
            1011110101
            1010010101
            1010000101
            1011111101
            1000000001
            1111111111
            """)
        self.assertEqual(self.f(m5), 0)

        m6 = self.s2g("""
            1111111111
            1000000001
            1011111101
            1010000101
            1010110101
            1010110101
            1010000101
            1011111101
            1000000001
            1111111111
            """)
        self.assertEqual(self.f(m6), 2)

        m7 = self.s2g("""
            01010101010
            10101010101
            01010101010
            10101010101
            01010101010
            10101010101
            01010101010
            """)
        self.assertEqual(self.f(m7), 22)

        m8 = self.s2g("""
            0000000110
            0011011110
            0011011000
            0000000100
            1111001100
            0111000000
            0001110000
            0001110110
            0001010110
            0000010000
            """)
        self.assertEqual(self.f(m8), 3)

    @staticmethod
    def s2g(s):
        """
        Converts an island map in string form, e.g.

            11000
            11000
            00100
            00011

        into a grid (List[List[str]]):

            [['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']]
        """
        return [[c for c in line.strip()] for line in s.strip().split('\n')]

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

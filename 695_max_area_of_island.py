#!/usr/bin/env python

import unittest

class Solution:
    def dfs(self, grid, num_rows, num_cols, r, c):
        if grid[r][c] == 0:
            return 0

        # saw a 1, so make it a 0
        grid[r][c] = 0

        size = 1

        # can go left
        if c > 0:
            size += self.dfs(grid, num_rows, num_cols, r, c - 1)

        # can go up
        if r > 0:
            size += self.dfs(grid, num_rows, num_cols, r - 1, c)

        # can go right
        if c < num_cols - 1:
            size += self.dfs(grid, num_rows, num_cols, r, c + 1)

        # can go down
        if r < num_rows - 1:
            size += self.dfs(grid, num_rows, num_cols, r + 1, c)

        return size

    def maxAreaOfIsland(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])

        max_island_size = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    max_island_size = max(max_island_size, self.dfs(grid, num_rows, num_cols, r, c))

        return max_island_size

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.maxAreaOfIsland

    def test_base(self):
        g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.assertEqual(self.f(g), 6)

        g = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(self.f(g), 0)

        g = [[0]]
        self.assertEqual(self.f(g), 0)

        g = [[1]]
        self.assertEqual(self.f(g), 1)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

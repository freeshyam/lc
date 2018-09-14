#!/usr/bin/env python

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.size = 1

class UnionFind:
    def __init__(self):
        self.d = {}
        self._num_sets = 0

    @property
    def num_sets(self):
        return self._num_sets

    def add(self, key):
        if key not in self.d:
            self.d[key] = Node(key)
            self._num_sets += 1

    def find(self, key):
        p = self.d[key]

        # find the root ancestor of p.
        # when the loop terminates, p is the root ancestor
        children = []
        while p.parent is not p:
            children.append(p)
            p = p.parent

        # path compression
        for child in children:
            child.parent = p

        return p

    def union(self, x_key, y_key):
        x_node, y_node = self.find(x_key), self.find(y_key)

        if x_node is not y_node:

            big, small = x_node, y_node
            if small.size > big.size:
                big, small = small, big

            small.parent = big
            big.size += small.size

            self._num_sets -= 1


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])
        island_tracker = UnionFind()

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    island_tracker.add((row, col))

                    # check cell left of current position for island
                    if col > 0 and grid[row][col - 1] == '1':
                        island_tracker.union((row, col), (row, col - 1))

                    # check cell above of current position for island
                    if row > 0 and grid[row - 1][col] == '1':
                        island_tracker.union((row, col), (row - 1, col))

        return island_tracker.num_sets


class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.numIslands

    def test_base(self):
        m1 = self.s2g("""
            11110
            11010
            11000
            00000
            """)
        self.assertEqual(self.f(m1), 1)

        m2 = self.s2g("""
            11000
            11000
            00100
            00011
            """)
        self.assertEqual(self.f(m2), 3)

        m3 = self.s2g("""
            11000001100
            11000101100
            00111000000
            00011001100
            10000011001
            """)
        self.assertEqual(self.f(m3), 7)

        m4 = self.s2g("""
            11111111111
            00000000000
            11111111111
            00000000000
            11111111111
            00000000000
            11111111111
            """)
        self.assertEqual(self.f(m4), 4)

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
        self.assertEqual(self.f(m5), 9)

        m6 = self.s2g("""
            11111111111
            00000100000
            11111111111
            00000100000
            11111111111
            00000100000
            11111111111
            """)
        self.assertEqual(self.f(m6), 1)

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
        self.assertEqual(self.f(m2), 1)

        m3 = self.s2g("""
            01101101100
            """)
        self.assertEqual(self.f(m3), 3)

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
        self.assertEqual(self.f(m4), 4)

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
        self.assertEqual(self.f(m5), 1)

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
        self.assertEqual(self.f(m6), 3)

        m7 = self.s2g("""
            01010101010
            10101010101
            01010101010
            10101010101
            01010101010
            10101010101
            01010101010
            """)
        self.assertEqual(self.f(m7), 38)

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

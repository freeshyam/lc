#!/usr/bin/env python

import unittest

from collections import defaultdict

class Solution:
    def longestIncreasingPath(self, matrix):
        # [] or [[]]
        if not matrix or not matrix[0]:
            return 0

        next_moves = defaultdict(list)
        num_inbound_edges = defaultdict(int)

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # special case: 1x1 matrix, e.g. [[1]]
        if num_rows == 1 and num_cols == 1:
            return 1

        for row in range(num_rows):
            for col in range(num_cols):
                # can look up
                if row > 0 and matrix[row - 1][col] > matrix[row][col]:
                    next_moves[(row, col)].append((row - 1, col))
                    num_inbound_edges[(row - 1, col)] += 1

                # can look right
                if col < num_cols - 1 and matrix[row][col + 1] > matrix[row][col]:
                    next_moves[(row, col)].append((row, col + 1))
                    num_inbound_edges[(row, col + 1)] += 1

                # can look down
                if row < num_rows - 1 and matrix[row + 1][col] > matrix[row][col]:
                    next_moves[(row, col)].append((row + 1, col))
                    num_inbound_edges[(row + 1, col)] += 1

                # can look left
                if col > 0 and matrix[row][col - 1] > matrix[row][col]:
                    next_moves[(row, col)].append((row, col - 1))
                    num_inbound_edges[(row, col - 1)] += 1

        start_positions = [(row, col) for row in range(num_rows) for col in range(num_cols)
                           if (row, col) not in num_inbound_edges]

        return max(self.dfs(next_moves, num_inbound_edges, pos, 1) for pos in start_positions)

    def dfs(self, next_moves, num_inbound_edges, position, path_length):
        if position not in next_moves:
            print(path_length, "at", position)
            return path_length

        for next_pos in next_moves[position]:
            if num_inbound_edges[next_pos] > 0:
                num_inbound_edges[next_pos] -= 1

        lengths = []
        for next_pos in next_moves[position]:
            if num_inbound_edges[next_pos] == 0:
                #print('{} --> {}, path_length = {}'.format(position, next_pos, path_length))
                lengths.append(self.dfs(next_moves, num_inbound_edges, next_pos, path_length + 1))

        return max(lengths) if lengths else path_length + 1

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.longestIncreasingPath

    def test_base(self):
        '''
        self.assertEqual(self.f([]), 0)
        self.assertEqual(self.f([[]]), 0)
        self.assertEqual(self.f([[1]]), 1)
        self.assertEqual(self.f([[1, 2, 3]]), 3)

        nums = [[1],
                [2],
                [3]]
        self.assertEqual(self.f(nums), 3)

        nums = [[9, 9, 4],
                [6, 6, 8],
                [2, 1, 1]]
        self.assertEqual(self.f(nums), 4)

        nums = [[3, 4, 5],
                [3, 2, 6],
                [2, 2, 1]]
        self.assertEqual(self.f(nums), 4)
        '''

        nums = [[0,1,2,3,4,5,6,7,8,9],
                [19,18,17,16,15,14,13,12,11,10],
                [20,21,22,23,24,25,26,27,28,29],
                [39,38,37,36,35,34,33,32,31,30],
                [40,41,42,43,44,45,46,47,48,49],
                [59,58,57,56,55,54,53,52,51,50],
                [60,61,62,63,64,65,66,67,68,69],
                [79,78,77,76,75,74,73,72,71,70],
                [80,81,82,83,84,85,86,87,88,89],
                [99,98,97,96,95,94,93,92,91,90],
                [100,101,102,103,104,105,106,107,108,109],
                [119,118,117,116,115,114,113,112,111,110],
                [120,121,122,123,124,125,126,127,128,129],
                [139,138,137,136,135,134,133,132,131,130],
                [0,0,0,0,0,0,0,0,0,0]]
        #self.assertEqual(self.f(nums), 140)

        nums = [[0,1,2,3,4,5,6,7,8,9],
                [19,18,17,16,15,14,13,12,11,10],
                [20,21,22,23,24,25,26,27,28,29],
                [39,38,37,36,35,34,33,32,31,30],
                [40,41,42,43,44,45,46,47,48,49],
                [0,0,0,0,0,0,0,0,0,0]]
        self.assertEqual(self.f(nums), 50)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)
    """
    s = Solution()
    nums = [[0,1,2,3,4,5,6,7,8,9],
            [19,18,17,16,15,14,13,12,11,10],
            [20,21,22,23,24,25,26,27,28,29],
            [39,38,37,36,35,34,33,32,31,30],
            [40,41,42,43,44,45,46,47,48,49],
            [59,58,57,56,55,54,53,52,51,50],
            [60,61,62,63,64,65,66,67,68,69],
            [79,78,77,76,75,74,73,72,71,70],
            [80,81,82,83,84,85,86,87,88,89],
            [99,98,97,96,95,94,93,92,91,90],
            [100,101,102,103,104,105,106,107,108,109],
            [119,118,117,116,115,114,113,112,111,110],
            [120,121,122,123,124,125,126,127,128,129],
            [139,138,137,136,135,134,133,132,131,130],
            [0,0,0,0,0,0,0,0,0,0]]
    print(s.longestIncreasingPath(nums))
    """

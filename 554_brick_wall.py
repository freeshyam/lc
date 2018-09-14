#!/usr/bin/env python

import unittest

from collections import Counter

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        c = Counter()
        num_rows = len(wall)

        for row in wall:
            acc = 0
            for num in row[:-1]:
                acc += num
                c[acc] += 1

        # number of occurrences of the most common prefix sum in c (if c is not empty)
        num_occ = c.most_common(1)[0][1] if c else 0

        return num_rows - num_occ

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.leastBricks

    def test_base(self):
        t1 = [[1,2,2,1],
              [3,1,2],
              [1,3,2],
              [2,4],
              [3,1,2],
              [1,3,1,1]]
        self.assertEqual(self.f(t1), 2)

        t2 = [[1,2,2,1],
              [6],
              [2,1,3],
              [3,3],
              [6],
              [6]]
        self.assertEqual(self.f(t2), 3)

        t3 = [[6],
              [6],
              [6],
              [3,3],
              [6],
              [6]]
        self.assertEqual(self.f(t3), 5)

        t4 = [[6],
              [6],
              [6],
              [6],
              [6],
              [6]]
        self.assertEqual(self.f(t4), 6)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)


#!/usr/bin/env python

import unittest

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from itertools import islice

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if not intervals:
            return res

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        res.append(sorted_intervals[0])

        for interval in islice(sorted_intervals, 1, None):
            if self.is_intersecting(res[-1], interval):
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)

        return res

    def is_intersecting(self, x, y):
        """
        Returns True if the two intervals are intersecting.
        Precondition: x.start <= y.start

        :type x: Interval
        :type y: Interval
        :rtype: bool
        """
        return y.start <= x.end

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def itt(intervals):
    return [(i.start, i.end) for i in intervals]

class UT1(unittest.TestCase):
    def setUp(self):
        s = Solution()
        self.f = s.merge

    def test_base(self):
        tc0 = []
        self.assertEqual(itt(self.f(tc0)), [])

        tc1 = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
        self.assertEqual(itt(self.f(tc1)), [(1, 6), (8, 10), (15, 18)])

        tc2 = [Interval(0, 3), Interval(3, 5), Interval(-5, -2), Interval(-17, -3)]
        self.assertEqual(itt(self.f(tc2)), [(-17, -2), (0, 5)])

        tc3 = [Interval(5, 7), Interval(1, 4), Interval(5, 11), Interval(-1, 2)]
        self.assertEqual(itt(self.f(tc3)), [(-1, 4), (5, 11)])

        tc4 = [Interval(3, 9), Interval(14, 14), Interval(2, 4), Interval(16, 17),
               Interval(11, 13), Interval(1, 50)]
        self.assertEqual(itt(self.f(tc4)), [(1, 50)])

        tc5 = [Interval(3, 9), Interval(14, 14), Interval(2, 4), Interval(16, 17),
               Interval(11, 13), Interval(17, 20)]
        self.assertEqual(itt(self.f(tc5)), [(2, 9), (11, 13), (14, 14), (16, 20)])

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

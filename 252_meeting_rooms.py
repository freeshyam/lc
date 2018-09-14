#!/usr/bin/env python

import unittest

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        ivals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(ivals)):
            if ivals[i].start < ivals[i - 1].end:
                return False
        return True

def t2i(tuple_intervals):
    return [Interval(s, e) for s, e, in tuple_intervals]

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.canAttendMeetings

    def test_base(self):
        self.assertEqual(self.f(t2i([])), True)

        intervals = [(0, 30), (5, 10), (15, 20)]
        self.assertEqual(self.f(t2i(intervals)), False)

        intervals = [(7, 10), (2, 4)]
        self.assertEqual(self.f(t2i(intervals)), True)

        intervals = [(13, 15), (1, 13)]
        self.assertEqual(self.f(t2i(intervals)), True)

        intervals = [(1, 2)]
        self.assertEqual(self.f(t2i(intervals)), True)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

#!/usr/bin/env python

import unittest

"""
class HitCounter(object):
    def __init__(self):
        self.timestamps = []
        self.timestamp_to_hits = {}
        self._DURATION = 60 * 5

    def hit(self, timestamp):
        if timestamp not in self.timestamp_to_hits:
            self.timestamps.append(timestamp)

        self.timestamp_to_hits[timestamp] = self.timestamp_to_hits.get(timestamp, 0) + 1

    def getHits(self, timestamp):
        start_idx = self._get_index_of_earliest_timestamp(timestamp)

        if start_idx == -1:
            return 0

        return sum(self.timestamp_to_hits[self.timestamps[i]]
                   for i in range(start_idx, len(self.timestamps)))

    def _get_index_of_earliest_timestamp(self, timestamp):
        # timestamp from which we start counting hits
        start_timestamp = timestamp - self._DURATION + 1

        i, j = 0, len(self.timestamps) - 1
        while i <= j:
            mid_idx = (i + j) // 2
            if start_timestamp <= self.timestamps[mid_idx]:
                if (mid_idx - 1 == -1
                    or self.timestamps[mid_idx - 1] < start_timestamp):
                    return mid_idx
                j = mid_idx - 1
            else:
                i = mid_idx + 1

        return -1
"""

from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # deque containing lists of length 2;
        # each list is of the form [timestamp, hit_count]
        self.counts = deque()
        self.total_hits = 0
        self._DURATION = 60 * 5

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if self.counts and self.counts[-1][0] == timestamp:
            self.counts[-1][1] += 1
        else:
            self.counts.append([timestamp, 1])
        self.total_hits += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        start_timestamp = timestamp - self._DURATION + 1

        while self.counts and self.counts[0][0] < start_timestamp:
            self.total_hits -= self.counts[0][1]
            self.counts.popleft()

        return self.total_hits

"""
307 -> [8, 307]

0  1  2   3   4   5   6    7    8
3, 5, 6, 10, 11, 12, 20, 240, 255

"""

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

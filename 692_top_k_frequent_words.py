#!/usr/bin/env python

from __future__ import print_function
import unittest

from collections import Counter, deque
from itertools import islice
import heapq

"""
class Solution:
    def topKFrequent(self, words, k):
        # :type words: List[str]
        # :type k: int
        # :rtype: List[str]
        c = Counter(words)
        return [word for word, _ in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:k]]
"""

class WordFreq:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif (self.count == other.count
              and self.word > other.word):
            return True
        return False

class Solution:
    def topKFrequent(self, words, k):
        # :type words: List[str]
        # :type k: int
        # :rtype: List[str]

        c = Counter(words)

        min_heap = []
        count_items = c.items()

        for word, count in islice(count_items, 0, k):
            heapq.heappush(min_heap, WordFreq(word, count))

        for word, count in islice(count_items, k, None):
            heapq.heappushpop(min_heap, WordFreq(word, count))

        r = deque()
        for _ in range(k):
            r.appendleft(heapq.heappop(min_heap).word)

        return list(r)

# Try to solve it in O(n log k) time and O(n) extra space.
# Can you solve it in O(n) time with only O(k) extra space?

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_standard(self):
        s0_input = "rome wasn't built in a day".split()
        s0_k = 3
        s0_ans = ["a", "built", "day"]

        s1_input = "oh the the the fun abc abc kjlhas dfhalk lh dfjl ahjfsafjlk then then then abc bay bay bay".split()
        s1_k = 3
        s1_ans = ["abc", "bay", "the"]

        s2_input = "zebra yellow xylophone rand op cat cat apple sand apple juice apple jack bob cat cat zebra".split()
        s2_k = 4
        s2_ans = ["cat", "apple", "zebra", "bob"]

        #self.assertEqual(self.s.topKFrequent(s0_input, s0_k), s0_ans)
        self.assertEqual(self.s.topKFrequent(s1_input, s1_k), s1_ans)
        self.assertEqual(self.s.topKFrequent(s2_input, s2_k), s2_ans)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/env python

import unittest

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        max_heap = [(-count, char) for char, count in Counter(S).items()]
        heapq.heapify(max_heap)
        out = []

        while max_heap:
            count0, char0 = heapq.heappop(max_heap)
            if not out or out[-1] != char0:
                out.append(char0)
                if count0 + 1 < 0:
                    heapq.heappush(max_heap, (count0 + 1, char0))
            elif max_heap:
                count1, char1 = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (count0, char0))
                out.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(max_heap, (count1 + 1, char1))
            else:
                return ''

        return ''.join(out)

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.reorganizeString

    def test_base(self):
        self.assertEqual(self.f('aab'), 'aba')
        self.assertEqual(self.f('aaab'), '')
        self.assertEqual(self.f('aaaaaaaaaaaaaabbbb'), '')
        self.assertEqual(self.f('aaaaabbbbb'), 'ababababab')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

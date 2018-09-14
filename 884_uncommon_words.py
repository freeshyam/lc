#!/usr/bin/env python

import unittest
from collections import Counter

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_words = set(A.split())
        B_words = set(B.split())
        A_exactly_once = {word for word, count in Counter(A.split()).items() if count == 1}
        B_exactly_once = {word for word, count in Counter(B.split()).items() if count == 1}

        return list((A_exactly_once ^ B_exactly_once) - (A_words & B_words))

class UT1(unittest.TestCase):
    def setUp(self):
        s = Solution()
        self.f = s.uncommonFromSentences

    def test_base(self):
        self.assertEqual(sorted(self.f('this apple is sweet', 'this apple is sour')), sorted(['sweet', 'sour']))
        self.assertEqual(sorted(self.f('apple apple', 'banana')), sorted(['banana']))
        self.assertEqual(sorted(self.f('s z z z s', 's z ejt')), sorted(['ejt']))

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

#!/usr/bin/env python

import unittest

from collections import deque, defaultdict

class Solution:
    @staticmethod
    def first_char_difference(word1, word2):
        """
        Return the first character difference between word1 and word2
        as a 2-tuple if it exists, otherwise None.

        If word1 is a prefix of word2 (or vice-versa), None is returned.
        """
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                return (c1, c2)
        return None

    @staticmethod
    def lt_mappings(word_list):
        """
        Given a list of lexographically sorted words,
        return a set of 2-tuple character comparisons (c1, c2),
        where c1 < c2 for each tuple.
        """
        mappings = set()
        for i in range(0, len(word_list) - 1):
            r = Solution.first_char_difference(word_list[i], word_list[i + 1])
            if r:
                mappings.add(r)

        return mappings

    def alienOrder(self, words):
        unique_chars = set(''.join(words))

        # character -> the set of characters greater than it
        char_to_chars_gt = defaultdict(set)

        # character -> the number of characters it is greater than
        char_to_num_gt = defaultdict(int)

        for c1, c2 in self.lt_mappings(words):
            char_to_chars_gt[c1].add(c2)
            char_to_num_gt[c2] += 1

        topo_sort = []

        # start with all characters that are not greater than any other character
        q = deque(c for c in unique_chars if c not in char_to_num_gt)

        while q:
            curr_char = q.popleft()
            topo_sort.append(curr_char)

            if curr_char in char_to_chars_gt:
                for c in char_to_chars_gt[curr_char]:
                    char_to_num_gt[c] -= 1
                    if char_to_num_gt[c] == 0:
                        q.append(c)

        return ''.join(topo_sort) if len(topo_sort) == len(unique_chars) else ''


class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.alienOrder

    def test_base(self):
        word_list = [
            'wrt',
            'wrf',
            'er',
            'ett',
            'rftt'
        ]
        self.assertEqual(self.f(word_list), 'wertf')

        self.assertEqual(self.f(['z', 'x']), 'zx')
        self.assertEqual(self.f(['z']), 'z')
        self.assertEqual(self.f(['z', 'z']), 'z')
        self.assertEqual(self.f(['z', 'x', 'z']), '')

        word_list = [
            'www',
            'we',
            'wr',
            'wt',
            'wf',
            'eee',
            'er',
            'et',
            'ef',
            'rrr',
            'rt',
            'rf',
            'ttt',
            'tf',
            'few',
            'fff'
        ]
        self.assertEqual(self.f(word_list), 'wertf')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

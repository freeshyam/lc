#!/usr/bin/env python3

import unittest

"""
0  1  2  3  4  5  6  7  8
a  b  c  d  e  f  g  a  b

length = 9
length - max = 9-7 = 2
"""

"""
def lengthOfLongestSubstring(self, s):
    n = len(s)
    cset = set()

    i = 0
    j = 0
    max_len = 0
    while j < n:
        if s[j] not in cset:
            cset.add(s[j])
            j += 1
            max_len = max(max_len, j - i)
        else:
            cset.remove(s[i])
            i += 1

    return max_len
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_to_idx = {}

        max_len = 0
        start_of_subtr_idx = 0

        for idx, c in enumerate(s):
            if c in char_to_idx:
                start_of_subtr_idx = max(start_of_subtr_idx, char_to_idx[c] + 1)

            max_len = max(max_len, idx - start_of_subtr_idx + 1)
            char_to_idx[c] = idx

        return max_len

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.lengthOfLongestSubstring

    def test_standard(self):
        self.assertEqual(self.f('abcabcbb'), 3)
        self.assertEqual(self.f('bbbbb'), 1)
        self.assertEqual(self.f('pwwkew'), 3)
        self.assertEqual(self.f('abcdefgabcdefg'), 7)
        self.assertEqual(self.f(' '), 1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

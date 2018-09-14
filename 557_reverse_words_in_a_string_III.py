#!/usr/bin/env python

import unittest

class Solution(object):
    @staticmethod
    def revword(s):
        # Method 1: Convert string to a list of characters,
        #           reverse the list, then concatenate the characters
        #           in the list back into a string
        #
        #revcharlist = list(s)
        #revcharlist.reverse()
        #return ''.join(revcharlist)

        # Method 2: Old-school reverse iteration over the string
        #           and concatenation
        #
        #output = ""
        #for i in range(len(s) - 1, -1, -1):
        #    output += s[i]
        #return output

        # Method 3: Python built-ins (reverse iterator + join)
        return ''.join(reversed(s))

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        return ' '.join(map(self.revword, word_list))

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.reverseWords(""), "")

    def test_standard(self):
        self.assertEqual(self.s.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")
        self.assertEqual(self.s.reverseWords("Write some more songs using this"), "etirW emos erom sgnos gnisu siht")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

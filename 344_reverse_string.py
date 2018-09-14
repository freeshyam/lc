#!/usr/bin/env python3

import unittest

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        ls = len(s)
        x = ls // 2

        r = ls

        for i in range(0, x):
            r -= 1
            l[i], l[r] = l[r], l[i]

        return "".join(l)

        # 4 -> 2
        # 5 -> 2
        # 0, 1 | 3, 2
        # 0, 1 | 4, 3
        # 0, 5 - 1 = 4
        # 1, 4 - 1 = 3
        # 0, 4 - 1 = 3
        # 1, 3 - 1 = 2
        """
        for i in range(0, x):
            right_index = ls - 1 - i
            tmp = l[i]
            l[i] = l[right_index]
            l[right_index] = tmp

        return "".join(l)
        """

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.reverseString(""), "")

    def test_standard(self):
        self.assertEqual(self.s.reverseString("bob"), "bob")
        self.assertEqual(self.s.reverseString("dog"), "god")
        self.assertEqual(self.s.reverseString("cat"), "tac")
        self.assertEqual(self.s.reverseString("1298"), "8921")
        self.assertEqual(self.s.reverseString("giraffe"), "effarig")
        self.assertEqual(self.s.reverseString("aabb"), "bbaa")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

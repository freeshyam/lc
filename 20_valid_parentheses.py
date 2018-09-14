#!/usr/bin/env python

import unittest

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        m = {')': '(',
             '}': '{',
             ']': '['}

        open_p = m.values()
        close_p = m.keys()

        for c in s:
            if c in open_p:
                stack.append(c)
            elif c in close_p:
                try:
                    x = stack.pop()
                except IndexError as e:
                    return False
                if x != m[c]:
                    return False

        return not stack

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertTrue(self.s.isValid(""))

    def test_standard(self):
        self.assertTrue(self.s.isValid("()"))
        self.assertTrue(self.s.isValid("(){}[]"))
        self.assertTrue(self.s.isValid("[{()}]"))

    def test_negative(self):
        self.assertFalse(self.s.isValid("("))
        self.assertFalse(self.s.isValid(")"))
        self.assertFalse(self.s.isValid("[{]"))
        self.assertFalse(self.s.isValid("[{("))
        self.assertFalse(self.s.isValid("[{()}"))
        self.assertFalse(self.s.isValid("]"))
        self.assertFalse(self.s.isValid("([)]"))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

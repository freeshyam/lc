#!/usr/bin/env python

import unittest

class Solution(object):
    def simplifyPath(self, path):
        pl = filter(lambda x: x, path.split("/"))
        stack = []
        for token in pl:
            if token == ".":
                pass
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return "/" + "/".join(stack)

    def simplifyPath2(self, path):
        stack = ["/"]
        token = ""
        for c in path:
            if c == "/":
                self.handle_token(token, stack)
                token = ""

                if stack[-1] != "/":
                    stack.append(c)
            else:
                token += c
        self.handle_token(token, stack)

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack)

    def handle_token(self, token, stack):
        if token:
            if token == ".":
                pass
            elif token == "..":
                if len(stack) > 1:
                    stack.pop()
                    stack.pop()
            else:
                stack.append(token)

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.simplifyPath(""), "/")
        self.assertEqual(self.s.simplifyPath("/"), "/")

    def test_level1(self):
        self.assertEqual(self.s.simplifyPath("/a/b/"), "/a/b")
        self.assertEqual(self.s.simplifyPath("/a/adj/c"), "/a/adj/c")
        self.assertEqual(self.s.simplifyPath("/lol.doc"), "/lol.doc")
        self.assertEqual(self.s.simplifyPath("/c/../../../../jj/"), "/jj")
        self.assertEqual(self.s.simplifyPath("/kaj/ca/bb///////c/"), "/kaj/ca/bb/c")
        self.assertEqual(self.s.simplifyPath("/jajk/$&*($daskd//"), "/jajk/$&*($daskd")
        self.assertEqual(self.s.simplifyPath("/ajlkja/ada/a/sas/sa/as/a/"), "/ajlkja/ada/a/sas/sa/as/a")

    def test_level2(self):
        self.assertEqual(self.s.simplifyPath("/../"), "/")
        self.assertEqual(self.s.simplifyPath("/home/"), "/home")
        self.assertEqual(self.s.simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(self.s.simplifyPath("/./a"), "/a")
        self.assertEqual(self.s.simplifyPath("/a/b/../d/./../n"), "/a/n")
        self.assertEqual(self.s.simplifyPath("/abc/123/."), "/abc/123")
        self.assertEqual(self.s.simplifyPath("/abc/123/.."), "/abc")
        self.assertEqual(self.s.simplifyPath("/al/jsdha//////jkas///sample.txt"), "/al/jsdha/jkas/sample.txt")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/env python

import unittest

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate_helper(valid_prefix, left_needed, right_needed):
            if right_needed == 0:
                out.append(valid_prefix)

            if left_needed > 0:
                generate_helper(valid_prefix + '(', left_needed - 1, right_needed)

            if right_needed > left_needed:
                generate_helper(valid_prefix + ')', left_needed, right_needed - 1)

        out = []
        generate_helper('', n, n)
        return out

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.generateParenthesis

    def test_base(self):
        out = [
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()'
        ]
        self.assertEqual(sorted(self.f(3)), out)

        out = [
            '(((())))',
            '((()()))',
            '((())())',
            '((()))()',
            '(()(()))',
            '(()()())',
            '(()())()',
            '(())(())',
            '(())()()',
            '()((()))',
            '()(()())',
            '()(())()',
            '()()(())',
            '()()()()'
        ]
        self.assertEqual(sorted(self.f(4)), out)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

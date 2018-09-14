#!/usr/bin/env python

import unittest

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        output = ['']

        for d in digits:
            output[:] = [s + letter for s in output for letter in digit_to_chars[d]]

        return output

"""
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        output = []
        arr = [0] * len(digits)

        def generate(idx):
            if idx == len(digits):
                output.append(''.join(arr))
            else:
                for c in digit_to_chars[digits[idx]]:
                    arr[idx] = c
                    generate(idx + 1)

        generate(0)

        return output
"""

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.letterCombinations

    def test_base(self):
        self.assertEqual(self.f(''), [])
        self.assertEqual(self.f('23'), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

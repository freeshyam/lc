#!/usr/bin/env python

import unittest

class Solution(object):
    def myAtoi(self, str):
        # 0 is the initial/default value of the integer answer
        # if the beginning part of str (excluding whitespace) cannot
        # be identified as an integer
        i = 0
        sign = 1
        plusminus = "+-"
        digits = "0123456789"
        d = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
             "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        INT_MAX = 2**31 - 1
        INT_MIN = -1 * 2**31

        stack = []
        s = str.strip()
        if s:
            first = s[0]
            if first in plusminus:
                s = s[1:]
                if first == "-":
                    sign = -1
            for c in s:
                if c in digits:
                    stack.append(c)
                else:
                    break

            factor = 1
            while stack:
                digit = stack.pop()
                i += d[digit] * factor
                factor *= 10

        ans = i * sign
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN

        return ans

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.myAtoi(""), 0)

    def test_standard(self):
        self.assertEqual(self.s.myAtoi("1"), 1)
        self.assertEqual(self.s.myAtoi("8219"), 8219)
        self.assertEqual(self.s.myAtoi("+42"), 42)
        self.assertEqual(self.s.myAtoi("0042"), 42)
        self.assertEqual(self.s.myAtoi("-42"), -42)

    def test_float(self):
        self.assertEqual(self.s.myAtoi("892.291"), 892)
        self.assertEqual(self.s.myAtoi("+19.31"), 19)
        self.assertEqual(self.s.myAtoi("-19.31"), -19)

    def test_mixed(self):
        self.assertEqual(self.s.myAtoi("4120 absak kqjw"), 4120)
        self.assertEqual(self.s.myAtoi("77abc"), 77)
        self.assertEqual(self.s.myAtoi("293-01"), 293)

    def test_invalid(self):
        self.assertEqual(self.s.myAtoi("--8912"), 0)
        self.assertEqual(self.s.myAtoi("++8912"), 0)
        self.assertEqual(self.s.myAtoi("anlks8132"), 0)
        self.assertEqual(self.s.myAtoi(".9123"), 0)

    def test_whitespace(self):
        self.assertEqual(self.s.myAtoi("   "), 0)
        self.assertEqual(self.s.myAtoi("   1302"), 1302)
        self.assertEqual(self.s.myAtoi("   1302    "), 1302)
        self.assertEqual(self.s.myAtoi("   -232    "), -232)
        self.assertEqual(self.s.myAtoi("   +232    "), 232)

    def test_edgemaxmin(self):
        self.assertEqual(self.s.myAtoi("2147483647"), 2147483647)
        self.assertEqual(self.s.myAtoi("2147483648"), 2147483647)
        self.assertEqual(self.s.myAtoi("-2147483648"), -2147483648)
        self.assertEqual(self.s.myAtoi("-2333333333"), -2147483648)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

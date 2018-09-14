#!/usr/bin/env python3

import unittest

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        length = len(s)
        max_i = length - 1
        twok = 2 * k

        curr = 0
        r = curr + twok - 1

        while curr < length and r < length:
            self.rev(l, curr, curr + k - 1)
            curr = r + 1
            r = curr + twok - 1

        if curr < length and max_i - curr + 1 < k:
            self.rev(l, curr, max_i)
        elif curr < length and max_i - curr + 1 >= k:
            self.rev(l, curr, curr + k - 1)

        return "".join(l)

    def rev(self, l, a, b):
        if a < b:
            length = b - a + 1
            m = length // 2
            j = b

            # a=2, b=4 -> 2, 3, 4
            # length = 3
            # m = 1
            # range(2, 2 + 1) = [2]
            # r = b
            # i is counter being incremented
            # j is counter being decremented
            for i in range(a, a + m):
                l[i], l[j] = l[j], l[i]
                j -= 1

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        pass
        #self.assertEqual(self.s.reverseString(""), "")

    def test_standard(self):
        self.assertEqual(self.s.reverseStr("abcdefg", 2), "bacdfeg")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

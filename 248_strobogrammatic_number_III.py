#!/usr/bin/env python3

import unittest

class Solution:
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        low_i = int(low)
        high_i = int(high)

        ans = [[] for _ in range(len(high) + 1)]
        ans[0].extend([''])
        ans[1].extend(['0', '1', '8'])

        count = 0

        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

        for i in range(2, len(high) + 1):
            for s in ans[i - 2]:
                for head, tail in pairs:
                    strobo_s = head + s + tail
                    ans[i].append(strobo_s)
                    if i >= len(low) and strobo_s[0] != '0':
                        n = int(strobo_s)
                        if n >= low_i and n <= high_i:
                            count += 1

        return (count, ans)

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.findStrobogrammatic

    def test_standard(self):
        self.assertEqual(sorted(self.f(1)), sorted(['0', '1', '8']))
        self.assertEqual(sorted(self.f(2)), sorted(['11', '69', '88', '96']))
        self.assertEqual(sorted(self.f(3)), sorted(['101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986']))

if __name__ == "__main__":
    s = Solution()
    print(s.strobogrammaticInRange('50', '100004'))
    #suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)

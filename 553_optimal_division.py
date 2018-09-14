#!/usr/bin/env python
import functools
import unittest

class Solution(object):
    @staticmethod
    def _div_eval(S):
        return functools.reduce(lambda x, y: float(x) / y, S)

    @staticmethod
    def _div(A, i, j):
        B = [Solution._div_eval(x) for x in [A[:i], A[i:j], A[j:]] if x]
        return Solution._div_eval(B)

    @staticmethod
    def _div_str(S):
        return '/'.join([str(x) for x in S])

    @staticmethod
    def _out_str(A, i, j):
        B = [x for x in [Solution._div_str(A[:i]),
                         '(' + Solution._div_str(A[i:j]) + ')',
                         Solution._div_str(A[j:])] if x]
        return '/'.join(B)

    @staticmethod
    def _calc(current_max, current_str, A, i, j):
        candidate = Solution._div(A, i, j)
        if candidate > current_max:
            return candidate, Solution._out_str(A, i, j)
        return current_max, current_str

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        max_v = Solution._div_eval(nums)
        max_s = Solution._div_str(nums)
        ln = len(nums)

        window = len(nums) - 1
        while window > 1:
            for i in range(0, ln - window + 1):
                max_v, max_s = Solution._calc(max_v, max_s, nums, i, i + window)
            window -= 1

        return max_s

class Variant2(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_base(self):
        self.assertEqual(self.sol.optimalDivision([1000,100,10,2]), '1000/(100/10/2)')
        self.assertEqual(self.sol.optimalDivision([1, 2, 3]), '1/(2/3)')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(Variant2)

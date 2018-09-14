#!/usr/bin/env python

import unittest

class Solution(object):
    @staticmethod
    def mid_index(left, right):
        return left + ((right - left) / 2)

    @staticmethod
    def arrlen(left, right):
        if left > right:
            return 0

        return right - left + 1

    @staticmethod
    def pair_indices(nums, left, right):
        mid = Solution.mid_index(left, right)

        # index left of mid
        lom = mid - 1

        # index right of mid
        rom = mid + 1

        if lom >= left and nums[lom] == nums[mid]:
            return (lom, mid)
        elif rom <= right and nums[mid] == nums[rom]:
            return (mid, rom)
        # did not find a pair -- found the answer instead
        # since nums[lom] != nums[mid] and nums[mid] != nums[rom]
        else:
            return (mid, mid)

    @staticmethod
    def part(nums, left, right):
        # subarray of length 1
        if left == right:
            return left

        p1, p2 = Solution.pair_indices(nums, left, right)

        # found the solution early
        if p1 == p2:
            return p1

        left_of_p1 = p1 - 1
        right_of_p2 = p2 + 1

        left_len = Solution.arrlen(left, left_of_p1)
        right_len = Solution.arrlen(right_of_p2, right)

        if left_len > 0 and left_len % 2 == 1:
            return Solution.part(nums, left, left_of_p1)
        elif right_len > 0 and right_len % 2 == 1:
            return Solution.part(nums, right_of_p2, right)

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        left = 0
        right = nums_len - 1

        if nums_len > 0 and nums_len % 2 == 1:
            return nums[self.part(nums, left, right)]

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty1(self):
        a = True

    def test_empty(self):
        self.assertEqual(self.s.singleNonDuplicate([1]), 1)
        self.assertEqual(self.s.singleNonDuplicate([1]), 0)

    def test_standard(self):
        self.assertEqual(self.s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2)
        self.assertEqual(self.s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]), 10)
        self.assertEqual(self.s.singleNonDuplicate([8, 9, 9, 10, 10, 42, 42]), 8)
        self.assertEqual(self.s.singleNonDuplicate([0, 0, 4, 4, 7]), 7)
        self.assertEqual(self.s.singleNonDuplicate([0, 0, 1, 2, 2]), 1)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

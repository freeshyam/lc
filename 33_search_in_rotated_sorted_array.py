#!/usr/bin/env python

import unittest

class Solution:
    @staticmethod
    def find_offset(nums):
        start, end = 0, len(nums) - 1

        while True:
            if nums[start] < nums[end]:
                return start

            m = start + (end - start) // 2

            if start == end or nums[m - 1] > nums[m]:
                return m

            if nums[start] >= nums[m] <= nums[end]:
                end = m - 1
            elif nums[start] <= nums[m] >= nums[end]:
                start = m + 1

    def search(self, nums, target):
        if not nums:
            return -1

        N = len(nums)
        k = self.find_offset(nums)
        start, end = 0, N - 1

        while start <= end:
            m = start + (end - start) // 2

            translated_idx = (m + k) % N
            if nums[translated_idx] == target:
                return translated_idx

            if nums[translated_idx] < target:
                start = m + 1
            elif nums[translated_idx] > target:
                end = m - 1

        return -1

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.search

    def test_base(self):
        self.assertEqual(self.f([], 2), -1)
        self.assertEqual(self.f([5, 6, 0, 1, 2, 3, 4], 72), -1)
        self.assertEqual(self.f([5, 6, 0, 1, 2, 3, 4], -23), -1)
        self.assertEqual(self.f([5, 6, 0, 1, 2, 3, 4], 2.5), -1)

        self.assertEqual(self.f([5, 6, 0, 1, 2, 3, 4], 5), 0)
        self.assertEqual(self.f([4, 5, 6, 0, 1, 2, 3], 5), 1)
        self.assertEqual(self.f([3, 4, 5, 6, 0, 1, 2], 5), 2)
        self.assertEqual(self.f([2, 3, 4, 5, 6, 0, 1], 5), 3)
        self.assertEqual(self.f([1, 2, 3, 4, 5, 6, 0], 5), 4)
        self.assertEqual(self.f([0, 1, 2, 3, 4, 5, 6], 5), 5)
        self.assertEqual(self.f([6, 0, 1, 2, 3, 4, 5], 5), 6)
        self.assertEqual(self.f([2, 1], 1), 1)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

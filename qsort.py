#!/usr/bin/env python

import unittest
import random

def qsort(A):
    def qsort_helper(A, start, end):
        """
        start:i  < pivot
        i:j      = pivot
        j:k      not yet inspected
        k:end    > pivot
        """
        if end - start <= 1:
            return

        i = j = start
        k = end

        pivot = A[start]
        j += 1

        while j < k:
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j + 1
            elif A[j] == pivot:
                j += 1
            else:
                k -= 1
                A[j], A[k] = A[k], A[j]

        qsort_helper(A, start, i)
        qsort_helper(A, k, end)

    qsort_helper(A, 0, len(A))
    return A

class UT1(unittest.TestCase):
    def setUp(self):
        pass

    def test_base(self):
        l = [random.randint(-100, 100) for _ in range(1000)]
        sorted_l = sorted(l)
        self.assertEqual(qsort(l), sorted_l)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

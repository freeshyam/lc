#!/usr/bin/env python

import unittest

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head = before = ListNode(0)
        dummy_head.next = it = head

        for _ in range(1, m):
            before, it = before.next, it.next

        for _ in range(n - m):
            tmp = it.next
            it.next, tmp.next, before.next = tmp.next, before.next, tmp

        return dummy_head.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def to_ll(xs):
    dummy_head = tail = ListNode(0)

    for x in xs:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy_head.next

def ll_to_str(l):
    out = []
    p = l

    while p:
        out.append(str(p.val))
        p = p.next

    return '->'.join(out)

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.reverseBetween

    def test_base(self):
        input_list = to_ll([1])
        output_list = self.f(input_list, 1, 1)
        self.assertEqual(ll_to_str(output_list), '1')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 2, 4)
        self.assertEqual(ll_to_str(output_list), '1->4->3->2->5')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 2, 3)
        self.assertEqual(ll_to_str(output_list), '1->3->2->4->5')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 3, 3)
        self.assertEqual(ll_to_str(output_list), '1->2->3->4->5')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 1, 5)
        self.assertEqual(ll_to_str(output_list), '5->4->3->2->1')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 1, 2)
        self.assertEqual(ll_to_str(output_list), '2->1->3->4->5')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

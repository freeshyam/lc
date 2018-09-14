#!/usr/bin/env python

import unittest

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = it = head

        while it and it.next:
            tmp = it.next
            it.next, tmp.next, dummy_head.next = tmp.next, dummy_head.next, tmp

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
        self.f = self.s.reverseList

    def test_base(self):
        input_list = to_ll([])
        output_list = self.f(input_list)
        self.assertEqual(ll_to_str(output_list), '')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list)
        self.assertEqual(ll_to_str(output_list), '5->4->3->2->1')

        input_list = to_ll([1])
        output_list = self.f(input_list)
        self.assertEqual(ll_to_str(output_list), '1')

        input_list = to_ll([1, 2])
        output_list = self.f(input_list)
        self.assertEqual(ll_to_str(output_list), '2->1')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

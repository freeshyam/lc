#!/usr/bin/env python

import unittest

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy_head = last_node = ListNode(0)
        dummy_head.next = p = head

        length = 0
        while p:
            length += 1
            last_node = last_node.next
            p = p.next

        r = k % length
        if r == 0:
            return head

        p = dummy_head
        for _ in range(length - r):
            p = p.next

        new_head = p.next
        last_node.next = head
        p.next = None

        return new_head

# Definition for singly-linked list.
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
        self.f = self.s.rotateRight

    def test_base(self):
        input_list = to_ll([])
        output_list = self.f(input_list, 123)
        self.assertEqual(ll_to_str(output_list), '')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 1)
        self.assertEqual(ll_to_str(output_list), '5->1->2->3->4')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 2)
        self.assertEqual(ll_to_str(output_list), '4->5->1->2->3')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 7)
        self.assertEqual(ll_to_str(output_list), '4->5->1->2->3')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 3)
        self.assertEqual(ll_to_str(output_list), '3->4->5->1->2')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 4)
        self.assertEqual(ll_to_str(output_list), '2->3->4->5->1')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 5)
        self.assertEqual(ll_to_str(output_list), '1->2->3->4->5')

        input_list = to_ll([1, 2, 3, 4, 5])
        output_list = self.f(input_list, 10)
        self.assertEqual(ll_to_str(output_list), '1->2->3->4->5')

        input_list = to_ll([1])
        output_list = self.f(input_list, 10)
        self.assertEqual(ll_to_str(output_list), '1')

        input_list = to_ll([1, 2])
        output_list = self.f(input_list, 1)
        self.assertEqual(ll_to_str(output_list), '2->1')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

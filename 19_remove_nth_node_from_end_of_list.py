#!/usr/bin/env python

import unittest


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = slow = ListNode(0)
        dummy_head.next = fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_head.next

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
        self.f = self.s.removeNthFromEnd

    def test_base(self):
        input_ll = to_ll([1, 2, 3, 4, 5])
        output_ll = self.f(input_ll, 2)
        self.assertEqual(ll_to_str(output_ll), '1->2->3->5')

        input_ll = to_ll([1])
        output_ll = self.f(input_ll, 1)
        self.assertEqual(ll_to_str(output_ll), '')

        input_ll = to_ll([1, 2])
        output_ll = self.f(input_ll, 2)
        self.assertEqual(ll_to_str(output_ll), '2')

        input_ll = to_ll([1, 2])
        output_ll = self.f(input_ll, 1)
        self.assertEqual(ll_to_str(output_ll), '1')

        input_ll = to_ll([1, 2, 3])
        output_ll = self.f(input_ll, 3)
        self.assertEqual(ll_to_str(output_ll), '2->3')

        input_ll = to_ll([1, 2, 3, 4, 5, 6, 7, 8])
        output_ll = self.f(input_ll, 5)
        self.assertEqual(ll_to_str(output_ll), '1->2->3->5->6->7->8')

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

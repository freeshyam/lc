#!/usr/bin/env python

import unittest

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        p = head
        while p:
            node_copy = RandomListNode(p.label)
            node_copy.next = p.next
            p.next = node_copy
            p = node_copy.next

        p = head
        while p:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next

        p = head
        head_copy = p_copy = p.next
        while p:
            p.next = p.next.next
            if p.next is not None:
                p_copy.next = p_copy.next.next
                p_copy = p_copy.next
            p = p.next

        return head_copy

def to_ll(xs):
    dummy_head = tail = RandomListNode(0)

    for x in xs:
        tail.next = RandomListNode(x)
        tail = tail.next

    return dummy_head.next

def ll_to_str(l):
    out = []
    p = l

    while p:
        out.append(str(p.label))
        p = p.next

    return '->'.join(out)

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.copyRandomList

    def test_base(self):
        input_ll = to_ll([1, 2, 3, 4, 5, 6, 7, 8])
        output_ll = self.f(input_ll)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

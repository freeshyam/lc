#!/usr/bin/env python

import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        R = None

        while p:
            tmp = p
            p = p.next
            tmp.next = R
            R = tmp

        return R

def list_to_LL(xs):
    H = None
    p = None
    if xs:
        for x in xs:
            node = ListNode(x)
            if not H:
                H = node
                p = node
            else:
                p.next = node
                p = p.next
    return H

def print_LL(head):
    p = head
    while p:
        print p.val
        p = p.next

def LL_equal(head1, head2):
    p1 = head1
    p2 = head2
    equal = True
    while p1 and p2:
        if p1.val != p2.val:
            equal = False
        p1 = p1.next
        p2 = p2.next
    if p1 != p2:
        equal = False

    return LL_equal

def works(l1):
    s = Solution()
    ll_1 = list_to_LL(l1)
    ll_2 = s.reverseList(s.reverseList(ll_1))
    return LL_equal(ll_1, ll_2)


class UnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        self.assertTrue(works(None))
        self.assertTrue(works([]))

    def test_standard(self):
        self.assertTrue(works([1, 2, 3, 4, 5]))
        self.assertTrue(works([1]))
        self.assertTrue(works([91, 92, 93]))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

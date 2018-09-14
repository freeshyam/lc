#!/usr/bin/env python3

import unittest

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = current_node = ListNode(0)

        carry = 0
        while l1 or l2:
            l1_digit = l1.val if l1 else 0
            l2_digit = l2.val if l2 else 0
            total_sum = carry + l1_digit + l2_digit

            digit = total_sum % 10
            carry = total_sum // 10

            current_node.next = ListNode(digit)
            current_node = current_node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current_node.next = ListNode(carry)
            current_node = current_node.next

        return dummy_head.next

def list_to_linkedlist(xs):
    dummy_head = tail = ListNode(0)

    for x in xs:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy_head.next

def number_to_linkedlist(k):
    if k == 0:
        return ListNode(0)

    dummy_head = tail = ListNode(0)
    while k > 0:
        tail.next = ListNode(k % 10)
        k //= 10
        tail = tail.next

    return dummy_head.next

def linkedlist_to_str(L):
    parts = []

    while L:
        parts.append(str(L.val))
        L = L.next

    return '->'.join(parts)

def summer(x, y):
    s = Solution()
    x = number_to_linkedlist(x)
    y = number_to_linkedlist(y)
    return linkedlist_to_str(s.addTwoNumbers(x, y))

# d -> 0 -> 1 -> 2 -> None
def rev(L):
    dummy_head = ListNode(0)
    dummy_head.next = it = L

    while it and it.next:
        tmp = it.next
        it.next, tmp.next, dummy_head.next = tmp.next, dummy_head.next, tmp

    return dummy_head.next

def rev2(L):
    h = None

    while L:
        after = L.next
        L.next = h
        h = L
        L = after

    return h

def direct(x, y):
    return linkedlist_to_str(number_to_linkedlist(x + y))

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_standard(self):
        self.assertEqual(summer(99, 99), direct(99, 99))
        self.assertEqual(summer(100, 23), direct(100, 23))
        self.assertEqual(summer(0, 0), direct(0, 0))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

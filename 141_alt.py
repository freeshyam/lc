#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def next(self, p):
        if p:
            return p.next
        return None

    def hasCycle(self, head):
        if not head:
            return False

        p1 = head
        p2 = head

        while True:
            p1 = self.next(p1)
            p2 = self.next(self.next(p2))

            if p1 == None and p2 == None:
                return False
            elif p1 == p2:
                return True

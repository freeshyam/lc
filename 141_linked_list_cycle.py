#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def nodeInHashTable(self, ht, node):
        try:
            return ht[node] == True
        except KeyError:
            return False

    def hasCycle(self, head):
        if not head:
            return False

        ht = {}

        ht[head] = True

        n = head
        while True:
            n = n.next
            if n == None:
                return False
            elif self.nodeInHashTable(ht, n):
                return True
            ht[n] = True

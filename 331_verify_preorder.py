#!/usr/bin/env python

import unittest

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    def pop_completed(self, stack):
        while stack and (stack[-1].left and stack[-1].right):
            stack.pop()

    def assign_node(self, node, val):
        if not node.left:
            node.left = val
            return
        if not node.right:
            node.right = val

    def isValidSerialization(self, preorder):
        if not preorder:
            return False
        if preorder == "#":
            return True

        nodes = preorder.split(",")
        stack = []

        while nodes:
            nodeval = nodes[0]
            if nodeval == '#':
                if stack:
                    self.assign_node(stack[-1], nodeval)
                    nodes = nodes[1:]
                    self.pop_completed(stack)
                    if not stack:
                        break
                else:
                    break
            else:
                if stack:
                    self.assign_node(stack[-1], nodeval)
                stack.append(Node(nodeval))
                nodes = nodes[1:]

        if not stack and not nodes:
            return True
        else:
            return False
    """
    def reduce_stack(self, stack, length):
        while (length > 2
               and stack[-1] == "#" and stack[-2] == "#"
               and stack[-3] != "#"):
            stack.pop()
            stack.pop()
            stack[-1] = "#"
            length -= 2
        return length

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        stack = []
        length = 0

        for node in nodes:
            stack.append(node)
            length += 1
            length = self.reduce_stack(stack, length)

        return length == 1 and stack[0] == "#"

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.isValidSerialization(""), False)
        self.assertEqual(self.s.isValidSerialization("#"), True)

    def test_should_be_true(self):
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("9,3,#,#,2,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,#"), True)

    def test_should_be_false(self):
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#,8"), False)
        self.assertEqual(self.s.isValidSerialization("9,3,#,#,2,#"), False)
        self.assertEqual(self.s.isValidSerialization("1,#"), False)
        self.assertEqual(self.s.isValidSerialization("9,#,#,1"), False)
        self.assertEqual(self.s.isValidSerialization("#,1,#,#,2,#,#"), False)
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2"), False)
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2,#"), False)
        self.assertEqual(self.s.isValidSerialization("#,#,#"), False)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def nodeval(node):
    if node:
        return node.val
    return None

def is_same(t1, t2):
    if t1 and t2:
        vals_same = nodeval(t1) == nodeval(t2)
        return (vals_same and is_same(t1.left, t2.left)
                and is_same(t2.right, t2.right))
    elif not t1 and not t2:
        return True
    else:
        return False

def doubleinv(t):
    s = Solution()
    return s.invertTree(s.invertTree(t))

class Solution(object):
    def swap(self, node):
        tmp = node.left
        node.left = node.right
        node.right = tmp

    def invertTree(self, root):
        if root:
            self.swap(root)
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        #      1
        self.t0 = TreeNode(1)

        #      1
        #     / \
        #    1   1
        self.t1 = TreeNode(1)
        self.t1.left = TreeNode(1)
        self.t1.right = TreeNode(1)

        #      1
        #     / \
        #    2   3
        #   /     \
        #  4       5
        self.t2 = TreeNode(1)
        self.t2.left = TreeNode(2)
        self.t2.right = TreeNode(3)
        self.t2.left.left = TreeNode(4)
        self.t2.right.right = TreeNode(5)

        #      1
        #     / \
        #    3   2
        #   /     \
        #  5       4
        self.t3 = TreeNode(1)
        self.t3.left = TreeNode(3)
        self.t3.right = TreeNode(2)
        self.t3.left.left = TreeNode(5)
        self.t3.right.right = TreeNode(4)

        #      1
        #     / \
        #    3   2
        #   / \   \
        #  5   6   4
        self.t4 = TreeNode(1)
        self.t4.left = TreeNode(3)
        self.t4.right = TreeNode(2)
        self.t4.left.left = TreeNode(5)
        self.t4.left.left = TreeNode(6)
        self.t4.right.right = TreeNode(4)

        #      1
        #     / \
        #    3   2
        #   / \   \
        #  5   6   4
        #           \
        #            7
        #             \
        #              8
        self.t5 = TreeNode(1)
        self.t5.left = TreeNode(3)
        self.t5.right = TreeNode(2)
        self.t5.left.left = TreeNode(5)
        self.t5.left.left = TreeNode(6)
        self.t5.right.right = TreeNode(4)
        self.t5.right.right.right = TreeNode(7)
        self.t5.right.right.right.right = TreeNode(8)

    def test_empty(self):
        self.assertTrue(is_same(self.t0, doubleinv(self.t0)))

    def test_standard(self):
        self.assertTrue(is_same(self.t1, doubleinv(self.t1)))
        self.assertTrue(is_same(self.t2, doubleinv(self.t2)))
        self.assertTrue(is_same(self.t3, doubleinv(self.t3)))
        self.assertTrue(is_same(self.t4, doubleinv(self.t4)))
        self.assertTrue(is_same(self.t5, doubleinv(self.t5)))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

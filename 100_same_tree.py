#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    @staticmethod
    def nodeval(node):
        if node:
            return node.val
        return None

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return (self.nodeval(p) == self.nodeval(q) and
                    self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        elif not p and not q:
            return True

        # else, exactly one of p or q is None
        # while the other is not, so they are not equal
        return False

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        #      1
        self.t0 = TreeNode(1)

        #      1
        #     / \
        #    2   3
        self.t1 = TreeNode(1)
        self.t1.left = TreeNode(2)
        self.t1.right = TreeNode(3)

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
        #    2   3
        #         \
        #          4
        self.t3 = TreeNode(1)
        self.t3.left = TreeNode(2)
        self.t3.right = TreeNode(3)
        self.t3.right.right = TreeNode(4)

    def test_empty(self):
        self.assertTrue(self.s.isSameTree(None, None))

    def test_standard(self):
        self.assertTrue(self.s.isSameTree(self.t0, self.t0))
        self.assertTrue(self.s.isSameTree(self.t1, self.t1))
        self.assertTrue(self.s.isSameTree(self.t2, self.t2))
        self.assertTrue(self.s.isSameTree(self.t3, self.t3))

    def test_negative(self):
        self.assertFalse(self.s.isSameTree(None, self.t1))

        self.assertFalse(self.s.isSameTree(self.t0, self.t1))
        self.assertFalse(self.s.isSameTree(self.t1, self.t2))
        self.assertFalse(self.s.isSameTree(self.t2, self.t3))
        self.assertFalse(self.s.isSameTree(self.t1, self.t2))

        self.assertFalse(self.s.isSameTree(self.t1, self.t3))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

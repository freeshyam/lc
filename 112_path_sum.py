#!/usr/bin/env python

import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, root, sum, acc):
        if root and root.left == None and root.right == None:
            return sum == acc + root.val
        if root:
            return (self.helper(root.left, sum, acc + root.val)
                    or self.helper(root.right, sum, acc + root.val))
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root:
            return self.helper(root, sum, 0)
        return False

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
        self.t4.left.right = TreeNode(6)
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
        self.t5.left.right = TreeNode(6)
        self.t5.right.right = TreeNode(4)
        self.t5.right.right.right = TreeNode(7)
        self.t5.right.right.right.right = TreeNode(8)

        #      1
        #     / \
        #    3   2
        #   / \   \
        #  5   6   4
        self.t6 = TreeNode(1)
        self.t6.left = TreeNode(3)
        self.t6.left.left = TreeNode(5)
        self.t6.left.right = TreeNode(6)
        self.t6.right = TreeNode(2)
        self.t6.right.right = TreeNode(4)

        #      1
        #     /
        #    2
        self.t7 = TreeNode(1)
        self.t7.left = TreeNode(2)

    def test_empty(self):
        self.assertTrue(self.s.hasPathSum(self.t0, 1))

    def test_standard(self):
        self.assertTrue(self.s.hasPathSum(self.t1, 2))
        self.assertTrue(self.s.hasPathSum(self.t2, 7))
        self.assertTrue(self.s.hasPathSum(self.t2, 9))
        self.assertTrue(self.s.hasPathSum(self.t3, 7))
        self.assertTrue(self.s.hasPathSum(self.t3, 9))
        self.assertTrue(self.s.hasPathSum(self.t4, 10))
        self.assertTrue(self.s.hasPathSum(self.t4, 7))
        self.assertTrue(self.s.hasPathSum(self.t4, 9))
        self.assertTrue(self.s.hasPathSum(self.t5, 9))
        self.assertTrue(self.s.hasPathSum(self.t5, 10))
        self.assertTrue(self.s.hasPathSum(self.t5, 22))
        self.assertTrue(self.s.hasPathSum(self.t6, 9))
        self.assertTrue(self.s.hasPathSum(self.t7, 3))
        self.assertFalse(self.s.hasPathSum(self.t7, 1))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

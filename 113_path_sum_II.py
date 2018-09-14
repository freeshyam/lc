#!/usr/bin/env python

import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def r2l(node, result, desired_sum, acc):
            if not node:
                return
            elif node.left == None and node.right == None and node.val == desired_sum:
                result.append(acc + [node.val])
            else:
                r2l(node.left, result, desired_sum - node.val, acc + [node.val])
                r2l(node.right, result, desired_sum - node.val, acc + [node.val])

        R = []
        r2l(root, R, sum, [])
        return R


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.pathSum

        self.tree = TreeNode(5)
        self.tree.left = TreeNode(4)
        self.tree.right = TreeNode(8)

        self.tree.left.left = TreeNode(11)
        self.tree.left.left.left = TreeNode(7)
        self.tree.left.left.right = TreeNode(2)

        self.tree.right.left = TreeNode(13)
        self.tree.right.right = TreeNode(4)
        self.tree.right.right.left = TreeNode(5)
        self.tree.right.right.right = TreeNode(1)

    def test_standard(self):
        self.assertEqual(self.f(self.tree, 22), [[5, 4, 11, 2], [5, 8, 4, 5]])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

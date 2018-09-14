#!/usr/bin/env python

import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, rlist):
            if root:
                inorder(root.left, rlist)
                rlist.append(root.val)
                inorder(root.right, rlist)

        result = []
        inorder(root, result)
        return result

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.inorderTraversal

        self.tree = TreeNode(1)
        self.tree.left = TreeNode(2)
        self.tree.right = TreeNode(3)

        self.tree.left.left = TreeNode(4)
        self.tree.left.right = TreeNode(5)

    def test_standard(self):
        self.assertEqual(self.f(self.tree), [4, 2, 5, 1, 3])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

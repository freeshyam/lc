#!/usr/bin/env python

import unittest

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def binary_tree_height(self, root):
        if not root:
            return -1
        else:
            return 1 + max(self.binary_tree_height(root.left),
                           self.binary_tree_height(root.right))

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        #      1
        self.t0 = Node(1)

        #      1
        #     / \
        #    1   1
        self.t1 = Node(1)
        self.t1.left = Node(1)
        self.t1.right = Node(1)

        #      1
        #     / \
        #    1   1
        #         \
        #          1
        self.t2 = Node(1)
        self.t2.left = Node(1)
        self.t2.right = Node(1)
        self.t2.right.right = Node(1)

        #      1
        #     / \
        #    1   1
        #     \   \
        #      1   1
        #     /
        #    1
        self.t3 = Node(1)
        self.t3.left = Node(1)
        self.t3.left.right = Node(1)
        self.t3.left.right.left = Node(1)
        self.t3.right = Node(1)
        self.t3.right.right = Node(1)

        #      1
        #       \
        #        1
        #         \
        #          1
        #           \
        #            1
        #           / \
        #          1   1
        #         /   / \
        #        1   1   1
        #               /
        #              1
        self.t4 = Node(1)
        self.t4.right = Node(1)
        self.t4.right.right = Node(1)
        self.t4.right.right.right = Node(1)
        self.t4.right.right.right.left = Node(1)
        self.t4.right.right.right.left.left = Node(1)
        self.t4.right.right.right.right = Node(1)
        self.t4.right.right.right.right.left = Node(1)
        self.t4.right.right.right.right.right = Node(1)
        self.t4.right.right.right.right.right.left = Node(1)

    def test_empty(self):
        self.assertEqual(self.s.binary_tree_height(self.t0), 0)

    def test_standard(self):
        self.assertEqual(self.s.binary_tree_height(self.t1), 1)
        self.assertEqual(self.s.binary_tree_height(self.t2), 2)
        self.assertEqual(self.s.binary_tree_height(self.t3), 3)
        self.assertEqual(self.s.binary_tree_height(self.t4), 6)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

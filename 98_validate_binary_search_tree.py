#!/usr/bin/env python

import unittest

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        def is_bst(root, minval, maxval):
            if not root:
                return True

            if ((minval is not None and root.val <= minval)
                or (maxval is not None and root.val >= maxval)):
                return False

            new_minval = min(minval, root.val) if minval is not None else root.val
            new_maxval = min(maxval, root.val) if maxval is not None else root.val

            return (is_bst(root.left, minval, new_maxval)
                    and is_bst(root.right, new_minval, maxval))

        return is_bst(root, None, None)

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.isValidBST

    def test_is_bst(self):
        self.assertEqual(self.f(None), True)

        t = Node(1)
        self.assertEqual(self.f(t), True)

        #      3
        #     / \
        #    2   4
        t = Node(3)
        t.left = Node(2)
        t.right = Node(4)
        self.assertEqual(self.f(t), True)

        #      7
        #     / \
        #    6   8
        #         \
        #          9
        t = Node(7)
        t.left = Node(6)
        t.right = Node(8)
        t.right.right = Node(9)
        self.assertEqual(self.f(t), True)

        #      9
        #     / \
        #    5   22
        #     \   \
        #      8   92
        #     /
        #    6
        t = Node(9)
        t.left = Node(5)
        t.left.right = Node(8)
        t.left.right.left = Node(6)
        t.right = Node(22)
        t.right.right = Node(92)
        self.assertEqual(self.f(t), True)

        #      9
        #     / \
        #    5   22
        #   / \   \
        #  3   8   92
        #     /
        #    6
        t = Node(9)
        t.left = Node(5)
        t.right = Node(22)
        t.left.left = Node(3)
        t.left.right = Node(8)
        t.left.right.left = Node(6)
        t.right.right = Node(92)
        self.assertEqual(self.f(t), True)

    def test_is_not_bst(self):
        #      1
        #     /
        #    1
        t = Node(1)
        t.left = Node(1)
        self.assertEqual(self.f(t), False)

        #      1
        #       \
        #        1
        t = Node(1)
        t.right = Node(1)
        self.assertEqual(self.f(t), False)

        #      5
        #     / \
        #    2   4
        t = Node(5)
        t.left = Node(2)
        t.right = Node(4)
        self.assertEqual(self.f(t), False)

        #      1
        #     / \
        #    2   3
        #         \
        #          4
        t = Node(1)
        t.left = Node(2)
        t.right = Node(3)
        t.right.right = Node(4)
        self.assertEqual(self.f(t), False)

        #      9
        #     / \
        #    5   22
        #     \   \
        #      16  92
        #     /
        #    3
        t = Node(9)
        t.left = Node(5)
        t.left.right = Node(16)
        t.left.right.left = Node(3)
        t.right = Node(22)
        t.right.right = Node(92)
        self.assertEqual(self.f(t), False)

        #     10
        #     / \
        #    2   15
        #   / \   \
        #  1   13  20
        t = Node(10)
        t.left = Node(2)
        t.right = Node(15)
        t.left.left = Node(1)
        t.left.right = Node(13)
        t.right.right = Node(20)
        self.assertEqual(self.f(t), False)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

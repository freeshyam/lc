#!/usr/bin/env python

import unittest

"""
Sample test data

nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]
nestedList = [3, [4, [5, 6], [7, [8], [-1, -2, -3], 10], [15, 18], 42, 91, [-100]], 1]
nestedList = [3, [4, [5, 6], [7, [8], [], [[], [], 18, 19, 20, ], [[[]]], 7, []], 2]]

Your NestedIterator object will be instantiated and called as such:

i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
"""

class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.current_iter = iter(nestedList)
        self.cached_next = None

    def next(self):
        if self.cached_next is not None:
            retval = self.cached_next
            self.cached_next = None
            return retval

        while True:
            elem = next(self.current_iter, None)
            if elem is None:
                if not self.stack:
                    raise StopIteration
                self.current_iter = self.stack.pop()
            elif elem.isInteger():
                return elem.getInteger()
            else:
                self.stack.append(self.current_iter)
                self.current_iter = iter(elem.getList())

    def hasNext(self):
        if self.cached_next is not None:
            return True

        try:
            self.cached_next = self.next()
            return True
        except StopIteration:
            return False

"""
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        self.current_iter = iter(nestedList)
        self.cached_next = None

    def next(self):
        if self.cached_next is not None:
            retval = self.cached_next
            self.cached_next = None
            return retval

        while True:
            elem = next(self.current_iter, None)
            if elem is None:
                if not self.stack:
                    raise StopIteration
                self.current_iter = self.stack.pop()
            elif type(elem) == int:
                return elem
            else:
                self.stack.append(self.current_iter)
                self.current_iter = iter(elem)

    def hasNext(self):
        if self.cached_next is not None:
            return True

        try:
            self.cached_next = self.next()
            return True
        except StopIteration:
            return False
"""

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.foo

    def test_base(self):
        pass

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

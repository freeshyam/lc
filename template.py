#!/usr/bin/env python

import unittest



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

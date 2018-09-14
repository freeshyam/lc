#!/usr/bin/env python

import unittest

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        all_rooms = set(range(len(rooms)))
        visited = set()

        def visit(rooms, visited, room_num):
            visited.add(room_num)
            for room in rooms[room_num]:
                if room not in visited:
                    visit(rooms, visited, room)

        visit(rooms, visited, 0)

        return visited == all_rooms

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.canVisitAllRooms

    def test_base(self):
        self.assertEqual(self.f([[1],[2],[3],[]]), True)
        self.assertEqual(self.f([[1,3],[3,0,1],[2],[0]]), False)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

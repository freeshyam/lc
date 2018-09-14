#!/usr/bin/env python

import unittest

from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        courses = list(range(numCourses))
        prerequisite_to_courses = defaultdict(set)
        course_to_num_prerequisites = defaultdict(int)

        for course, prerequisite in prerequisites:
            course_to_num_prerequisites[course] += 1
            prerequisite_to_courses[prerequisite].add(course)

        topo_sort = []

        q = deque(c for c in range(numCourses) if c not in course_to_num_prerequisites)

        while q:
            completed_course = q.popleft()
            topo_sort.append(completed_course)

            if completed_course in prerequisite_to_courses:
                for k in prerequisite_to_courses[completed_course]:
                    course_to_num_prerequisites[k] -= 1
                    if course_to_num_prerequisites[k] == 0:
                        q.append(k)

        return topo_sort if len(topo_sort) == numCourses else []

class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.findOrder

    def test_base(self):
        self.assertEqual(self.f(2, [[1,0]]), [0, 1])
        self.assertEqual(self.f(4, [[1,0],[2,0],[3,1],[3,2]]), [0, 1, 2, 3])

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

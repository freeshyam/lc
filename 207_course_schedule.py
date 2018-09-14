#!/usr/bin/env python

import unittest

from collections import deque, defaultdict

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # :type numCourses: int
        # :type prerequisites: List[List[int]]
        # :rtype: bool
        courses = list(range(numCourses))
        course_to_prerequisites = defaultdict(set)
        prerequisite_to_courses = defaultdict(set)

        for course, prerequisite in prerequisites:
            course_to_prerequisites[course].add(prerequisite)
            prerequisite_to_courses[prerequisite].add(course)

        topo_sort = []

        # put courses without prerequisites in the queue
        q = deque(c for c in courses if c not in course_to_prerequisites)

        while q:
            completed_course = q.popleft()
            topo_sort.append(completed_course)
            if completed_course in prerequisite_to_courses:

                # given that we completed a course completed_course:
                # for all courses k that have completed_course as a prerequisite,
                # remove completed_course from k's prerequisite list
                for k in prerequisite_to_courses[completed_course]:
                    course_to_prerequisites[k].remove(completed_course)

                    if not course_to_prerequisites[k]:
                        q.append(k)

        return len(topo_sort) == numCourses
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        courses = list(range(numCourses))
        course_to_num_prerequisites = defaultdict(int)
        prerequisite_to_courses = defaultdict(set)

        for course, prerequisite in prerequisites:
            prerequisite_to_courses[prerequisite].add(course)
            course_to_num_prerequisites[course] += 1

        num_courses_completed = 0

        # put courses without prerequisites in the queue
        q = deque(c for c in courses if c not in course_to_num_prerequisites)

        while q:
            completed_course = q.popleft()
            num_courses_completed += 1

            # if completed_course is a prerequisite for other courses
            if completed_course in prerequisite_to_courses:

                # given that we completed a course completed_course:
                # for all courses k that have completed_course as a prerequisite,
                # decrement k's prerequisite course count by 1
                for k in prerequisite_to_courses[completed_course]:
                    course_to_num_prerequisites[k] -= 1
                    if course_to_num_prerequisites[k] == 0:
                        q.append(k)

        return num_courses_completed == numCourses


class UT1(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.f = self.s.canFinish

    def test_base(self):
        self.assertEqual(self.f(2, [[1,0]]), True)
        self.assertEqual(self.f(2, [[1,0],[0,1]]), False)

def unit_test(cls):
    suite = unittest.TestLoader().loadTestsFromTestCase(cls)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    unit_test(UT1)

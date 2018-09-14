#!/usr/bin/env python

"""
There are N plants in a garden. Each of these plants has been added with
some amount of pesticide. After each day, if any plant has more pesticide
than the plant at its left, being weaker than the left one, it dies. You
are given the initial values of pesticide in each plant. Print the number
of days after which no plant dies, i.e. the time after which there are no
plants with more pesticide content than the plant to their left.

The input consists of an integer N. The next line consists of N integers
describing the array P where P[i] denotes the amount of pesticide in plant i.

Output a single value equal to the number of days after which no plants die.

Sample input:
7
6 5 8 4 7 10 9

6 5   4      9
6 5   4

Sample output:
2

Sample input:
99
1 99 98 97 96 95 94 93 92 ... 2

Sample output:
98

"""

starting_num_plants = int(raw_input())
plants = map(int, raw_input().split())

# _ 1 _ _ _ _ _ _
# 1 2 3 4 5 6 7 8

def solution(num_plants, plants):
    if num_plants < 2:
        return 1

    candidates = plants
    days = 0
    to_del = []

    last_c = candidates[0]
    while True:
        for i, c in enumerate(candidates):
            if i > 0 and c > last_c:
                to_del.append(i)
            last_c = c
        if not to_del:
            return days
        while to_del:
            candidates.pop(to_del.pop())
        days += 1

print solution(starting_num_plants, plants)

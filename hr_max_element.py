#!/usr/bin/env python

def main():
num_queries = int(raw_input())
stack = []
max_stack = []

for _ in xrange(num_queries):
    q = map(int, raw_input().split())

    cmd_num = q[0]

    if cmd_num == 1:
        val = q[1]
        stack.append(val)
        if not max_stack or val >= max_stack[-1]:
            max_stack.append(val)
    elif cmd_num == 2:
        x = stack.pop()
        if x == max_stack[-1]:
            max_stack.pop()
    elif cmd_num == 3:
        print max_stack[-1]

if __name__ == "__main__":
    main()

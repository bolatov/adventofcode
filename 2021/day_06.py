#!/usr/local/bin/python3

from collections import deque
import sys


def _read(input_file="input.txt"):
    with open(input_file) as f:
        line = f.readline()
        return [int(i) for i in line.split(",")]


def part_1(input_file):
    state = deque(_read(input_file))
    days = 80
    for day in range(days):
        curlen = len(state)
        for _ in range(curlen):
            num = state.popleft()
            if num == 0:
                state.extend([6, 8])
            else:
                state.append(num-1)
    return len(state)


if __name__ == "__main__":
    input_file = sys.argv[1]
    ans = part_1(input_file)
    print("Part 1:", ans)

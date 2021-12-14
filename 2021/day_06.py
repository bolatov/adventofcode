#!/usr/local/bin/python3

from collections import deque, Counter
import sys


def _read(input_file="input.txt"):
    with open(input_file) as f:
        line = f.readline()
        return [int(i) for i in line.split(",")]


def part_1(input_file, days=80):
    state = deque(_read(input_file))
    for day in range(days):
        curlen = len(state)
        for _ in range(curlen):
            num = state.popleft()
            if num == 0:
                state.extend([6, 8])
            else:
                state.append(num-1)
    return len(state)


def part_2(input_file, days=80):
    numbers = _read(input_file)
    mp = [0 for _ in range(10)]
    for num in numbers:
        mp[num] += 1
    for day in range(days):
        new_mp = [0 for _ in range(10)]
        for num, count in enumerate(mp):
            if num == 0:
                new_mp[6] += count
                new_mp[8] += count
            else:
                new_mp[num-1] += count
        mp = new_mp
    return sum(mp)


if __name__ == "__main__":
    input_file = sys.argv[1]
    days = int(sys.argv[2])
    #ans = part_1(input_file, days)
    #print("Part 1:", ans)
    ans = part_2(input_file, days)
    print("Part 2:", ans)

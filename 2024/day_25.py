import heapq
import math
import re
import sys


def read_input(filename="input.txt"):
    locks = []
    keys = []
    max_height = 0
    with open(filename) as f:
        is_first_line = True
        height = 0
        is_lock = None # extending downward
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                is_first_line = True
                height = 0
                continue
            height += 1
            max_height = max(height-2, max_height)
            if is_first_line:
                is_first_line = False
                if '#' * len(line) == line:
                    is_lock = True
                    cur = [0 for _ in range(len(line))]
                    locks.append(cur)
                else:
                    is_lock = False
                    cur = [-1 for _ in range(len(line))]
                    keys.append(cur)
            else:
                cur = locks[-1] if is_lock else keys[-1]
                for i in range(len(line)):
                    if line[i] == "#":
                        cur[i] += 1
    return locks, keys, max_height


def part1(locks, keys, height):
    result = 0
    for lock in locks:
        for key in keys:
            is_fit = True
            for l, k in zip(lock, key):
                if l + k > height:
                    is_fit = False
                    break
            if is_fit:
                result += 1
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    locks, keys, height = read_input(filename)
    print("Part 1: ", part1(locks, keys, height))
    #print("Part 2: ", part2(graph))

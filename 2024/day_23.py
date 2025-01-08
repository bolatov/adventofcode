import heapq
import math
import re
import sys


def read_input(filename="input.txt"):
    arr = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            a, b = line.split("-")
            arr.append((a,b))
    return arr


def part1(pairs):
    g = {}
    for a, b in pairs:
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        g[a].append(b)
        g[b].append(a)
    result = set()
    for a in g.keys():
        for b in g[a]:
            for c in g[b]:
                if a in g[c] and (a[0]=="t" or b[0]=="t" or c[0]=="t"):
                    result.add(str(sorted([a, b, c])))
    return len(result)


def part2(secrets):
    result = 0
    return result

if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    print("Part 1: ", part1(arr))
    #print("Part 2: ", part2(arr, 2000))

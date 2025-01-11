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


def part1(g):
    result = set()
    for a in g.keys():
        for b in g[a]:
            for c in g[b]:
                if a in g[c] and (a[0]=="t" or b[0]=="t" or c[0]=="t"):
                    result.add(str(sorted([a, b, c])))
    return len(result)


def part2(g):
    result = None
    for v in g.keys():
        print(f"{v}")
        vcopy = g[v].copy()
        vcopy.add(v)
        local_result = None
        for u in g[v]:
            ucopy = g[u].copy()
            ucopy.add(u)
            print(f"\t {vcopy} {ucopy}")
            intersection = vcopy & ucopy
            all_connected = True
            for k in intersection:
                kcopy = g[k].copy()
                kcopy.add(k)
                if not (intersection < kcopy):
                    all_connected = False
                    break
            if all_connected and (result is None or len(intersection) > len(result)):
                result = intersection
    if result is None:
        return None
    return ",".join(sorted(result))


def convert_to_graph(pairs):
    g = {}
    for a, b in pairs:
        if a not in g:
            g[a] = set()
        if b not in g:
            g[b] = set()
        g[a].add(b)
        g[b].add(a)
    return g


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    graph = convert_to_graph(arr)
    print("Part 1: ", part1(graph))
    print("Part 2: ", part2(graph))

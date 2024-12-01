#!/usr/local/bin/python3

import heapq


def add_pair(q, pair):
    heapq.heappush(q, pair)
    return q


def get_top(q):
    return heapq.heappop(q)


def read_input_as_maps(filename="input.txt"):
    mp1, mp2 = {}, {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            v1, v2 = map(int, line.split())
            mp1[v1] = mp1.get(v1, 0) + 1
            mp2[v2] = mp2.get(v2, 0) + 1
    return mp1, mp2


def get_min_prio_queues(mp1, mp2):
    q1, q2 = [], []
    for key_value in mp1.items():
        heapq.heappush(q1, key_value)
    for key_value in mp2.items():
        heapq.heappush(q2, key_value)
    return q1, q2


def part1():
    mp1, mp2 = read_input_as_maps()
    q1, q2 = get_min_prio_queues(mp1, mp2)
    result = 0
    while q1 and q2:
        p1, p2 = get_top(q1), get_top(q2)
        v1, cnt1 = p1
        v2, cnt2 = p2
        result += abs(v1 - v2)
        if cnt1 - 1 > 0:
            q1 = add_pair(q1, (v1, cnt1 - 1))
        if cnt2 - 1 > 0:
            q2 = add_pair(q2, (v2, cnt2 - 1))
    print("Part 1: ", result)
    return result


def part2():
    mp1, mp2 = read_input_as_maps()
    result = 0
    for key in mp1.keys():
        result += key * mp2.get(key, 0)
    print("Part 2: ", result)
    return result

if __name__ == "__main__":
    part1()
    part2()

#!/usr/local/bin/python3
import sys


def read_input(filename="input.txt"):
    arr = []
    with open(filename) as f:
        c = f.read().strip()
        for i in c.split():
            arr.append(int(i))
        return arr


def apply_rule(num):
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        s = str(num)
        n = len(s)
        x, y = int(s[:n//2].strip()), int(s[n//2:].strip())
        return [x, y]
    return [num * 2024]


def part1(arr, iterations):
    #print(arr)
    q = arr
    for iteration in range(iterations):
        print(iteration)
        qprime = []
        for x in q:
            qprime.extend(apply_rule(x))
        q = qprime
    print(f"Part 1: {len(q)}")
    return len(q)


def part2(arr):
    result = 0
    print(f"Part 2: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    part1(arr, 25)
    #part1(arr, 75)

import heapq
import math
import re
import sys


def read_input(filename="input.txt"):
    arr = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            arr.append(int(line))
    return arr


def calculate_nth(secret, n):
    def mix(a, b):
        return a ^ b
    def prune(a):
        return a % 16777216
    for _ in range(n):
        secret = prune(mix(secret * 64, secret))
        secret = prune(mix(secret // 32, secret))
        secret = prune(mix(secret * 2048, secret))
    return secret


def part1(arr, iterations):
    result = 0
    for num in arr:
        nth = calculate_nth(num, iterations)
        #print(f"{num}: {nth}")
        result += nth
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    print("Part 1: ", part1(arr, 2000))

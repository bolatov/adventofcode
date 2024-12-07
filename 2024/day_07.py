#!/usr/local/bin/python3
import sys

def read_input(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(line.strip()))
    return matrix


def bfs(arr, expected_value):
    q = [(arr[0], 0)]
    while q:
        cur_value, idx = q.pop()
        if idx == len(arr)-1:
            if expected_value == cur_value:
                return True
            continue
        idx += 1
        q.append((cur_value + arr[idx], idx))
        q.append((cur_value * arr[idx], idx))
    return False


def bfs2(arr, expected_value):
    q = [(arr[0], 0)]
    while q:
        cur_value, idx = q.pop()
        if idx == len(arr)-1:
            if expected_value == cur_value:
                return True
            continue
        idx += 1
        q.append((cur_value + arr[idx], idx))
        q.append((cur_value * arr[idx], idx))
        concat = str(cur_value) + str(arr[idx])
        q.append((int(concat), idx))
    return False


def part1(filename):
    result1 = 0
    result2 = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            value, nums = line.strip().split(":")
            value = int(value)
            arr = list(map(int, nums.split()))
            if bfs(arr, value):
                result1 += value
            elif bfs2(arr, value):
                result2 += value

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2+result1}")
    return 0


def part2(matrix):
    result = 0
    print(f"Part 1: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    part1(filename)
    #part2(matrix)

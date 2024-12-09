#!/usr/local/bin/python3
import sys


def read_input(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        content = f.read()
        c = list(content.strip())
        arr = list(map(int, c))
        assert len(arr) % 2 == 1, "Input length should be odd"
        return arr


def part1(arr):
    result = 0
    idx_left = 1
    position = arr[0]
    ispace = 1
    iright_file = len(arr)-1
    idx_right = len(arr) // 2
    while ispace < iright_file:
        #print(f"{ispace} < {iright_file} {arr[ispace]} {arr[iright_file]}")
        while arr[ispace] > 0 and arr[iright_file] > 0:
            #print(f"position * idx_right: {position} * {idx_right}")
            result += idx_right * position
            position += 1
            arr[ispace] -= 1
            arr[iright_file] -= 1
        if arr[iright_file] <= 0:
            iright_file -= 2
            idx_right -= 1
        if arr[ispace] <= 0:
            for x in range(arr[ispace+1]):
                #print(f"position + idx_left : {position} * {idx_left}")
                result += idx_left * position
                position += 1
            idx_left += 1
            ispace += 2
    print(f"Part 1: {result}")
    return result


def part2(arr):
    for i in range(len(arr)):
        if i % 2 == 1:
            arr[i] *= -1
    result = 0
    i = 0
    position = 0
    while i < len(arr):
        #print()
        if arr[i] > 0:
            for _ in range(arr[i]):
                #print(f"{position}: {i // 2}")
                result += (i // 2) * position
                position += 1
        else:
            end = len(arr) - 1
            while end > i and arr[i] < 0:
                if arr[end] > 0 and arr[end] <= abs(arr[i]):
                    arr[i] += arr[end]
                    for _ in range(arr[end]):
                        #print(f"{position}: {end // 2}")
                        result += (end // 2) * position
                        position += 1
                    arr[end] *= -1
                end -= 2
            if arr[i] < 0:
                position -= arr[i]
        i += 1
    print(f"Part 2: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    part1(list(arr))
    part2(list(arr))

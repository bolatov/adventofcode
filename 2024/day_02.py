#!/usr/local/bin/python3


def read_input_as_matrix(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            arr = list(map(int, line.split()))
            if arr:
                matrix.append(arr)
    return matrix


def check(arr, func):
    for j in range(1, len(arr)):
        if not func(arr[j-1], arr[j]):
            return False
    return True


def greater(i, j):
    return i < j and (1 <= j-i <= 3)


def less(i, j):
    return i > j and (1 <= i-j <= 3)


def is_safe(arr):
    return check(arr, greater) or check(arr, less)


def part1(matrix):
    result = 0
    for arr in matrix:
        if is_safe(arr):
            result += 1
    print("Part 1: ", result)
    return result

def count_violations(arr, func):
    result = []
    for j in range(1, len(arr)):
        if not func(arr[j-1], arr[j]):
            result.append(j)
    return result


def is_safe_with_toleration(arr):
    #print("  Checking:", arr)
    v1, v2 = count_violations(arr, greater), count_violations(arr, less)
    if len(v1) == 0 or len(v2) == 0:
        return True
    for idx in range(len(arr)):
        if check(arr[:idx] + arr[idx+1:], greater):
            return True
    for idx in range(len(arr)):
        if check(arr[:idx] + arr[idx+1:], less):
            return True
    return False


def part2(matrix):
    result = 0
    for arr in matrix:
        if is_safe_with_toleration(arr):
            #print("Part 2:", arr)
            result += 1
    print("Part 2: ", result)
    return result

if __name__ == "__main__":
    matrix = read_input_as_matrix()
    part1(matrix)
    part2(matrix)

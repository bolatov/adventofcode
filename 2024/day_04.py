#!/usr/local/bin/python3
import sys

def read_input_as_matrix(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(line.strip())
    return matrix


XMAS = "XMAS"
DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1)
]


def dfs(matrix, i, j, idx, ii, jj):
    if idx == len(XMAS)-1:
        return 1
    rows, cols = len(matrix), len(matrix[0])
    result = 0
    inext, jnext = i+ii, j+jj
    if (0 <= inext < rows) and (0 <= jnext < cols) and (matrix[inext][jnext] == XMAS[idx+1]):
        result += dfs(matrix, inext, jnext, idx+1, ii, jj)
    return result


def part1(matrix):
    result = 0
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == XMAS[0]:
                for ii, jj in DIRS:
                    if (0 <= i+ii < rows) and (0 <= j+jj < cols):
                        result += dfs(matrix, i, j, 0, ii, jj)
    print("Part 1: ", result)
    return result


def part2(matrix):
    result = 0
    rows, cols = len(matrix), len(matrix[0])
    topleft, bottomright = (-1,-1), (1,1)
    topright, bottomleft = (-1,1), (1,-1)
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != "A":
                continue
            if not (
                    (0 <= i-1) and (i+1 < rows) and (0 <= j-1) and (j+1 < cols)
            ):
                continue
            if not (
                    (matrix[i+topleft[0]][j+topleft[1]] == "M" and matrix[i+bottomright[0]][j+bottomright[1]] == "S") or
                    (matrix[i+topleft[0]][j+topleft[1]] == "S" and matrix[i+bottomright[0]][j+bottomright[1]] == "M")
            ):
                continue
            if not (
                    (matrix[i+topright[0]][j+topright[1]] == "M" and matrix[i+bottomleft[0]][j+bottomleft[1]] == "S") or
                    (matrix[i+topright[0]][j+topright[1]] == "S" and matrix[i+bottomleft[0]][j+bottomleft[1]] == "M")
            ):
                continue
            result += 1
    print("Part 2: ", result)
    return result

if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    matrix = read_input_as_matrix(filename)
    part1(matrix)
    part2(matrix)

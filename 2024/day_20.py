import heapq
import math
import re
import sys


INF = 1e9+7
NORTH = -1,  0
EAST  =  0,  1
SOUTH =  1,  0
WEST  =  0, -1
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
WALL = -1
EMPTY = -2


def read_input(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            arr = []
            for char in line:
                arr.append(char)
            matrix.append(arr)
    return matrix


def print_matrix(matrix, start, end, chars):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = "."
            if chars[row][col] == "#":
                value = "#"
            elif math.isclose(matrix[row][col], INF):
                value = "."
            elif (row, col) == start:
                value = "S"
            elif (row, col) == end:
                value = "E"
            else:
                value = matrix[row][col]
            print(value, end="\t")
        print()
    print()


def is_between(begin, end, value):
    return begin <= value < end


def part1(matrix, start, end, threshold):
    rows, cols = len(matrix), len(matrix[0])
    dist = [[INF for _ in range(cols)] for _ in range(rows)]
    dist[start[0]][start[1]] = 1

    # Calculate the distances from S to (i, j)
    q = [start]
    path = set()
    while q:
        i, j = q.pop()
        path.add((i,j))
        for direction in DIRECTIONS:
            ii, jj = direction
            inext, jnext = i + ii, j + jj
            if (
                    is_between(0, rows, inext) and is_between(0, cols, jnext) and 
                    matrix[inext][jnext] != "#" and
                    dist[i][j] + 1 < dist[inext][jnext]
            ):
                dist[inext][jnext] = dist[i][j] + 1
                if (inext, jnext) != end:
                    q.append((inext, jnext))
    print(f"end: {dist[end[0]][end[1]]}")
    print_matrix(dist, start, end, matrix)

    # Check if crossing the # will save picoseconds
    cheats = {}
    for i,j in path:
        for direction in DIRECTIONS:
            ii, jj = direction
            inext, jnext = i + ii, j + jj
            if (
                    is_between(0, rows, inext) and is_between(0, cols, jnext) and 
                    matrix[inext][jnext] == "#" 
            ):
                for facing in DIRECTIONS:
                    rr, cc = facing
                    rnext, cnext = inext + rr, jnext + cc
                    if (
                            is_between(0, rows, rnext) and is_between(0, cols, cnext) and 
                            matrix[rnext][cnext] != "#" and
                            dist[i][j] + 2 < dist[rnext][cnext]
                    ):
                        saved = dist[rnext][cnext] - (dist[i][j] + 2)
                        #print(f"saved {saved} between ({(i,j)}) and ({(rnext,cnext)}) {dist[i][j]}+2 < {dist[rnext][cnext]}")
                        if saved not in cheats:
                            cheats[saved] = set()
                        cheats[saved].add((inext, jnext))
    #print(cheats)
    result = 0
    for key in sorted(cheats.keys()):
        #print(f"{key}: {len(cheats[key])}")
        if key >= threshold:
            result += len(cheats[key])
    return result


def find_start_end(matrix):
    start, end = None, None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "S":
                start = row, col
            elif matrix[row][col] == "E":
                end = row, col
    return start, end


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    matrix = read_input(filename)
    start, end = find_start_end(matrix)
    print("Part 1: ", part1(matrix, start, end, 100))

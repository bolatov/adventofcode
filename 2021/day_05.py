#!/usr/local/bin/python3

import sys


MATRIX_SIZE = int(1e3)


def _read(input_file="input.txt"):
    vents = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.split("->")
            x1, y1 = [int(num) for num in left.split(",")]
            x2, y2 = [int(num) for num in right.split(",")]
            vents.append([(x1, y1), (x2, y2)])
        return vents


def _get_horizontal_lines(lines):
    horizontal_lines = []
    for line in lines:
        p1, p2 = line
        _, y1 = p1
        _, y2 = p2
        if y1 == y2:
            horizontal_lines.append(line)
    return horizontal_lines


def _get_vertical_lines(lines):
    vertical_lines = []
    for line in lines:
        p1, p2 = line
        x1, _ = p1
        x2, _ = p2
        if x1 == x2:
            vertical_lines.append(line)
    return vertical_lines


def _add_horizontal_lines(matrix, lines):
    for i, line in enumerate(lines):
        #print(f"adding horizontal line {i}/{len(lines)}")
        p1, p2 = line
        if p1[0] < p2[0]:
            x1, y1 = p1
            x2, y2 = p2
        else:
            x1, y1 = p2
            x2, y2 = p1
        matrix[x1][y1] += 1
        matrix[x2+1][y2] -= 1


def _add_vertical_lines(matrix, lines):
    for i, line in enumerate(lines):
        #print(f"adding vertical line {i}/{len(lines)}")
        p1, p2 = line
        if p1[1] < p2[1]:
            x1, y1 = p1
            x2, y2 = p2
        else:
            x1, y1 = p2
            x2, y2 = p1
        matrix[x1][y1] += 1
        matrix[x2][y2+1] -= 1


def _count_overlaps(horizontal_lines_matrix, vertical_lines_matrix):
    for j in range(MATRIX_SIZE):
        for i in range(1, MATRIX_SIZE):
            horizontal_lines_matrix[i][j] += horizontal_lines_matrix[i-1][j]
    for i in range(MATRIX_SIZE):
        for j in range(1, MATRIX_SIZE):
            vertical_lines_matrix[i][j] += vertical_lines_matrix[i][j-1]
    overlaps = 0
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            summ = horizontal_lines_matrix[row][col] + vertical_lines_matrix[row][col]
            if summ > 1:
                overlaps += 1
    return overlaps


def part_1(input_file):
    vents = _read(input_file)
    #print(f"vents={vents}")
    horizontal_lines = _get_horizontal_lines(vents)
    vertical_lines = _get_vertical_lines(vents)
    #print(f"horizontal_lines_count={len(horizontal_lines)}")
    #print(f"vertical_lines_count={len(vertical_lines)}")
    horizontal_lines_matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    vertical_lines_matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    _add_horizontal_lines(horizontal_lines_matrix, horizontal_lines)
    #print(f"Added horizontal lines to matrix")
    _add_vertical_lines(vertical_lines_matrix, vertical_lines)
    #print(f"Added vertical lines to matrix")
    overlaps = _count_overlaps(horizontal_lines_matrix, vertical_lines_matrix)
    #for row in horizontal_lines_matrix:
    #    print(row)
    return overlaps


if __name__ == "__main__":
    input_file = sys.argv[1]
    ans = part_1(input_file)
    print("Part 1:", ans)
    #ans = part_2(input_file)
    #print("Part 2:", ans)

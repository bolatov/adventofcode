#!/usr/local/bin/python3
import sys

def read_input(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(line.strip()))
    return matrix


def get_frequency_positions(matrix):
    freq_pos = {} # frequency -> position[]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            freq = matrix[row][col]
            if freq == ".":
                continue
            position = (row, col)
            if freq not in freq_pos:
                freq_pos[freq] = []
            freq_pos[freq].append(position)
    return freq_pos


def is_between(begin, end, value):
    return begin <= value < end


def calculate_antinodes(position_a, position_b, rows, cols):
    nodes = set() # position
    row_a, col_a = position_a
    row_b, col_b = position_b
    row_delta = row_b - row_a
    col_delta = col_b - col_a
    if is_between(0, rows, row_a - row_delta) and is_between(0, cols, col_a - col_delta):
        nodes.add((row_a - row_delta, col_a - col_delta))
    if is_between(0, rows, row_b + row_delta) and is_between(0, cols, col_b + col_delta):
        nodes.add((row_b + row_delta, col_b + col_delta))
    return nodes


def part1(matrix):
    result = set()
    freq_pos = get_frequency_positions(matrix)
    rows, cols = len(matrix), len(matrix[0])
    for positions in freq_pos.values():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                pos_a, pos_b = positions[i], positions[j]
                antinodes = calculate_antinodes(pos_a, pos_b, rows, cols)
                result = result.union(antinodes)
    print(f"Part 1: {len(result)}")
    return result


def part2(matrix):
    result = 0
    print(f"Part 1: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    matrix = read_input(filename)
    part1(matrix)
    #part2(matrix)
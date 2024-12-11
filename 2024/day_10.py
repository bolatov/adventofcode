#!/usr/local/bin/python3
import sys


def read_input(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            arr = []
            for char in line.strip():
                if char == ".":
                    char = "-1"
                arr.append(int(char))
            matrix.append(arr)
    return matrix


def find_start_positions(matrix):
    positions = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                positions.add((row, col))
    return positions


def bfs(matrix, start_pos):
    reachable_9s = set()
    q = [(start_pos, set())]
    while q:
        pos, visited = q.pop()
        visited.add(pos)
        ipos, jpos = pos
        if matrix[ipos][jpos] == 9:
            reachable_9s.add((ipos, jpos))
            continue
        if ipos - 1 >= 0 and (ipos-1, jpos) not in visited and matrix[ipos-1][jpos] - matrix[ipos][jpos] == 1:
            q.append(((ipos-1, jpos), visited.copy()))
        if jpos - 1 >= 0 and (ipos, jpos-1) not in visited and matrix[ipos][jpos-1] - matrix[ipos][jpos] == 1:
            q.append(((ipos, jpos-1), visited.copy()))
        if ipos + 1 < len(matrix) and (ipos+1, jpos) not in visited and matrix[ipos+1][jpos] - matrix[ipos][jpos] == 1:
            q.append(((ipos+1, jpos), visited.copy()))
        if jpos + 1 < len(matrix[0]) and (ipos, jpos+1) not in visited and matrix[ipos][jpos+1] - matrix[ipos][jpos] == 1:
            q.append(((ipos, jpos+1), visited.copy()))
    return len(reachable_9s)


def bfs2(matrix, start_pos):
    result = 0
    q = [(start_pos, set())]
    while q:
        pos, visited = q.pop()
        visited.add(pos)
        ipos, jpos = pos
        if matrix[ipos][jpos] == 9:
            result += 1
            continue
        if ipos - 1 >= 0 and (ipos-1, jpos) not in visited and matrix[ipos-1][jpos] - matrix[ipos][jpos] == 1:
            q.append(((ipos-1, jpos), visited.copy()))
        if jpos - 1 >= 0 and (ipos, jpos-1) not in visited and matrix[ipos][jpos-1] - matrix[ipos][jpos] == 1:
            q.append(((ipos, jpos-1), visited.copy()))
        if ipos + 1 < len(matrix) and (ipos+1, jpos) not in visited and matrix[ipos+1][jpos] - matrix[ipos][jpos] == 1:
            q.append(((ipos+1, jpos), visited.copy()))
        if jpos + 1 < len(matrix[0]) and (ipos, jpos+1) not in visited and matrix[ipos][jpos+1] - matrix[ipos][jpos] == 1:
            q.append(((ipos, jpos+1), visited.copy()))
    return result

def part1(matrix):
    result = 0
    start_positions = find_start_positions(matrix)
    for start_pos in start_positions:
        result += bfs(matrix, start_pos)
    print(f"Part 1: {result}")
    return result


def part2(matrix):
    result = 0
    start_positions = find_start_positions(matrix)
    for start_pos in start_positions:
        result += bfs2(matrix, start_pos)
    print(f"Part 2: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    matrix = read_input(filename)
    part1(matrix)
    part2(matrix)

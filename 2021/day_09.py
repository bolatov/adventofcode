#!/usr/local/bin/python3

from collections import deque, Counter
import sys


def _read(input_file="input.txt"):
    matrix = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            row = []
            line = line.strip()
            for char in line:
                row.append(int(char))
            matrix.append(row)
    return matrix


def is_lowest(mm, i, j):
    neighs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for ii, jj in neighs:
        if 0 <= i+ii < len(mm) and 0 <= j+jj < len(mm[0]):
            if mm[i][j] >= mm[i+ii][j+jj]:
                return False
    return True

        
def get_lowest_points(mm):
    points = []
    for i in range(len(mm)):
        for j in range(len(mm[i])):
            if is_lowest(mm, i, j):
                points.append((i, j))
    return points


def part_1(mm):
    ans = 0
    for i, j in get_lowest_points(mm):
        ans += 1 + mm[i][j]
    return ans


def part_2(mm):
    neighs = [(0,1), (0,-1), (1,0), (-1,0)]
    basin_sizes = []
    for point in get_lowest_points(mm):
        basin = set()
        q = deque([point])
        while q:
            i, j = q.popleft()
            basin.add(i*len(mm[0]) + j)
            for ii, jj in neighs:
                if ((0 <= i+ii < len(mm) and 0 <= j+jj < len(mm[0])) 
                        and (mm[i][j] < mm[i+ii][j+jj])
                        and ((i+ii)*len(mm[0]) + (j+jj) not in basin)
                        and (mm[i+ii][j+jj] != 9)):
                    basin.add((i+ii)*len(mm[0]) + (j+jj))
                    q.append((i+ii, j+jj))
        basin_sizes.append(len(basin))
    sorted_basins = sorted(basin_sizes, reverse=True)
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]


if __name__ == "__main__":
    input_file = sys.argv[1]
    mm = _read(input_file)
    ans = part_1(mm)
    print("Part 1:", ans)
    ans = part_2(mm)
    print("Part 2:", ans)

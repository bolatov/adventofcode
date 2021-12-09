#!/usr/local/bin/python3

import sys


MATRIX_SIZE = int(1e3)
#MATRIX_SIZE = int(11)


def _read(input_file="input.txt"):
    vents = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.split("->")
            x1, y1 = [int(num) for num in left.split(",")]
            x2, y2 = [int(num) for num in right.split(",")]
            # store as row-col instead of x-y coordinates
            vents.append(sorted([(y1, x1), (y2, x2)])) 
        return vents


def get_hm(hlines):
    matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    for line in hlines:
        p1, p2 = line
        r1, c1 = p1
        r2, c2 = p2
        matrix[r1][c1] += 1
        matrix[r2][c2+1] -= 1
    for row in range(len(matrix)):
        for col in range(1, len(matrix[row])):
            matrix[row][col] += matrix[row][col-1]
    return matrix


def get_vm(vlines):
    matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    for line in vlines:
        p1, p2 = line
        r1, c1 = p1
        r2, c2 = p2
        matrix[r1][c1] += 1
        matrix[r2+1][c2] -= 1
    for col in range(MATRIX_SIZE):
       for row in range(1, MATRIX_SIZE):
           matrix[row][col] += matrix[row-1][col]
    return matrix


def get_dm(dlines):
    leftm = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    leftdiag = list(filter(lambda line: line[0][1] > line[1][1], dlines))
    for line in leftdiag:
        p1, p2 = line
        r1, c1 = p1
        r2, c2 = p2
        leftm[r1][c1] += 1
        if r2+1 < MATRIX_SIZE and c2-1 >= 0:
            leftm[r2+1][c2-1] -= 1
    lstartpos = [(0, col) for col in range(MATRIX_SIZE)] # first row
    lstartpos.extend([(row, MATRIX_SIZE-1) for row in range(1, MATRIX_SIZE)]) # last column except for one
    for row, col in lstartpos:
        nextrow, nextcol = row+1, col-1
        while nextrow < MATRIX_SIZE and nextcol >= 0:
            leftm[nextrow][nextcol] += leftm[row][col]
            row, col = nextrow, nextcol
            nextrow, nextcol = nextrow + 1, nextcol - 1

    rightm = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    rightdiag = list(filter(lambda line: line[0][1] < line[1][1], dlines))
    for line in rightdiag:
        p1, p2 = line
        r1, c1 = p1
        r2, c2 = p2
        rightm[r1][c1] += 1
        if r2+1 < MATRIX_SIZE and c2+1 < MATRIX_SIZE:
            rightm[r2+1][c2+1] -= 1
    rstartpos = [(0, col) for col in range(MATRIX_SIZE)] # first row
    rstartpos.extend([(row, 0) for row in range(1, MATRIX_SIZE)]) # first column except for one
    for row, col in rstartpos:
        nextrow, nextcol = row+1, col+1
        while nextrow < MATRIX_SIZE and nextcol < MATRIX_SIZE:
            rightm[nextrow][nextcol] += rightm[row][col]
            row, col = nextrow, nextcol
            nextrow, nextcol = nextrow + 1, nextcol + 1
    return leftm, rightm


def count_overlaps(hm, vm, ldiagm, rdiagm):
    overlaps = 0
    #matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
    for row in range(MATRIX_SIZE):
        for col in range(MATRIX_SIZE):
            summ = hm[row][col] + vm[row][col] + ldiagm[row][col] + rdiagm[row][col]
            #matrix[row][col] = summ
            if summ > 1:
                overlaps += 1
    #for row in matrix:
    #    for value in row:
    #        if value == 0:
    #            print('.', end=' ')
    #        else:
    #            print(value, end=' ')
    #    print()
    return overlaps


def part_2(input_file):
    lines = _read(input_file)
    hlines = filter(lambda line: line[0][0] == line[1][0], lines)
    vlines = filter(lambda line: line[0][1] == line[1][1], lines)
    dlines = filter(lambda line: line[0][0] != line[1][0] and line[0][1] != line[1][1], lines)
    hm = get_hm(hlines)
    vm = get_vm(vlines)
    ldiagm, rdiagm = get_dm(list(dlines))
    return count_overlaps(hm, vm, ldiagm, rdiagm)


if __name__ == "__main__":
    input_file = sys.argv[1]
    ans = part_2(input_file)
    print("Part 2:", ans)

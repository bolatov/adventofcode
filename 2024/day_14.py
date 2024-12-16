import re
import sys


def read_input(filename="input.txt"):
    puzzle_input = []
    pattern = re.compile(r"-?\d+")
    with open(filename) as f:
        for line in f.readlines():
            x, y, vx, vy = re.findall(pattern, line)
            position, velocity = (int(x), int(y)), (int(vx), int(vy))
            puzzle_input.append((position, velocity))
    return puzzle_input


def calc_robots(matrix, row, maxrows, col, maxcols):
    assert maxrows - row == 51, f"{row} {maxrows} {col} {maxcols}"
    assert maxcols - col == 50, f"{row} {maxrows} {col} {maxcols}"
    result = 0
    for r in range(row, maxrows):
        for c in range(col, maxcols):
            result += matrix[r][c]
    return result


def part1(arr, seconds, rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for position, velocity in arr:
        col, row = position
        vcol, vrow = velocity
        newcol, newrow = (col + vcol*seconds) % cols, (row + vrow*seconds) % rows
        matrix[newrow][newcol] += 1
    #for line in matrix:
    #    print(line)
    midrow = rows // 2
    midcol = cols // 2
    q1 = calc_robots(matrix, 0, midrow, 0, midcol)  # top left
    q2 = calc_robots(matrix, 0, midrow, midcol+1, cols)   # top right
    q3 = calc_robots(matrix, midrow+1, rows, 0, midcol)   # bottom left
    q4 = calc_robots(matrix, midrow+1, rows, midcol+1, cols)  # bottom right
    result = q1 * q2 * q3 * q4
    print(f"Part 1: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    part1(arr, 100, 103, 101)
    #part1(arr, 100, 101, 103)
    #part2(machines)

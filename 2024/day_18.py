import re
import sys


def read_input(filename="input.txt"):
    positions = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            x, y = line.split(",")
            row, col = int(y), int(x)
            positions.append((row, col))
    return positions



INF = 1e9
def part1(corrupted, rows, cols):
    #print("corrupted:", corrupted)
    memo = {
        (0, 0): 0
    }
    q = [(0, 0)]
    south = 1, 0
    east = 0, 1
    west = 0, -1
    north = -1, 0
    while q:
        row, col = q.pop()
        steps = memo[(row, col)]
        for facing in [south, east, west, north]:
            nextpos = row + facing[0], col + facing[1]
            if nextpos not in corrupted and 0 <= nextpos[0] < rows and 0 <= nextpos[1] < cols and steps + 1 < memo.get(nextpos, INF):
                memo[nextpos] = steps + 1
                q.append(nextpos)
    end = rows-1, cols-1
    return memo.get(end, -1)


def part2(positions, rows, cols):
    result = len(positions)-1
    low, high = 0, len(positions)-1
    while low <= high:
        mid = low + (high - low) // 2
        res = part1(set(positions[:mid+1]), rows, cols)
        if res == -1:
            #print(f"mid={mid} -1")
            high = mid - 1
            result = min(result, mid)
        else:
            #print(f"mid={mid} {res}")
            low = mid + 1
    return positions[result]


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    positions = read_input(filename)
    print("Part 1: ", part1(set(positions[:1024]), 71, 71))
    print("Part 2: ", part2(positions, 71, 71))

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
    while q:
        row, col = q.pop()
        steps = memo[(row, col)]

        nextpos = row, col+1
        if nextpos not in corrupted and 0 <= nextpos[0] < rows and 0 <= nextpos[1] < cols and steps + 1 < memo.get(nextpos, INF):
            memo[nextpos] = steps + 1
            q.append(nextpos)
        nextpos = row+1, col
        if nextpos not in corrupted and 0 <= nextpos[0] < rows and 0 <= nextpos[1] < cols and steps + 1 < memo.get(nextpos, INF):
            memo[nextpos] = steps + 1
            q.append(nextpos)
        nextpos = row, col-1
        if nextpos not in corrupted and 0 <= nextpos[0] < rows and 0 <= nextpos[1] < cols and steps + 1 < memo.get(nextpos, INF):
            memo[nextpos] = steps + 1
            q.append(nextpos)
        nextpos = row-1, col
        if nextpos not in corrupted and 0 <= nextpos[0] < rows and 0 <= nextpos[1] < cols and steps + 1 < memo.get(nextpos, INF):
            memo[nextpos] = steps + 1
            q.append(nextpos)
    #for i in range(rows):
    #    for j in range(cols):
    #        if (i,j) in corrupted:
    #            print("#", end="")
    #        #elif (i,j) in memo:
    #        #    print(memo[(i,j)], end="")
    #        else:
    #            print(".", end="")
    #        print("", end="")
    #    print()
    #print()
    result = memo[(rows-1, cols-1)]
    print(f"Part 1: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    positions = read_input(filename)
    print("Part 1: ", part1(set(positions[:1024]), 71, 71))

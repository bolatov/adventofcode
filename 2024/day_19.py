import heapq
import re
import sys


def read_input(filename="input.txt"):
    designs = []
    is_read_patterns = True
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                is_read_patterns = False
                continue
            if is_read_patterns:
                patterns = line.split(", ")
            else:
                designs.append(line)
    return patterns, designs



def is_possible(design, patterns):
    q = [(len(design), design)]
    visited = set()
    while q:
        size, state = heapq.heappop(q)
        visited.add(size)
        if size == 0:
            return True
        while size >= 1:
            if state[:size] in patterns:
                next_state = state[size:]
                next_size = len(next_state)
                if next_size not in visited:
                    heapq.heappush(q, (next_size, next_state))
            size -= 1
    return False


def part1(patterns, designs):
    result = 0
    for i in range(len(designs)):
        design = designs[i]
        if is_possible(design, patterns):
            result += 1
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    towel_patterns, desired_designs = read_input(filename)
    print("Part 1: ", part1(set(towel_patterns), desired_designs))

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
    #print(f"patterns: {patterns}")
    #print(f"designs: {designs}")
    possible_designs = list()
    for i in range(len(designs)):
        design = designs[i]
        if is_possible(design, patterns) > 0:
            possible_designs.append(design)
    return possible_designs


def calc_diff_ways(design, patterns):
    n = len(design)
    dp = [0 for _ in range(n + 1)]
    dp[n] = 1
    while n > 0:
        #print(f"n = {n} {design[-n:]}")
        s = design[-n:]
        if dp[n] > 0:
            for i in range(1, n+1):
                prefix = s[:i]
                #print(f"  i={i} prefix: '{prefix}'")
                if prefix in patterns:
                    dp[n-i] += dp[n]
                    #print(f"    dp: {dp}")
        n -= 1
        #print()
    return dp[0]


def part2(patterns, designs):
    print("-="*50)
    #print(f"patterns: {patterns}")
    #print(f"designs: {designs}")
    result = 0
    for design in designs:
        result += calc_diff_ways(design, patterns)
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    towel_patterns, desired_designs = read_input(filename)
    possible_designs = part1(set(towel_patterns), desired_designs)
    print("Part 1: ", len(possible_designs))
    print("Part 2: ", part2(towel_patterns, possible_designs))

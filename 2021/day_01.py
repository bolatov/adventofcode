#!/usr/local/bin/python3

def _get_depths(filename="input.txt"):
    depths = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            depths.append(int(line))
    return depths


def part_1():
    prev_depth = float("inf")
    ans = 0
    for cur_depth in _get_depths():
        if cur_depth > prev_depth:
            ans += 1
        prev_depth = cur_depth
    print("Part 1:", ans)


def part_2():
    window_size = 3
    ans = 0
    depths = _get_depths()
    for i in range(window_size, len(depths)):
        if depths[i] > depths[i-window_size]:
            ans += 1
    print("Part 2:", ans)


if __name__ == "__main__":
    part_1()
    part_2()

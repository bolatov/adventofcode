#!/usr/local/bin/python3


def _get_directions(filename="input.txt"):
    directions = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            command, offset = line.split()
            directions.append((command, int(offset)))
    return directions


def part_1():
    commands = _get_directions()
    row, col = 0, 0
    for direction, offset in commands:
        if direction == "forward":
            rx, ry = 1, 0
        elif direction == "up":
            rx, ry = 0, -1
        else:
            rx, ry = 0, 1
        row, col = row + (rx*offset), col + (ry*offset)
    print("Part 1:", row * col)


def part_2():
    commands = _get_directions()
    row, col, aim = 0, 0, 0
    for direction, x in commands:
        if direction == "forward":
            row += x
            col += aim * x
        elif direction == "up":
            aim -= x
        else:
            aim += x
    print("Part 2:", row * col)


if __name__ == "__main__":
    part_1()
    part_2()

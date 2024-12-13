import re
import sys


def get_x_y(line):
    _, rhs = line.split(":")
    x, y = rhs.split(",")
    x, y = x.strip(), y.strip()
    x, y = int(x[1:]), int(y[1:])
    return x, y


def get_prize_xy(line):
    _, rhs = line.split(":")
    x, y = rhs.split(",")
    x, y = x.strip(), y.strip()
    return int(x[2:]), int(y[2:])


def read_input(filename="input.txt"):
    machines = []
    three = 3
    with open(filename) as f:
        c = f.read().strip().replace("\n\n", "\n")
        lines = list(c.split("\n"))
        for i in range(0, len(lines), 3):
            #print(f"{i}: {lines[i]}")
            ax, ay = get_x_y(lines[i])
            bx, by = get_x_y(lines[i+1])
            px, py = get_prize_xy(lines[i+2])
            machines.append([
                (ax, ay), (bx, by), (px, py)
            ])
    return machines


def part1(machines, max_iters):
    #print(machines)
    result = 0
    for machine in machines:
        a, b, prize = machine
        ax, ay = a
        bx, by = b
        min_cost = -1
        for ai in range(max_iters):
            for bi in range(max_iters):
                if (ax*ai + bx*bi, ay*ai + by*bi) == prize:
                    cost = 3*ai + bi
                    if min_cost == -1:
                        min_cost = cost
                    else:
                        min_cost = min(cost, min_cost)
        if min_cost > -1:
            #print(f"{prize}: {min_cost}")
            result += min_cost
    print(f"Part 1: {result}")
    return result


def part2(machines):
    result = 0
    for machine in machines:
        a, b, prize = machine
        ax, ay = a
        bx, by = b
        px, py = prize
        px, py = px + 10000000000000, py + 10000000000000
        min_cost = -1
        y = (ax*py - ay*px) / (ax*by - ay*bx)
        x = (px - bx*y) // ax
        if abs(ax*x + bx*y - px) < 0.001 and abs(ay*x + by*y - py) < 0.001:
            result += 3*x + y
    print(f"Part 2: {result}")
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    machines = read_input(filename)
    part1(machines, 100)
    part2(machines)

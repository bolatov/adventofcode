#!/usr/local/bin/python3

from collections import Counter
import sys


def _read(input_file="input.txt"):
    with open(input_file) as f:
        line = f.readline()
        return [int(i) for i in line.split(",")]


def part_1(input_file):
    numbers = _read(input_file)
    counter = Counter(numbers)
    least_possible_fuel = float("inf")
    for num in numbers:
        fuel = 0
        for pos, count in counter.items():
            fuel += abs(pos-num) * count
        least_possible_fuel = min(least_possible_fuel, fuel)
    return least_possible_fuel


def part_2(input_file):
    numbers = _read(input_file)
    min_pos, max_pos = min(numbers), max(numbers)
    counter = Counter(numbers)
    min_value = float("inf")
    for num in range(min_pos, max_pos+1):
        #print(f"num={num}")
        total_fuel = 0
        for pos, count in counter.items():
            diff = abs(pos - num)
            fuel = diff * (diff + 1) // 2
            #print(f"\t{pos} -> {num} = {fuel}")
            total_fuel += fuel * count
        min_value = min(min_value, total_fuel)
    return min_value


if __name__ == "__main__":
    input_file = sys.argv[1]
    ans = part_1(input_file)
    print("Part 1:", ans)
    ans = part_2(input_file)
    print("Part 2:", ans)


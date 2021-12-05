#!/usr/local/bin/python3

import sys


def _get_numbers(filename="input.txt"):
    numbers = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            num = line.strip()
            numbers.append(num)
    return numbers


def _get_rates(numbers):
    gamma, epsilon = 0, 0
    size = len(numbers[0])
    for pos in range(size):
        ones, zeros = 0, 0
        for num in numbers:
            if num[pos] == '1':
                ones += 1
            else:
                zeros += 1
        value = 1 if ones >= zeros else 0
        gamma |= value
        epsilon |= 1 - value
        gamma <<= 1
        epsilon <<= 1
    gamma >>= 1
    epsilon >>= 1
    return gamma, epsilon


def part_1(input_file):
    numbers = _get_numbers(input_file)
    gamma, epsilon = _get_rates(numbers)
    print("Part 1:", gamma * epsilon)


def _filter(numbers, position, value):
    return [num for num in numbers if num[position] == value]


def _get_rating(numbers, check_bit_criteria, position=0):
    ones = _filter(numbers, position, value='1')
    zeros = _filter(numbers, position, value='0')
    chosen_numbers = ones if check_bit_criteria(len(ones), len(zeros)) else zeros
    if len(chosen_numbers) == 1:
        return int(chosen_numbers[0], 2)
    return _get_rating(chosen_numbers, check_bit_criteria, position+1)


def part_2(input_file):
    numbers = _get_numbers(input_file)
    oxygen_rating = _get_rating(numbers, lambda x,y : x >= y)
    co2_rating = _get_rating(numbers, lambda x,y : x < y)
    print(f"oxygen={oxygen_rating} co2={co2_rating}")
    print("Part 2:", oxygen_rating * co2_rating)


if __name__ == "__main__":
    input_file = sys.argv[1]
    part_1(input_file)
    part_2(input_file)

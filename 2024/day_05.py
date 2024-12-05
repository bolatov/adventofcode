#!/usr/local/bin/python3
import re
import sys


def read_input(filename="input.txt"):
    rules = {} # int -> int[]
    matrix = []  # int[][]
    with open(filename) as f:
        lines = f.readlines()
        irow, n = 0, len(lines)
        while irow < n:
            line = lines[irow].strip()
            irow += 1
            if line == "":
                break
            i, j = line.split("|")
            i, j = int(i), int(j)
            arr = rules.get(i, [])
            arr.append(j)
            rules[i] = arr
        #print("Rules:", rules)
        while irow < n:
            line = lines[irow].strip()
            irow += 1
            arr = []
            for num in line.split(","):
                arr.append(int(num))
            matrix.append(arr)
        #print("Matrix:", matrix)
        return rules, matrix


def in_right_order(rules, mp):
    # check if rules are respected
    for rule_key, rule_nums in rules.items():
        if rule_key not in mp:
            continue
        rule_key_positions = mp[rule_key]
        for left_pos in rule_key_positions:
            for rule_num in rule_nums:
                if rule_num not in mp:
                    continue
                for right_pos in mp[rule_num]:
                    if left_pos > right_pos:
                        return [left_pos, right_pos]
    return []


def build_mp(arr):
    mp = {}
    for i in range(len(arr)):
        pos = mp.get(arr[i], [])
        pos.append(i)
        mp[arr[i]] = pos
    return mp


def get_correct_orders(rules, matrix):
    result = []
    for matrix_row in range(len(matrix)):
        arr = matrix[matrix_row]
        mp = build_mp(arr)
        if in_right_order(rules, mp) == []:
            result.append(matrix_row)
    return result


def part1(rules, matrix):
    result = 0
    for irow in get_correct_orders(rules, matrix):
        result += matrix[irow][len(matrix[irow])//2]
    print("Part 1:", result)
    return result


def order(rules, arr):
    mp = build_mp(arr)
    res = in_right_order(rules, mp)
    if res == []:
        return arr
    ipos, jpos = res
    arr[jpos], arr[ipos] = arr[ipos], arr[jpos]
    return order(rules, arr)


def part2(rules, matrix):
    result = 0
    correct_orders = set(get_correct_orders(rules, matrix))
    for irow in range(len(matrix)):
        if irow in correct_orders:
            continue
        ordered = order(rules, matrix[irow])
        result += ordered[len(ordered)//2]
    print("Part 2: ", result)
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules, matrix = read_input(filename)
    part1(rules, matrix)
    part2(rules, matrix)

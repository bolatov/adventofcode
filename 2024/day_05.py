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


#def get_correct_orders(rules, matrix):
def part1(rules, matrix):
    result = 0
    for matrix_row in range(len(matrix)):
        arr = matrix[matrix_row]
        in_right_order = True
        mp = {}
        for i in range(len(arr)):
            pos = mp.get(arr[i], [])
            pos.append(i)
            mp[arr[i]] = pos
        #print(mp)
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
                            in_right_order = False
        if in_right_order:
            result += arr[len(arr)//2]
    print("Part 1:", result)
    return result


def part2(s):
    result = 0
    print("Part 2: ", result)
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    rules, matrix = read_input(filename)
    part1(rules, matrix)
    #part2(s)

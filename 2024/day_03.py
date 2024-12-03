#!/usr/local/bin/python3
import re

def read_input_as_string(filename="input.txt"):
    res = ""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            res += line
    return res


MUL_OPEN = "mul("
COMMA = ","
CLOSE = ")"


def part1(s):
    #print("String: ", s)
    result = 0
    i, n = 0, len(s)
    while i < n:
        if MUL_OPEN == s[i:i+len(MUL_OPEN)]:
            #print("if: ", i)
            i += len(MUL_OPEN)
            x = ""
            while i < n and ("0" <= s[i] <= "9"):
                #print("while x: ", i, x)
                x += s[i]
                i += 1
            if s[i] == ",":
                #print("if comma:", i)
                i += 1
                y = ""
                while i < n and ("0" <= s[i] <= "9"):
                    #print("while y:", i, y)
                    y += s[i]
                    i += 1
                #print("got x,y:", x, y, i)
                if s[i:i+len(CLOSE)] == CLOSE:
                    #print("if close:", i)
                    i += len(CLOSE)
                    result += int(x) * int(y)
        else:
            i += 1

    print("Part 1: ", result)
    return result


def part1_with_regex(s):
    matches = re.findall(r"mul\((\d+),(\d+)\)", s, re.DOTALL)
    res = 0
    for s in matches:
        x, y = s
        res += int(x) * int(y)
    print("Part 1 (with regex): ", res)
    return res


def part2(matrix):
    result = 0
    for arr in matrix:
        if is_safe_with_toleration(arr):
            #print("Part 2:", arr)
            result += 1
    print("Part 2: ", result)
    return result

if __name__ == "__main__":
    s = read_input_as_string()
    part1(s)
    part1_with_regex(s)
    #part2(matrix)

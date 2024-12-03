#!/usr/local/bin/python3
import re
import sys

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
DO = "do()"
DONT = "don't()"


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

    print("Part 1:", result)
    return result


def part1_with_regex(s):
    matches = re.findall(r"mul\((\d+),(\d+)\)", s, re.DOTALL)
    res = 0
    for s in matches:
        x, y = s
        res += int(x) * int(y)
    print("Part 1 (with regex): ", res)
    return res


def part2_with_regex(s):
    matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", s, re.DOTALL)
    result = 0
    enabled = True
    for match in matches:
        if DO == match:
            enabled = True
            #print("Enabled")
            continue
        elif DONT == match:
            enabled = False
            #print("Disabled")
            continue
        if not enabled:
            continue
        x, y = match[len(MUL_OPEN):len(match)-1].split(",")
        #print(f"\tMultiply {x} * {y}")
        result += int(x) * int(y)
    print("Part 2 (with regex):", result)
    return result
    

def part2(s):
    result = 0
    i, n = 0, len(s)
    enabled = True
    while i < n:
        if DO == s[i:i+len(DO)]:
            enabled = True
            i += len(DO)
        elif DONT == s[i:i+len(DONT)]:
            enabled = False
            i += len(DONT)
        elif MUL_OPEN == s[i:i+len(MUL_OPEN)]:
            i += len(MUL_OPEN)
            x = ""
            while i < n and ("0" <= s[i] <= "9"):
                x += s[i]
                i += 1
            if s[i] == ",":
                i += 1
                y = ""
                while i < n and ("0" <= s[i] <= "9"):
                    y += s[i]
                    i += 1
                if s[i:i+len(CLOSE)] == CLOSE:
                    i += len(CLOSE)
                    if enabled:
                        result += int(x) * int(y)
        else:
            i += 1
    print("Part 2: ", result)
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    s = read_input_as_string(filename)
    part1(s)
    part1_with_regex(s)
    part2(s)
    part2_with_regex(s)

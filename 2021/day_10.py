#!/usr/local/bin/python3

from collections import deque, Counter
import sys


HIGH_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
LOW_SCORES = {"(": 1, "[": 2, "{": 3, "<": 4}
LEGAL_PAIRS = {"(": ")", "{": "}", "[": "]", "<": ">"}


def _read(input_file="input.txt"):
    with open(input_file) as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def corrupted_index(chunk):
    stack = []
    for i, char in enumerate(chunk):
        if not stack:
            if char in LEGAL_PAIRS:
                stack.append(char)
            else:
                return -1
        else:
            if char in LEGAL_PAIRS:
                stack.append(char)
            elif char == LEGAL_PAIRS[stack[-1]]:
                stack.pop()
            else:
                return i
    return -1


def part_1(chunks):
    ans = 0
    for chunk in chunks:
        index = corrupted_index(chunk)
        if index >= 0:
            ans += HIGH_SCORES[chunk[index]]
    return ans


def part_2(chunks):
    answers = []
    for chunk in chunks:
        index = corrupted_index(chunk)
        if index >= 0:
            continue
        stack = []
        ans = 0
        for char in chunk:
            if not stack:
                stack.append(char)
            else:
                if char in LEGAL_PAIRS:
                    stack.append(char)
                else:
                    stack.pop()
        while stack:
            ans *= 5
            ans += LOW_SCORES[stack[-1]]
            stack.pop()
        answers.append(ans)
    return sorted(answers)[len(answers)//2]


if __name__ == "__main__":
    input_file = sys.argv[1]
    chunks = _read(input_file)
    ans = part_1(chunks)
    print("Part 1:", ans)
    ans = part_2(chunks)
    print("Part 2:", ans)

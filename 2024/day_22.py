import heapq
import math
import re
import sys


def read_input(filename="input.txt"):
    arr = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            arr.append(int(line))
    return arr


def mix(a, b): return a ^ b
def prune(a):  return a % 16777216
def calc_next(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def part1(arr, iterations):
    result = 0
    for secret in arr:
        for _ in range(iterations):
            secret = calc_next(secret)
        result += secret
    return result


def part2(secrets, iterations):
    mps = []
    unique_sequences = set()
    sequence_size = 4
    for secret in secrets:
        #print(f"secret = {secret}")
        mp = {}
        mps.append(mp)
        sequence = []
        cur = secret
        for i in range(iterations):
            nxt = calc_next(cur)
            nxt_price = nxt % 10
            cur_price = cur % 10
            diff = nxt_price - cur_price
            sequence.append(diff)
            if len(sequence) > sequence_size:
                sequence.pop(0)
            #print(f"{i}: {nxt}-{cur} diff={diff} sequence={sequence}")
            if len(sequence) == sequence_size:
                key = str(sequence)
                unique_sequences.add(key)
                if key not in mp:
                    mp[key] = nxt_price
            cur = nxt
    #print(mps)
    result = 0
    for seq in unique_sequences:
        temp_result = 0
        for mp in mps:
            temp_result += mp.get(seq, 0)
        if temp_result > result:
            #print(f"seq={seq} result={temp_result}")
            result = temp_result
    return result

if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    arr = read_input(filename)
    #print("Part 1: ", part1(arr, 2000))
    print("Part 2: ", part2(arr, 2000))

import heapq
import math
import re
import sys


def fnAND(x, y): return x & y
def fnOR(x, y):  return x | y
def fnXOR(x, y): return x ^ y


def read_input(filename="input.txt"):
    values = {}
    conns = []
    with open(filename) as f:
        is_reading_values = True
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                is_reading_values = False
                continue
            if is_reading_values:
                var, value = line.split(":")
                values[var.strip()] = int(value.strip())
            else:
                var1, fn, var2, _, var3 = line.split(" ")
                if fn == "AND":
                    fn = fnAND
                elif fn == "OR":
                    fn = fnOR
                elif fn == "XOR":
                    fn = fnXOR
                conn = var1, var2, fn, var3
                conns.append(conn)
    return values, conns


def part1(values, connections):
    while connections:
        nxt_conns = []
        for conn in connections:
            var1, var2, fn, var3 = conn
            if var1 in values and var2 in values:
                values[var3] = fn(values[var1], values[var2])
            else:
                nxt_conns.append(conn)
        connections = nxt_conns
    #for k in sorted(values.keys()):
    #    print(f"{k}: {values[k]}")
    z_keys = sorted([k for k, v in values.items() if k[0] == "z"])
    #print(z_keys)
    result = 0
    for i in range(len(z_keys)):
        result |= values[z_keys[i]] << i
    return result


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    wire_values, gate_connections = read_input(filename)
    print("Part 1: ", part1(wire_values, gate_connections))
    #print("Part 2: ", part2(graph))

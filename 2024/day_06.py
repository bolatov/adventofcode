#!/usr/local/bin/python3
import sys

def read_input_as_matrix(filename="input.txt"):
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(line.strip()))
    return matrix


def get_next_pos(position, direction):
    ii, jj = direction
    i, j = position
    return (i+ii, j+jj)


def is_outside(matrix, position):
    i, j = position
    rows, cols = len(matrix), len(matrix[0])
    return i < 0 or i >= rows or j < 0 or j >= cols


def is_obstacle(matrix, position):
    i, j = position
    return matrix[i][j] == "#"


up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)


def change_direction(direction):
    if direction == up:
        return right
    if direction == right:
        return down
    if direction == down:
        return left
    if direction == left:
        return up
    raise ValueError(f"Passed direction {direction} is not valid")


def find_init_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            char = matrix[i][j]
            if char == "^":
                return (i, j), up
            if char == ">":
                return (i, j), right
            if char == "v":
                return (i, j), down
            if char == "<":
                return (i, j), left
    raise ValueError("Initial position is not found")


def visit(matrix, cur_pos, direction):
    visited = dict()
    while True:
        if cur_pos in visited and direction in visited[cur_pos]:
            return -1
        if cur_pos not in visited:
            visited[cur_pos] = set()
        visited[cur_pos].add(direction)
        next_pos = get_next_pos(cur_pos, direction)
        if is_outside(matrix, next_pos):
            break
        if is_obstacle(matrix, next_pos):
            direction = change_direction(direction)
            continue
        cur_pos = next_pos
    return visited


def part1(matrix):
    cur_pos, direction = find_init_position(matrix)
    visited = visit(matrix, cur_pos, direction)
    result = len(visited)
    print(f"Part 1: {result}")
    return result


def print_matrix(matrix, visited, obstacles, init_pos):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            pos = (i, j)
            if matrix[i][j] == "#":
                print("#", end="")
            elif pos == init_pos:
                print("^", end="")
            elif pos in obstacles:
                print(f"{obstacles[(i,j)]}", end="")
            elif pos in visited:
                dirs = visited[pos]
                if (up in dirs or down in dirs) and (left in dirs or right in dirs):
                    print("+", end="")
                elif up in dirs or down in dirs:
                    print("|", end="")
                elif left in dirs or right in dirs:
                    print("-", end="")
                else:
                    print("Z", end="")
            else:
                print(".", end="")
            print(" ", end="")
        print()
    print()


def produces_loop(matrix, cur_pos, direction, visited, vis_prime, obstacle_pos):
    #print(f"1. cur_pos {cur_pos} direction is {direction} obstacle is at {obstacle_pos}")
    #direction = change_direction(direction)
    #cur_pos = get_next_pos(cur_pos, direction)
    #print(f"2. cur_pos {cur_pos} direction is {direction} obstacle is at {obstacle_pos}")
    while True:
        #print(f"\tcur_pos {cur_pos} direction is {direction}")
        if direction in vis_prime.get(cur_pos, set()):
            return True
        #if (direction in visited.get(cur_pos, set()) or 
        #        direction in vis_prime.get(cur_pos, set())):
        #    return True
        if cur_pos not in vis_prime:
            vis_prime[cur_pos] = set()
        vis_prime[cur_pos].add(direction)
        next_pos = get_next_pos(cur_pos, direction)
        if is_outside(matrix, next_pos):
            #print(f"\t{next_pos} is outside")
            break
        if is_obstacle(matrix, next_pos) or next_pos == obstacle_pos:
            direction = change_direction(direction)
            #print(f"\tchange direction to {direction}")
            continue
        cur_pos = next_pos
    return False


def part2_old(matrix):
    init_pos, direction = find_init_position(matrix)
    cur_pos = (init_pos[0], init_pos[1])
    visited = dict()
    obstacles = dict()
    while True:
        if cur_pos not in visited:
            visited[cur_pos] = set()
        visited[cur_pos].add(direction)
        next_pos = get_next_pos(cur_pos, direction)
        if is_outside(matrix, next_pos):
            break
        if is_obstacle(matrix, next_pos):
            direction = change_direction(direction)
        else:
            if next_pos != init_pos and produces_loop(matrix, cur_pos, direction, visited, dict(), next_pos):
                obstacles[next_pos] = len(obstacles) + 1
            cur_pos = next_pos

    #print_matrix(matrix, visited, obstacles, init_pos)
    result = len(obstacles)
    print(f"Part 2: {result}")
    return result


def part2(matrix):
    init_pos, direction = find_init_position(matrix)
    possible_positions = visit(matrix, init_pos, direction)
    result = 0
    for cur_pos in possible_positions.keys():
        if cur_pos == init_pos:
            continue
        icur, jcur = cur_pos
        value = matrix[icur][jcur]
        matrix[icur][jcur] = "#"
        if visit(matrix, init_pos, direction) == -1:
            result += 1
        matrix[icur][jcur] = value
    print(f"Part 2: {result}")


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    matrix = read_input_as_matrix(filename)
    part1(matrix)
    part2(matrix)

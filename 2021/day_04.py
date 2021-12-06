#!/usr/local/bin/python3

import sys


GRID_SIZE = 5


def _read(input_file="input.txt"):
    numbers = []
    boards = []
    with open(input_file) as f:
        # Read random numbers
        line = f.readline()
        for str_num in line.split(","):
            numbers.append(int(str_num))
        f.readline()

        # Read board(s) 
        line = f.readline()
        while line:
            board = [[int(num) for num in line.split()]]
            for row in range(GRID_SIZE-1):
                line = f.readline()
                board.append([int(num) for num in line.split()])
            boards.append(board)
            f.readline()
            line = f.readline()
        return numbers, boards


def _check_if_contains(board, num):
    for row, values in enumerate(board):
        for col, value in enumerate(values):
            if value == num:
                return row, col
    return None


def _is_full_row(marked, row):
    return all(marked[row])


def _is_full_col(marked, col):
    return all(row[col] for row in marked)


def _play_bingo(numbers, board, marked):
    step = 0
    for i, num in enumerate(numbers):
        cell = _check_if_contains(board, num)
        if cell:
            row, col = cell
            marked[row][col] = True
            if _is_full_row(marked, row) or _is_full_col(marked, col):
                return i
    return -1


def _calc_score(numbers, marked, win_step, board):
    unmarked_sum = 0
    for row, values in enumerate(marked):
        for col, value in enumerate(values):
            if not marked[row][col]:
                unmarked_sum += board[row][col]
    return unmarked_sum * numbers[win_step]


def part_1(input_file):
    numbers, boards = _read(input_file)
    print(f"numbers={numbers}")
    print(f"board_count={len(boards)}")
    print(f"last_board={boards[-1]}")
    best_step, best_score = None, None
    for i in range(len(boards)):
        marked = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        win_step = _play_bingo(numbers, boards[i], marked)
        if win_step > -1 and (best_step is None or win_step < best_step):
            best_step = win_step
            best_score = _calc_score(numbers, marked, win_step, boards[i])
    return best_score


def part_2(input_file):
    numbers, boards = _read(input_file)
    print(f"numbers={numbers}")
    print(f"board_count={len(boards)}")
    print(f"last_board={boards[-1]}")
    best_step, best_score = None, None
    for i in range(len(boards)):
        marked = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        win_step = _play_bingo(numbers, boards[i], marked)
        if win_step > -1 and (best_step is None or win_step > best_step):
            best_step = win_step
            best_score = _calc_score(numbers, marked, win_step, boards[i])
    return best_score


if __name__ == "__main__":
    input_file = sys.argv[1]
    ans = part_1(input_file)
    print("Part 1:", ans)
    ans = part_2(input_file)
    print("Part 2:", ans)

#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def initialize_chessboard(size):
    """Initialize an `size`x`size` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for _ in range(size)]
    [row.append(' ') for _ in range(size) for row in chessboard]
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return chessboard


def get_solution_positions(chessboard):
    """Return the list of lists representation in a chessboard."""
    solution_positions = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution_positions.append([r, c])
                break
    return solution_positions


def mark_invalid_spots(chessboard, row, col):
    """Mark invalid spots on a chessboard."""
    # Mark out all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark out all backwards spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark out all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark out all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # Mark out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(chessboard):
        solutions.append(get_solution_positions(chessboard))
        return solutions

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            tmp_chessboard = deepcopy_chessboard(chessboard)
            tmp_chessboard[row][col] = "Q"
            mark_invalid_spots(tmp_chessboard, row, col)
            solutions = recursive_solve(tmp_chessboard, row + 1,
                                        queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)

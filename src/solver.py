"""This file contains short functions to generate and solve sudoku puzzles.
The puzzle format is conceptualized as a grid as follows:
 - Row (r, row)
 - Column (c or col),
 - And having value (v or val).

The code prioritizes readability vs performance, but performs adequately."""
from random import sample


def show(grid):
    """Takes the grid dict and prints it in 9x9 with seperators."""
    for row in range(9):
        s = ""
        if row == 3 or row == 6: print("---------+---------+---------")
        for col in range(9):
            if col == 3 or col == 6: s+= "|"
            s += " {} ".format(grid.get((row, col), "_"))
        print(s)
    print()


def validate(grid, row, col, val):
    """Checks presence of val in grid row, col, and square."""
    for (r, c), v in grid.items():
        if r == row and c == col:
            continue
        if r == row and v == val:
            return False
        elif c == col and v == val:
            return False
        elif r//3 == row//3 and c//3 == col//3 and v == val:
            return False
    return True


def validate_grid(grid):
    """Returns whether every cell in the grid contains a valid value."""
    return all(validate(grid, r, c, v) for (r, c), v in grid.items())


def emplace_at(grid, row, col):
    """ Returns whether the grid value at (row, col) was set in place."""
    # Return case
    if row == 9:
        return True

    # Get next cell coordinates
    next_row, next_col = (row, col+1) if col < 8 else (row+1, 0)

    # Skip setting this cell if it is already in the grid
    if (row, col) in grid:
        return emplace_at(grid, next_row, next_col)

    # Search for this cell's value
    for n in sample(list(range(1, 10)), 9):
        if not validate(grid, row, col, n):
            continue

        grid[(row, col)] = n

        if emplace_at(grid, next_row, next_col):
            return True
        else: # Backtrack
            del grid[(row, col)]

    return False


def full_grid(grid={}):
    """Returns a dictionary representing a sudoku game."""
    emplace_at(grid, 0, 0)
    return grid


def new_partial_grid(n=31, grid=None):
    """Samples n cells from the grid."""
    grid = grid or full_grid()
    return {(r, c): v for (r, c), v in sample(list(grid.items()), n)}


def new_game(n=31):
    """Returns a sampled grid."""
    return new_partial_grid(n)


def solve(grid):
    """Modified the grid in place and returns whether it is solved."""
    return full_grid(grid, 0, 0)


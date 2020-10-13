#!usr\bin\python3
# Class to analyse game state and determine actions

from cell import Cell
from grid import Grid

class Solver():

    def __init__(self):
        pass

    def get_unknown_candidates(self, grid):
        """
        Get all unknowns that are bordered by numbers.
        """
        candidates = []
        for row in range(grid.height):
            for col in range(grid.width):
                if grid.cells[row][col].state == None and \
                   len(grid.get_numbered_neighbours(row, col)) > 0:
                    candidates.append((row, col))
        return candidates

    def get_numbered_candidates(self, grid):
        """
        Get all numbers that are bordered by unknowns.
        """
        candidates = []
        for row in range(grid.height):
            for col in range(grid.width):
                if type(grid.cells[row][col].state) is int and \
                   len(grid.get_unknown_neighbours(row, col)) > 0:
                    candidates.append((row, col))
        return candidates

    def iterate_solver(self, grid):
        """
        Get all numbers that are bordered by unknowns.
        """
        reveal_cells = []
        reveal_adj_cells = []
        flag_cells = []
        guess_cell = []
        guess_chance = 1
        for row in range(grid.height):
            for col in range(grid.width):
                state = grid.cells[row][col].state
                if type(state) is int:
                    unknown_neighbours = grid.get_unknown_neighbours(row, col)
                    if len(unknown_neighbours) > 0:
                        flagged_neighbours = grid.get_flagged_neighbours(row, col)
                        num_unflagged_mine_neighbours = state - len(flagged_neighbours)
                        if num_unflagged_mine_neighbours == 0:
                            reveal_adj_cells += [grid.cells[row][col]]
                            reveal_cells += [cell for cell in unknown_neighbours]
                        elif num_unflagged_mine_neighbours == len(unknown_neighbours):
                            flag_cells += [cell for cell in unknown_neighbours]
                        elif num_unflagged_mine_neighbours/len(unknown_neighbours) < guess_chance:
                            guess_cell = unknown_neighbours[0]
                            guess_chance = num_unflagged_mine_neighbours/len(unknown_neighbours)
        if reveal_adj_cells == [] and flag_cells == []:
            # If no deterministic option, guess where to place a flag
            # Note that the guessing mechanism is very unsuccessful
            print('Guessing next flag, prob of bomb={}'.format(guess_chance))
            flag_cells += [guess_cell]
        return set(reveal_adj_cells), set(flag_cells)

if __name__ == "__main__":
    pass
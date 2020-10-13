#!usr/bin/python3
# Bot to play minesweeper (specifically at http://minesweeperonline.com/)

# We want to find probability of a bomb for all unknown cells bordering numbers.
# Iterate through numbered cells. If there is an unknown, assign probability based on (number - adjecent flags)/number of unknowns. Overwrite probabilities with lower ones
# If there are any 0s, reveal. If there are any 100s, flag. If there are none of these, reveal lowest probability.

# https://quantum-p.livejournal.com/19616.html Try doing this for advanced solver

from solver import Solver
from agent import Agent

if __name__ == "__main__":
    agent = Agent()
    solver = Solver()

    agent.start_game()
    num_unknown_cells_old = 0
    game_over = False
    while not game_over:
        num_unknown_cells = agent.update_values()
        game_over = game_over or num_unknown_cells_old == num_unknown_cells
        game_over = game_over or num_unknown_cells == 0
        num_unknown_cells_old = num_unknown_cells
        reveal_adj_cells, flag_cells = solver.iterate_solver(agent.grid)
        print(agent.grid)
        for cell in flag_cells:
            agent.flag_square(cell.location)
        for cell in reveal_adj_cells:
            agent.reveal_adj_squares(cell.location)


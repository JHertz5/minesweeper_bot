#!usr\bin\python3
# Class to provide interaction with actual game

# left-click to empty square to reveal
# right click empty square to flag
# middle-click or left and right click to reveal adjacent squares

import pyautogui
import random
from cell import Cell
from grid import Grid

class Agent():

    COLOUR_NUMBER_MAPPING = {
        (189,189,189) : 0,
        (  0,  0,255) : 1,
        (  0,123,  0) : 2,
        (255,  0,  0 ): 3,
        (  0,  0,123) : 4,
        (123,  0,  0) : 5,
        (  0,123,123) : 6,
        (  0,  0,  0) : 'X',
    }

    def __init__(self):
        pass

    def start_game(self):
        self.start_location = pyautogui.locateCenterOnScreen('./game_over.png')
        if self.start_location is None:
            self.start_location = pyautogui.locateCenterOnScreen('./start.png')
        if self.start_location is None:
            self.start_location = pyautogui.locateCenterOnScreen('./win.png')
        if self.start_location is None:
            raise Exception('Could not find start button')
        pyautogui.click(self.start_location)

        # get all coordinates fo all cells in grid
        cells = [Cell(*cell_location) for cell_location in pyautogui.locateAllOnScreen('./blank.png')]
        self.grid = Grid(cells)
        
        # reveal random cell to start game
        rand_row = random.randint(0, self.grid.height-1)
        rand_col = random.randint(0, self.grid.width-1)
        self.reveal_square((rand_row, rand_col))

    def reveal_square(self, location):
        """
        Left click a given cell. Note that this will not affect revealed or
        flagged cells. Return whether a game over is detected.
        """
        row, col = location
        pyautogui.click(self.grid.cells[row][col].sample_point, button='left')

    def flag_square(self, location):
        """ 
        Right click a given cell. Note that this will not affect revealed cells
        """
        row, col = location
        pyautogui.click(self.grid.cells[row][col].sample_point, button='right')
        self.grid.cells[row][col].state = 'X'

    def reveal_adj_squares(self, location):
        """
        Middle click a given cell. Note that this will not affect unrevealed
        squares.
        """
        row, col = location
        pyautogui.click(self.grid.cells[row][col].sample_point, button='middle')

    def update_values(self):
        """
        Check all cells and update any new values. Return number of unknown cells
        """
        pyautogui.moveTo(self.start_location) # Move cursor out of the way
        unknown_cells = 0
        image = pyautogui.screenshot()
        for col in range(self.grid.width):
            for row in range(self.grid.height):
                if self.grid.cells[row][col].state == None:
                    # For each unknown cell, check whether state has been revealed. Empty
                    # cells and unrevealed cells are differentiated by the colour of
                    # the top left pixel of the cell.
                    state = self.COLOUR_NUMBER_MAPPING[image.getpixel(self.grid.cells[row][col].sample_point)]
                    top_left_pixel_colour = image.getpixel(self.grid.cells[row][col].left_top)
                    if state != 0 or top_left_pixel_colour != (255, 255, 255):
                        self.grid.cells[row][col].state = state
                    else:
                        unknown_cells += 1
        return unknown_cells

if __name__ == "__main__":
    agent = Agent()
    agent.start_game()
    # agent.flag_square(agent.grid.cells[0])
    agent.reveal_square((0, 0))
    agent.reveal_square((0, 1))
    agent.update_values()
    print(agent.grid)
    print(agent.grid.number_unknown_flag_neighbours((0, 1)))
    # agent.reveal_adj_squares(agent.grid.cells[2])    
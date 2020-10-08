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
        if self.start_location is not None:
            pyautogui.click(self.start_location)
        else:
            self.start_location = pyautogui.locateCenterOnScreen('./start.png')
            if self.start_location is not None:
                pyautogui.click(self.start_location)
            else:
                raise Exception('Could not find start button')

        # get all coordinates fo all cells in grid
        cells = [Cell(*cell_location) for cell_location in pyautogui.locateAllOnScreen('./blank.png')]
        self.grid = Grid(cells)
        
        # reveal random cell to start game
        rand_row = random.randint(0, self.grid.height-1)
        rand_col = random.randint(0, self.grid.width-1)
        self.reveal_square(rand_col, rand_row)

    def reveal_square(self, col, row):
        """
        Left click a given cell. Note that this will not affect revealed or
        flagged cells.
        """
        pyautogui.click(self.grid.cells[col][row].centre, button='left')
        state = self.COLOUR_NUMBER_MAPPING[pyautogui.pixel(*self.grid.cells[col][row].centre)]
        self.grid.reveal_square(col, row, state)
        self.update_values()

    def flag_square(self, cell):
        """ 
        Right click a given cell. Note that this will not affect revealed cells
        """
        pyautogui.click(cell.centre, button='right')

    def reveal_adj_squares(self, cell):
        """
        Middle click a given cell. Note that this will not affect unrevealed
        squares.
        """
        pyautogui.click(cell.centre, button='middle')

    def update_values(self):
        """
        Check all cells and update any new values
        # TODO find a way to make more concise. use get_item set_item in grid?
        """
        image = pyautogui.screenshot()
        for col in range(self.grid.width):
            for row in range(self.grid.height):
                if self.grid.cells[col][row].state == ' ':
                    # For each unknown cell, check whether state has been revealed. Empty
                    # cells and unrevealed cells are differentiated by the colour of
                    # the top left pixel of the cell.
                    state = self.COLOUR_NUMBER_MAPPING[image.getpixel((self.grid.cells[col][row].centre))]
                    top_left_pixel_colour = image.getpixel((self.grid.cells[col][row].left_top))
                    if state != 0 or top_left_pixel_colour != (255, 255, 255):
                        self.grid.cells[col][row].state = state

if __name__ == "__main__":
    agent = Agent()
    agent.start_game()
    # agent.flag_square(agent.grid.cells[0])
    agent.update_values()
    agent.reveal_square(0, 0)
    agent.update_values()
    agent.reveal_square(1, 0)
    agent.update_values()
    # agent.reveal_adj_squares(agent.grid.cells[2])    
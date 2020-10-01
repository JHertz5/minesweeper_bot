#!usr\bin\python3
# Class to provide interaction with actual game

# left-click to empty square to reveal
# right click empty square to flag
# middle-click or left and right click to reveal adjacent squares

import pyautogui
import random
from cell import Cell

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
        self.cells = [Cell(*cell_location) for cell_location in pyautogui.locateAllOnScreen('./blank.png')]
        # reveal random cell to start game
        self.reveal_square(random.choice(self.cells))

    def reveal_square(self, cell):
        """
        Left click a given cell. Note that this will not affect revealed or
        flagged cells.
        TODO check all cells for changes
        """
        pyautogui.click(cell.centre, button='left')
        cell.unknown = False
        cell.state = self.COLOUR_NUMBER_MAPPING[pyautogui.pixel(*cell.centre)]
        print(cell.state)

    def flag_square(self, cell):
        """ 
        Right click a given cell. Note that this will not affect revealed cells
        """
        pyautogui.click(cell.centre, button='right')
        cell.unknown = False

    def reveal_adj_squares(self, cell):
        """
        Middle click a given cell. Note that this will not affect unrevealed
        squares.
        """
        pyautogui.click(cell.centre, button='middle')

    def update_values(self):
        """
        Check all cells and update any new values
        """
        image = pyautogui.screenshot()
        unknown_cells = [(index, cell) for index, cell in enumerate(self.cells) if cell.unknown == True]
        for index, cell in unknown_cells:
            # For each unkown cell, check whether state has been revealed. Empty
            # cells and unrevealed cells are differentiated by the colour of
            # the top left pixel of the cell.
            state = self.COLOUR_NUMBER_MAPPING[image.getpixel((cell.centre[0], cell.centre[1]))]
            if state != 0 or \
               image.getpixel((cell.left_top[0], cell.left_top[1])) != (255, 255, 255):
                self.cells[index].state = state
                self.cells[index].unknown = False

if __name__ == "__main__":
    agent = Agent()
    agent.start_game()
    # agent.flag_square(agent.cells[0])
    agent.update_values()
    agent.reveal_square(agent.cells[0])
    agent.update_values()
    agent.reveal_square(agent.cells[1])
    agent.update_values()
    # agent.reveal_adj_squares(agent.cells[2])    
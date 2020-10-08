#!usr\bin\python3
# Class to model the full grid

from cell import Cell

class Grid():

    def __init__(self, cells):
        self.width  = int((cells[-1].centre[0] - cells[0].centre[0])/Cell.DIMENSIONS[0] + 1)
        self.height = int((cells[-1].centre[1] - cells[0].centre[1])/Cell.DIMENSIONS[1] + 1)
        self.cells = [[cells[row*self.width + col] for row in range(self.height)] for col in range(self.width)]
    
    def __getitem__(self, xy):
        row, col = xy
        return self.cells[row][col]

    def reveal_square(self, col, row, state):
        """
        Left click a given cell. Note that this will not affect revealed or
        flagged cells.
        """
        self.cells[col][row].state = state
        print(self.cells[col][row].state)

    def flag_square(self, col, row):
        """ 
        Right click a given cell. Note that this will not affect revealed cells
        """
        pass

    def reveal_adj_squares(self, cell):
        """
        Middle click a given cell. Note that this will not affect unrevealed
        squares.
        """
        # pyautogui.click(cell.centre, button='middle')


if __name__ == "__main__":
    pass
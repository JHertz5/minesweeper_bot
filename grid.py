#!usr\bin\python3
# Class to model the full grid

from cell import Cell

class Grid():

    def __init__(self, cells):
        self.width  = int((cells[-1].left_top[0] - cells[0].left_top[0])/Cell.DIMENSIONS[0] + 1)
        self.height = int((cells[-1].left_top[1] - cells[0].left_top[1])/Cell.DIMENSIONS[1] + 1)
        self.cells = [[cells[row*self.width + col] for col in range(self.width)] for row in range(self.height)]
        for row in range(self.height):
            for col in range(self.width):
                self.cells[row][col].location = (row, col)
    
    def __str__(self):
        print_str  = '┌' + '─' * (self.width * 2 + 1) + '┐\n'
        for row in range(self.height):
            print_str += '│ ' + ' '.join([str(cell) for cell in self.cells[row]]) + ' │\n'
        print_str += '└' + '─' * (self.width * 2 + 1) + '┘\n'

        return str(print_str)
    
    def get_neighbours(self, row, col):
        """
        Get each neighbour of cell.
        """
        neighbour_location_diffs = [(-1, -1),
                                    ( 0, -1),
                                    ( 1, -1),
                                    ( 1,  0),
                                    ( 1,  1),
                                    ( 0,  1),
                                    (-1,  1),
                                    (-1,  0)]
        neighbours = []
        for diff in neighbour_location_diffs:
            if (row + diff[0] >= 0 and
                row + diff[0] < self.height and
                col + diff[1] >= 0 and
                col + diff[1] < self.width):
                neighbours.append(self.cells[row + diff[0]][col + diff[1]])
        return neighbours

    def get_unknown_neighbours(self, row, col):
        """
        Returns numbers of cells adjeacent to (row, col) that are unknown
        """
        return [cell for cell in self.get_neighbours(row, col) if cell.state == None ]

    def get_flagged_neighbours(self, row, col):
        """
        Returns numbers of cells adjeacent to (row, col) that are flags
        """
        return [cell for cell in self.get_neighbours(row, col) if cell.state == 'X']

    def get_numbered_neighbours(self, row, col):
        """
        Returns numbers of cells adjeacent to (row, col) that are numbered.
        """
        return [cell for cell in self.get_neighbours(row, col) if type(cell.state) is int]

if __name__ == "__main__":
    pass
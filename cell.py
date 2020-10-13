#!usr\bin\python3
# Class to model single cell of the grid

class Cell():

    DIMENSIONS = (16, 16)
    STATE_PRINT = {

        None : '·',
        'X' : '\033[38;5;0mX\033[m', # X -> black
        0 : ' ',                     # 0 -> blank
        1 : '\033[38;5;33m1\033[m',  # 1 -> light blue
        2 : '\033[38;5;46m2\033[m',  # 2 -> green
        3 : '\033[38;5;196m3\033[m', # 3 -> red
        4 : '\033[38;5;21m4\033[m',  # 4 -> dark blue
        5 : '\033[38;5;124m5\033[m', # 5 -> dark red
        6 : '\033[38;5;86m6\033[m'   # 6 -> cyan
    }

    def __init__(self, left, top, width, height):
        self.left_top = (int(left), int(top))
        self.sample_point = (int(left + width/2), int(top + height/2))
        self.state = None

    def __str__(self):
        return self.STATE_PRINT[self.state]

if __name__ == "__main__":
    cell = Cell(1, 2, 3, 4)
    for key in cell.STATE_PRINT.keys():
        print(cell.STATE_PRINT[key])
    pass
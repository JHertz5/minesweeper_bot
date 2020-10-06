#!usr\bin\python3
# Class to model single cell of the grid

class Cell():

    DIMENSIONS = (16, 16)

    def __init__(self, left, top, width, height):
        self.left_top = (int(left), int(top))
        self.centre = (left + width/2, top + height/2)
        self.state = ' '
        self.unknown = True

if __name__ == "__main__":
    pass
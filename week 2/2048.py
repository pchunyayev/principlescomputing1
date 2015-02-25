"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def move_left(line):
    """
    Function to move all the cells to the left
    """
    no_zeros_line = []
    zeros_line = []
    for cell in line:
        if cell != 0:
            no_zeros_line.append(cell)
        else: 
            zeros_line.append(cell)
    return no_zeros_line + zeros_line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    ordered_line = move_left(line)
    merged_line = list(ordered_line)
    merged_flag = 0
    for index in range(0, len(ordered_line)):
        if merged_flag == 1:
            merged_flag = 0
            continue
        if index - 1 >= 0 and ordered_line[index-1] == ordered_line[index]:
            merged_line[index-1] = ordered_line[index-1] + ordered_line[index]
            merged_line[index] = 0
            merged_flag = 1
    
    merged_ordered_line = move_left(merged_line)
    return merged_ordered_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = []
        for row in range(self._grid_height):
            reset_row = [0] * self._grid_width
            self._board.append(reset_row)
            row += 1
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._board)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zeros = 0
        for row in self._board:
            if 0 in row:
                zeros += 1
        if zeros > 0:
            random_number = random.randrange(10)
            if random_number == 9:
                cell_to_place = 4
            else: 
                cell_to_place = 2
            while True:
                row_for_tile = random.randrange(self._grid_height)
                col_for_tile = random.randrange(self._grid_width)
                if self.get_tile(row_for_tile, col_for_tile) == 0:
                    self.set_tile(row_for_tile, col_for_tile, cell_to_place)
                    break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

#import user39_7p5exTFbTowuChb_2 as twenty48_testsuite
#twenty48_testsuite.test_class(TwentyFortyEight)

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

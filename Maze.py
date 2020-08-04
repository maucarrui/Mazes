# Cell class.
from Cell import *

# Miner class.
from Miner import *

# Random functions
import random

class Maze:
    """
    Class for a maze.
    """

    # The board that represents the maze.
    board = None

    # Number of columns the board will have.
    x_size = None
    # Number of rows the board will have.
    y_size = None

    # The miner of the maze.
    miner = None

    def __init__(self, X, Y):
        """
        Creates a maze given the number of rows (X) and columns (Y) 
        the board will have.
        :param X: The number of rows the board will have.
        :param Y: The number of columns the board will have.
        """
        self.x_size = X
        self.y_size = Y

        # Create the board.
        self.board = [ [None for _ in range(Y)] for _ in range(X) ]

        # Fill the board.
        for x in range(X):
            for y in range(Y):
                self.board[x][y] = Cell(x, y)

        # Places a miner in a random location.
        initial_X = random.randint(0, X-1)
        initial_Y = random.randint(0, Y-1)

        self.miner = Miner(initial_X,
                           initial_Y,
                           self.board[initial_X][initial_Y])

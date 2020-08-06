# Cell class.
from Cell import *

# Miner class.
from Miner import *

# Traveler class.
from Traveler import *

# Random functions
import random

class Maze:
    """
    Class for a maze.
    """

    # The board that represents the maze.
    board = None

    # The board that will be traversed using BFS and DFS.
    board_BFS = None
    board_DFS = None

    # Number of columns the board will have.
    x_size = None
    # Number of rows the board will have.
    y_size = None

    # The miner of the maze.
    miner = None

    # The travelers of the maze.
    traveler_BFS = None
    traveler_DFS = None

    # If the traveler have started.
    travelers_started = False

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

        # Sets a random cell as the start of the maze.
        random_y = random.randint(0, Y-1)
        self.board[0][random_y].start = True

        # Spawns the travelers in the beginning of the maze.
        self.traveler_BFS = Traveler('BFS', self.board[0][random_y])
        self.traveler_DFS = Traveler('DFS', self.board[0][random_y])

        # Sets a random cell as the ending of the maze.
        random_y = random.randint(0, Y-1)
        self.board[-1][random_y].end = True

        # Places a miner in a random location.
        initial_X = random.randint(0, X-1)
        initial_Y = random.randint(0, Y-1)

        self.miner = Miner(initial_X,
                           initial_Y,
                           self.board[initial_X][initial_Y])

    def clone_board(self):
        """
        Clones the current board.
        :return: The cloned board.
        """
        X = self.x_size
        Y = self.y_size
        clone = [ [None for _ in range(Y)] for _ in range(X)]

        for x in range(X):
            for y in range(Y):
                clone[x][y] = self.board[x][y].clone()

        return clone

    def build_maze_step_by_step(self):
        """
        Builds the maze step by step.
        """
        if (not self.miner.is_done()):
            self.miner.explore(self.board)

    def solve_maze_step_by_step(self):
        """
        Solves the maze step by step.
        :param method: The method that will be used to search the exit.
        """
        if (self.miner.is_done()):

            # If the travelers are starting then
            # we assign them each a board.
            if not self.travelers_started:
                self.travelers_started = True
                self.board_BFS = self.clone_board()
                self.board_DFS = self.clone_board()

                
            self.traveler_BFS.search(self.board_BFS, 'BFS')
            self.traveler_DFS.search(self.board_DFS, 'DFS')
        


# Random functions
import random

class Miner:
    """
    Class for a miner, responsible of building the maze.
    """

    # Coordinates of the miner in the board.
    X = 0
    Y = 0

    # Log of visited cells.
    log = None

    def __init__(self, X, Y, cell):
        """
        Creates a miner.
        :param X: Initial position in the x-axis.
        :param Y: Initial position in the y-axis.
        :param cell: Initial cell where the miner spawns.
        """
        self.X = X
        self.Y = Y
        
        self.log = [cell]

    def move(self, X, Y):
        """
        Move the miner to the given coordinate.
        :param X: The x-axis of the coordinate to move.
        :param Y: The y-axis of the coordinate to move.
        """
        self.X = X
        self.Y = Y

    def is_valid_move(self, X, Y, board):
        """
        Returns whether the miner can move to the given position 
        in the board; in other words, if the cell is in a valid
        position and it has not been discovered.
        :param X: The x-axis of the coordinate to check.
        :param Y: The y-axis of the coordinate to check.
        :param board: The board where the miner is located.
        :return: True if it can move to the given position, False
            in other case.
        """
        valid = (X >= 0) and (X < len(board))
        valid = valid and (Y >= 0) and (Y < len(board[0]))
        valid = valid and (not board[X][Y].has_been_discovered())

        return valid

    def valid_moves(self, board):
        """
        Returns the valid moves the miner can perform.
        :param board: The board where the miner is located.
        :return: A list containing all of the valid moves the miner 
            can perform.
        """
        valid_moves = []
        
        if (self.is_valid_move(self.X, self.Y - 1, board)):
            valid_moves.append('up')
            
        if (self.is_valid_move(self.X, self.Y + 1, board)):
            valid_moves.append('down')
            
        if (self.is_valid_move(self.X - 1, self.Y, board)):
            valid_moves.append('left')
            
        if (self.is_valid_move(self.X + 1, self.Y, board)):
            valid_moves.append('right')

        return valid_moves

    def dig(self, board, direction):
        """
        The miner digs the board in the given direction.
        :param board: The board where the miner is located.
        :param direction: The direction the miner will dig.
        """
        current_cell = board[self.X][self.Y]
        current_cell.discovered = True

        if direction == 'up':
            # Carves the wall where the miner came out.
            current_cell.carve_wall('upper')
            
            self.move(self.X, self.Y - 1)
            
            # Carves the wall where the miner came in.
            current_cell = board[self.X][self.Y]
            current_cell.carve_wall('bottom')

        elif direction == 'down':
            current_cell.carve_wall('bottom')

            self.move(self.X, self.Y + 1)

            current_cell = board[self.X][self.Y]
            current_cell.carve_wall('upper')

        elif direction == 'left':
            current_cell.carve_wall('left')

            self.move(self.X - 1, self.Y)

            current_cell = board[self.X][self.Y]
            current_cell.carve_wall('right')

        elif direction == 'right':
            current_cell.carve_wall('right')

            self.move(self.X + 1, self.Y)

            current_cell = board[self.X][self.Y]
            current_cell.carve_wall('left')

        current_cell.discovered = True
        self.log.append(current_cell)

    def explore(self, board):
        """
        The miner moves one step into a random direction in the board.
        :param board: The board where the miner is located.
        """

        valid_dirs = self.valid_moves(board)

        # If there are no valid directions then the miner is in a
        # dead end. We return to the previous cell.
        if (len(valid_dirs) == 0):
            self.log.pop()

            if (len(self.log) != 0):
                previous_cell = self.log[-1]
                self.move(previous_cell.X, previous_cell.Y)
        else:
            random.shuffle(valid_dirs)
            new_dir = valid_dirs[0]
            self.dig(board, new_dir)

    def build_maze(self, board):
        """
        Builds the maze.
        :param: The board where the miner is located.
        """
        while (len(self.log) > 0):
            self.explore(board)

    def is_done(self):
        """
        Returns whether the miner has finished building the maze.
        :return: True if miner is done, False otherwise.
        """
        return (len(self.log) == 0)
            

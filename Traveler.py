class Traveler:
    """
    Class for a traveler, the one who will escape the maze.
    """

    # The current position of the traveler.
    X = 0
    Y = 0

    # The list that contains the cells where traveler can move to.
    log = None

    def __init__(self, initial_cell):
        """
        Creates a traveler.
        :param initial_cell: The initial cell where the traveler will spawn.
        """
        self.log = [initial_cell]
        self.X   = initial_cell.X
        self.Y   = initial_cell.Y

    def search(self, board, method):
        """
        Searches for the exit of the maze.
        :param board: The board where the traveler is located.
        :param method: The method that will be used to search the exit.
            (DFS or BFS)
        :return: The cell which is the exit of the maze if the current cell
            is the exit, None otherwise.
        """

        # Move to the next cell.
        if (method == 'DFS'):
            current_cell = self.log.pop()
        elif (method == 'BFS'):
            current_cell = self.log.pop(0)

        current_cell.explored = True

        # Update current position
        self.X = current_cell.X
        self.Y = current_cell.Y

        # Generate the next batch of cells that the traveler can move to.
        possible_moves = [(current_cell.upper_wall,  self.X, self.Y - 1),
                          (current_cell.bottom_wall, self.X, self.Y + 1),
                          (current_cell.left_wall,   self.X - 1, self.Y),
                          (current_cell.right_wall,  self.X + 1, self.Y)]

        for move in possible_moves:
            wall = move[0]
            X    = move[1]
            Y    = move[2]
            
            if not wall:
                new_cell = board[X][Y]

                if not new_cell.explored:
                    new_cell.previous = current_cell
                    self.log.append(new_cell)

        if current_cell.end:
            return current_cell
        else:
            return None
        
        
        

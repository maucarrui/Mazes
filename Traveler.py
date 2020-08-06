class Traveler:
    """
    Class for a traveler, the one who will escape the maze.
    """

    # Name of the traveler.
    name = None

    # The current position of the traveler.
    X = 0
    Y = 0

    # The current cell of the traveler.
    current_cell = None

    # The list that contains the cells where traveler can move to.
    log = None

    # Number of steps taken.
    steps = 0

    # If the traveler has found the exit.
    found_exit = False

    def __init__(self, name, initial_cell):
        """
        Creates a traveler.
        :param name: The name for the traveler.
        :param initial_cell: The initial cell where the traveler will spawn.
        """
        self.log = [initial_cell]
        self.X   = initial_cell.X
        self.Y   = initial_cell.Y
        
        self.name = name

    def search(self, board, method):
        """
        Searches for the exit of the maze.
        :param board: The board where the traveler is located.
        :param method: The method that will be used to search the exit.
            (DFS or BFS)
        :return: The cell which is the exit of the maze if the current cell
            is the exit, None otherwise.
        """

        if (self.found_exit):
            return self.current_cell

        # Move to the next cell.
        if (method == 'DFS'):
            self.current_cell = self.log.pop()
        elif (method == 'BFS'):
            self.current_cell = self.log.pop(0)

        self.current_cell.explored = True
        self.steps += 1

        # Update current position
        self.X = self.current_cell.X
        self.Y = self.current_cell.Y

        # Generate the next batch of cells that the traveler can move to.
        possible_moves = [(self.current_cell.upper_wall,  self.X, self.Y - 1),
                          (self.current_cell.bottom_wall, self.X, self.Y + 1),
                          (self.current_cell.left_wall,   self.X - 1, self.Y),
                          (self.current_cell.right_wall,  self.X + 1, self.Y)]

        for move in possible_moves:
            wall = move[0]
            X    = move[1]
            Y    = move[2]
            
            if not wall:
                new_cell = board[X][Y]

                if not new_cell.explored and not new_cell.start:
                    new_cell.previous = self.current_cell
                    self.log.append(new_cell)

        if self.current_cell.end:
            self.found_exit = True
            print(self.name + ' found exit in ' + str(self.steps) + ' steps.')
            return self.current_cell

        else:
            return None
        
        
        

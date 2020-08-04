class Cell:
    """
    Class for a cell.
    """
    
    # The position of the cell in the x-axis.
    posX = None
    # The position of the cell in the y-axis.
    posY = None
    
    # The status of the walls that surround the cell.
    upper_wall  = True
    bottom_wall = True
    left_wall   = True
    right_wall  = True

    # The status of the cell
    discovered = False

    def __init__(self, X, Y):
        """
        Creates a cell given the X and Y coordinates.
        :param X: The X coordinate.
        :param Y: The Y coordinate.
        """
        self.posX = X
        self.posY = Y

    def carve_wall(self, wall):
        """
        Carves a wall of the cell, modifying the given wall status.
        :param wall: The wall that will be carved.
        """
        if wall == 'upper':
            self.upper_wall = False
        elif wall == 'bottom':
            self.botton_wall = False
        elif wall == 'left':
            self.left_wall = False
        elif wall == 'right':
            self.right_wall = False

    def has_been_discovered(self):
        """
        Returns whether the cell has been discovered or not.
        :return: Whether the cell has been discovered or not.
        """
        return self.discovered


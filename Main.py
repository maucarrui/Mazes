# Maze class.
from Maze import *

# Lines, circles and the graphics needed.
import pygame

class Canvas:
    """
    Class for a canvas, the representation of the maze in screen.
    """

    # Colors. (Taken from the Dracula Theme Palette <3)
    black     = pygame.Color('#282a36')
    dark_gray = pygame.Color('#44475a') # Background.
    white     = pygame.Color('#f8f8f2') # Player.
    dark_blue = pygame.Color('#6272a4') # Walls of the maze.
    cyan      = pygame.Color('#8be9fd')
    green     = pygame.Color('#50fa7b') # Beginning of the maze.
    orange    = pygame.Color('#ffb86c') 
    pink      = pygame.Color('#ff79c6')
    purple    = pygame.Color('#bd93f9') # Vertex of the graph.
    red       = pygame.Color('#ff5555') # End of the maze.
    yellow    = pygame.Color('#f1fa8c')

    # The screen of the canvas.
    screen = None

    # The width and height of the canvas.
    width  = 0
    height = 0

    # The maze.
    maze = None

    # Scale.
    scale = 40

    def __init__(self, X, Y):
        """
        Creates a canvas for the maze.
        :param X: The number of rows for the maze.
        :param Y: The number of columns for the maze.
        """
        self.width  = X * self.scale
        self.height = Y * self.scale
        size = (self.width, self.height)

        self.maze = Maze(X, Y)
        
        # Initialize the pygame module.
        pygame.init()

        # Create screen.
        pygame.display.set_caption('Mazes')
        self.screen = pygame.display.set_mode(size)

    def draw_maze(self):
        """
        Draws the current state of the maze.
        """

        for x in range(self.maze.x_size):
            for y in range(self.maze.y_size):

                cell = self.maze.board[x][y]

                # Draw upper wall of cell.
                if cell.upper_wall:
                    pygame.draw.line(self.screen,
                                     self.dark_blue,
                                     (x * self.scale, y * self.scale),
                                     ((x+1) * self.scale, y * self.scale),
                                     3)
                    
                # Draw bottom wall of cell.
                if cell.bottom_wall:
                    pygame.draw.line(self.screen,
                                     self.dark_blue,
                                     (x * self.scale, (y+1) * self.scale),
                                     ((x+1) * self.scale, (y+1) * self.scale),
                                     3)

                # Draw left wall of cell.
                if cell.left_wall:
                    pygame.draw.line(self.screen,
                                     self.dark_blue,
                                     (x * self.scale, y * self.scale),
                                     (x * self.scale, (y+1) * self.scale),
                                     3)

                # Draw right wall of cell.
                if cell.right_wall:
                    pygame.draw.line(self.screen,
                                     self.dark_blue,
                                     ((x+1) * self.scale, y * self.scale),
                                     ((x+1) * self.scale, (y+1) * self.scale),
                                     3)

    def draw_graph(self):
        """
        Draws the current state of the maze as a graph.
        """
        
        center = int(self.scale / 2)
        size   = int(self.scale / 4)

        # Note: Drawing edges and vertices in the same cycle can
        # be done, however some edges end up over the vertices,
        # resulting in an ugly graph; to solve this, in the first
        # cycle we draw all the edges and then in the second cycle
        # we draw the vertices.

        # Draw edges.
        for x in range(self.maze.x_size):
            for y in range(self.maze.y_size):

                cell = self.maze.board[x][y]

                # Draw upper edge.
                if cell.upper_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     ((x * self.scale) + center,
                                      ((y-1) * self.scale) + center),
                                     2)

                # Draw bottom edge.
                if cell.bottom_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     ((x * self.scale) + center,
                                      ((y+1) * self.scale) + center),
                                     2)

                # Draw left edge.
                if cell.left_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     (((x-1) * self.scale) + center,
                                      (y * self.scale) + center),
                                     2)

                # Draw right edge.
                if cell.right_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     (((x+1) * self.scale) + center,
                                      (y * self.scale) + center),
                                     2)
                    
        # Drawing vertex.
        for x in range(self.maze.x_size):
            for y in range(self.maze.y_size):
                # Draw vertex.
                pygame.draw.circle(self.screen,
                                   self.purple,
                                   ((x * self.scale) + center,
                                    (y * self.scale) + center),
                                   size)
        

    def run(self):
        """
        Main loop where the canvas will be printed and the main 
        events will be handled.
        """
        running = True
        
        while running:
            self.screen.fill(self.dark_gray)

            self.draw_maze()
            self.draw_graph()
            
            for event in pygame.event.get():

                # If the user closes the window.
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
        


if __name__ == '__main__':
    canvas = Canvas(20, 20)
    canvas.run()
        

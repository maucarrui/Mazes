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
    white     = pygame.Color('#f8f8f2') # Miner.
    dark_blue = pygame.Color('#6272a4') # Walls of the maze.
    cyan      = pygame.Color('#8be9fd')
    green     = pygame.Color('#50fa7b') # Beginning of the maze.
    orange    = pygame.Color('#ffb86c') # Traveler.
    pink      = pygame.Color('#ff79c6')
    purple    = pygame.Color('#bd93f9') # Vertex of the graph.
    red       = pygame.Color('#ff5555') # End of the maze.
    yellow    = pygame.Color('#f1fa8c') # Edges of the graph.

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

    def draw_path_maze(self, cell, color):
        """
        Draws the path of a cell in the maze.
        :param cell: The cell which path will be drawn.
        :param color: The color of the path.
        """
        center = int(self.scale / 2)
        
        if cell.previous is not None:
            pygame.draw.line(self.screen,
                             color,
                             ((cell.X * self.scale) + center,
                              (cell.Y * self.scale) + center),
                             ((cell.previous.X * self.scale) + center,
                              (cell.previous.Y * self.scale) + center),
                             1)
            
            self.draw_path_maze(cell.previous, color)

    def draw_traveler_maze(self, traveler):
        """
        Draws the given traveler in the maze.
        :param traveler: The traveler to draw.
        """
        if (not self.maze.miner.is_done()):
            return
        
        center  = int(self.scale / 2)
        size    = int(self.scale / 4)

        # If the exit has been found, print the solution.
        if traveler.found_exit:
            self.draw_path_maze(traveler.current_cell, self.white)
        
        # Draw possible moves for the traveler.
        else:
            possible_moves = traveler.log

            for cell in possible_moves:

                x = cell.X
                y = cell.Y

                # Draw path.
                self.draw_path_maze(cell, self.yellow)

                # Draw move.
                pygame.draw.circle(self.screen,
                                   self.cyan,
                                   ((x * self.scale) + center,
                                    (y * self.scale) + center),
                                   size)

            # Draw traveler.
            if (self.maze.miner.is_done()):
                x = traveler.X
                y = traveler.Y

                pygame.draw.circle(self.screen,
                                   self.orange,
                                   ((x * self.scale) + center,
                                    (y * self.scale) + center),
                                   size)
                             

    def draw_maze(self):
        """
        Draws the current state of the maze.
        """

        # Variables needed to draw the miner.
        miner_x = self.maze.miner.X
        miner_y = self.maze.miner.Y
        center  = int(self.scale / 2)
        size    = int(self.scale / 4)

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

                # Draw start.
                if (cell.start):
                    pygame.draw.circle(self.screen,
                                       self.green,
                                       ((x * self.scale) + center,
                                        (y * self.scale) + center),
                                       size + 2)

                # Draw end.
                if (cell.end):
                    pygame.draw.circle(self.screen,
                                       self.red,
                                       ((x * self.scale) + center,
                                        (y * self.scale) + center),
                                       size + 2)

        # Draw miner.
        if (not self.maze.miner.is_done()):
            x = miner_x
            y = miner_y
            pygame.draw.circle(self.screen,
                               self.white,
                               ((x * self.scale) + center,
                                (y * self.scale) + center),
                               size)
                                           
                                           

    def draw_graph(self):
        """
        Draws the current state of the maze as a graph.
        """
        
        center = int(self.scale / 2)
        size   = int(self.scale / 4)

        # Variables to draw the miner.
        miner_x = self.maze.miner.X
        miner_y = self.maze.miner.Y

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
                if not cell.upper_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     ((x * self.scale) + center,
                                      ((y-1) * self.scale) + center),
                                     2)

                # Draw bottom edge.
                if not cell.bottom_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     ((x * self.scale) + center,
                                      ((y+1) * self.scale) + center),
                                     2)

                # Draw left edge.
                if not cell.left_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     (((x-1) * self.scale) + center,
                                      (y * self.scale) + center),
                                     2)

                # Draw right edge.
                if not cell.right_wall:
                    pygame.draw.line(self.screen,
                                     self.yellow,
                                     ((x * self.scale) + center,
                                      (y * self.scale) + center),
                                     (((x+1) * self.scale) + center,
                                      (y * self.scale) + center),
                                     2)

                # Draw miner.
                if (not self.maze.miner.is_done()):
                    if (x == miner_x) and (y == miner_y):
                        pygame.draw.circle(self.screen,
                                           self.white,
                                           ((x * self.scale) + center,
                                            (y * self.scale) + center),
                                           size + 2)
                    
        # Drawing vertex.
        for x in range(self.maze.x_size):
            for y in range(self.maze.y_size):
                cell = self.maze.board[x][y]

                if cell.start:
                    color = self.green
                elif cell.end:
                    color = self.red
                else:
                    color = self.purple
                    
                pygame.draw.circle(self.screen,
                                   color,
                                   ((x * self.scale) + center,
                                    (y * self.scale) + center),
                                   size)
        

    def run(self):
        """
        Main loop where the canvas will be printed and the main 
        events will be handled.
        """
        running    = True
        mode       = 'maze'
        auto_mine  = False
        traveler   = 'DFS'
        auto_solve = False

        traveler_BFS = self.maze.traveler_BFS
        traveler_DFS = self.maze.traveler_DFS
        
        while running:
            self.screen.fill(self.dark_gray)

            if mode == 'maze':
                self.draw_maze()

                if traveler == 'DFS':
                    self.draw_traveler_maze(traveler_DFS)
                else:
                    self.draw_traveler_maze(traveler_BFS)
                
            if mode == 'graph':
                self.draw_graph()

            if auto_mine and not self.maze.miner.is_done():
                self.maze.build_maze_step_by_step()

            if auto_solve:
                if not traveler_BFS.found_exit or not traveler_DFS.found_exit:
                    self.maze.solve_maze_step_by_step()
            
            for event in pygame.event.get():

                # If the user closes the window.
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    # Generate maze.
                    if event.key == pygame.K_w:
                        auto_mine = not auto_mine
                    
                    # Move the miner one step.
                    if event.key == pygame.K_q:
                        self.maze.build_maze_step_by_step()

                    # Switch view.
                    if event.key == pygame.K_m:
                        if mode == 'maze':
                            mode = 'graph'
                        else:
                            mode = 'maze'

                    # Switch traveler.
                    if event.key == pygame.K_s:
                        if traveler == 'BFS':
                            traveler = 'DFS'
                        else:
                            traveler = 'BFS'

                    # Generate solution.
                    if event.key == pygame.K_r:
                        auto_solve = not auto_solve

                    # Solve maze.
                    if event.key == pygame.K_e:
                        self.maze.solve_maze_step_by_step()
                    

            pygame.display.update()
        


if __name__ == '__main__':
    canvas = Canvas(20, 20)
    canvas.run()
        

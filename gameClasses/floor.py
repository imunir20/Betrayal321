import pygame
from gameClasses.tile import Tile


# Color codes
BLACK = (0, 0, 0)
GREY = (90, 90, 90)

DIM = 4        # NOT USED ANYMORE, IGNORE       Dimensions: DIM x DIM rooms on a floor
TWIDTH = 160       # Tile width
THEIGHT = 160      # Tile height
lineBorders = 4            # Width of the game board's grid borders
lineColor = GREY           # Color of the game board's grid borders


class Floor:
    def __init__(self, floorType):
        self.tiles = []                  # To be expanded into a 2D array that will represent the game board grid
        self.floorType = floorType       # 0 for Basement, 1 for Ground Floor, 2 for Upper Floor
        self.dim = 0                     # Dimensions of the floor (dim x dim rooms on a floor)

        if floorType == 0 or floorType == 1:        # Basement and Ground floor are 4x4 (16 rooms on those floors)
            self.dim = 4
        else:
            self.dim = 3                            # Upper floor is 3x3 (has 9 rooms)




    # Draws the tiles currently on the game board onto the game screen
    def draw(self, win):               
        for x in range(self.dim):
            for y in range(self.dim):
                if self.tiles[x][y].unlocked:    # If the tile has been unlocked/successfully clicked, then draw it
                    self.tiles[x][y].draw(win, self.floorType)   # If it hasn't been clicked, then don't draw, tile is still blank

        xPos = self.tiles[0][0].x                # X coordinate of top left corner of the tile
        yPos = self.tiles[0][0].y                # Y coordinate of top left corner of the tile
        xSpacing = TWIDTH * self.dim                  # Total width of all tiles combined
        ySpacing = THEIGHT * self.dim                 # Total height of all tiles combined
        pygame.draw.line(win, lineColor, (xPos, yPos), (xPos + xSpacing, yPos), width = lineBorders)  # Draw leftmost line on grid
        pygame.draw.line(win, lineColor, (xPos, yPos), (xPos, yPos + ySpacing), width = lineBorders)  # Draw topmost line on grid
        
        # Goes down grid and draws horizontal lines of grid
        for x in range(self.dim):
            xPos = self.tiles[x][0].x
            yPos = self.tiles[x][0].y
            pygame.draw.line(win, lineColor, (xPos, yPos + (THEIGHT)), (xPos + xSpacing, yPos + (THEIGHT)), width = lineBorders)
        
        # Goes across grid and draws vertical lines of grid
        for y in range(self.dim):
            xPos = self.tiles[0][y].x
            yPos = self.tiles[0][y].y
            pygame.draw.line(win, lineColor, (xPos + (TWIDTH), yPos), (xPos + (TWIDTH), yPos + ySpacing), width = lineBorders)
        

    # Pass in width and height of game screen/window
    def buildFloor(self, width, height):
        color = BLACK

        # Loops through grid and 'builds' the floor by creating tiles and putting it in the 2D array/grid
        for x in range(self.dim):
            self.tiles.append([])          # Add a new row to tiles grid, continue to make the array/grid 2-dimensional
            for y in range(self.dim):

                # Calculates position of tiles in the grid
                # If first in its row, then this is a special case for calculating the position
                if y == 0:
                    xPos = round((width - (self.dim * TWIDTH))/2)
                    yPos = round((height - (self.dim * THEIGHT))/2)        # Y position for tile first in its row
                    if x != 0:
                        yPos = self.tiles[x-1][y].y + THEIGHT         # Y position for all rows after first
                    room = Tile(xPos, yPos, x, y, color, TWIDTH, THEIGHT)
                    self.tiles[x].append(room)

                # Calculates position for tiles not the 1st tile in its row
                else:
                    oldX = self.tiles[x][y-1].x + TWIDTH
                    oldY = self.tiles[x][y-1].y
                    room = Tile(oldX, oldY, x, y, color, TWIDTH, THEIGHT)
                    self.tiles[x].append(room)
        if self.floorType == 1:
            self.tiles[2][3].unlocked = 1          # Entrance hall explored by default
            self.tiles[2][2].unlocked = 1          # Same with foyer
            self.tiles[2][1].unlocked = 1          # Same with grand staircase

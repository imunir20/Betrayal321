import pygame
from gameClasses.roomImgs import *

BLACK = (0, 0, 0)       # Color code for BLACK

class Tile:
    def __init__(self, x, y, row, col, color, width, height):
        self.x = x               # X coordinate of top left corner of tile
        self.y = y               # Y coordinate of top left corner of tile
        self.row = row
        self.col = col
        self.color = color       # Was used for debugging purposes, just put BLACK (0, 0, 0) by default when creating a Tile instance
        self.width = width       # Width of tile
        self.height = height     # Height of tile
        self.unlocked = 0        # If the room has been explored/unlocked
    
    # Win is the window to be drawn on
    def draw(self, win, floor):
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))    # Draws a rectangle behind room, used for debugging
        # Create a function that selects a random valid room to draw on the tile from a set of arrays
        # Example arrays: All possible basement rooms array, all possible ground rooms array, all possible upper floor rooms array
        # Abandoned room image is a placeholder for now
        
        if floor == 1 and self.row == 2 and self.col == 3:
            win.blit(staticEntrance, (self.x, self.y))
        elif floor == 1 and self.row == 2 and self.col == 2:
            win.blit(staticFoyer, (self.x, self.y))
        elif floor == 1 and self.row == 2 and self.col == 1:
            win.blit(staticGrandStaircase, (self.x, self.y))
        elif floor == 1 and self.row == 3 and self.col == 2:
           win.blit(basementStairs, (self.x, self.y))
        elif floor == 0 and self.row == 2 and self.col == 2:
            win.blit(basementLanding, (self.x, self.y))
        elif floor == 2 and self.row == 1 and self.col == 1:
            win.blit(upperLanding, (self.x, self.y))
        else:
            win.blit(abandoned, (self.x, self.y))
    

    def click(self, pos, pInfo):             # pos: position of mouse when mouse was clicked
        mouseX = pos[0]
        mouseY = pos[1]
        row = pInfo.location[1]
        col = pInfo.location[2]
        if self.x < mouseX < self.x + self.width and self.y < mouseY < self.y + self.height:   # C hecks to see if mouse x and y coords.
            if self.row + 1 == row and self.col == col or self.row - 1 == row and self.col == col or self.row == row and self.col + 1 == col or self.row == row and self.col - 1 == col:
                self.unlocked = 1                                       # are within tile's x and y coords. when the mouse was clicked
                return True
        else:
            return False
        

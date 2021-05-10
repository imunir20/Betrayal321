import pygame


# Contains the unique fields for each player


BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)
RED = (255, 69, 0)
DGREEN = (34, 139, 34)

pColors = [DGREEN, WHITE, RED, GREY]        # Colors for each player

THALF = 80
RECTSIZE = 10

class PlayerInfo:
    def __init__(self, id):
        self.pid = id            # Player ID (Player 0, Player 1, Player 2, Player 3)
        self.location = [1, 2, 3]        # Current location of the player  (current floor, row on the floor, column on that floor) -- start position at row 2, column 3
        self.floorView = 1                # The floor that the player is LOOKING at (not necessarily the one that they are on)
        self.currState = 'G'             # Current state of the player (Can be 'G' -- get the game, 'M' -- made a move)
                                         # More states to be added in the future most likely
        self.tile = None
        #self.distance = 0
        self.rollTurn = 0
        self.remMoves = -1
        if id == 0:
            self.remMoves = 4
            self.currState = 'W'


    def drawPlayer(self, win):
        if self.pid == 0:
            pygame.draw.rect(win, pColors[self.pid], (self.tile.x + THALF - RECTSIZE, self.tile.y + THALF - RECTSIZE, RECTSIZE, RECTSIZE))      # Top left
        elif self.pid == 1:
            pygame.draw.rect(win, pColors[self.pid], (self.tile.x + THALF + RECTSIZE, self.tile.y + THALF - RECTSIZE, RECTSIZE, RECTSIZE))       # Top right
        elif self.pid == 2:
            pygame.draw.rect(win, pColors[self.pid], (self.tile.x + THALF - RECTSIZE, self.tile.y + THALF + RECTSIZE, RECTSIZE, RECTSIZE))       # Bottom left
        else:
            pygame.draw.rect(win, pColors[self.pid], (self.tile.x + THALF + RECTSIZE, self.tile.y + THALF + RECTSIZE, RECTSIZE, RECTSIZE))      # Bottom right 



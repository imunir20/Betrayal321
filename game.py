import pygame
import os

from pygame import event
from gameClasses.playerinfo import PlayerInfo
from gameClasses.character import Character
from gameClasses.floor import Floor
from gameClasses.button import Button
from gameClasses.roomImgs import *
#from client import win
pygame.font.init()

# ----------- CONSTANTS ---------------------

# Feel free to add any constants


WHITE = (255, 255, 255)    
BLACK = (0, 0, 0)
GREY = (90, 90, 90)
RED = (220, 20, 60)
DRED = (255, 0, 0)
BLUE = (30, 144, 255)
GREEN = (50, 205, 50)
ORANGE = (255, 195, 0)
PURPLE = (148, 0, 211)
GOLD = (255, 215, 0)



width = 1250           # Width of game window 
height = 835           # NOT THE REAL HEIGHT OF THE GAME WINDOW, IGNORE THIS VARIABLE, USED FOR SOMETHING ELSE
trueHeight = 750       # REAL HEIGHT OF THE GAME WINDOW




bigFrankFont = pygame.font.Font("assets/Frankentype.otf", 50)    # Imported font (larger font size)
frankFont = pygame.font.Font("assets/Frankentype.otf", 25)       # Same imported font, just smaller size
smallFrankFont = pygame.font.Font("assets/Frankentype.otf", 22)      # Even smaller text

# -------- END OF CONSTANTS -------------------

# ------------ ASSETS -----------------------

# Some basic loading and scaling of images for later use

gameLogo = pygame.image.load(os.path.join('assets', 'misc', 'logo.png'))
gameLogo = pygame.transform.scale(gameLogo, (180, 50))


eventCardImage = pygame.image.load(os.path.join('assets', 'misc', 'event_back.jpg'))
eventCardImage = pygame.transform.scale(eventCardImage, (round(eventCardImage.get_width() * 0.25), round(eventCardImage.get_height() * 0.25)))

omenCardImage = pygame.image.load(os.path.join('assets', 'misc', 'omen_back.jpg'))
omenCardImage = pygame.transform.scale(eventCardImage, (round(omenCardImage.get_width() * 0.25), round(omenCardImage.get_height() * 0.25)))


# Characters
p0Img = pygame.image.load(os.path.join('assets', 'misc', 'brandonjaspers.png'))
p0Img = pygame.transform.scale(p0Img, (150, 150))
p1Img = pygame.image.load(os.path.join('assets', 'misc', 'fatherrhinehardt.png'))
p1Img = pygame.transform.scale(p1Img, (150, 150))
p2Img = pygame.image.load(os.path.join('assets', 'misc', 'flashwilliams.png'))
p2Img = pygame.transform.scale(p2Img, (150, 150))
p3Img = pygame.image.load(os.path.join('assets', 'misc', 'professorlongfellow.png'))
p3Img = pygame.transform.scale(p3Img, (150, 150))

# List that contains all the player images
playerImgs = [p0Img, p1Img, p2Img, p3Img]

# Character classes
p0 = Character('Brandon Jaspers', 4, 4, 4, 3)
p1 = Character('Father Rhinehardt', 3, 2, 6, 4)
p2 = Character('Flash Williams', 6, 3, 3, 3)
p3 = Character('Prof. Longfellow', 4, 3, 3, 5)

# Floor buttons (shown as text on the actual game screen on the left side)
upperFloorText = Button("Upper Floor", frankFont, 10, trueHeight - 300, WHITE)
groundFloorText = Button("Ground Floor", frankFont, 10, trueHeight - 270, WHITE)
basementFloorText = Button("Basement", frankFont, 10, trueHeight - 240, WHITE)

# Floor buttons in a list
floorButtons = [basementFloorText, groundFloorText, upperFloorText]


# All the possible backgrounds that are used in the game
# Note that this first one, "jail.jpg" is not being used right now, but the other 3 are
bgd = pygame.image.load(os.path.join('assets', 'misc', 'jail.jpg'))
bgd = pygame.transform.scale(bgd, (width, trueHeight))

# Used as the background for the ground floor
bgd2 = pygame.image.load(os.path.join('assets', 'misc', 'foyer.jpg'))
bgd2 = pygame.transform.scale(bgd2, (width, trueHeight))

# Used as the background for the basement floor
bgd3 = pygame.image.load(os.path.join('assets', 'misc', 'basement.png'))
bgd3 = pygame.transform.scale(bgd3, (width, trueHeight))

# Used as the background for the upper floor
bgd4 = pygame.image.load(os.path.join('assets', 'misc', 'upstairs.png'))
bgd4 = pygame.transform.scale(bgd4, (width, trueHeight))

paperBgd = pygame.image.load(os.path.join('assets', 'misc', 'charbg.jpg'))
paperBgd = pygame.transform.scale(paperBgd, (groundFloorText.width + 15, 95))

# Variable that stores the image of the current background being shown on the game screen of the player
# By default, this is bgd2 since the player begins the game at the ground floor
currBgd = bgd2

numPlayers = 4

# ----------- END OF ASSETS --------------------




class Game:
    def __init__(self, id):
        self.playerId = id
        self.pInfo = []
        for i in range(numPlayers):
            self.pInfo.append(PlayerInfo(i))
            #self.pInfo[i].pid = i
        #self.pInfo = PlayerInfo()         # Contains all the unique fields for a player, see the class to look at these fields
        #self.pInfo.pid = id              # Player ID (e.g. Player 0, Player 1, Player 2, Player 3)

        #self.id = id
        #self.pStatus = [False, False, False, False]     # Keeps track if players have gone; first index for player 0, 2nd for p1, etc.

        self.players = [p0, p1, p2, p3]          # List of character objects initialized earlier in this file
        
        # Building/Initializing all the floors
        # buildFloor function builds the 2D list/array that represents the grid/floor you see on the game screen
        # See the floor.py file for more details
        self.base = Floor(0)
        self.base.buildFloor(width, height) 
        self.ground = Floor(1)
        self.ground.buildFloor(width, height)
        self.upper = Floor(2)
        self.upper.buildFloor(width, height)

        for i in range(numPlayers):
            self.pInfo[i].tile = self.ground.tiles[2][3]
        #self.pInfo.tile = self.ground.tiles[2][3]
        
        self.commentary = "Welcome .. to your worst nightmare"         # Commentary text shown at the top of the screen

        self.ready = False                   # If the game is ready/has started


    # Basic getter function
    def connected(self):
        return self.ready


    # Draws the game onto the game window
    def drawGame(self, win):

        # Stores the character of the client into this local player variable
        #player = self.players[self.pInfo.pid]
        player = self.players[self.playerId]

        # Default floor buttons color is white
        basementFloorText.color = WHITE
        groundFloorText.color = WHITE
        upperFloorText.color = WHITE


        # These if statements check which floor the client/player is on, and makes that floor button's text RED, and sets the background for that floor
        if self.pInfo[self.playerId].floorView == 0:
            basementFloorText.color = RED
            currFloor = self.base
            currBgd = bgd3
        elif self.pInfo[self.playerId].floorView == 1:
            groundFloorText.color = RED
            currFloor = self.ground
            currBgd = bgd2
        else:
            upperFloorText.color = RED
            currFloor = self.upper
            currBgd = bgd4
        

        win.fill(WHITE)                       # Just makes the background, don't know why I still include this line lol
        win.blit(currBgd, (0, 0))              # Display the background image
        win.blit(gameLogo, (10, 15))           # Draw the game logo at the top left corner
        #win.blit(paperBgd, (0, trueHeight - 185))           # Paper background displayed before character picture, stats
        #win.blit(playerImgs[self.pInfo.pid], (10, trueHeight - 150))        # Draw the client/player's character picture in bottom left corner
        win.blit(playerImgs[self.playerId], (10, trueHeight - 150))

        #win.blit(paperBgd, (0, trueHeight - 305))
        # Draw the floor buttons -- look at the button.py file to see how these are drawn
        basementFloorText.draw(win)
        groundFloorText.draw(win)
        upperFloorText.draw(win)


        # Draw the event, omen card images

        win.blit(eventCardImage, (7, 85))
        win.blit(omenCardImage, (133, 85))


        # Render the fonts to be drawn on the screen
        commText = bigFrankFont.render(self.commentary, False, WHITE)
        nameText = frankFont.render(player.name, False, WHITE)
        #spdText = smallFrankFont.render('Speed: ' + str(player.spd), False, WHITE)
        #mightText = smallFrankFont.render('Might: ' + str(player.str), False, WHITE)
        #sanText = smallFrankFont.render('Sanity: ' + str(player.san), False, WHITE)
        #knowText = smallFrankFont.render('Knowledge: ' + str(player.int), False, WHITE)

        spdText = smallFrankFont.render('Speed: ', False, DRED)
        mightText = smallFrankFont.render('Might: ', False, BLUE)
        sanText = smallFrankFont.render('Sanity: ', False, PURPLE)
        knowText = smallFrankFont.render('Knowledge: ', False, GOLD)

        spdNum = smallFrankFont.render(str(player.spd), False, WHITE)
        mightNum = smallFrankFont.render(str(player.str), False, WHITE)
        sanNum = smallFrankFont.render(str(player.san), False, WHITE)
        knowNum = smallFrankFont.render(str(player.int), False, WHITE)


        # Draw the rendered fonts
        win.blit(commText, ((width/2) - (commText.get_width()/2), 10))
        win.blit(nameText, (10, trueHeight - 180))                  
        win.blit(spdText, (165, trueHeight - 120))
        win.blit(mightText, (165, trueHeight - 90))
        win.blit(sanText, (165, trueHeight - 60))
        win.blit(knowText, (165, trueHeight - 30))


        win.blit(spdNum, (160 + spdText.get_width(), trueHeight - 120))
        win.blit(mightNum, (160 + mightText.get_width(), trueHeight - 90))
        win.blit(sanNum, (160 + sanText.get_width(), trueHeight - 60))
        win.blit(knowNum, (160 + knowText.get_width(), trueHeight - 30))



        
        # Draw the current floor/grid and the rooms that have been explored
        currFloor.draw(win)
        for i in range(numPlayers):
            if self.pInfo[self.playerId].floorView == self.pInfo[i].location[0]:
                self.pInfo[i].drawPlayer(win)
        #self.pInfo.drawPlayer(win)



import pygame
pygame.font.init()

class Button:
    def __init__(self, text, font, x, y, color):
        self.text = text         # button text
        self.font = font         # button text font
        self.x = x                # x coordinate of the button's position
        self.y = y                # y coordinate of the button's position
        self.color = color        # color of the button's text

        #self.height = height
        #self.width = width


        sampleText = self.font.render(self.text, False, self.color)

        self.width = sampleText.get_width()          # width of the button text
        self.height = sampleText.get_height()        # height of the button text


    # Change this function later to include a font variable to allow for imported fonts and remove the comicsans line
    # Remove anti-aliasing (False instead of 1), change color as needed in the font.render line later
    def draw(self, win):
        newButton = self.font.render(self.text, False, self.color)          # Render the button (it is just text that acts as a button)
        win.blit(newButton, (self.x, self.y))                          # Draw the button
        

        # Ignore these lines, this is old code just kept just in case
        # pygame.draw.rect(win, (255, 255, 255), (self.x + self.width, self.y + self.height, 5, 5))
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        #font = pygame.font.SysFont("comicsans", 40)
        #text = font.render(self.text, 1, (255,255,255))
        #win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    # Detects if the button has been clocked
    def click(self, pos):
        x1 = pos[0]      # x coordinate of where the mouse was clicked
        y1 = pos[1]      # y coordinate of where the mouse was clicked
        if self.x < x1 < self.x + self.width and self.y < y1 < self.y + self.height:
            return True
        else:
            return False
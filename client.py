import pygame
import os
import pickle
from network import Network
from game import Game
from game import floorButtons
from gameClasses.button import Button
pygame.font.init()




width = 1250                       # Width of the game screen
height = 835                       # THIS IS NOT THE REAL HEIGHT OF THE GAME SCREEN, IGNORE THIS VARIABLE, IT IS USED FOR SOMETHING ELSE
trueHeight = 750                   # THIS IS THE REAL HEIGHT OF THE GAME SCREEN
win = pygame.display.set_mode((width, trueHeight))            # Game window
pygame.display.set_caption("Betrayal at House on the Hill")
FPS = 60


DIM = 4                                # NOT USED ANYMORE       Dimensions of the grid/floor

numPlayers = 4

# -------------- Color Codes -------------------

# Feel free to add more, can find color codes from Google

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)

# -------------- End of color codes --------------------------------




# -------------- ASSETS LOADING AND SCALING --------------------------

bigFrankFont = pygame.font.Font("assets/Frankentype.otf", 100)    # Imported font (larger font size)
frankFont = pygame.font.Font("assets/Frankentype.otf", 35)       # Same imported font, just smaller size
smallFrankFont = pygame.font.Font("assets/Frankentype.otf", 22)      # Even smaller text

houseBgd = pygame.image.load(os.path.join('assets', 'misc', 'haunted-house.jpg'))          # Load haunted house image, scale it
houseBgd = pygame.transform.scale(houseBgd, (width, trueHeight))

gameLogo = pygame.image.load(os.path.join('assets', 'misc', 'logo.png'))            # Load logo image, scale it
gameLogo = pygame.transform.scale(gameLogo, (275, 80))

helpBgd = pygame.image.load(os.path.join('assets', 'misc', 'charbg.jpg'))
helpBgd = pygame.transform.scale(helpBgd, (width, trueHeight))


# ------------ END OF ASSETS LOADING AND SCALING ----------------------------



# This functions draws the window.
# Either draws the waiting for players screen if game hasn't started yet, or draws the actual game screen
# Please look at the drawGame function in game.py to learn more about how the game screen is drawn

def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        win.fill(WHITE)
        win.blit(houseBgd, (0, 0))              # Draw background image onto screen
        win.blit(gameLogo, (10, 15))            # Draw game logo at top left corner of screen
        waitText = bigFrankFont.render('Waiting for Players...', False, WHITE)         # Render the waiting for players font
        win.blit(waitText, ((width/2) - (waitText.get_width()/2), (trueHeight/2) - waitText.get_height()/2))    # Draw the rendered font

    else:
        game.drawGame(win)               # Look at this function in game.py for more details


    pygame.display.update()           # Update the game screen with the new changes


# Main game loop

def main():
    run = True                          # Basic initializations
    clock = pygame.time.Clock()
    n = Network()                     # Setup connections between the client (player) and the server
    player = int(n.getP())            # Server will send back the number of the player, which is then stored in this player variable
    print("You are player", player)      # Debug message printed to console
    game = Game(player)                # Initialize game object with player ID given to us by the server
    if player == 0:
        game.pInfo[player].currState = 'W'
    else:
        game.pInfo[player].currState = 'G'         # Set the current state of the client's game to 'G', which means "get the game"

    # Actual game loop
    while run: 
        clock.tick(FPS)           # Game runs at 60 FPS
        try:
            if game.pInfo[player].currState == 'G':          # Player/Client will try to get game
                game = n.sendGame(game)              # Player will send their game to server for it to be updated
                if game.pInfo[player].currState == 'W':
                    game.pInfo[player].currState = 'W'
                else:
                    game.pInfo[player].currState = 'G'           # Make sure that the player/client will continue to try and get the game in next loop iteration
            elif game.pInfo[player].currState == 'D':
                game = n.sendGame(game)             # Get/Update game from the server
                game.pInfo[player].currState = 'G'
            else:
                game = n.sendGame(game)             # Get/Update game from the server
                game.pInfo[player].currState = 'W'
                #game.pInfo[player].currState = 'G'          
                
        except Exception as e:            # Exception handling
            print("Main loop error")
            print(e)
            run = False
            print("Couldn't get game..")
            break

        redrawWindow(win, game, player)            # Draw the game with the updated game sent to us by the server

        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # If the player clicked the 'X' button in top right corner to exit
                run = False                      # Stop the game loop
                pygame.quit()                   # Quit the game
            
            if event.type == pygame.MOUSEBUTTONDOWN:        # If the click has clicked their mouse
                mouse = pygame.mouse.get_pos()               # Get coordinates of where mouse was clicked
                print(mouse)                  # Helpful debug print statement to see coordinates of where mouse clicked
                
                clicker = True               # Used to skip future nested for loops down below for better efficiency
                
                for i in range(3):            # Traverse through the 3 floor buttons
                    if floorButtons[i].click(mouse) and game.connected():      # If one of the floor buttons was clicked on
                        game.pInfo[player].floorView = i                 # Then the player wants to look at another floor, change appropriate variable
                        clicker = False                      # Won't have to check if they clicked on tile cause they clicked on a floor button (not possible to click on both)
                
                if clicker:                                  # Will only execute if a floor button was not clicked
                    if game.pInfo[player].floorView == 0:           # Current floor is basement if they are looking at basement (0)
                        currFloor = game.base
                    elif game.pInfo[player].floorView == 1:          # Current floor is ground floor if they are looking at ground floor (1)
                        currFloor = game.ground
                    else:                                   # Else, current floor must be upper floor if they are not looking at the other two other floors (2)
                        currFloor = game.upper
                    
                    if game.pInfo[player].currState == 'W':
                        #currRow = game.pInfo[player].location[1]
                        #currCol = game.pInfo[player].location[2]
                        for x in range(currFloor.dim):           # Traverse that floor's grid to see if one of its tiles/squares were clicked on
                            for y in range(currFloor.dim):
                                if currFloor.tiles[x][y].click(mouse, game.pInfo[player]) and game.connected():        # If one of the tiles/squares were clicked on
                                    game.pInfo[player].remMoves = game.pInfo[player].remMoves - 1
                                    if game.pInfo[player].remMoves == 0:
                                        game.pInfo[player].currState = 'D'
                                        #game.pInfo[player].remMoves = -1
                                        #game.pInfo[(player + 1) % numPlayers].remMoves = game.players[(player + 1) % numPlayers].spd
                                        #game.pInfo[(player + 1) % numPlayers].currState = 'W'
                                    else:    
                                        game.pInfo[player].currState = 'M'                                    # Update the current state to be "M", meaning the player made a move
                                    #game.currFloor.tiles[x][y].unlocked = 1       # Already done in click function of tile
                                    
                                    
                                                    
                                    if game.pInfo[player].location[0] == 1 and x == 2 and y == 1:
                                        game.upper.tiles[1][1].unlocked = 1
                                        game.pInfo[player].location[0] = 2
                                        game.pInfo[player].location[1] = 1
                                        game.pInfo[player].location[2] = 1
                                        game.pInfo[player].tile = game.upper.tiles[1][1]
                                    elif game.pInfo[player].location[0] == 1 and x == 3 and y == 2:
                                        game.base.tiles[2][2].unlocked = 1
                                        game.pInfo[player].location[0] = 0
                                        game.pInfo[player].location[1] = 2
                                        game.pInfo[player].location[2] = 2
                                        game.pInfo[player].tile = game.base.tiles[2][2]
                                    elif game.pInfo[player].location[0] == 0 and x == 2 and y == 2:
                                        game.ground.tiles[3][2].unlocked = 1
                                        game.pInfo[player].location[0] = 1
                                        game.pInfo[player].location[1] = 3
                                        game.pInfo[player].location[2] = 2
                                        game.pInfo[player].tile = game.ground.tiles[3][2]
                                    elif game.pInfo[player].location[0] == 2 and x == 1 and y == 1:
                                        game.ground.tiles[2][1].unlocked = 1
                                        game.pInfo[player].location[0] = 1
                                        game.pInfo[player].location[1] = 2
                                        game.pInfo[player].location[2] = 1
                                        game.pInfo[player].tile = game.ground.tiles[2][1]
                                    else:
                                        game.pInfo[player].location[1] = x
                                        game.pInfo[player].location[2] = y
                                        game.pInfo[player].tile = currFloor.tiles[x][y]
                                    break
                                    
                                    
                                    #game.pInfo[player].location[1] = x
                                    #game.pInfo[player].location[2] = y
                                    #game.pInfo[player].tile = currFloor.tiles[x][y]
                                    #break
                
        redrawWindow(win, game, player)                                 # Redraw window to reflect the new changes

# Draws menu screen and goes into game when the player clicks

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)          # Game runs at 60 FPS

        # Draws menu screen
        
        win.fill(WHITE)
        win.blit(houseBgd, (0, 0))
        win.blit(gameLogo, (10, 15))
        #win.blit(gameLogo, ((width/2) - (gameLogo.get_width()/2), (trueHeight/2) - (gameLogo.get_height()/2) - 225))
        playText = bigFrankFont.render('PLAY', False, WHITE)
        helpText = bigFrankFont.render("HOW TO PLAY", False, WHITE)
        #win.blit(playText, ((width/2) - (playText.get_width()/2), trueHeight/2))
        playButton = Button("PLAY", bigFrankFont, (width/2) - (playText.get_width()/2), trueHeight/2, WHITE)
        helpButton = Button("How to play", bigFrankFont, (width/2) - (helpText.get_width()/2), trueHeight/2 + 125, WHITE)
        playButton.draw(win)
        helpButton.draw(win)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # If the player tried exiting, then exit the game
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:         # If the player clicked (anywhere), then leave main menu and put them in a game or waiting queue for a game
                mousePos = pygame.mouse.get_pos()
                if playButton.click(mousePos):
                    run = False
                if helpButton.click(mousePos):
                    win.fill(WHITE)
                    win.blit(helpBgd, (0, 0))
                    hText0 = frankFont.render("How to play Betrayal at House on the Hill", False, WHITE)
                    hText1 = frankFont.render("There are two stages: The exploration and haunt phases", False, WHITE)
                    hText2 = frankFont.render("When exploring, players explore rooms according to the speed stat", False, WHITE)
                    hText3 = frankFont.render("Exploring certain rooms will trigger events, affecting stats", False, WHITE)
                    hText4 = frankFont.render("Some rooms will trigger omens, events related to the Haunt", False, WHITE)
                    hText5 = frankFont.render("The Haunt begins when dice rolled during an omen is less than the omen count", False, WHITE)
                    hText6 = frankFont.render("A traitor is revealed and must eliminate the heroes (remaining players", False, WHITE)
                    hText7 = frankFont.render("The traitor and heroes may engage in combat using their stats and dice rolls", False, WHITE)
                    hText8 = frankFont.render("If the traitor eliminates the heroes, the traitor wins, otherwise, the heroes win", False, WHITE)

                    win.blit(hText0, (width/2 - hText0.get_width()/2, 10))

                    hTexts = [hText1, hText2, hText3, hText4, hText5, hText6, hText7, hText8]

                    currentYPos = 0
                    for k in range(8):
                        if k == 0:
                            win.blit(hTexts[k], (10, 75))
                            currentYPos = 75 + 75
                        else:
                            win.blit(hTexts[k], (10, currentYPos))
                            currentYPos = currentYPos + 75

                    backText = bigFrankFont.render("Back", False, WHITE)
                    backButton = Button("Back", bigFrankFont, (width/2) - (backText.get_width()/2), trueHeight - 90, WHITE)
                    backButton.draw(win)
                    pygame.display.update()
                    run2 = True
                    while run2:
                        for bigEvent in pygame.event.get():
                            if bigEvent.type == pygame.QUIT:
                                pygame.quit()
                                run2 = False
                            if bigEvent.type == pygame.MOUSEBUTTONDOWN:
                                mouseLoc = pygame.mouse.get_pos()
                                if backButton.click(mouseLoc):
                                    run2 = False


    main()                               # Run the main game loop


# When this client.py file is ran, these 2 lines of code below are the first ones to be executed
while True:
    menu_screen()
import socket
from _thread import *
import pickle
from game import Game

server = "192.168.1.161"      # If running the server locally on your computer, make this your IPv4 address (can be found using ipconfig command on terminal)
port = 5353                   # Unused/free port usually, so we will use it for our server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Listen for connections
s.listen()
print("Waiting for a connection, Server Started")

connected = set()
# Store the currently running games in this list
games = {}
idCount = 0


# Lots of commented out debugging statements used from earlier, you can ignore them
def threaded_client(conn, p, gameId):
    global idCount
    conn.sendall(str.encode(str(p)))
    #games[gameId].currPlayer = p

    reply = ""
    while True:
        try:
            #print("Attempting to read string that was sent by client")
            #data = conn.recv(4096).decode()
            data = pickle.loads(conn.recv(2048*4))
            #print("Received the send")
            if gameId in games:
                game = games[gameId]

                if not data:
                    #print("Not data")
                    break
                else:
                    tempId = data.playerId
                    if data.pInfo[tempId].currState == 'G' or data.pInfo[tempId].currState == 'W':         # If the player is trying to get the game
                        #print("Server sending the game")
                        #games[gameId].pInfo = data.pInfo         # Don't lose their unique player info
                        games[gameId].playerId = tempId
                        if games[gameId].pInfo[tempId].currState == 'F':
                            games[gameId].pInfo[tempId] = data.pInfo[tempId] 
                            games[gameId].pInfo[tempId].remMoves = game.players[tempId].spd
                            games[gameId].pInfo[tempId].currState = 'W'
                        else:
                            games[gameId].pInfo[tempId] = data.pInfo[tempId] 
                        conn.sendall(pickle.dumps(games[gameId]))        # Send them the new/updated game (pickle.dumps used for encryption)
                    else:                                        # Else, current state must be 'M', meaning the client/player made a move
                        #print("Server updating the game")
                        games[gameId] = data
                        if data.pInfo[tempId].currState == 'D':
                            games[gameId].pInfo[tempId].remMoves = -1
                            games[gameId].pInfo[tempId].currState == 'G'
                            #game.pInfo[(tempId + 1) % numPlayers].remMoves = game.players[(tempId + 1) % numPlayers].spd
                            games[gameId].pInfo[(tempId + 1) % numPlayers].currState = 'F'
                        else:
                            games[gameId].pInfo[tempId].currState = 'W'
                        #games[gameId] = data                       # Update the game stored by the server
                        conn.sendall(pickle.dumps(games[gameId]))        # Send them the new game, doesn't really do much though
                                                                         # Pickle.dumps just encrypts the object
                    #print("About to print length, then dump the game")
                    #print(len(game))
                    #print("Hello? Was length printed?")
                    #conn.sendall(pickle.dumps(game))
                    #print("Dump operation done")

            else:
                break
        except Exception as e:
            print(e)
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


# Number of players that play in a game -- Feel free to use 2 for easy testing purposes, but 4 will be used for submission
numPlayers = 4
p = 0
while True:
    # Accept the new connection
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    # Assign the game ID
    gameId = (idCount - 1)//numPlayers
    if (idCount % numPlayers == 1):
        # Create the game
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        if(idCount % numPlayers == 0):
            # Enough players in game, start the game
            games[gameId].ready = True
        p = (p + 1) % numPlayers

    # Start a new thread for this new client connection
    start_new_thread(threaded_client, (conn, p, gameId))
import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ""      # ipconfig command on terminal to find IP Address
        self.port = 5353
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)
            pass

    def send(self, data):
        try:
            #self.client.send(str.encode(data))
            #return pickle.loads(self.client.recv(2048*16))
            self.client.sendall(str.encode(data))
            #print("Sucessful send?")
            response = pickle.loads(self.client.recv(2048*4))
            print(response)
            return response
        except socket.error as e:
            print("Network send error")
            print(e)
    
    def sendGame(self, data):
        try:
            self.client.sendall(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)

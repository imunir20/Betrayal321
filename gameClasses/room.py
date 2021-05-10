
class Room:
     def __init__(self, event, item, name, left, right, up, down, floor):
        self.event = event #int, event number, set to 0 if no event
        self.item = item #char,
        self.name = name #string
        self.l = left ###
        self.r = right#All
        self.u = up   #Boolean, if t, path is free, else path is walled
        self.d = down ####
        self.floor = floor # 0 b, 1 bg, 2 g, 3 gu, 4 u, 5 ub, 6 all
    
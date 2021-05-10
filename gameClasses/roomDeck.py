
from gameClasses import Room

class RoomDeck:
     def __init__(self):
        self.hall = Room(0, null, "Hall", 0, 0, 1, 1, 3) #Room(eventNum, itemCode, name, left, right, up, down, floor)
        abandonedRoom = Room(0, 'o', "Abandoned Room", 1, 1, 1, 1, 1)
        attic = Room(1, null, "Attic", 0, 0, 0, 1, 4)
        balcony = Room(0, 'o', "Balcony", 0, 0, 1, 1, 4)
        ballroom = 0
        BasementLanding = 0
        Bedroom = 0
        BloodyRoom = 0
        Catacombs = 0
        Chapel = 0
        CharredRoom = 0
        Chasm = 0
        CoalChute = 0
        CollapsedRoom = 0
        Conservatory = 0
        CreakyHallway = 0
        Crypt = 0
        DiningRoom = 0
        DustyHallway = 0
        EntranceHall(s) = 0
        Foyer(s) = 0
        FurnaceRoom = 0
        Gallery = 0
        GameRoom = 0
        Gardens = 0
        GrandStaircase(s) = 0
        Graveyard = 0
        Gymnasium = 0
        JunkRoom = 0
        Kitchen = 0
        Larder = 0
        Library = 0
        MasterBedroom = 0
        MysticElevator = 0
        OperatingLaboratory = 0    
        OrganRoom = 0
        Patio = 0
        PentagramChamber = 0
        ResearchLaboratory = 0
        Servants’Quarters = 0
        StairsfromBedroom = 0
        StatuaryCorridor = 0
        Storeroom = 0
        Tower = 0
        UndergroundLake = 0
        UpperLanding(s) = 0
        Vault = 0
        WineCellar = 0
        self.deck = []
        
def draw(self, expected):
        
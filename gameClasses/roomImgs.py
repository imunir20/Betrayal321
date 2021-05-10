import pygame
import os

TILEWIDTH = 160
TILEHEIGHT = 160

# For all images, first load it in with the correct path using pygame.image.load and os.path.join
# After doing above step, then scale the image to TILEWIDTH, TILEHEIGHT size

# Use the abandoned-room asset as an example


abandoned = pygame.image.load(os.path.join('assets', 'rooms', 'abandoned-room.jpg'))
abandoned = pygame.transform.scale(abandoned, (TILEWIDTH, TILEHEIGHT))

attic = pygame.image.load(os.path.join('assets', 'rooms', 'attic.jpg'))
attic = pygame.transform.scale(attic, (TILEWIDTH, TILEHEIGHT))

balcony = pygame.image.load(os.path.join('assets', 'rooms', 'balcony.jpg'))
balcony = pygame.transform.scale(balcony, (TILEWIDTH, TILEHEIGHT))

ballroom = pygame.image.load(os.path.join('assets', 'rooms', 'ballroom.jpg'))
ballroom = pygame.transform.scale(ballroom, (TILEWIDTH, TILEHEIGHT))

basementLanding = pygame.image.load(os.path.join('assets', 'rooms', 'basement-landing.jpg'))
basementLanding = pygame.transform.scale(basementLanding, (TILEWIDTH, TILEHEIGHT))

basementStairs = pygame.image.load(os.path.join('assets', 'rooms', 'basement-stairs.jpg'))
basementStairs = pygame.transform.scale(basementStairs, (TILEWIDTH, TILEHEIGHT))

bedroom = pygame.image.load(os.path.join('assets', 'rooms', 'bedroom.jpg'))
bedroom = pygame.transform.scale(bedroom, (TILEWIDTH, TILEHEIGHT))

catacombs = pygame.image.load(os.path.join('assets', 'rooms', 'catacombs.jpg'))
catacombs = pygame.transform.scale(catacombs, (TILEWIDTH, TILEHEIGHT))

charredRoom = pygame.image.load(os.path.join('assets', 'rooms', 'charred-room.jpg'))
charredRoom = pygame.transform.scale(charredRoom, (TILEWIDTH, TILEHEIGHT))

chasm = pygame.image.load(os.path.join('assets', 'rooms', 'chasm.jpg'))
chasm = pygame.transform.scale(chasm, (TILEWIDTH, TILEHEIGHT))

coalChute = pygame.image.load(os.path.join('assets', 'rooms', 'coal-chute.jpg'))
coalChute = pygame.transform.scale(coalChute, (TILEWIDTH, TILEHEIGHT))

collapsedRoom = pygame.image.load(os.path.join('assets', 'rooms', 'collapsed-room.jpg'))
collapsedRoom = pygame.transform.scale(collapsedRoom, (TILEWIDTH, TILEHEIGHT))

conservatory = pygame.image.load(os.path.join('assets', 'rooms', 'conservatory.jpg'))
conservatory = pygame.transform.scale(conservatory, (TILEWIDTH, TILEHEIGHT))

creakyHallway = pygame.image.load(os.path.join('assets', 'rooms', 'creaky-hallway.jpg'))
creakyHallway = pygame.transform.scale(creakyHallway, (TILEWIDTH, TILEHEIGHT))

diningRoom = pygame.image.load(os.path.join('assets', 'rooms', 'dining-room.jpg'))
diningRoom = pygame.transform.scale(diningRoom, (TILEWIDTH, TILEHEIGHT))

dustyHallway = pygame.image.load(os.path.join('assets', 'rooms', 'dusty-hallway.jpg'))
dustyHallway = pygame.transform.scale(dustyHallway, (TILEWIDTH, TILEHEIGHT))

furnaceRoom = pygame.image.load(os.path.join('assets', 'rooms', 'furnace-room.jpg'))
furnaceRoom = pygame.transform.scale(furnaceRoom, (TILEWIDTH, TILEHEIGHT))

gallery = pygame.image.load(os.path.join('assets', 'rooms', 'gallery.jpg'))
gallery = pygame.transform.scale(gallery, (TILEWIDTH, TILEHEIGHT))

gameRoom = pygame.image.load(os.path.join('assets', 'rooms', 'game-room.jpg'))
gameRoom = pygame.transform.scale(gameRoom, (TILEWIDTH, TILEHEIGHT))

gardens = pygame.image.load(os.path.join('assets', 'rooms', 'gardens.jpg'))
gardens = pygame.transform.scale(gardens, (TILEWIDTH, TILEHEIGHT))

gym = pygame.image.load(os.path.join('assets', 'rooms', 'gymnasium.jpg'))
gym = pygame.transform.scale(gym, (TILEWIDTH, TILEHEIGHT))

junkRoom = pygame.image.load(os.path.join('assets', 'rooms', 'junk-room.jpg'))
junkRoom = pygame.transform.scale(junkRoom, (TILEWIDTH, TILEHEIGHT))

kitchen = pygame.image.load(os.path.join('assets', 'rooms', 'kitchen.jpg'))
kitchen = pygame.transform.scale(kitchen, (TILEWIDTH, TILEHEIGHT))

larder = pygame.image.load(os.path.join('assets', 'rooms', 'larder.jpg'))
larder = pygame.transform.scale(larder, (TILEWIDTH, TILEHEIGHT))

library = pygame.image.load(os.path.join('assets', 'rooms', 'library.jpg'))
library = pygame.transform.scale(library, (TILEWIDTH, TILEHEIGHT))

masterBedroom = pygame.image.load(os.path.join('assets', 'rooms', 'master-bedroom.jpg'))
masterBedroom = pygame.transform.scale(masterBedroom, (TILEWIDTH, TILEHEIGHT))

operatingLab = pygame.image.load(os.path.join('assets', 'rooms', 'operating-laboratory.jpg'))
operatingLab = pygame.transform.scale(operatingLab, (TILEWIDTH, TILEHEIGHT))

organRoom = pygame.image.load(os.path.join('assets', 'rooms', 'organ-room.jpg'))
organRoom = pygame.transform.scale(organRoom, (TILEWIDTH, TILEHEIGHT))

panicRoom = pygame.image.load(os.path.join('assets', 'rooms', 'panic-room.jpg'))
panicRoom = pygame.transform.scale(panicRoom, (TILEWIDTH, TILEHEIGHT))

patio = pygame.image.load(os.path.join('assets', 'rooms', 'patio.jpg'))
patio = pygame.transform.scale(patio, (TILEWIDTH, TILEHEIGHT))

pentagramChamber = pygame.image.load(os.path.join('assets', 'rooms', 'pentagram-chamber.jpg'))
pentagramChamber = pygame.transform.scale(pentagramChamber, (TILEWIDTH, TILEHEIGHT))

researchLab = pygame.image.load(os.path.join('assets', 'rooms', 'research-laboratory.jpg'))
researchLab = pygame.transform.scale(researchLab, (TILEWIDTH, TILEHEIGHT))

servantsQuarters = pygame.image.load(os.path.join('assets', 'rooms', 'servants-quarters.jpg'))
servantsQuarters = pygame.transform.scale(servantsQuarters, (TILEWIDTH, TILEHEIGHT))

staticEntrance = pygame.image.load(os.path.join('assets', 'rooms', 'static-entrance-hall.jpg'))
staticEntrance = pygame.transform.scale(staticEntrance, (TILEWIDTH, TILEHEIGHT))

staticFoyer = pygame.image.load(os.path.join('assets', 'rooms', 'static-foyer.jpg'))
staticFoyer = pygame.transform.scale(staticFoyer, (TILEWIDTH, TILEHEIGHT))

staticGrandStaircase = pygame.image.load(os.path.join('assets', 'rooms', 'static-grand-staircase.jpg'))
staticGrandStaircase = pygame.transform.scale(staticGrandStaircase, (TILEWIDTH, TILEHEIGHT))

statuaryCorridor = pygame.image.load(os.path.join('assets', 'rooms', 'statuary-corridor.jpg'))
statuaryCorridor = pygame.transform.scale(statuaryCorridor, (TILEWIDTH, TILEHEIGHT))

storeRoom = pygame.image.load(os.path.join('assets', 'rooms', 'storeroom.jpg'))
storeRoom = pygame.transform.scale(storeRoom, (TILEWIDTH, TILEHEIGHT))

tower = pygame.image.load(os.path.join('assets', 'rooms', 'tower.jpg'))
tower = pygame.transform.scale(tower, (TILEWIDTH, TILEHEIGHT))

undergroundLake = pygame.image.load(os.path.join('assets', 'rooms', 'underground-lake.jpg'))
undergroundLake = pygame.transform.scale(undergroundLake, (TILEWIDTH, TILEHEIGHT))

upperLanding = pygame.image.load(os.path.join('assets', 'rooms', 'upper-landing.jpg'))
upperLanding = pygame.transform.scale(upperLanding, (TILEWIDTH, TILEHEIGHT))

vault = pygame.image.load(os.path.join('assets', 'rooms', 'vault.jpg'))
vault = pygame.transform.scale(vault, (TILEWIDTH, TILEHEIGHT))

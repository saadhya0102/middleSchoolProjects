import pygame
import math
import time
import random

mainClock = pygame.time.Clock()
pygame.init()

tree = pygame.image.load("tree.png")
bush = pygame.image.load("bush.png")
pavement = pygame.image.load("pavement.png")
bush = pygame.transform.scale(bush, (50,50))
tree = pygame.transform.scale(tree, (64,124))
pavement = pygame.transform.scale(pavement, (750,750))
long_dirt = pygame.transform.scale(pavement, (50,250))


screen = pygame.display.set_mode([700,700])

# colors
black = (0,0,0)
white = (255,255,255)

# world/map variables

# you start in a village in the approximate center of the map

# 0,0 is the top corner, down is -1, up is +1, left is -1,000,000 , right is 1,000,000
# need a minimap that shows location.

current_map = "city square"
current_location = "city"

# use if statement to check what map you are in and then load the nessecary information
# use location for speeding up the game, check location before checking  map, so that the game goes faster and doesn't slow down after a while.





# other variables

classes  = ["warrior","mage",'healer','crafter','archer','architect','scholar','sage', 'rogue', 'engineer', 'tank', 'poisoner']
# sage is basically diviner/seer



# functions

def treeline(x, y, number):
    global tree
    for m in range(number):
        screen.blit(tree, (x,y))
        y += 64

def create_bush(x, y):
    global bush
    screen.blit(bush, (x,y))

def create_square(x,y, number):
    global bush
    number -= 1
    default_x = x
    default_y = y
    side = 1
    for c in range(number * 4):
        screen.blit(bush,(x,y))
        if side == 1:
            if x == default_x + (number * 50):
                side = 2
            else:
                x += 50
        if side == 2:
            if y == default_y + (number * 50):
                side = 3
            else:
                y += 50
        if side == 3:
            if x == default_x:
                side = 4
            else:
                x -= 50
        if side == 4:
            y -= 50
                
def city_square():
    screen.blit(pavement, (-20,-20))
        
    

last_time = time.time()
pos = 0

running = True
while running:
    # frame per second setting
    current_time = pygame.time.get_ticks()
    screen.fill((0,200,0))
    dt = time.time()- last_time
    last_time = time.time()
    dt*=60
    pos = 0
    pos += 3 * int(dt)
    # exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
    # Main Code starts here

    if current_location == "city":
        if current_map == "city square":
            city_square()
        if current_map == "city park center":
            pass
            # add respawn point
            
    

    # ending code    
    pygame.display.update()    
    mainClock.tick(60)
pygame.quit()


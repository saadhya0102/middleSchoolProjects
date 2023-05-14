import pygame
import math
import time
import random

mainClock = pygame.time.Clock()
pygame.init()

# closed? large map with several areas, classes like ritualist and enhancer with bonuses like new abilities. Each class you use will give you certain abilities.
#For example, the juggernaut will increase defense passively and even more if equipped. You can see armor and weapons that are equipped. You can learn from trainers and the library
# Unique characters with specific attitudes towards others. They will pick from a list of phrases to say based on friendship level and stuff. 
# Enemy monsters that drop loot, teleportation system, simlilar movement to prodigy. Several tool/weapon slots that grant abilities. 1 ability at a time. Keybinds for now, but menu screen later on.
# reccomendation book for reading the terms and conditions that tells you the best stuff to do. Massive events like wars/bosses and traavelers occasionaly, but with a storyline(generator).
# Time goes on, with farming occuring. Shop where loot can be sold or bought, but you can also craft it yourself. Class evolution. Example: Crafter => Speed crafter or high crafter, then add magic 
# Crafting is a big but unnessecasy part of the game. You get materials from loot and shop and places like that. Combine them with a blueprint that you can get from the same sources, and you will craft a weapon.
# Friendship level, level, each class level, skill level. Are the multiple types of levels, all in a different way.
#Stats are constitution, Stamina, agility, mana, mana regen. ,charisma,  intelligence, and luck. You can increase them by using the effects or trainign for 2 minutes in various places.
# Skills are like reading, drawing, fireball, lightning, swordsmanship, dagger proficiency, farming, ... 
# YOu slowly unlock more of the map as you become stronger. Data is saved using sockets- take a tutorial.
# ONline auto save
# hardannor is the name of the city 



tree = pygame.image.load("tree.png")
bush = pygame.image.load("bush.png")
pavement_square = pygame.image.load("pavement.png")# full square
pavement = pygame.image.load("floor.png")# small square
bush = pygame.transform.scale(bush, (50,50))
tree = pygame.transform.scale(tree, (64,124))
pavement_square = pygame.transform.scale(pavement_square, (750,750))
pavement = pygame.transform.scale(pavement, (50,50))

screen = pygame.display.set_mode([700,700])

# colors
black = (0,0,0)
white = (255,255,255)

# world/map variables

# you start in a village in the approximate center of the map

# 0,0 is the top corner, down is -1, up is +1, left is -1,000,000 , right is 1,000,000
# need a minimap that shows location.

current_location = "hardannor"
current_district = "park"
current_state = "exploring" # expoloring = walking, crafting,shopping, riding,fighting...

mapx = 0
mapy = 0

# use if statement to check what map you are in and then load the nessecary information
# use location for speeding up the game, check location before checking  map, so that the game goes faster and doesn't slow down after a while.





# other variables

classes  = ["warrior","mage",'healer','crafter','archer','architect','scholar','sage', 'rogue', 'engineer', 'tank', "enchanter", "blacksmith", "dasher",]#dasher will become speedster or kinetomancer
# sage is basically diviner/seer



# list of buildings: blacksmith, castle, several houses, walls, guild halls(for each guild like own or warriors or achitects... ), a park


# functions

def treeline(x, y, number):
    global tree
    global mapx
    global mapy
    for m in range(number):
        screen.blit(tree, (x,y))
        y += 64

def create_bush(x, y):
    global bush
    global mapx
    global mapy
    screen.blit(bush, (x,y))

def create_square(x,y, number):# bush square hollow
    global bush
    global mapx
    global mapy
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
    global mapx
    global mapy
    a = 0
    b = 0
    for x in range(196):
        
        screen.blit(pavement, (a*50,b*50))
        a+= 1
        
        if a == 14:
            b+= 1
            a = 0
        
    
def city_cross_2():
    global mapx
    global mapy
    a = 0
    b = 0
    for x in range(28):
        screen.blit(pavement, ((a*50) + 300, b*50))
        a += 1
        if a == 2:
            a = 0
            b += 1
    a = 0
    b = 0

    for x in range(28):
        screen.blit(pavement, ((a*50), (b*50) + 300))
        b += 1
        if b == 2:
            b = 0
            a += 1                
    
def city_cross_3():
    global mapx
    global mapy
    a = 0
    b = 0
    for x in range(42):
        screen.blit(pavement, ((a*50) + 275, b*50))
        a += 1
        if a == 3:
            a = 0
            b += 1
    a = 0
    b = 0

    for x in range(42):
        screen.blit(pavement, ((a*50), (b*50) + 275))
        b += 1
        if b == 3:
            b = 0
            a += 1  

def text(phrase,x,y, color, font_size):
    font = pygame.font.Font('freesansbold.ttf',font_size)
    blitext = font.render(phrase,True,color)
    screen.blit(blitext, (x,y))




def create_section():
    pass
    

  
    
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
    if current_state == "exploring":
        if current_location == "hardannor":
            if current_district == "park":
                pass
        if mapx > -750 and mapx < 750: 
                city_cross_2()
                create_square(0,0,6)
                create_square(100,100,2)
                create_square(-100,-100,2)
                
                create_square(400,400,6)
                create_square(500,500,2)
                
                create_square(400,0,6)
                create_square(500,100,2)
                
                create_square(0,400,6)
                create_square(100,500,2)

                            
            # add respawn point


    

    # other districts in city: inner wall, castle, housing... other locations: outer wall, 
        
            

    # ending code    
    pygame.display.update()    
    mainClock.tick(60)
pygame.quit()


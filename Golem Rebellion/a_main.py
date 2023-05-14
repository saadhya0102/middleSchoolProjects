import pygame
import random
import time
import functions
import animations
# Game Outline: Settlement building will be a part but not the main point, will be storyline based. Golems are underlings of dwarves, player is only golem with sentience, escapes,
#tries to defeat the dwarves. Abilities: Create new golems with materials you can farm, have animations for each building that produces something(eg iron mine, copper mine, farm?)
# In settlement interface, players can trade with other civilizations for resources, manage an army, advance in the campaign(against dwarves)
# Players won't control golems directly, but can hire troops and organize them.
# BATTLE CRY COMBAT SYSTEM
#List of things to do:
#1 finish trade interface: trade options, money system ----------------------------------------------------
#2 do army overview: Shows the troops availible, maximum possible troops if you use all of your materials, and your heroes. Heros will be extra strong troops that the player can control.
#3 do hero summon interface: Will start with one hero, the player can control them, various rarities, offer passive boost if active, only 5 active heroes at a time, they have permadeath.
#4 make the town hall: Center of the town, not sure what player would do in it. This will improve the things that players can buy, unlock new upgrades, etc. like clash of clans
#5 make a building menu: Player can drag and drop building onto anywhere they want, as long as the space is not occupied by any other building. clash of clans
#6 make a campaign interface: Against the dwarves, think clash of clans campaign, gain troops and supplies with each raid. clash of clans
#7 make it possible to place buildings: Drag and drop system, utilize the grid system, 62x62 empty space, 64x64 including white lines, note it is only 63x63 inside,
# so start with same coord as grid lines. 
#8 make roads that connect the buildings(AI based automatic generation, connect to town hall)
#9 create golem, with multipe options based on availible materials. EG; clay golem, stone, iron, other materials, magical, etc.
#10 make golems walk on the roads with basic ai
#11 random events that happen once in a while, in which the player has a choice to make(attacked by a third party,option to save someone, rebellion, etc.)
#12 randomly generated names, talents, special abilities, preferences, and speech bubbles(make a list of possible speech, then randomly assign a few to each generated unit or just use full dictonary
#13 player can control heroes, automatically has abilities that have a large visual aspect.
#14 cutscenes
#15 openable side bar with save, back to main menu, collection, etc.
#16 add a save feature
#17 tutorial
#18 make a seperate py file with all sprites and animations.
from pygame import mixer
mainClock = pygame.time.Clock()
pygame.init()

mixer.music.load("Adventure.wav")
mixer.music.play(-1)
screen = pygame.display.set_mode([820,694])

inventory_slot = pygame.image.load("inventory_slot.png")
grass = pygame.image.load("grass.png")
up_arrow = pygame.image.load("Up_arrow.png")
down_arrow = pygame.image.load("Down_arrow.png")
Trade_Button = pygame.image.load("Trade_Button.png")
# colors # _r is radiance, allows variable brightness of colors.
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,100,0)
blue = (0,0,255)
brown = (129,100,71)
swamp_green = (24, 138, 20)
cool_blue = (58, 134, 183)
green = (0, 255, 0)
gray = (123,123,123)
grey = (150, 150, 150)
dark_brown = (101,67,33)
gold = (212,175,55)
yellow = (255, 255, 0)
purple = (106, 13 ,173)
orange = (255, 165, 0)
electric_blue = (75, 199, 205)
# Variables
coin_count = 1938 # will be counted in base cop., will display as cop. sil and gold

mapx = 0#originally 0
mapy = 0
round_mapx = 0
round_mapy = 0
UI = "play screen"# others are trading, battle, individual workplaces, walking, menu, settings, home screen
left_change =0
right_change = 0
up_change = 0
down_change = 0
x_cord_grid = 0
y_cord_grid = 0
grid_squares = []
starting = True
x_coordinate = 0
y_coordinate = 0
x_coordinate_corner = 379
y_coordinate_corner = 380
previous_x = 0
previous_y = 0
font = pygame.font.Font('freesansbold.ttf',35)
at_door = False
door_state = "closed"
door_change = "ready" # other is "happened"
door_frame = 0
button_frame = 0
door_key_up = False
small_font = False
interface_subset = "trading"
interface_subset_subset = ["normal", 0, "name"] # when normal, do normal things, when not normal, do whatever its supposed to do. Number is the number used to find corresponding values in lists
# name is the display name of the object
goblin_list = [['basic dagger', 2, white, 5, 0, 'none', 'yes', 1],['wooden shield', 1, white, 0, 3, 'none', 'yes', 1], ['shortsword', 5, white, 8, 1, 'none', 'no', 3],
               ['dagger', 2, green, 5, 0, 'none', 'no', 2],['dagger', 2, blue, 5, 0, 'none', 'no', 5],['dagger', 2, purple, 5, 0, 'none', 'no', 10],
               ['dagger', 2, yellow, 5, 0, 'none', 'no', 20],['dagger', 2, orange, 5, 0, 'none', 'no', 50],['dagger', 2, white, 5, 0, 'none', 'no', 1],
               ['dagger', 2, white, 5, 0, 'none', 'no', 1],['dagger', 2, white, 5, 0, 'none', 'mo', 1]]
# these lists have the lists of objects that they sell [name, cost, rarity, atk stat, def stat, effect, buyability, point cost effect if they have one, buyability]
elf_list = [['dagger', 2, white, 5, 0, 'none', 'yes', 1], ['shield', 1, white, 0, 3, 'none', 'yes', 1]]
C_list = []
specie_trade_list = [goblin_list, elf_list, C_list]
sby = 0
current_mby = 0
previous_mby = 0
sby_state = "not scrolling" # other is scrolling, duh
sbd = 0
trading_count = 0 # total available trading options, list in scollable area
trading_list = [] # every trade available and info on it
trading_ratio = 1 # 1 pixel moved in the scroll bar is equal to how many in the scrollable area
tby = 0
buying = "not ready "
# FUnctions

def create_grass():
    global x_cord_grid
    global y_cord_grid
    global mapx
    global mapy
    global x_coordinate
    global y_coordinate
    default_x = x_cord_grid
    default_y = y_cord_grid

    pass

def create_grid():# creates and moves the grid so that you will always see the grid
    global x_cord_grid
    global y_cord_grid
    global mapx
    global mapy
    global x_coordinate
    global y_coordinate
    default_x = x_cord_grid
    default_y = y_cord_grid

    top_x = x_cord_grid
    top_y = y_cord_grid
    # Creates the grid
    for a in range(21):
        pygame.draw.line(screen, white, (x_cord_grid+mapx,top_y+mapy), (x_cord_grid+mapx,top_y+1260+mapy))
        pygame.draw.line(screen, white, (top_x+mapx, y_cord_grid+mapy),(top_x+mapx+1260,y_cord_grid+mapy))
        x_cord_grid += 63
        y_cord_grid += 63

    x_cord_grid = default_x
    y_cord_grid = default_y
    
    # moves the grid
    if (0-mapx) < 63 + x_cord_grid:
        x_cord_grid -= 63
    if (0-mapx) > 63 + x_cord_grid:
        x_cord_grid += 63
    if (0-mapy) < 63 + y_cord_grid:
        y_cord_grid -= 63
    if (0-mapy) > 63 + y_cord_grid:
        y_cord_grid += 63

# pygame.draw.rect(screen, black, (mapx-189, mapy-189, (63 * (5)), (63 * (5))))




def scroll_bar_function():
    global sby
    global scroll_bar_button
    global current_mby
    global previous_mby
    global sby_state
    global sbd
    global trading_count
    global trading_list
    global trading_ratio
    
    pos = pygame.mouse.get_pos()

    if scroll_bar_button.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
        sby_state = "scrolling"
        sbd = pos[1] - (sby + 171)
    elif event.type == pygame.MOUSEBUTTONUP and sby_state == "scrolling":
        sby_state = "not scrolling"

    if sby_state == "scrolling":
        sby = pos[1] - 171 - sbd
    if sby > 282:
        sby = 282    
    if sby < 0:
        sby = 0

    

def add_trade( specie, rarity, cost):# material is the good, cost is the well cost, city is the place it came from, time is how many days for it to arrive.
    global trading_list
    info = [specie, rarity, cost]
    trading_list.append(info)

   
def blit_trade_info(number):
    global tby
    global trading_list
    specie = trading_list[number][0]
    rarity = trading_list[number][1]
    cost = trading_list[number][2]
    
    font = pygame.font.Font('freesansbold.ttf',35)
    name_text = font.render(specie ,True, white)
    
    #font = pygame.font.Font('freesansbold.ttf',20)
    #product_text = font.render("product:" + rarity ,True, black)
    
    font = pygame.font.Font('freesansbold.ttf',20)
    cost_text = font.render("cost:" + str(cost) ,True, white)
    



    screen.blit(name_text,(80,170 + 80*number - tby))
    screen.blit(cost_text,(600,190 + 80*number - tby))

    # functions.

def create_buildings():# make a list with all values, number will determine which building it is.
    pass

        # does something if button is clicked
# rarity is: white, green, blue, purple, yellow, orange, 
add_trade("goblin", white, 1)# example, remove later
add_trade("elf", green, 2)# example, remove later
add_trade("...", blue, 3)# example, remove later
add_trade("D", purple, 4)# example, remove later
add_trade("E", yellow, 5)# example, remove later
add_trade("F", orange, 6)# example, remove later
add_trade("F", orange, 6)# example, remove later
add_trade("F", orange, 6)# example, remove later
add_trade("F", orange, 6)# example, remove later

last_time = time.time()
pos = 0

running = True
while running:


    # frame per second setting
    current_time = pygame.time.get_ticks()
    dt = time.time()- last_time
    last_time = time.time()
    dt*=30
    pos = 0
    pos += 3 * int(dt)
    
    # exits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Main Code

    if UI == "play screen":
        screen.fill((swamp_green))

        # blitting the buttons
        play_button = pygame.draw.rect(screen, brown, (200, 322, 420, 50), border_radius = 12)
        how_to_play_button = pygame.draw.rect(screen, brown, (200, 392, 420, 50), border_radius = 12)
        Achievements_button = pygame.draw.rect(screen, brown, (200, 462, 420, 50), border_radius = 12)
        pygame.draw.rect(screen, brown, (200, 532, 420, 50), border_radius = 12)

        font = pygame.font.Font('freesansbold.ttf',80)
        text1 = font.render("GOLEM REBELLION" ,True, black)
        
        font = pygame.font.Font('freesansbold.ttf',35)
        
        text2 = font.render("Play" ,True, black)
        text3 = font.render("How to Play" ,True, black)
        text4 = font.render("Achievements" ,True, black)
        text5 = font.render("Extra Button what should this be?" ,True, black)

        screen.blit(text1, (10,35))
        screen.blit(text2, (375,327))
        screen.blit(text3, (310,397))
        screen.blit(text4, (300,467))
        screen.blit(text5, (200,537))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 if play_button.collidepoint(mouse_pos):
                     UI = "building"
                 if how_to_play_button.collidepoint(mouse_pos):
                     UI = "how to play"
                 if Achievements_button.collidepoint(mouse_pos):
                     UI = "Achievements"

    if UI == "building" or UI == "walking":
        screen.fill((swamp_green))
        #create_grid()

        # Movement
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_change = 6
            if event.key == pygame.K_RIGHT:
                right_change = 6
            if event.key == pygame.K_UP:
                down_change = 6
            if event.key == pygame.K_DOWN:
                up_change = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_change = 0
                
            if event.key == pygame.K_RIGHT:
                right_change = 0
                
            if event.key == pygame.K_UP:
                down_change = 0

            if event.key == pygame.K_DOWN:
                up_change = 0


        mapx += (left_change - right_change)
        mapy += (down_change - up_change)

        
        

        # Buildings Make a function later that will auto create them

        
        #place_holder_ = pygame.draw.rect(screen, black, (mapx-72, mapy-72, (63 * (variable)) + 1, (63 * (variable)) + 1))

        
        # UI CHANGES
        if UI == "building":
            functions.create_grid(screen, x_cord_grid, y_cord_grid,mapx, mapy, x_coordinate, y_coordinate)
            x_cord_grid = functions.function_x_cord_grid
            y_cord_grid = functions.function_y_cord_grid
        if UI == "walking":
            pass

            
        # show coordinates
        functions.show_coordinates(mapx, mapy, x_coordinate, y_coordinate, screen)
        x_coordinate = functions.x_coordinate_value
        y_coordinate = functions.y_coordinate_value
        
        # create material displays. These will show how much base materials they have: processed wood, processed stone, magic gems, several metals, and gold, clay, etc?.
        pygame.draw.rect(screen, black, (255, 0, 100, 26), border_radius = 12)
        pygame.draw.rect(screen, white, (258, 3, 94, 20), border_radius = 12)

        pygame.draw.rect(screen, black, (355, 0, 100, 26), border_radius = 12)
        pygame.draw.rect(screen, white, (358, 3, 94, 20), border_radius = 12)
        
        pygame.draw.rect(screen, black, (455, 0, 100, 26), border_radius = 12)
        pygame.draw.rect(screen, white, (458, 3, 94, 20), border_radius = 12)
    
        #show inventory slots
        screen.blit(inventory_slot,(70,600))
        screen.blit(inventory_slot,(140,600))
        screen.blit(inventory_slot,(210,600))
        screen.blit(inventory_slot,(280,600))
        screen.blit(inventory_slot,(350,600))
        screen.blit(inventory_slot,(420,600))
        screen.blit(inventory_slot,(490,600))
        screen.blit(inventory_slot,(560,600))
        screen.blit(inventory_slot,(630,600))
        screen.blit(inventory_slot,(700,600))


        previous_x = mapx
        previous_y = mapy


        Settlement_interface_button = pygame.draw.rect(screen, black, (10, 10, 73, 73) , border_radius = 12)

        if event.type == pygame.MOUSEBUTTONUP:
                 mouse_pos = pygame.mouse.get_pos()
                 if Settlement_interface_button.collidepoint(mouse_pos):
                     UI = "settlement interface"



    if UI == "settlement interface":
        screen.fill((dark_brown))
        functions.create_sub_interface_buttons(screen)
        Back_button_walking = pygame.draw.rect(screen, white, (747, 635, 53, 53) , border_radius = 12)
        

        if event.type == pygame.MOUSEBUTTONUP:
                 mouse_pos = pygame.mouse.get_pos()
                 if Back_button_walking.collidepoint(mouse_pos):
                     UI = "building"
                 functions.sub_interface_buttons(screen,interface_subset)
                 current_interface_subset = interface_subset
                 interface_subset = functions.interface_subset
                 if current_interface_subset != interface_subset:
                     sby = functions.sby

        if functions.interface_change is True:
            interface_subset_subset[0] = 'normal'
            
        if interface_subset == "trading":
            
            if interface_subset_subset[0] == "goblin":
                pass

            elif interface_subset_subset[0] == "elf":
                pass

            if interface_subset_subset[0] != "normal":# IF IT IS NOT NORMAL
                pygame.draw.rect(screen, gold, (20, 100, 780, 524 ), border_radius = 12)
                pygame.draw.rect(screen, brown, (40, 140, 700, 444 ), border_radius = 12)
                sb_tb_ratio = ((len(specie_trade_list[interface_subset_subset[1]])- 5)*80)/282 - (20/282)
                trade_return_button = pygame.draw.rect(screen, black, ( 65, 634, 125, 30 ), border_radius = 12)
                mouse_pos = mouse_pos = pygame.mouse.get_pos()
                if trade_return_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
                    interface_subset_subset[0] = 'normal'
                    sby = 0
                for x in range(len(specie_trade_list[interface_subset_subset[1]])):# 0 will be goblins, 1 will be elve, etc. for int_s_s[1]
                    screen.blit(Trade_Button, (65, 160 + (x*80) - tby))
                    font = pygame.font.Font('freesansbold.ttf',35)
                    trade_cost_text = font.render(str(specie_trade_list[interface_subset_subset[1]][x][1]) ,True, gold)
                    if len(specie_trade_list[interface_subset_subset[1]][x][0]) > 9:############## THIS IS A PROGRAM TO MULTILINE THE NAME IF IT HAS MORE THAN X LETTERS
                        font = pygame.font.Font('freesansbold.ttf',20)##############
                        small_font = True
                    word_number = 1
                    if small_font is True:
                        #trade_text_new = ["", "", "", "", "", ""]
                        #small_font = False
                        #space_list = []
                        #trade_text_list = list(specie_trade_list[interface_subset_subset[1]][x][0])   
                        #for y in range( len(specie_trade_list[interface_subset_subset[1]][x][0])):
                        #    if trade_text_list[y] == ' ':
                        #        space_list.append(y)
                        #current_space_list = 0
                        #for y in range(len(specie_trade_list[interface_subset_subset[1]][x][0])):
                        #    if y < space_list[current_space_list]:
                        #        trade_text_new[y] = trade_text_new[y] + trade_text_list[y]
                        #    elif y == space_list[current_space_list] and space_list[current_space_list] != space_list[len(space_list) - 1]:
                        #        current_space_list += 1
                        #    
                        #print(trade_text_new)
                        space_letter = []
                        small_font = False 
                        trade_text_word = ["", "", "", "", "", ""] # will contain each word seperately to be blitted
                        trade_text_word_letter_count = [0, 0, 0, 0, 0, 0]# will contain the number of letters in each word for spacing purposes
                        trade_word_letter_list = list(specie_trade_list[interface_subset_subset[1]][x][0])
                        for i in range(len((specie_trade_list[interface_subset_subset[1]][x][0]))):
                            if trade_word_letter_list[i] != " ":
                                trade_text_word[word_number -1] = trade_text_word[word_number - 1] + trade_word_letter_list[i]
                                trade_text_word_letter_count[word_number - 1] += 1
                            elif trade_word_letter_list[i] == " ":
                                word_number += 1
                        if trade_word_letter_list[i] == "%":
                                space_letter.append([i, word_number - 1])
                                print(space_letter)
                    if word_number == 1:
                        trade_text = font.render(specie_trade_list[interface_subset_subset[1]][x][0] ,True, specie_trade_list[interface_subset_subset[1]][x][2])
                    if word_number >= 2:
                        trade_text = font.render(trade_text_word[0] ,True, specie_trade_list[interface_subset_subset[1]][x][2])# creates two seperate words to blit above one another
                        trade_text_2 = font.render(trade_text_word[1] ,True, specie_trade_list[interface_subset_subset[1]][x][2])
                    if word_number >= 3:
                        trade_text_3 = font.render(trade_text_word[2] ,True, specie_trade_list[interface_subset_subset[1]][x][2])

                    if specie_trade_list[interface_subset_subset[1]][x][5] != 'none':
                        trade_effect_text = font.render(specie_trade_list[interface_subset_subset[1]][x][5] ,True, specie_trade_list[interface_subset_subset[1]][x][2])
                        screen.blit(trade_effect_text,(500,170+ (x*80) - tby))
                        
                    font = pygame.font.Font('freesansbold.ttf',20)
                    trade_atk_text = font.render("attack: " + str(specie_trade_list[interface_subset_subset[1]][x][3]) ,True, specie_trade_list[interface_subset_subset[1]][x][2])
                    trade_def_text = font.render("defense: " + str(specie_trade_list[interface_subset_subset[1]][x][4]) ,True, specie_trade_list[interface_subset_subset[1]][x][2])

                    # blit the stats of the weapon, change font size based on word count
                    if word_number == 1:
                        screen.blit(trade_text, (75,178+ (x*80) - tby))
                    if word_number == 2:
                        word_count_1 = trade_text_word_letter_count[0]
                        word_count_2 = trade_text_word_letter_count[1]
                        if word_count_1 > word_count_2:
                            word_count_diff = word_count_1 - word_count_2
                            screen.blit(trade_text, (90 ,170+ (x*80) - tby))
                            screen.blit(trade_text_2, (90 + 10*word_count_diff,190 + (x*80) - tby))
                        elif word_count_2 > word_count_1:
                            word_count_diff = word_count_2 - word_count_1
                            screen.blit(trade_text, (90 + 10*word_count_diff,170+ (x*80) - tby))
                            screen.blit(trade_text_2, (90,190 + (x*80) - tby))
                        else:
                            screen.blit(trade_text, (90,170+ (x*80) - tby))
                            screen.blit(trade_text_2, (90,190 + (x*80) - tby))

                        
                    screen.blit(trade_cost_text,(500,178+ (x*80) - tby))
                    screen.blit(trade_atk_text,(350,170+ (x*80) - tby))
                    screen.blit(trade_def_text,(350,195 + (x*80) - tby))

                    # buttons to buy the product
                    product_buy_button = pygame.draw.rect(screen, black, ( 550, 165 + (x*80) - tby, 50, 50 ))                    
                    mouse_pos = mouse_pos = pygame.mouse.get_pos()
                    if product_buy_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                        buying = 'ready'
                    if product_buy_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP and buying == 'ready' and specie_trade_list[interface_subset_subset[1]][x][6] == "yes":
                        coin_count -= specie_trade_list[interface_subset_subset[1]][x][1]
                        buying = 'not ready'
                pygame.draw.rect(screen, dark_brown, (40, 584, 700, 110 ), border_radius = 12)
                pygame.draw.rect(screen, gold, (40, 584, 700, 40 ))
                pygame.draw.rect(screen, black, ( 65, 634, 125, 30 ), border_radius = 12)

# [name, cost, rarity, atk stat, def stat,
#effect if they have one, buyability]
            
            if interface_subset_subset[0] == "normal":# IF IT IS NORMAL
                pygame.draw.rect(screen, gold, (20, 100, 780, 524 ), border_radius = 12)
                # requirements: various materials, time to reach settlement, cost per 1

                pygame.draw.rect(screen, brown, (40, 140, 700, 444 ), border_radius = 12)

                # trades 
                trading_box_count = 0
                for x in range(len(trading_list)):
                    
                    #pygame.draw.rect(screen, trading_list[x][1], (65, 160 + 80*trading_box_count - tby, 650, 60 ), border_radius = 12)
                    screen.blit(Trade_Button, (65, 160 + 80*trading_box_count - tby))
                    button = pygame.draw.rect(screen, gold, (65 + 260 , 180 + 80*trading_box_count - tby, 125, 30 ), border_radius = 12)
                    blit_trade_info(trading_box_count)
                    trading_box_count += 1 
                    # this adds the button on each tab to the screen, delete this when you add a trading tab sprite
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
                        sby = 0
                        interface_subset_subset[0] = [trading_list[x][0], x]
                        interface_subset_subset[1] = x
                        interface_subset_subset[2] = [trading_list[x][0], x]
                pygame.draw.rect(screen, gold, (40, 584, 700, 40 ) , border_radius = 12)
                pygame.draw.rect(screen, dark_brown, (0, 624, 740, 80 ), border_radius = 12)

                # scroll bar connection to trading, max sby is 282, divide by # of trades to get scroll bar y-cord to trade boxes y ratio
                
                # blitting trade text onto the squares
                
                pygame.draw.rect(screen, dark_brown, (0, 0, 820, 100 ), border_radius = 12)
                functions.create_sub_interface_buttons(screen)
            sb_tb_ratio = ((len(trading_list)- 5)*80)/282 - (20/282)
            #print(str(sb_tb_ratio))
            tby = int(sby * sb_tb_ratio)
                # displaying the amount of money the player has
            pygame.draw.rect(screen, dark_brown, (0, 0, 820, 100 ), border_radius = 12)
            functions.create_sub_interface_buttons(screen)
            functions.coin_display(screen, coin_count)
            pygame.draw.rect(screen, gold, (20, 100, 780, 40 ), border_radius = 12)
 
        if interface_subset == "army overview":
            pygame.draw.rect(screen, white, (20, 100, 780, 524 ), border_radius = 12)#battle cry type, create units out of unit, weapon, shield, armor. Unit's core will determine abilities.

        if interface_subset == "hero summon":
            pygame.draw.rect(screen, blue, (20, 100, 780, 524 ), border_radius = 12)
        
        if interface_subset == "building menu":
            pygame.draw.rect(screen, grey, (20, 100, 780, 524 ), border_radius = 12)
            if interface_subset == "normal":
                pass            # sub_sub_ints are resource, army, decor, hero, defense
            
        
        if interface_subset == "campaign":# note: add multiple difficulties
            pygame.draw.rect(screen, brown, (20, 100, 780, 524 ), border_radius = 12)

        if interface_subset == "collection":# scroll bar is on opposite side, that half of the screen shows the various things, while the other half has the description and stuff in another file
            # create the icons where the collection will be displayed
            pygame.draw.rect(screen, swamp_green, (20, 100, 780, 524 ), border_radius = 12)
            collection_length = 20
            sb_tb_ratio = ((collection_length - 5)*75)/282 - (20/282)
            tby = int(sby * sb_tb_ratio)
            print(str(sby))
            for x in range(collection_length):            
                 for y in range(5):
                    pygame.draw.rect(screen, grey, (35 + (y)*75, 160 - tby + (x*75), 64, 64 ), border_radius = 12)
            # 65, 160 + tby

        # scroll bar in settlement interface
        if interface_subset == "trading":
            pygame.draw.rect(screen, gray, (757, 140, 31, 444), border_radius = 12)
            pygame.draw.rect(screen, black, (757, 140, 31, 31))
            screen.blit(up_arrow,(757,140))
            pygame.draw.rect(screen, black, (757, 553, 31, 31))
            screen.blit(down_arrow,(757,553))
            scroll_bar_button = pygame.draw.rect(screen, brown, (757, sby + 171, 31, 100 ))
            scroll_bar_function()
        if interface_subset == "collection":
            pygame.draw.rect(screen, gray, (417, 140, 31, 444), border_radius = 12)
            pygame.draw.rect(screen, black, (417, 140, 31, 31))
            screen.blit(up_arrow,(417,140))
            pygame.draw.rect(screen, black, (417, 553, 31, 31))
            screen.blit(down_arrow,(417,553))
            scroll_bar_button = pygame.draw.rect(screen, brown, (417, sby + 171, 31, 100 ))
            scroll_bar_function()

    pygame.display.update()

    mainClock.tick(30)
pygame.quit()

import pygame
import math
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
dark_brown = (101,67,33)
gold = (212,175,55)
grey = (150, 150, 150)
sby = 0
interface_subset = "trading"
interface_change = True

def show_coordinates(mapx, mapy, x_coordinate, y_coordinate, screen):
    global x_coordinate_value
    global y_coordinate_value
    if (31-mapx) > 64*(x_coordinate + 1) - 1:
        x_coordinate += 1

    if (0 + mapy)-31 < 64*(y_coordinate - 1) + 1:
        y_coordinate -= 1

    if (0 - mapx)-31 < 64*(x_coordinate - 1) +1:
        x_coordinate -= 1

    if (31+mapy) > 64*(y_coordinate + 1) - 1:
        y_coordinate += 1

    x_coordinate_value = x_coordinate
    y_coordinate_value = y_coordinate
    
    pygame.draw.rect(screen, black, (580, 25, 215, 50))
    pygame.draw.rect(screen, white, (583, 28, 209, 44))
    if x_coordinate <= 99 or y_coordinate <= 99:
        font = pygame.font.Font('freesansbold.ttf',40)
    else:
        font = pygame.font.Font('freesansbold.ttf',35)
    text = font.render("X:" + str(x_coordinate) + "," + "Y:" + str(y_coordinate) ,True, black)
    text_rect = text.get_rect(center=(687, 52))
    screen.blit(text, text_rect)
    
def create_sub_interface_buttons(screen):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    button1 = pygame.draw.rect(screen, gold, (20, 60, 123, 30 ), border_radius = 12)   
    button2 = pygame.draw.rect(screen, white, (151, 60, 123, 30 ), border_radius = 12)
    button3 = pygame.draw.rect(screen, blue, (282, 60, 123, 30 ), border_radius = 12)
    button4 = pygame.draw.rect(screen, grey, (413, 60, 123, 30 ), border_radius = 12)
    button5 = pygame.draw.rect(screen, brown, (544, 60, 123, 30 ), border_radius = 12)
    button6 = pygame.draw.rect(screen, swamp_green, (675, 60, 123, 30 ), border_radius = 12)

def sub_interface_buttons(screen,current_interface_subset):
    global sby
    global interface_change
    global interface_subset
    interface_change = False

    mouse_pos = pygame.mouse.get_pos()
    if button1.collidepoint(mouse_pos):
        interface_subset = "trading"
        sby = 0
        interface_change = True
    if button2.collidepoint(mouse_pos):
        interface_subset = "army overview"
        sby = 0
        interface_change = True

    if button3.collidepoint(mouse_pos):
        interface_subset = "hero summon"
        sby = 0
        interface_change = True

    if button4.collidepoint(mouse_pos):
        interface_subset = "building menu"
        sby = 0
        interface_change = True

    if button5.collidepoint(mouse_pos):
        interface_subset = "campaign"
        sby = 0
        interface_change = True

    if button6.collidepoint(mouse_pos):
        interface_subset = "collection"
        sby = 0
        interface_change = True
def coin_display(screen, coin_count):
    c = 0
    s = 0
    g = 0
    g = math.floor(coin_count/100)
    s = math.floor( (coin_count - 100*g)/10)
    c = math.floor(coin_count - (100*g) - (10*s) )
    font = pygame.font.Font('freesansbold.ttf',35)
    coin_text = font.render("gold:" + str(g) + "  silver:" + str(s) + " copper:" + str(c) ,True, gold)
    screen.blit(coin_text,(350,20))

def create_grid(screen, x_cord_grid, y_cord_grid,mapx, mapy, x_coordinate, y_coordinate):
    global function_x_cord_grid
    global function_y_cord_grid

    default_x = x_cord_grid
    default_y = y_cord_grid

    top_x = x_cord_grid
    top_y = y_cord_grid
    # Creates the grid
    for a in range(21):
        pygame.draw.line(screen, white, (x_cord_grid+mapx,top_y+mapy - 64), (x_cord_grid+mapx,top_y+1280+mapy - 64))
        pygame.draw.line(screen, white, (top_x+mapx, y_cord_grid+mapy - 64),(top_x+mapx+1280,y_cord_grid+mapy - 64))
        x_cord_grid += 64
        y_cord_grid += 64

    x_cord_grid = default_x
    y_cord_grid = default_y
    
    # moves the grid
    if (0-mapx) < 64 + x_cord_grid:
        x_cord_grid -= 64
    if (0-mapx) > 64 + x_cord_grid:
        x_cord_grid += 64
    if (0-mapy) < 64 + y_cord_grid:
        y_cord_grid -= 64
    if (0-mapy) > 6 + y_cord_grid:
        y_cord_grid += 64
    function_x_cord_grid = x_cord_grid
    function_y_cord_grid = y_cord_grid


def trade_options_buttons(screen, trade_list, tby):# make buttons that work on each of the trade options
    for x in range(len(trade_list)):
        # create button at the right spot
        pygame.draw.rect(screen, gold, (65 + 200, 180 + 80*(x) - tby, 250, 20 ), border_radius = 12)
        # checks if button is being clicked

        # does something if button is clicked

def trade_tabs():
    pass
    
    
    







    

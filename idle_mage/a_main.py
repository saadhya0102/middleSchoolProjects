import pygame
import random
import time
from pygame import mixer
mainClock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode([800,600])


mixer.music.load("Adventure.wav")
mixer.music.play(-1)
# save feature that gives player a string that they can turn in the next day to get back their progress
# music by peterfiftyfour on SoundCloud
# red = melee, yellow = gold, green = heal, blue = melee+ranged, orange = ranged, white enhance, black necromancer, violet = defense, indigo = strong but slow ranged.
black = (0,0,0)
white = (255,255,255)
yellow_tan = (240,210,140)
lava = (244,114,9)
dark_brown = (101,67,33)
red = (255,0,0)
orange = (255,150,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
indigo = (200,130,200)
violet = (100, 50, 145)
gold = (212,175,55)
menu_fireball_x = 210
test = 0
rat_row = 7
health_buff_percent = 1
attack_buff_percent = 1
health_percent = 100
e_health_percent = 100
e_current_health = 15# change for emeny health current
e_current_damage = 5
e_total_health = 15
current_health = 10
current_damage = 100
q = False
enemy_state = "alive"
ow =pygame.image.load("o_w.png")
ow =  pygame.transform.scale(ow ,(150,150))
bw =pygame.image.load("b_w.png")
bw =  pygame.transform.scale(bw ,(250,150))
rw = pygame.image.load("r_w.png")
vwa = pygame.image.load("v_w_1.png")
vwb = pygame.image.load("v_w_2.png")
vwc = pygame.image.load("v_w_3.png")
iw = pygame.image.load("i_w.png")
weapon_list = []


shield = pygame.image.load("shield.png")
sword_img = pygame.image.load("sword.png")

rat = pygame.image.load("rat.png")
c_rat = pygame.image.load("crouch_rat.png")

brat = pygame.transform.scale(rat, (100,100))
bcrat = pygame.transform.scale(c_rat, (100,100))
drat = pygame.image.load("drat.png")
drat = pygame.transform.scale(drat, (100,100))
boss = pygame.image.load("boss_rat.png")
boss = pygame.transform.scale(boss, (100,100))

coin = pygame.image.load("coin.png")

fireball = pygame.image.load("fireball2.png")

r_wizard = pygame.image.load("red_wizard.png")
big_r = pygame.transform.scale(r_wizard, (500,500))

o_wizard = pygame.image.load("orange_wizard.png")
big_o = pygame.transform.scale(o_wizard, (500,500))

y_wizard = pygame.image.load("yellow_wizard.png")
big_y = pygame.transform.scale(y_wizard, (500,500))

g_wizard = pygame.image.load("green_wizard.png")
big_g = pygame.transform.scale(g_wizard, (500,500))

bu_wizard = pygame.image.load("blue_wizard.png")
big_bu = pygame.transform.scale(bu_wizard, (500,500))

v_wizard = pygame.image.load("violet_wizard.png")
big_v = pygame.transform.scale(v_wizard, (500,500))

i_wizard = pygame.image.load("indigo_wizard.png")
big_i = pygame.transform.scale(i_wizard, (500,500))

w_wizard = pygame.image.load("white_wizard.png")
big_w = pygame.transform.scale(w_wizard, (500,500))

ba_wizard = pygame.image.load("black_wizard.png")
big_ba = pygame.transform.scale(ba_wizard, (500,500))
r=[r_wizard,big_r,0,1,20,5, red, 5, (1/8), 10, 10]
o=[o_wizard,big_o,0,1,5,15, orange, 5, (1.5), 10, 5]
y=[y_wizard,big_y,0,1, 5, "pass", yellow, 5, 5, 1, 5]
g=[g_wizard,big_g,0,1, 5, "pass", green, 5, 5, 1, 5]
bu=[bu_wizard,big_bu,0,1,10,10, blue, 5, 1, 10, 5]
v=[v_wizard,big_v,0,1, 1, 15, violet, 5, 25, 5, 2]
i=[i_wizard,big_i,0,1, 1, 50, indigo, 5, 50, 5, 1]
w =[w_wizard,big_w,0,1,10,10, white, 5, 1, 1, 1]
ba=[ba_wizard,big_ba,0,1,1, 1, black, 500, 1, 2, 1]
# last value is the maximum level pic[9], last last value is maximum 


l_r = pygame.transform.scale(r_wizard, (100,100))
l_o = pygame.transform.scale(o_wizard, (100,100))
l_y = pygame.transform.scale(y_wizard, (100,100))
l_g = pygame.transform.scale(g_wizard, (100,100))
l_bu = pygame.transform.scale(bu_wizard, (100,100))
l_i = pygame.transform.scale(i_wizard, (100,100))
l_v = pygame.transform.scale(v_wizard, (100,100))
l_w = pygame.transform.scale(w_wizard, (100,100))
l_ba = pygame.transform.scale(ba_wizard, (100,100))


unit_number = 0
coin_count = 500000
coin_unit_place = 1
coin_count_x = 725
stage = "menu"
part = "overview"
sword_y = 55
level = 1
frame_number = 0
attack_timer = 0
monsters_killed = 0
player_state = "alive"
font = pygame.font.Font('freesansbold.ttf',64)

title = font.render("Idle Adventure",True,lava)
play_text = font.render("Play",True,black)
credit_text = font.render("Credits",True,black)
how_to_play_text = font.render("How to Play",True,black)
collection_text = font.render("Collection",True,black)
font = pygame.font.Font('freesansbold.ttf',40)
coin_text = font.render(str(coin_count),True,yellow)

hire_text = font.render("Hire", True, black)
level_button_text = font.render("Level Up", True, black)

level_text = font.render("Level:" + str(level),True,blue)

font = pygame.font.Font('freesansbold.ttf',30)

credit_developer = font.render("Developer: Wattled Rocket ",True,blue)

credit_pixel_art = font.render("Pixel Art: Wattled Rocket; inspired by",True,blue)
credit_pixel_art_two = font.render("Vimlark's wizard from the Ultimate Game Jam",True,blue)

credit_music = font.render("Music:",True,blue)
font = pygame.font.Font('freesansbold.ttf',40)

monster_count = font.render(str(monsters_killed) + "/10" ,True, black)
owx = 340
bwx =400
rwx = 460
vwcx = 280
iwx = 220

def wizard_attack():
    #425, 250
    global enemy_state
    global r
    global b
    global o
    global v
    global i
    global rwx
    global bwx
    global owx
    global vwcx
    global iwx
    if enemy_state == "alive":

        if r[2] > 0:
            screen.blit(rw, (rwx, 280))
            rwx += 1
        if o[2] > 0:
            screen.blit(ow, (owx, 280))
            owx += 3

        if bu[2] > 0:
            screen.blit(bw, (bwx, 280))
        if v[2] > 0:
            screen.blit(vwb, (500, 260))
        if i[2] > 0:
            screen.blit(iw, (iwx, 235))
            iwx += 5
    
def hire_cost_func(cost):
    font = pygame.font.Font('freesansbold.ttf',40)

    thecostofhiring = font.render("Cost:" + str(cost), True, black)
    screen.blit(thecostofhiring, (530,305))
                               
last_time = time.time()
pos = 0
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

    attack_timer += 1
    dt = time.time()- last_time
    last_time = time.time()
    if part == "overview":
        dt*=60
        pos = 0
        pos += 3 * int(dt)
    else:
        dt*=20
        pos = 0
        pos += 3 * int(dt)        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    
    if stage == "menu":
        screen.fill(yellow_tan)
        for x in range(10):
            screen.blit(ba_wizard, (-10,200 + (x * 25)))
            screen.blit(w_wizard, (15,200 + (x * 25)))
            screen.blit(y_wizard, (40,200 + (x * 25)))
            screen.blit(g_wizard, (65,200 + (x * 25)))
            screen.blit(i_wizard, (90,200 + (x * 25)))
            screen.blit(v_wizard, (115,200 + (x * 25)))
            screen.blit(o_wizard, (140,200 + (x * 25)))
            screen.blit(bu_wizard, (165,200 + (x * 25)))
            screen.blit(r_wizard, (190,200 + (x * 25)))
            if rat_row >= 7:
                screen.blit(rat, (575,200 + (x * 25)))
            if rat_row >= 6:
                screen.blit(rat, (605,200 + (x * 25)))
            if rat_row >= 5:
                screen.blit(rat, (635,200 + (x * 25)))
            if rat_row >= 4:
                screen.blit(rat, (665,200 + (x * 25)))
            if rat_row >= 3:
                screen.blit(rat, (695,200 + (x * 25)))
            if rat_row >= 2:
                screen.blit(rat, (725,200 + (x * 25)))
            if rat_row >= 1:
                screen.blit(rat, (755,200 + (x * 25)))
        for x in range(10):
            if rat_row > 0:
                screen.blit(fireball, (int(menu_fireball_x), 210 + (25 * x)))    
        frame_number += 1
        if frame_number >= 45:
            frame_number = 0
            if rat_row < 0:
                rat_row -= 1
        if rat_row <= -2:
            rat_row = 7



        play_button = pygame.draw.rect(screen, lava, (250, 200, 300, 64))
        credits_button = pygame.draw.rect(screen, lava, (250, 300, 300, 64))
        collection_button = pygame.draw.rect(screen, lava, (225, 400, 350, 64))
        how_to_play_button = pygame.draw.rect(screen, lava, (215, 500, 370, 64))

        screen.blit(title, (162,50))
        screen.blit(play_text, (332,197))
        screen.blit(credit_text, (288,297))
        screen.blit(how_to_play_text, (215,497))
        screen.blit(collection_text, (236,400))
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                stage = "play"
            if credits_button.collidepoint(mouse_pos):
                stage = "credits"
            if collection_button.collidepoint(mouse_pos):
                stage = "collection"
            if how_to_play_button.collidepoint(mouse_pos):
                stage = "how to play"

    if stage == "play":
        screen.fill(dark_brown)
        

        font = pygame.font.Font('freesansbold.ttf',40)
        coin_text = font.render(str(coin_count),True,yellow)
        screen.blit(coin, (750,10))
        if coin_count >= 10*coin_unit_place:
            coin_unit_place *= 10
            unit_number += 1
        coin_count_x = 725 - (unit_number*25)

        screen.blit(coin_text, (coin_count_x,10))
        if coin_unit_place > coin_count and coin_count != 0:
            coin_unit_place /= 10
            unit_number  -= 1
        pygame.draw.rect(screen, gold, (20, 50, 35, 500))
        pygame.draw.rect(screen, gold, (80, 50, 695, 500))

        overview_button = pygame.draw.rect(screen, white, (25, 55, 25, 40))
        screen.blit(shield, (25, 55))
        red_wizard_button = pygame.draw.rect(screen, red, (25, 105, 25, 40))
        orange_wizard_button = pygame.draw.rect(screen, orange, (25, 155,25, 40))
        yellow_wizard_button = pygame.draw.rect(screen, yellow, (25, 205, 25, 40))
        green_wizard_button = pygame.draw.rect(screen, green, (25, 255, 25, 40))
        blue_wizard_button = pygame.draw.rect(screen, blue, (25, 305, 25, 40))
        violet_wizard_button = pygame.draw.rect(screen, violet, (25, 355, 25, 40))
        indigo_wizard_button = pygame.draw.rect(screen, indigo, (25, 405, 25, 40))
        white_wizard_button = pygame.draw.rect(screen, white, (25, 455, 25, 40))
        black_wizard_button = pygame.draw.rect(screen, black, (25, 505, 25, 40))
        screen.blit(sword_img, (22,sword_y))
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if overview_button.collidepoint(mouse_pos):
                part = "overview"
                sword_y = 55
                
            elif red_wizard_button.collidepoint(mouse_pos):
                part = "red"
                sword_y = 105
                pic = r
                
            elif orange_wizard_button.collidepoint(mouse_pos):
                part = "orange"
                sword_y = 155
                pic = o

            elif yellow_wizard_button.collidepoint(mouse_pos):
                part = "yellow"
                sword_y = 205
                pic = y

            elif green_wizard_button.collidepoint(mouse_pos):
                part = "green"
                sword_y = 255
                pic = g

            elif blue_wizard_button.collidepoint(mouse_pos):
                part = "blue"
                sword_y = 305
                pic = bu

            elif violet_wizard_button.collidepoint(mouse_pos):
                part = "violet"
                sword_y = 355
                pic = v

            elif indigo_wizard_button.collidepoint(mouse_pos):
                part = "indigo"
                sword_y = 405
                pic = i

            elif white_wizard_button.collidepoint(mouse_pos):
                part = "white"
                sword_y = 455
                pic = w

            elif black_wizard_button.collidepoint(mouse_pos):
                part = "black"
                sword_y = 505
                pic = ba




                
        if part !="overview":
            screen.blit(pic[1], (0,50))
            font = pygame.font.Font('freesansbold.ttf',20)

            wizard_number_text = font.render("Number:" + str(pic[2]),True, black)
            wizard_level_current = font.render("Level:" + str(pic[3]),True,black)
            font = pygame.font.Font('freesansbold.ttf',40)
            

            if part == "black":
                hire_text = font.render("Hire", True, white)
                level_button_text = font.render("Level Up", True, white)
                level_cost_text = font.render("Cost:" + str(pic[7]), True, white)
                level_cost = font.render("Cost:" + str(round(pic[7])), True, white)
                hire_cost = font.render("Cost:" + str(round(pic[7])), True, white)

            else:
                hire_text = font.render("Hire", True, black)
                level_button_text = font.render("Level Up", True, black)
                level_cost_text = font.render("Cost:" + str(pic[7]), True, black)
                level_cost = font.render("Cost:" + str(round(pic[7])), True, black)
     
            
            level_cost = font.render("Cost:" + str(round(pic[7])), True, black)
            screen.blit(wizard_level_current, (170,420))
            screen.blit(wizard_number_text, (170,400))
            statone_button = pygame.draw.rect(screen, pic[6], ( 450,450, 300,50))
            hire_button = pygame.draw.rect(screen, pic[6], ( 450,350, 300,50))
            screen.blit(hire_text, (560,360))
            screen.blit(level_button_text, (520,458))
           
            mouse_pos = pygame.mouse.get_pos()

            
            
            screen.blit(level_cost_text, ( 525,500))
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if statone_button.collidepoint(mouse_pos) and pic[7] < coin_count and pic[9] > pic[3]:
                            pic[3] += 1
                            pic[4] += pic[4] * 1/10
                            coin_count -= pic[7]
                            pic[7] +=  round(pic[7] * 1/5)
                            if part != "yellow" and part != "green" and part != "black":
                                pic[5] = pic[4] * pic[8]
                            
                    if hire_button.collidepoint(mouse_pos) and pic[10] > pic[2]:
                        if part == "red":
                            coin_count -= 5
                            hire_cost_func(5)
                        if part == "orange":
                            coin_count -= 10
                            hire_cost_func(10)
                        if part == "yellow":
                            coin_count -= 15
                            hire_cost_func(15)
                        if part == "green":
                            coin_count -= 20
                            hire_cost_func(20)
                        if part == "blue":
                            coin_count -= 25
                            hire_cost_func(25)
                        if part == "violet":
                            coin_count -= 50
                            hire_cost_func(50)
                        if part == "indigo":
                            coin_count -= 100
                            hire_cost_func(100)
                        if part == "white":
                            coin_count -= 150
                            hire_cost_func(150)
                        if part == "black":
                            coin_count -= 1000
                            hire_cost_func(1000)
                        pic[2] += 1
                    current_health = total_health
                    e_current_health = e_total_health
            if part == "red" and coin_count >= 5:
                hire_cost_func(5)
            if part == "orange" and coin_count >= 10:
                hire_cost_func(10)
            if part == "yellow" and coin_count >= 15:
                hire_cost_func(15)
            if part == "green" and coin_count >= 20:
                hire_cost_func(20)
            if part == "blue" and coin_count >= 25:
                hire_cost_func(25)
            if part == "violet" and coin_count >= 50:
                hire_cost_func(50)
            if part == "indigo"and coin_count >= 100:
                hire_cost_func(100)
            if part == "white" and coin_count >= 150:
                hire_cost_func(150)
            if part == "black" and coin_count >= 1000:
                hire_cost_func(1000)
            if event.type == pygame.MOUSEBUTTONUP:
                    total_health = (r[4]*r[2]) + (o[4]*o[2]) + (bu[4]*bu[2]) + (i[4]*i[2]) + (v[4]*v[2])

                    total_damage = (r[5]*r[2]) + (o[5]*o[2]) + (bu[5]*bu[2]) + (i[5]*i[2]) + (v[5]*v[2])

            font = pygame.font.Font('freesansbold.ttf',20)

        if part == "red" or part == "orange" or part == "indigo" or part == "violet" or part == "blue":

            font = pygame.font.Font('freesansbold.ttf',20)
            wizard_hp_current = font.render("HP:" + str(round(pic[4])),True,black)
            wizard_damage_current = font.render("Damage:" + str(round(pic[5])),True,black)
            screen.blit(wizard_hp_current, (170, 440))
            screen.blit(wizard_damage_current, (170, 460))

        if part == "yellow":
            wizard_gold_per_second = font.render("Gold per second:" + str(round(pic[4], 2)), True, black)
            screen.blit(wizard_gold_per_second, (170,440))

            
        if part == "green":
            wizard_health_per_second = font.render("Healing per second:" + str(round(pic[4], 2)), True, black)
            screen.blit(wizard_health_per_second, (170,440))

            
        if part == "white":
            health_buff = font.render("Health Buff Percent:" + str(round(pic[4], 2)) + "%", True, black)
            attack_buff = font.render("Attack Buff Percent:" + str(round(pic[5], 2)) + "%", True, black)
            screen.blit(health_buff, (170,440))
            screen.blit(attack_buff, (170,460))
            
        if part == "black":
            font = pygame.font.Font('freesansbold.ttf',19)

            skeleton_power_total = font.render("Skeleton Strength:" + str(round(pic[5])) + str(" x ") + str(round(pic[4], 2)), True, black)
            screen.blit(skeleton_power_total, (170,440))

          ######################################################################################################################  
        if part == "overview":
            screen.blit(level_text, (80,5))
            if r[2] > 0:
                screen.blit(l_r, (400,250))
                q = True
            if bu[2] > 0:
                screen.blit(l_bu, (350,250))
                q = True
            if o[2] > 0:
                screen.blit(l_o, (300,250))
                q = True
            if v[2] > 0:
                screen.blit(l_v, (250,250))
                q = True
            if i[2] > 0:
                screen.blit(l_i, (200,250))
                q = True
            if g[2] > 0:
                screen.blit(l_g, (50,250))
                q = True
            if w[2] > 0:
                screen.blit(l_w, (50,480))
                q = True
            if ba[2] >  0:
                screen.blit(l_ba, (50,30))
                q = True

            if level >= 1 and level <= 9:
                if enemy_state == "alive":
                    screen.blit(brat, (500,242))
                if enemy_state == "dead":
                    screen.blit(drat, (500,242))
            if level == 10:
                screen.blit(boss, (500,242))

            # level scroll features

                

            # start battle
            if q == True:
                pygame.draw.rect(screen, black, (495,100,260,35))
                pygame.draw.rect(screen, black, (220,100,260,35))
                pygame.draw.rect(screen, gold, (225, 105, 250, 25))
                pygame.draw.rect(screen, gold, (500, 105, 250, 25))

                if enemy_state != "dead":
                    wizard_attack()


                if attack_timer >= 60:
                    if player_state == "dead":
                        e_total_health -= 2*level * level
                        e_current_health = e_total_health + total_damage
                        e_current_damage -= 2 * level
                        current_health = total_health + e_current_damage
                        monsters_killed = 0
                        level -= 1
                        player_state = "alive"
                        
                    if enemy_state == "dead":
                        enemy_state = "alive"
                        e_current_health = e_total_health + total_damage
                    if enemy_state == "alive":
                        attack_timer = 1
                        e_current_health -= total_damage * (1 + ((w[2] * w[4])/100))
                        current_health -= e_current_damage/ ((1 + ((w[2] * w[4])/100)))

                    if e_current_health <= 0:
                        enemy_state = "dead"
                        coin_count += level*level
                        current_health = total_health + e_current_damage
                        monsters_killed += 1
                    print(current_health)
                    if current_health <= 0:
                        player_state = "dead"


    
                    if y[2] > 0:
                        coin_count += y[2] * y[4]
                    if g[2] > 0:
                        current_health += g[2] * g[4]


                    rwx = 460
                    owx = 340
                    iwx = 220
                      

                    
                monster_count = font.render(str(monsters_killed) + "/10" ,True, black)
                if monsters_killed >= 10:
                    level += 1
                    e_total_health += 2*level * level 
                    e_current_health = e_total_health + total_damage
                    e_current_damage += 2 * level
                    monsters_killed = 0


                screen.blit(monster_count, (100,100))
                


                health_percent = round(100* current_health/total_health)
                e_health_percent = round(100* e_current_health/e_total_health)
                if health_percent > 100:
                    health_percent = 100
                if e_health_percent > 100:
                    e_health_percent = 100
                if health_percent > 0:
                    wizard_health_bar = pygame.draw.rect(screen, red, (225,105,round(health_percent*2.5),25))
                if e_health_percent > 0:
                    enemy_health_bar = pygame.draw.rect(screen, red, (500,105,round(e_health_percent*2.5),25))        

        


                if player_state == "dead":
                    pygame.draw.rect(screen, dark_brown, (120, 75, 615, 450))
                    font = pygame.font.Font('freesansbold.ttf',100)

                    death_text = font.render("You Died.. :(", True, black)
                    screen.blit(death_text, (135, 105))
                    


    if stage == "credits":
        screen.blit(credit_developer, (0,100))
        screen.blit(credit_pixel_art, (0,200))
        screen.blit(credit_music, (0,350))
        screen.blit(credit_pixel_art_two,(0,250))




    if rat_row >= 0:
        menu_fireball_x += 13.5 - (rat_row * 11/16)
        if  menu_fireball_x >= 770 - (rat_row * 30):
            menu_fireball_x = 210
            rat_row -= 1

    font = pygame.font.Font('freesansbold.ttf',40)
    level_text = font.render("Level:" + str(level),True,lava)
    pygame.display.update()
    if part == "overview":
        mainClock.tick(60)
    else:
        mainClock.tick(20)
    

pygame.quit()














import pygame
# have each animation be a list of sprites, cycle through them.
inventory_slot = pygame.image.load("inventory_slot.png")
grass = pygame.image.load("grass.png")
up_arrow = pygame.image.load("Up_arrow.png")
down_arrow = pygame.image.load("Down_arrow.png")
Trade_Button = pygame.image.load("Trade_Button.png")

golem_base = pygame.image.load("stone_golem_idle_1.png")
golem_idle_2 = pygame.image.load("stone_golem_idle_2.png")



golem_idle_animation = [golem_base, golem_idle_2]

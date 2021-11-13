import pygame

WIDTH, HEIGHT = 1200, 900
KÄSI = 6
SCALE = 4
VÄLI = False

#pildid
BG = pygame.image.load("img/bg.jpg")
tagus = pygame.image.load("img/tagus2.png")
TAGUS = pygame.transform.scale(tagus, (tagus.get_width()/SCALE, tagus.get_height()/SCALE))
LAIUS = TAGUS.get_width()
KÕRGUS = TAGUS.get_height()

POSX, POSY = WIDTH-(WIDTH-(650+LAIUS))/2 - LAIUS, 450 - KÕRGUS/2
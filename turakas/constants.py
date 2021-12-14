import pygame

WIDTH, HEIGHT = 1500, 900
KÄSI = 6
SCALE = 4
KÄIK = False
TAPMINE = False


#pildid
BG = pygame.image.load("img/bg.jpg")
tagus = pygame.image.load("img/tagus2.png")
TAGUS = pygame.transform.scale(tagus, (tagus.get_width()/SCALE, tagus.get_height()/SCALE))
LAIUS = TAGUS.get_width()
KÕRGUS = TAGUS.get_height()

POSX, POSY = WIDTH-(WIDTH-(650+LAIUS))/2, 450 - KÕRGUS/2

KOHAD = [(POSX-i*(LAIUS+50), POSY) for i in range(KÄSI)]
TAPMISKOHAD = [(el[0]+LAIUS/4, el[1]) for el in KOHAD]
KOHAD1 = [[(100 + i*80, 50) for i in range(30)]]
KOHAD2 = [[(100 + i*80, 850-KÕRGUS) for i in range(30)]]
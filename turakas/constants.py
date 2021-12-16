import pygame
pygame.font.init()

WIDTH, HEIGHT = 1500, 900
KÄSI = 6
SCALE = 4
TAPMINE = False

#pildid
NUPP = pygame.image.load("img/nupp2.png")
BG = pygame.image.load("img/bg.jpg")
tagus = pygame.image.load("img/tagus2.png")
TAGUS = pygame.transform.scale(tagus, (tagus.get_width()/SCALE, tagus.get_height()/SCALE))
LAIUS = TAGUS.get_width()
KÕRGUS = TAGUS.get_height()

POSX, POSY = WIDTH-(WIDTH-(650+LAIUS))/2+100, 450 - KÕRGUS/2
ROBOTO = pygame.font.Font("Roboto/Roboto-Light.ttf", 30)
ROBOTOBLACK = pygame.font.Font("Roboto/Roboto-Black.ttf", 200)
TULEMUS = pygame.font.Font("Roboto/Roboto-Light.ttf", 100)
KOMMENTAAR = pygame.font.Font("Roboto/Roboto-Light.ttf", 50)
UUESTI = pygame.font.Font("Roboto/Roboto-Light.ttf", 35)
LOLL = pygame.font.Font("Roboto/Roboto-Light.ttf", 70)



KOHAD = [(POSX-i*(LAIUS+50), POSY) for i in range(KÄSI)]
TAPMISKOHAD = [(el[0]+LAIUS/4, el[1]) for el in KOHAD]
KOHAD1 = [[(100 + i*80, 50) for i in range(30)]]
KOHAD2 = [[(100 + i*80, 850-KÕRGUS) for i in range(30)]]
import pygame
import random
from .constants import WIDTH, HEIGHT, BG, KÄSI, TAGUS, KÕRGUS, LAIUS, POSX, POSY, VÄLI
from .pakk import PAKK
from .kaardipilt import Kaart

KAARDID1 = []
KAARDID2 = []
MÄNGIJA1 = [x for x in range(KÄSI)]
MÄNGIJA2 = [x for x in range(KÄSI)]
KÄIMAS2 = []
KÄIMAS1 = []
VÄLI = []
TRUMP = []

class Mäng():
    def __init__(self):
        self.mängija1_alles = KÄSI
        self.mängija2_alles = KÄSI
        self.mängija1 = []
        self.mängija2 = []
        
        
        
    
    def draw_bg(self, win):
        laius = BG.get_width()  
        kõrgus = BG.get_height()
        for x in range(WIDTH//laius +1):
            for y in range(HEIGHT//kõrgus +1):
                win.blit(BG, (x*500,y*500))
        
    def loo_käed(self):
        for i in range(KÄSI*2):
            kaart = random.choice(PAKK)
            PAKK.remove(kaart)
            if i % 2 == 0:
                KAARDID1.append(Kaart(kaart.mast, kaart.väärtus, None))
            else:
                KAARDID2.append(Kaart(kaart.mast, kaart.väärtus, None))
        temp_trump = random.choice(PAKK)
        PAKK.remove(temp_trump)
        self.trump = Kaart(temp_trump.mast, temp_trump.väärtus, None)
        TRUMP.append(self.trump)

    def draw(self, win):
        self.draw_bg(win)
        
        for i in range(len(MÄNGIJA1)):
            KAARDID1[i] = Kaart(KAARDID1[i].kaart.mast, KAARDID1[i].kaart.väärtus, (100 + i*100, 50))
            win.blit(KAARDID1[i].pilt, (100 + i*100, 50))
            #KAARDID1.append(self.mängija1[i])
        for i in range(len(MÄNGIJA2)):
            KAARDID2[i] = Kaart(KAARDID2[i].kaart.mast, KAARDID2[i].kaart.väärtus, (100 + i*100, 850-KAARDID2[i].pilt.get_height()))
            win.blit(KAARDID2[i].pilt, (100 + i*100, 850-KAARDID2[i].pilt.get_height()))
            #KAARDID2.append(self.mängija2[i])

        self.draw_trump(win)
        if len(VÄLI) == 2:
            KÄIMAS1.remove(KÄIMAS1[0])
            KÄIMAS2.remove(KÄIMAS2[0])
            VÄLI.remove(VÄLI[0])
            VÄLI.remove(VÄLI[0])

        if len(KÄIMAS2) != 0:
            win.blit(KÄIMAS2[0].pilt, (POSX, POSY))
        
        if len(KÄIMAS1) != 0:
            win.blit(KÄIMAS1[0].pilt, (POSX+LAIUS/4, POSY))
        
        

    def draw_trump(self, win):
        trumbipilt = pygame.transform.rotozoom(self.trump.pilt, -90, 1)
        win.blit(trumbipilt, (50, 450-(LAIUS/2)))
        win.blit(TAGUS, (50, 450-(KÕRGUS/2)))

    def draw_kaart(self, win, kaart):
        win.blit(kaart, (600, 400))
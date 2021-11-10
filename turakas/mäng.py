import pygame
import random
from .constants import WIDTH, HEIGHT, BG, KÄSI
from .pakk import PAKK
from .kaardipilt import Kaart

KAARDID1 = []
KAARDID2 = []

class Mäng:
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
        
    def loo_käsi(self):
        for i in range(KÄSI*2):
            kaart = random.choice(PAKK)
            PAKK.remove(kaart)
            if i % 2 == 0:
                self.mängija1.append(Kaart(kaart.mast, kaart.väärtus, None))
            else:
                self.mängija2.append(Kaart(kaart.mast, kaart.väärtus, None))
    
    def draw(self, win):
        self.draw_bg(win)
        
        for i in range(KÄSI):
            self.mängija1[i] = Kaart(self.mängija1[i].kaart.mast, self.mängija1[i].kaart.väärtus, (50 + i*100, 50))
            win.blit(self.mängija1[i].pilt, (50 + i*100, 50))
            KAARDID1.append(self.mängija1[i])
        for i in range(KÄSI):
            self.mängija2[i] = Kaart(self.mängija2[i].kaart.mast, self.mängija2[i].kaart.väärtus, (50 + i*100, 850-self.mängija2[i].pilt.get_height()))
            win.blit(self.mängija2[i].pilt, (50 + i*100, 850-self.mängija2[i].pilt.get_height()))
            KAARDID2.append(self.mängija2[i])

        

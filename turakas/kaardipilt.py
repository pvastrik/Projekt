import pygame

from .constants import SCALE
from .pakk import Pakk
    
class Kaart:
    def __init__(self,mast, väärtus, pos):
        if not mast and not väärtus:
            self.kaart = None
        else:
            self.kaart = Pakk(mast, väärtus)
            if self.kaart.väärtus in ["J", "Q", "K"]:
                temp_pilt = pygame.image.load(f"img/cards/{väärtus}{mast}2.png")
            else:
                temp_pilt = pygame.image.load(f"img/cards/{väärtus}{mast}.png")
            self.pilt = pygame.transform.scale(temp_pilt, (temp_pilt.get_width()/SCALE, temp_pilt.get_height()/SCALE))
            self.tappa = True
            self.tapetud = None
        self.pos = pos
        

    def get_rekt(self):
        return self.pilt.get_rect()
        
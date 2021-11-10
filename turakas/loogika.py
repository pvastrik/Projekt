import pygame

from .mäng import Mäng, KAARDID2, KAARDID1
from .pakk import Pakk, PAKK
from .kaardipilt import Kaart

class Loogika:
    def __init__(self, win):
        self._init()
        self.win = win
        self.mäng = Mäng()

 
    def _init(self):
        self.valitud = None
        #self.kaart = Kaardipilt(None, None, None)
        self.turn = 2
        self.valid_moves = {}


    def update(self):
        self.mäng.draw(self.win)
        pygame.display.update()
    
    def reset(self):
        self._init()

    def kas_hiir(self, pos):
        if self.turn == 2:
            for kard in KAARDID2:
                
                rect1 = kard.get_rekt()
                rect_kaart = pygame.Rect((kard.pos[0], kard.pos[1]), (rect1[2], rect1[3]))
                if rect_kaart.collidepoint(pos):
                    return kard
            return False
        else:
            for kard in KAARDID1:
                rect1 = kard.get_rekt()
                rect_kaart = pygame.Rect((kard.pos[0], kard.pos[1]), (rect1[2], rect1[3]))
                if rect_kaart.collidepoint(pos):
                    return kard
            return False


    def select(self, pos):
        # if self.valitud:
        #     result = self._käi(None)
        #     if not result:
        #         self.valitud = None
        #         self.select(pos)    

        kaart = self.kas_hiir(pos)
        
        if kaart:
            print(kaart.kaart.väärtus)
            #self._käi(kaart)

    def _käi(self, kaart):
        pass

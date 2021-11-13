import pygame
from .constants import VÄLI
from .mäng import Mäng, KAARDID2, KAARDID1, MÄNGIJA2, MÄNGIJA1, KÄIMAS2, KÄIMAS1, VÄLI, TRUMP
from .pakk import Pakk, PAKK
from .kaardipilt import Kaart

class Loogika:

    def __init__(self, win):
        self._init()
        self.win = win
        self.mäng = Mäng()
    

 
    def _init(self):
        self.valitud = None
        self.turn = 2
        self.valid_moves = {}


    def update(self):
        self.mäng.draw(self.win)
        pygame.display.update()
    
    def reset(self):
        self._init()

    def kas_hiir(self, pos):
        if self.turn == 2:
            for kard in reversed(KAARDID2):
                
                rect1 = kard.get_rekt()
                rect_kaart = pygame.Rect((kard.pos[0], kard.pos[1]), (rect1[2], rect1[3]))
                if rect_kaart.collidepoint(pos):
                    return kard
            return False
        else:
            for kard in reversed(KAARDID1):
                rect1 = kard.get_rekt()
                rect_kaart = pygame.Rect((kard.pos[0], kard.pos[1]), (rect1[2], rect1[3]))
                if rect_kaart.collidepoint(pos):
                    return kard
            return False


    def select(self, pos):
        kaart = self.kas_hiir(pos)
        y = True
        if kaart:
            y = self._käi(kaart)
            if not y:
                return False

      

    def _käi(self, kaart):
        x = True
        if self.turn == 2:
            if len(KÄIMAS1) != 0:
                x = self._tapmine(kaart)
                if not x:
                    return False
            else:
                self._pane(kaart)
                self.turn = 1
        else:
            if len(KÄIMAS2) != 0:
                x = self._tapmine(kaart)
                if not x:
                    return False
            else:
                self._pane(kaart)
                self.turn = 2

    def _pane(self, kaart):
        if self.turn == 2:
            KÄIMAS2.append(kaart)
            KAARDID2.remove(kaart)
            MÄNGIJA2.remove(MÄNGIJA2[0])
            VÄLI.append(kaart)
        else:
            KÄIMAS1.append(kaart)
            KAARDID1.remove(kaart)
            MÄNGIJA1.remove(MÄNGIJA1[0])
            VÄLI.append(kaart)

    def _tapmine(self, kaart):
        trumbimast = TRUMP[0].kaart.mast
        tapjamast = kaart.kaart.mast
        if self.turn == 2:
            maasmast = KÄIMAS1[0].kaart.mast
            if maasmast == trumbimast:
                if (tapjamast == maasmast and kaart.kaart.tugevus > KÄIMAS1[0].kaart.tugevus): 
                    self._pane(kaart)
            else: 
                if (tapjamast == maasmast and kaart.kaart.tugevus > KÄIMAS1[0].kaart.tugevus) or tapjamast == trumbimast:
                    self._pane(kaart)
                else:
                    return False

        else:
            maasmast = KÄIMAS2[0].kaart.mast
            if maasmast == trumbimast:
                if (tapjamast == maasmast and kaart.kaart.tugevus > KÄIMAS2[0].kaart.tugevus): 
                    self._pane(kaart)
            else: 
                if (tapjamast == maasmast and kaart.kaart.tugevus > KÄIMAS2[0].kaart.tugevus) or tapjamast == trumbimast:
                    self._pane(kaart)
                else:
                    return False
        self.mäng.kaardid_maha(self.turn)
    

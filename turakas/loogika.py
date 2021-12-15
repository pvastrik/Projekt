import pygame
import operator
from .mäng import Mäng, KAARDID2, KAARDID1, KÄIMAS, TAPMAS, VÄLI, VÄLIVÄÄRTUS, TRUMP, VALID, võta, lõpp, maha, KÄIK
from .constants import LAIUS, TAPMINE, TAPMISKOHAD, TAGUS, KÕRGUS, KOHAD
from .pakk import Pakk, PAKK
from .kaardipilt import Kaart
from .nupud import Nupud

Color_line = (255, 0, 0)
class Loogika:

    def __init__(self, win):
        self._init()
        self.win = win
        self.mäng = Mäng()
    

 
    def _init(self):
        self.valitud = None
        self.valid_moves = {}
        self.turn = 2


    def update(self):
        self.mäng.draw(self.win)
        pygame.display.update()
    
    def reset(self):
        self._init()
        VALID.clear()

    def vaheta_käik(self):
        if self.turn == 2:
            self.turn = 1
            KÄIK.clear()
            KÄIK.append(1)
        else:
            self.turn = 2
            KÄIK.clear()
            KÄIK.append(2)
    def kas_hiir(self, pos):

        for kard in reversed(KAARDID2):  
            rect1 = kard.get_rekt()
            rect_kaart = pygame.Rect(kard.pos, (LAIUS, KÕRGUS))
            if rect_kaart.collidepoint(pos):
                return kard

        for kard in reversed(KAARDID1):
            rect1 = kard.get_rekt()
            rect_kaart = pygame.Rect(kard.pos, (LAIUS, KÕRGUS))
            if rect_kaart.collidepoint(pos):
                return kard

        for kard in KÄIMAS:
            rect_kaart = pygame.Rect(kard.pos, (LAIUS, KÕRGUS))
            if rect_kaart.collidepoint(pos):
                return kard
        for kard in VALID:
            if not kard.kaart:
                rect_kaart = pygame.Rect(kard.pos, (LAIUS, KÕRGUS))
            else:
                rect_kaart = pygame.Rect(KOHAD[KÄIMAS.index(kard)], (LAIUS, KÕRGUS))
            if rect_kaart.collidepoint(pos):
                return kard
        
        if self.turn == 1:
            if võta.rect.collidepoint(pos):
                return 3
        elif self.turn == 2:
            if maha.rect.collidepoint(pos):
                return 1
            if lõpp.rect.collidepoint(pos):
                return 1
        rect_pakk1 = pygame.Rect((50, 450-(KÕRGUS/2)), (LAIUS, KÕRGUS/2))
        if rect_pakk1.collidepoint(pos):
            return 2
        rect_pakk2 = pygame.Rect((50, 450), (LAIUS, KÕRGUS/2))
        if rect_pakk2.collidepoint(pos):
            return 3
        rect_trump = pygame.Rect((50, 450-(LAIUS/2)), (KÕRGUS, LAIUS))
        if rect_trump.collidepoint(pos):
            return 1
        return False

    def reset_valik(self):
        VALID.clear()
        self.valitud = None

    def select(self, pos):
        self.kaart = self.kas_hiir(pos)
        if self.kaart == 2:
            if self.turn == 2:
                for kaart in VÄLI:
                    KAARDID1.append(kaart)
            else:
                for kaart in VÄLI:
                    KAARDID2.append(kaart)
            self.mäng.kaardid_maha(self.turn)
        if self.kaart == 1:
            self.mäng.kaardid_maha(self.turn)
            self.vaheta_käik()
        if not self.kaart:
            self.reset_valik()
        else:
            if self.turn == 2:
                if self.kaart in KAARDID1:  
                    
                    self.reset_valik()
                    self.valitud = self.kaart
                    self.mäng.get_validmoves(self.kaart)
                    if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS and not TAPMAS:
                        if not VALID:
                            self.vaheta_käik()
                            self._pane(self.kaart)
                            self.reset_valik()
                        else:
                            VALID.append(Kaart(None, None, KOHAD[len(KÄIMAS)]))
                    
                elif self.valitud:
                    if self.kaart in VALID:
                        if not self.kaart.kaart:
                            self.vaheta_käik()
                            self._pane(self.valitud)
                        else:
                            self._pane(self.valitud, self.kaart)
                            self.kaart.tappa = False
                    self.reset_valik()
                else:
                    if self.kaart in KAARDID2:
                        if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS or not VÄLI:
                            if not self._pane(self.kaart):
                                return False
            else:
                if self.kaart in KAARDID2:  
                    self.reset_valik()
                    self.valitud = self.kaart
                    self.mäng.get_validmoves(self.kaart)
                    if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS and not TAPMAS:
                        if not VALID:
                            self.vaheta_käik()
                            self._pane(self.kaart)
                            self.reset_valik()
                        else:
                            VALID.append(Kaart(None, None, KOHAD[len(KÄIMAS)]))
                    else:
                        self.reset_valik()
                        self.valitud = self.kaart
                        self.mäng.get_validmoves(self.kaart)
                elif self.valitud:
                    if self.kaart in VALID:
                        if not self.kaart.kaart:
                            self.vaheta_käik()
                            self._pane(self.valitud)
                        else:
                            self._pane(self.valitud, self.kaart)
                            self.kaart.tappa = False
                    self.reset_valik()
                else:
                    if self.kaart in KAARDID1:
                        if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS or not VÄLI:
                            if not self._pane(self.kaart):
                                return False
                
                    
                    
    def select2(self, pos):
        self.kaart = self.kas_hiir(pos)
        if self.kaart == 2:
            self.mäng.kaardid_maha(self.turn)
            self.vaheta_käik()
        if self.kaart == 1:
            self.arvuti_käik()
        if self.kaart == 3:

            a = 0
            if not self.arvuti_juurde():
                a+=1
            if a == 0:
                self.mäng.draw(self.win)
                pygame.display.update()
                pygame.time.wait(1500)

            for kaart in VÄLI:
                KAARDID2.append(kaart)
                kaart.tappa = True
            self.mäng.kaardid_maha(self.turn)

            self.mäng.draw(self.win)
            pygame.display.update()
            pygame.time.wait(1500)
            self.arvuti_käik()

        if not self.kaart:
            self.reset_valik()
        else:
            if self.turn == 2:
                if self.kaart in KAARDID2:
                    if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS or not VÄLI:
                        if not self._pane(self.kaart):
                            return False

            else:
                if self.kaart in KAARDID2:  
                    self.reset_valik()
                    self.valitud = self.kaart
                    self.mäng.get_validmoves(self.kaart)
                    if self.kaart.kaart.väärtus in VÄLIVÄÄRTUS and not TAPMAS:
                        if not VALID:
                            self.vaheta_käik()
                            self.reset_valik()
                            self._pane(self.kaart)
                        else:
                            VALID.append(Kaart(None, None, KOHAD[len(KÄIMAS)]))
                    else:
                        self.reset_valik()
                        self.valitud = self.kaart
                        self.mäng.get_validmoves(self.kaart)
                elif self.valitud:
                    if self.kaart in VALID:
                        if not self.kaart.kaart:
                            self.vaheta_käik()
                            self._pane(self.valitud)
                        else:
                            valitud = self.valitud
                            self.reset_valik()
                            self._pane(valitud, self.kaart)
                            self.kaart.tappa = False
    def arvuti_tapa(self):
        tappa = sum(1 for card in KÄIMAS if card.tappa)
        for i in range(tappa):
            for kaart2 in reversed(KAARDID1):
                self.mäng.get_validmoves(kaart2)
                if VALID:
                    VALID.sort(key=operator.attrgetter("kaart.tugevus"))
                    self._pane(kaart2, VALID[0])
                    self.reset_valik()
                    break
        if sum(1 for card in KÄIMAS if card.tappa) > 0:
            for kaart in TAPMAS:
                KAARDID1.append(kaart)
                TAPMAS.clear()
                VÄLIVÄÄRTUS.remove(kaart.kaart.väärtus)
            return False
        KÄIK.clear()
        KÄIK.append(3)
        return True

    def arvuti_saada(self):
        for kaart in KAARDID1:
            if kaart.kaart.väärtus in VÄLIVÄÄRTUS:
                self.vaheta_käik()
                self._pane(kaart)
                return True
        return False
    
    def arvuti_juurde(self):
        i = 0
        for kaart in KAARDID1:
            if kaart.kaart.väärtus in VÄLIVÄÄRTUS:
                if not (kaart.kaart.mast == TRUMP[0].kaart.mast and kaart.kaart.tugevus > 8):
                    self._pane(kaart)
                    i+=1
                    break
                elif len(PAKK) <= 6:
                    self._pane(kaart)
                    i+=1
                    break
        if i == 0:
            return False
        return True
    def arvuti_käik(self):
        if self.turn==2:
            if not TAPMAS:
                if not self.arvuti_tapa():
                    if not self.arvuti_saada():
                        for kaart in VÄLI:
                            KAARDID1.append(kaart)
                            kaart.tappa = True
                        self.mäng.kaardid_maha(self.turn)
            elif len(KÄIMAS) != len(TAPMAS):
                if not self.arvuti_tapa():
                    for kaart in VÄLI:
                        KAARDID1.append(kaart)
                        kaart.tappa = True
                    self.mäng.kaardid_maha(self.turn)
            else:
                self.mäng.kaardid_maha(self.turn)
                self.vaheta_käik()
                self.mäng.draw(self.win)
                pygame.display.update()
                pygame.time.wait(1500)
                self.arvuti_käik()
        else:
            self.kaardid = [x for x in KAARDID1 if x.kaart.mast != TRUMP[0].kaart.mast]
            if self.kaardid:
                kaart = min(self.kaardid, key=operator.attrgetter("kaart.tugevus"))
            else:
                kaart = min(KAARDID1, key=operator.attrgetter("kaart.tugevus"))

            if not KÄIMAS:
                self._pane(kaart)  
            elif not self.arvuti_juurde():
                if len(KÄIMAS) == len(TAPMAS):
                    self.mäng.kaardid_maha(self.turn)
                    self.vaheta_käik()

    # def selectväli(self, pos):
    #     kaart = self.kas_hiir(pos)
    #     if kaart in KÄIMAS:
    #         if not self._tapmine(self.kaart, kaart):
    #             return False
    #     else:
    #         return False
      

    # def _käi(self, kaart): 
    #     if kaart in KAARDID2:
    #         if self.turn == 2:
    #             self._pane(kaart)
    #         else:
    #             x = self._tapmine(kaart)
    #             if not x:
    #                 return False
    #     elif kaart in KAARDID1:
    #         if self.turn == 2:
    #             x = self._tapmine(kaart)
    #             if not x:
    #                 return False
    #         else:
    #             self._pane(kaart)
                

    def _pane(self, kaart, kaart2=None):
        VÄLI.append(kaart)
        VÄLIVÄÄRTUS.append(kaart.kaart.väärtus)
        if self.turn == 2:
            if not kaart2:
                KAARDID2.remove(kaart)
                kaart.pos = KOHAD[len(KÄIMAS)]
                KÄIMAS.append(kaart)
                KÄIK.clear()
                KÄIK.append(2)
            else:
                KAARDID1.remove(kaart)
                kaart.pos = TAPMISKOHAD[KÄIMAS.index(kaart2)]
                TAPMAS.append(kaart)
                kaart2.tappa = False
        else:
            if not kaart2:
                KAARDID1.remove(kaart)
                kaart.pos = KOHAD[len(KÄIMAS)]
                KÄIMAS.append(kaart)
            else:
                KAARDID2.remove(kaart)
                kaart.pos = TAPMISKOHAD[KÄIMAS.index(kaart2)]
                TAPMAS.append(kaart)
                kaart2.tappa = False

                self.mäng.draw(self.win)
                pygame.display.update()
                pygame.time.wait(1000)
                self.arvuti_käik()

        # if len(VÄLI) == 8:
        #     self.mäng.kaardid_maha(self.turn)     
        #     self.vaheta_käik()   
        # if self.turn == 2:
        #     if kaart in KAARDID2:
        #         KÄIMAS.append(kaart)
        #         kaart.pos = KOHAD[KÄIMAS.index(kaart)]
        #         KAARDID2.remove(kaart)
        #         VÄLI.append(kaart)
        #         VÄLIVÄÄRTUS.append(kaart.kaart.väärtus)
        #     elif kaart in KAARDID1:
        #         TAPMAS.append(kaart)
        #         kaart.pos = TAPMISKOHAD[KÄIMAS.index(kaart2)]
        #         KAARDID1.remove(kaart)
        #         VÄLI.append(kaart)
        #         VÄLIVÄÄRTUS.append(kaart.kaart.väärtus)
        # else:
        #     if kaart in KAARDID1:
        #         KÄIMAS.append(kaart)
        #         kaart.pos = KOHAD[KÄIMAS.index(kaart)]
        #         KAARDID1.remove(kaart)
        #         VÄLI.append(kaart)
        #         VÄLIVÄÄRTUS.append(kaart.kaart.väärtus)
        #     elif kaart in KAARDID2:
        #         TAPMAS.append(kaart)
        #         kaart.pos = TAPMISKOHAD[KÄIMAS.index(kaart2)]
        #         KAARDID2.remove(kaart)
        #         VÄLI.append(kaart)
        #         VÄLIVÄÄRTUS.append(kaart.kaart.väärtus)
        # if len(VÄLI) == 4:
        #     self.vaheta_käik()
        # self.mäng.kaardid_maha(self.turn)
        
    # def _tapmine(self, kaart, välikaart):
    #     trumbimast = TRUMP[0].kaart.mast
    #     tapjamast = kaart.kaart.mast
    #     if self.turn == 2:
    #         maasmast = välikaart.kaart.mast
    #         if maasmast == trumbimast:
    #             if (tapjamast == maasmast and kaart.kaart.tugevus > välikaart.kaart.tugevus): 
    #                 self._pane(kaart)
    #         else: 
    #             if (tapjamast == maasmast and kaart.kaart.tugevus > välikaart.kaart.tugevus) or tapjamast == trumbimast:
    #                 self._pane(kaart)
    #             else:
    #                 return False

    #     else:
    #         maasmast = välikaart.kaart.mast
    #         if maasmast == trumbimast:
    #             if (tapjamast == maasmast and kaart.kaart.tugevus > välikaart.kaart.tugevus): 
    #                 self._pane(kaart)
    #         else: 
    #             if (tapjamast == maasmast and kaart.kaart.tugevus > välikaart.kaart.tugevus) or tapjamast == trumbimast:
    #                 self._pane(kaart)
    #             else:
    #                 return False
    #     self.mäng.kaardid_maha(self.turn)
    
    
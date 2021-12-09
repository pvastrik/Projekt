import pygame
import random
import operator
from .constants import WIDTH, HEIGHT, BG, KÄSI, TAGUS, KÕRGUS, LAIUS, POSX, POSY, KOHAD, TAPMISKOHAD, KOHAD1, KOHAD2
from .pakk import PAKK, MASTID
from .kaardipilt import Kaart


KAARDID1 = []
KAARDID2 = []
KÄIMAS = []
TAPMAS = []
VÄLI = []
VÄLIVÄÄRTUS = []
TRUMP = []
VALID =[]
class Mäng():
    def __init__(self):
        self.mängija1_alles = KÄSI
        self.mängija2_alles = KÄSI
        
        
        
    
    def draw_bg(self, win):
        laius = BG.get_width()  
        kõrgus = BG.get_height()
        for x in range(WIDTH//laius +1):
            for y in range(HEIGHT//kõrgus +1):
                win.blit(BG, (x*500,y*500))
        
    def loo_käed(self):
        random.shuffle(PAKK)
        for i in range(KÄSI*2):
            kaart = PAKK[0]
            PAKK.remove(kaart)
            if i % 2 == 0:
                KAARDID1.append(Kaart(kaart.mast, kaart.väärtus, None))
            else:
                KAARDID2.append(Kaart(kaart.mast, kaart.väärtus, None))
        temp_trump = PAKK[0]
        PAKK.remove(temp_trump)
        PAKK.append(temp_trump)
        self.trump = Kaart(temp_trump.mast, temp_trump.väärtus, None)
        TRUMP.append(self.trump)
        MASTID.insert(0, MASTID.pop(MASTID.index(self.trump.kaart.mast)))

    def uus_kaart(self, mängija):
        if mängija == 1:
            while len(KAARDID1) < KÄSI and len(PAKK) != 0:
                kaart = PAKK[0]
                PAKK.remove(kaart)
                KAARDID1.append(Kaart(kaart.mast, kaart.väärtus, None))
        else:
            while len(KAARDID2) < KÄSI and len(PAKK) != 0:
                kaart = PAKK[0]
                PAKK.remove(kaart)
                KAARDID2.append(Kaart(kaart.mast, kaart.väärtus, None))
            
    def draw(self, win):
        self.draw_bg(win)
        KAARDID1.sort(key=operator.attrgetter("kaart.tugevus"), reverse=True)
        KAARDID2.sort(key=operator.attrgetter("kaart.tugevus"), reverse=True)
        KAARDID1.sort(key=lambda mast: MASTID.index(mast.kaart.mast))
        KAARDID2.sort(key=lambda mast: MASTID.index(mast.kaart.mast))
        for i, kaard in enumerate(KAARDID1):
            kaard.pos = KOHAD1[i]
        for i, kaard in enumerate(KAARDID2):
            kaard.pos = KOHAD2[i]

        for kaart in KAARDID1:
            # KAARDID1[i].pos = (100 + i*80, 50)
            # win.blit(KAARDID1[i].pilt, (100 + i*80, 50))
            win.blit(kaart.pilt, kaart.pos)

        for kaart in KAARDID2:
            # KAARDID2[i].pos = (100 + i*80, 850-KAARDID2[i].pilt.get_height())
            # win.blit(KAARDID2[i].pilt, (100 + i*80, 850-KÕRGUS))
            win.blit(kaart.pilt, kaart.pos)
        self.draw_trump(win)
        if KÄIMAS:
            for i, kaart in enumerate(KÄIMAS):
                win.blit(kaart.pilt, kaart.pos)
        
        if TAPMAS:
            for i, kaart in enumerate(TAPMAS):
                win.blit(kaart.pilt, kaart.pos)
        
        for nonii in VALID:
            if not nonii.kaart:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect((nonii.pos[0]-2, nonii.pos[1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)

            elif nonii.kaart.mast in ["Ärtu", "Ruutu"]:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect((nonii.pos[0]-2, nonii.pos[1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)
            else:
                pygame.draw.rect(win, (255, 0, 0), pygame.Rect((nonii.pos[0]-2, nonii.pos[1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)

            #pygame.draw.circle(win, (0, 255, 0, 127), (nonii.pos[0]+LAIUS/2, nonii.pos[1]+KÕRGUS/2),20)
            # pygame.draw.lines(win, (0, 0, 255), False, ((nonii.pos[0], nonii.pos[1]+20), nonii.pos, (nonii.pos[0]+20, nonii.pos[1])), 8)
    def kaardid_maha(self, käik):
        TAPMAS.clear()
        KÄIMAS.clear()
        VÄLI.clear()
        VÄLIVÄÄRTUS.clear()
        if käik == 2:
            self.uus_kaart(2)
            self.uus_kaart(1)
        else:
            self.uus_kaart(1)
            self.uus_kaart(2)

    def saab_tappa(self, kaart1, kaart2):
        trumbimast = TRUMP[0].kaart.mast
        tapjamast = kaart1.kaart.mast
        maasmast = kaart2.kaart.mast

        if maasmast == trumbimast:
            if (tapjamast == maasmast and kaart1.kaart.tugevus > kaart2.kaart.tugevus): 
                return True
        else: 
            if (tapjamast == maasmast and kaart1.kaart.tugevus > kaart2.kaart.tugevus) or tapjamast == trumbimast:
                return True
        return False

    def get_validmoves(self, kaart):
        for kard in KÄIMAS:
            if self.saab_tappa(kaart, kard) and kard.tappa:
                VALID.append(kard)
        

    def draw_trump(self, win):
        trumbipilt = pygame.transform.rotozoom(self.trump.pilt, -90, 1)
        if len(PAKK) > 0:
            win.blit(trumbipilt, (50, 450-(LAIUS/2)))
        if len(PAKK) > 1:
            win.blit(TAGUS, (50, 450-(KÕRGUS/2)))
        if not PAKK:
            trump_temp = pygame.image.load(f"img/{self.trump.kaart.mast}.png")
            trump = pygame.transform.scale(trump_temp, (LAIUS*0.674, LAIUS*0.674))
            win.blit(trump, (100, 450-0.337*LAIUS))

    def draw_kaart(self, win, kaart):
        win.blit(kaart, (600, 400))
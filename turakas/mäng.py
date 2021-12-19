import pygame
import random
import operator
from .nupud import Nupud
from .constants import WIDTH, HEIGHT, BG, KÄSI, TAGUS, KÕRGUS, LAIUS, POSX, POSY, KOHAD, TAPMISKOHAD, KOHAD1, KOHAD2, FONT, FONT2, FONTBLACK, TULEMUS, KOMMENTAAR, UUESTI, LOLL
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
KÄIK = [2]
lõpp = Nupud(1250, 875 - 3*KÕRGUS/ 4, 0.6, "KÄIN")
võta = Nupud(1250, 875-3*KÕRGUS/4, 0.6, "VÕTAN")
maha = Nupud(1250, 875-3*KÕRGUS/4, 0.6, "MAHA")
kordaja = []
LÕPP = []


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
                kaart = PAKK.pop(0)
                KAARDID1.append(Kaart(kaart.mast, kaart.väärtus, None))
        else:
            while len(KAARDID2) < KÄSI and len(PAKK) != 0:
                kaart = PAKK.pop(0)
                KAARDID2.append(Kaart(kaart.mast, kaart.väärtus, None))
            
    def draw(self, win):
        self.draw_bg(win)
        KAARDID1.sort(key=operator.attrgetter("kaart.tugevus"), reverse=True)
        KAARDID2.sort(key=operator.attrgetter("kaart.tugevus"), reverse=True)
        KAARDID1.sort(key=lambda mast: MASTID.index(mast.kaart.mast))
        KAARDID2.sort(key=lambda mast: MASTID.index(mast.kaart.mast))

        if KÄIK[0] == 2:
            lõpp.draw(win)
        elif KÄIK[0] == 3:
            maha.draw(win)
        elif KÄIK[0] == 1:
            võta.draw(win)


        self.kaartide_kohad()
        for i, kaard in enumerate(KAARDID1):
            kaard.pos = KOHAD1[0][i]
            win.blit(TAGUS, kaard.pos)

        for i, kaard in enumerate(KAARDID2):
            kaard.pos = KOHAD2[0][i]
            win.blit(kaard.pilt, kaard.pos)

        self.draw_trump(win, TRUMP[0])
        self.kaartide_arv(win)
        if KÄIMAS:
            for i, kaart in enumerate(KÄIMAS):
                win.blit(kaart.pilt, KOHAD[i])
        
        if TAPMAS:
            for i, kaart in enumerate(TAPMAS):
                win.blit(kaart.pilt, TAPMISKOHAD[KÄIMAS.index(kaart.tapetud)])
        
        for nonii in VALID:
            if not nonii.kaart:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect((nonii.pos[0]-2, nonii.pos[1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)

            elif nonii.kaart.mast in ["Ärtu", "Ruutu"]:
                pygame.draw.rect(win, (0, 0, 0), pygame.Rect((KOHAD[KÄIMAS.index(nonii)][0]-2, KOHAD[KÄIMAS.index(nonii)][1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)
            else:
                pygame.draw.rect(win, (255, 0, 0), pygame.Rect((KOHAD[KÄIMAS.index(nonii)][0]-2, KOHAD[KÄIMAS.index(nonii)][1]-2), (LAIUS+6, KÕRGUS+12)),  4, 3)

        if not PAKK and (not len(KAARDID1) or not len(KAARDID2)):
            if not kordaja:
                LÕPP.append(1)
                kordaja.append(1)
                self.draw(win)
                pygame.display.update()
                pygame.time.wait(1000)
                self.lõpp(win, kordaja)
                kordaja.append(1)
            elif len(kordaja)==1:
                return True
            elif len(kordaja)==2:
                self.lõpp(win, kordaja)

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
    
    def kaartide_kohad(self):
        if len(KAARDID1) > 10 and len(KAARDID1) < 19:
            KOHAD1.clear()
            KOHAD1.append([(100 + i*(80-(len(KAARDID1)-10)*5), 50) for i in range(30)])
        if len(KAARDID2) > 10 and len(KAARDID2) < 19:
            KOHAD2.clear()
            KOHAD2.append([(100 + i*(80-(len(KAARDID2)-10)*5), 850-KÕRGUS) for i in range(30)])

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
        
    def kaartide_arv(self, win):
        if len(PAKK) > 0:
            arv = FONT.render(str(len(PAKK)), True, (0,0,0))
            arv_rect = arv.get_rect(center=(50+LAIUS/2, 450-(KÕRGUS/2)-15))
            win.blit(arv, arv_rect)

    def draw_trump(self, win, trump):
        trumbipilt = pygame.transform.rotozoom(trump.pilt, -90, 1)
        if len(PAKK) > 0:
            win.blit(trumbipilt, (50, 450-(LAIUS/2)))
        if len(PAKK) > 1:
            win.blit(TAGUS, (50, 450-(KÕRGUS/2)))
        if not PAKK:
            trump_temp = pygame.image.load(f"img/{trump.kaart.mast}.png")
            trump = pygame.transform.scale(trump_temp, (LAIUS*0.674, LAIUS*0.674))
            win.blit(trump, (100, 450-0.337*LAIUS))
    
    def lõpp(self, win, kordaja):
        fade = pygame.Surface((WIDTH, HEIGHT))
        self.draw_bg(fade)
        durak = FONTBLACK.render("DURAK", True, (0,0,0))
        durak_rect = durak.get_rect(center=(WIDTH/2, HEIGHT/3))
        võitja = FONTBLACK.render("TUBLI TÖÖ!", True, (0,0,0))
        tulemus_rect = võitja.get_rect(center=(WIDTH/2, HEIGHT/3))
        hing = TULEMUS.render("TÕELINE VÕITJA HING!", True, (0,0,0))
        hing_rect = hing.get_rect(center=(WIDTH/2, HEIGHT/3+130))
        loll = LOLL.render("KUI LOLL SAAB OLLA!", True, (0,0,0))
        loll_rect = loll.get_rect(center=(WIDTH/2+5, HEIGHT/3+130))
        nimed = FONT2.render("Priidik Meelo Västrik ja Elise Õispuu", True, (0,0,0))
        nimed_rect = nimed.get_rect(center=(WIDTH/2, 820))
        aasta = FONT2.render("2021", True, (0,0,0))
        aasta_rect = aasta.get_rect(center=(WIDTH/2, 860))
        uuesti = UUESTI.render("Uuesti mängimiseks vajuta tühikut", True, (0,0,0))
        uuesti_rect = uuesti.get_rect(center=(WIDTH/2, 2*HEIGHT/3))
        if not LÕPP:
            fade.set_alpha(0)
        if not KAARDID2:
            fade.blit(võitja, tulemus_rect)
            fade.blit(hing, hing_rect)
            fade.blit(uuesti, uuesti_rect)
            fade.blit(aasta, aasta_rect)
            fade.blit(nimed, nimed_rect)
        elif not KAARDID1:
            fade.blit(durak, durak_rect)
            fade.blit(loll, loll_rect)
            fade.blit(uuesti, uuesti_rect)
            fade.blit(aasta, aasta_rect)
            fade.blit(nimed, nimed_rect)

        if len(kordaja)==1:
            for alpha in range(0, 300, 3):
                fade.set_alpha(alpha)
                self.draw(win)
                win.blit(fade, (0,0))
                pygame.display.update()
                pygame.time.delay(1)
            LÕPP.append(1)
        win.blit(fade, (0,0))

    def animatsioon(self, win, kaart, alg, siht):
        x = (siht[0]-alg[0])/60
        y = (siht[1]-alg[1])/60
        for i in range(60):
            self.draw(win)
            win.blit(kaart.pilt, (alg[0]+x*(i+1), alg[1]+y*(i+1)))
            pygame.display.update()
            pygame.time.wait(10)

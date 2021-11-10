import pygame
import random
import ctypes
from turakas.constants import WIDTH, HEIGHT, POSX, POSY
from turakas.pakk import PAKK
from turakas.mäng import Mäng
from turakas.loogika import Loogika

ctypes.windll.shcore.SetProcessDpiAwareness(2)

pygame.init()

# kaardipakk 52 v 36 kaarti, kaardifailid listi?
# mõlemale 6 kaarti suvaliselt (random.choice listist?) (hiljem vb kuidagi lehvikuna?) (hiljem kaardi liikumise animatsioonid?)
# pakist järgmine kaart trump 
# alustaja valiminine? kummal väiksem trump
# vajutad kaardile ja see liigub väljakule alguses ainult üks, (hiljem iga kaart oma kohale)
# algne tapmine: vajutad kaardile: kui see sobib selle kaardi peale, siis see liigub sinna
# kui ei saa tappa, siis vajutad väljakul olevale kaardile ja see tuleb sulle kätte
# advanced tapmine: vajutad kaardile, ilmuvad võimalused, kuhu seda kaarti saab käia, tuleb uuesti vajutada tapetava kaardi peale
# nupp: VÕTAN, kui ei saa midagi tappa
# käigu lõpus läheb kord järgmisele

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turakas")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

x = 50
y = 50
vel = 100

card = pygame.image.load("img/cards/KÄrtu.png")
card = pygame.transform.scale(card, (card.get_width()/4, card.get_height()/4))
laius = card.get_width()
kõrgus = card.get_height()
kaart = pygame.Rect((x, y), (card.get_width(), card.get_height()))
liigub = False
liikumine = 0
kliki_counter = 0


trump = random.choice(PAKK)
PAKK.remove(trump)
trumbipilt = pygame.transform.rotozoom(pygame.image.load(f"img/cards/{trump.väärtus}{trump.mast}.png"), -90, 0.25)
trumbirect = ((50, 450-(laius/2)), (trumbipilt.get_width(), trumbipilt.get_height()))
tagus = pygame.image.load("img/tagus2.png")
tagus = pygame.transform.scale(tagus, (laius, kõrgus))

mäng = Mäng()
mäng.loo_käsi()
loogika = Loogika(WIN)
def draw_window():
    mäng.draw(WIN)
    # for i in range(12):
    #     WIN.blit(valitudpildid[i], valitudrect[i])
    WIN.blit(trumbipilt, trumbirect)
    WIN.blit(tagus, (50, 450-kõrgus/2))
    pygame.display.update()

def main():    
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                loogika.select(pos)
    #             for i in range(12):
                    
    #                 if valitudrect[len(valitudrect)-1-i].collidepoint(pos):
    # #                     sammx = (valitudrect[i].x-(POSX-kliki_counter*(10)))/FPS
    # #                     sammx = (valitudrect[i].x-POSX)/FPS
    # #                     sammy = (valitudrect[i].y-POSY)//FPS
    # #                     liigub = True
    # #                     liikuv = valitudrect[i]
    # #                     kliki_counter += 1
    #                     valitudrect[len(valitudrect)-1-i].move_ip(-(valitudrect[len(valitudrect)-1-i].x-POSX), -(valitudrect[len(valitudrect)-1-i].y-POSY))
    #                     break

                    
        keys = pygame.key.get_pressed()

        # if liigub:
        #     if liikumine < FPS:
        #         liikuv.move_ip(-sammx, -sammy)
        #         liikumine += 1
        #     else:
        #         liigub = False
        #         liikumine = 0
    #             if kaart.x < POSX and kaart.y < POSY:
    #                 kaart.move_ip(sammx, sammy)
    #             elif kaart.x < POSX and kaart.y > POSY:
    #                 kaart.move_ip(sammx,-sammy)
    #             elif kaart.x > POSX and kaart.y < POSY:
    #                 kaart.move_ip(-sammx,sammy)
    #             elif kaart.x > POSX and kaart.y > POSY:
    #                 kaart.move_ip(-sammx,-sammy)
        if keys[pygame.K_LEFT]:
            kaart.move_ip(-vel, 0)
        if keys[pygame.K_RIGHT]:
            kaart.move_ip(vel, 0)
            
        if keys[pygame.K_UP]:
            kaart.move_ip(0, -vel)
        if keys[pygame.K_DOWN]:
            kaart.move_ip(0, vel)
        
        draw_window()
            
main()
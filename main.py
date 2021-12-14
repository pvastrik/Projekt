import pygame
import random
import ctypes

from pygame.constants import RESIZABLE
from turakas.constants import WIDTH, HEIGHT, POSX, POSY, KÄIK
from turakas.pakk import PAKK
from turakas.mäng import Mäng
from turakas.loogika import Loogika

ctypes.windll.shcore.SetProcessDpiAwareness(2)

pygame.init()

# kaardipakk 52 v 36 kaarti, kaardifailid listi?
# mõlemale 6 kaarti suvaliselt (random.choice listist?) (hiljem vb kuidagi lehvikuna?) (hiljem kaardi liikumise animatsioonid?)
# pakist järgmine kaart trump 
# alustaja valiminine? kummal väiksem trump (VEEL TEHA)
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


mäng = Mäng()
loogika = Loogika(WIN)
def draw_window():
    mäng.draw(WIN)
    
    pygame.display.update()

def main():    
    clock = pygame.time.Clock()
    mäng.loo_käed()

    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not loogika.select2(pos):
                    continue
                
                    
        keys = pygame.key.get_pressed()

        
        draw_window()
            
main()
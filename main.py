import pygame
import random
import ctypes

from turakas.constants import WIDTH, HEIGHT, POSX, POSY
from turakas.pakk import Pakk
from turakas.mäng import Mäng, LÕPP
from turakas.loogika import Loogika, PAUS

ctypes.windll.shcore.SetProcessDpiAwareness(2)

pygame.init()

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
        events = pygame.event.get()
        if PAUS:
            events.clear()
            PAUS.clear()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and not PAUS:
                pos = pygame.mouse.get_pos()
                loogika.select2(pos)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and LÕPP:
            loogika.reset()
                    

        
        draw_window()
        
if __name__ == "__main__":            
    main()
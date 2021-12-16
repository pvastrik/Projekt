import pygame
import random
import ctypes

from pygame.constants import RESIZABLE
from turakas.constants import WIDTH, HEIGHT, POSX, POSY
from turakas.pakk import Pakk
from turakas.mäng import Mäng, kordaja
from turakas.loogika import Loogika

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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not loogika.select2(pos):
                    continue
                
                    

        
        draw_window()
        
if __name__ == "__main__":            
    main()
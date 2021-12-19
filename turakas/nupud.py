import pygame
from .constants import NUPP, FONT


class Nupud():
    def __init__(self, x, y, scale, text_input):
        image = NUPP
        width = image.get_width()
        height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        self.text_input = text_input
        self.text = FONT.render(self.text_input, True, (0, 0 ,0))
        self.rect = self.image.get_rect()
        self.text_rect = self.text.get_rect(center=(self.x+(width*scale)/2, self.y+(height*scale)/2))
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action  = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text, self.text_rect)

        return action
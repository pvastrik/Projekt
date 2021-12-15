import pygame

käigu_lõpp_img = pygame.image.load("nupud/nupp2.png").convert_alpha()
võta_üles_img = pygame.image.load("nupud/nupp2.png").convert_alpha()


käigu_lõpp_nupp = nupumain.Nupud(1170, 600, käigu_lõpp_img, 0.6)
võta_üles_nupp = nupumain.Nupud(1170, 680, võta_üles_img, 0.6)

class Nupud():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), (int(height * scale))))
        #self.text_input = text_input
        #self.text = nupp.main_font.render(self.text_input, True, "black")
        self.rect = self.image.get_rect()
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

        return action
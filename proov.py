import pygame

pygame.init()

win = pygame.display.set_mode((1200, 900))

pygame.display.set_caption("Turakas")
clock = pygame.time.Clock()

x = 50
y = 50
width = 100
height = 200
vel = 100
bg = pygame.image.load("bg.jpg")
card = pygame.image.load("cards/king_of_hearts.png")
scale = 4
card = pygame.transform.scale(card, (card.get_width()/scale, card.get_height()/scale))
pos1x = 650
pos1y = 400
kaart = pygame.Rect((x, y), (card.get_width(), card.get_height()))
liigub = False
liikumine = 0
def draw_window():
    for i in range(3):
        for j in range(2):
            win.blit(bg, (i*500,j*500))
    win.blit(card, kaart)
    pygame.display.update()
    
while True:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if kaart.collidepoint(pos):
                sammx = (kaart.x-pos1x)//30
                sammy = (kaart.y-pos1y)//30
                liigub = True

                 
    keys = pygame.key.get_pressed()

    if liigub:
        if liikumine < 30:
            kaart.move_ip(-sammx, -sammy)
            liikumine += 1
        else:
            liigub = False
            liikumine = 0
#             if kaart.x < pos1x and kaart.y < pos1y:
#                 kaart.move_ip(sammx, sammy)
#             elif kaart.x < pos1x and kaart.y > pos1y:
#                 kaart.move_ip(sammx,-sammy)
#             elif kaart.x > pos1x and kaart.y < pos1y:
#                 kaart.move_ip(-sammx,sammy)
#             elif kaart.x > pos1x and kaart.y > pos1y:
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
            

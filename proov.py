import pygame

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
class Kaart:
    def __init__(self, mast, väärtus):
        self.mast = mast
        self.väärtus = väärtus

mastid = ["Poti", "Ärtu", "Risti", "Ruutu"]
kaardid = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
väärtused = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

pakk = []
for mast in mastid:
    for kaart1 in kaardid:
        pakk.append(Kaart(mast, kaart1))
print(pakk)
    
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
            

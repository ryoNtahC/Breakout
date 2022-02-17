import pygame
from pygame.locals import *

pygame.init()

šírka_obrazovky = 1280
výška_obrazovky = 720

screen = pygame.display.set_mode((šírka_obrazovky, výška_obrazovky))
pygame.display.set_caption('Breakout')

font = pygame.font.SysFont('Times New Roman', 30)

# Farby
pozadie = (255, 255, 255)
block_blue = (65 ,105 ,225)
block_green = (60 ,179 ,113)
block_red = (220,20,60)
farba_palky = (142, 135, 123)
palka_obtiahnutie = (0, 0, 0)
text_farba = (78, 81, 139)

# Premenné
stĺpce = 6
riadky = 6
clock = pygame.time.Clock()
fps = 60
smrť = False
game_over = 0

obtiažnosť=input("Zadaj akú chceš obtiažnosť (ľahká,stredná,tažká):")

if obtiažnosť == "ľahká":

    def draw_text(text, font, text_farba, x, y):
        img = font.render(text, True, text_farba)
        screen.blit(img, (x, y))


    class wall():
        def __init__(self):
            self.šírka = šírka_obrazovky // stĺpce
            self.výška = 50

        def create_wall(self):
            self.blocks = []
            block_individual = []
            for riadok in range(riadky):
                block_riadky = []
                for stĺpec in range(stĺpce):
                    block_x = stĺpec * self.šírka
                    block_y = riadok * self.výška
                    rect = pygame.Rect(block_x, block_y, self.šírka, self.výška)
                    if riadok < 6:
                        sila = 1
                    block_individual = [rect, sila]
                    block_riadky.append(block_individual)
                self.blocks.append(block_riadky)

        def draw_wall(self):
            for riadok in self.blocks:
                for block in riadok:
                    # farby a životy blockov
                    if block[1] == 3:
                        block_stĺpec = block_red
                    elif block[1] == 2:
                        block_stĺpec = block_green
                    elif block[1] == 1:
                        block_stĺpec = block_blue
                    pygame.draw.rect(screen, block_stĺpec, block[0])
                    pygame.draw.rect(screen, pozadie, (block[0]), 2)


    class paddle():
        def __init__(self):
            self.reset()

        def move(self):
            self.smer = 0
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.smer = -1
            if key[pygame.K_RIGHT] and self.rect.right < šírka_obrazovky:
                self.rect.x += self.speed
                self.smer = 1

        def draw(self):
            pygame.draw.rect(screen, farba_palky, self.rect)
            pygame.draw.rect(screen, palka_obtiahnutie, self.rect, 3)

        def reset(self):
            self.výška = 20
            self.šírka = int(šírka_obrazovky / stĺpce)
            self.x = int((šírka_obrazovky / 2) - (self.šírka / 2))
            self.y = výška_obrazovky - (self.výška * 2)
            self.speed = 10
            self.rect = Rect(self.x, self.y, self.šírka, self.výška)
            self.smer = 0


    wall = wall()
    wall.create_wall()
    pálka = paddle()

    run = True
    while run:

        clock.tick(fps)

        screen.fill(pozadie)

        # draw všetkých objektov
        wall.draw_wall()
        pálka.draw()

        pygame.display.update()

    pygame.quit()
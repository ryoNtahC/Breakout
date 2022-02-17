import pygame
from pygame.locals import *

obtiažnosť=input("Zadaj akú chceš obtiažnosť (ľahká,stredná,tažká):")

if obtiažnosť == "ľahká":
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

    class game_ball():
        def __init__(self, x, y):
            self.reset(x, y)

        def move(self):

            kolízia = 5

            zničenie = 1
            počet_riadkov = 0
            for riadok in wall.blocks:
                počet = 0
                for item in riadok:
                    # zistuje kolízie
                    if self.rect.colliderect(item[0]):
                        # kolízia zhora
                        if abs(self.rect.bottom - item[0].top) < kolízia and self.speed_y > 0:
                            self.speed_y *= -1
                        # kolízia zdola
                        if abs(self.rect.top - item[0].bottom) < kolízia and self.speed_y < 0:
                            self.speed_y *= -1
                            #  kolízia zlava
                        if abs(self.rect.right - item[0].left) < kolízia and self.speed_x > 0:
                            self.speed_x *= -1
                        # kolízia sprava
                        if abs(self.rect.left - item[0].right) < kolízia and self.speed_x < 0:
                            self.speed_x *= -1
                        # znižuje životy blockov
                        if wall.blocks[počet_riadkov][počet][1] > 1:
                            wall.blocks[počet_riadkov][počet][1] -= 1
                        else:
                            wall.blocks[počet_riadkov][počet][0] = (0, 0, 0, 0)

                    #zisťuje či sú všetky blocky zničene ak nie celý rad nieje zničený
                    if wall.blocks[počet_riadkov][počet][0] != (0, 0, 0, 0):
                        zničenie = 0
                    počet += 1
                počet_riadkov += 1
            # zisťuje či sú všetky blocky zničene ak ano celý rad je zničený
            if zničenie == 1:
                self.game_over = 1

            if self.rect.left < 0 or self.rect.right > šírka_obrazovky:
                self.speed_x *= -1

            if self.rect.top < 0:
                self.speed_y *= -1
            if self.rect.bottom > výška_obrazovky:
                self.game_over = -1

            if self.rect.colliderect(pálka):
                if abs(self.rect.bottom - pálka.rect.top) < kolízia and self.speed_y > 0:
                    self.speed_y *= -1
                    self.speed_x += pálka.smer
                    if self.speed_x > self.max_rýchlosť:
                        self.speed_x = self.max_rýchlosť
                    elif self.speed_x < 0 and self.speed_x < -self.max_rýchlosť:
                        self.speed_x = -self.max_rýchlosť
                else:
                    self.speed_x *= -1

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            return self.game_over

        def draw(self):
            pygame.draw.circle(screen, farba_palky, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                               self.ball_rad)
            pygame.draw.circle(screen, palka_obtiahnutie, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),
                               self.ball_rad, 3)

        def reset(self, x, y):
            self.ball_rad = 10
            self.x = x - self.ball_rad
            self.y = y
            self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
            self.speed_x = 4
            self.speed_y = -4
            self.max_rýchlosť = 5
            self.game_over = 0


    wall = wall()
    wall.create_wall()
    pálka = paddle()
    lopta = game_ball(pálka.x + (pálka.šírka // 2), pálka.y - pálka.výška)

    run = True
    while run:

        clock.tick(fps)

        screen.fill(pozadie)

        # draw všetkých objektov
        wall.draw_wall()
        pálka.draw()
        lopta.draw()

        pygame.display.update()

    pygame.quit()
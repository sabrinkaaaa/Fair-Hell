import pygame
from load_images import load_image

class Jump:
    def __init__(self):
        self.jump = False

    def jump_act(self):
        self.jump = -50

    def jump1(self):
        a = 0
        b = 0
        if self.jump < 50:
            self.jump += 5
            a = True
        else:
            a = False
        if self.jump < 0:
            b = True
        else:
            b = False
        return a, b


class Player:
    def __init__(self, pers):
        self.pers = pers  # 'argo''peop''priz''diav'
        self.coords = self.x, self.y = 110, 175
        # скорость передвижения 10 px
        self.hp = 300
        if self.pers == 'priz':
            self.viz = False
        self.spos = 20
        self.jump = Jump

    def cords(self, x, jump):
        self.x += x
        if jump[0]:
            if jump[1]:
                self.y += 5
            else:
                self.y -=5

    def jump1(self):
        self.jump.jump_act()
    def attack(self):
        pass



def main():
    pygame.init()
    size = width, height = 1100, 700
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pass
                if event.key == pygame.K_z:
                    # атака
                    pass
                if event.key == pygame.K_x:
                    # Супер атака(способности)
                    pass
                if event.key == pygame.K_c:
                    # блок(90% урона будет блокировано)
                    pass
    pygame.quit()


main()

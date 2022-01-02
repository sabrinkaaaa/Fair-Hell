import pygame


class Player:
    def init(self, pers):
        self.pers = pers
        self.coords = self.x, self.y = 110, 175
        # скорость передвижения 10 px
        self.hp = 300
        if self.pers == 'priz':
            self.viz = False
        self.spos = 20

    def cords(self, x,y):
        self.x += x
        self.y += y

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

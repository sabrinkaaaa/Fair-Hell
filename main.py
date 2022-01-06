import pygame

pygame.init()
abc = pygame.sprite.Group()


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


class Player(pygame.sprite.Sprite):
    def __init__(self, pers, *group):
        super().__init__(group)
        self.image = pygame.image.load('data/mario.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.pers = pers  # 'argo''peop''priz''diav'
        self.rect.x, self.rect.y = 110, 525
        # скорость передвижения 10 px
        self.hp = 300
        if self.pers == 'priz':
            self.viz = False
        self.spos = 20
        self.jump1 = False
        self.jump = False

    def cords(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def attack(self):
        pass

    def jump_act(self):
        print('activate jump')
        if not self.jump1:
            self.jump = -150
            self.jump1 = True

    def update(self, *args):
        if self.jump1:
            if self.jump < 150:
                self.jump += 1
                if self.jump < 0:
                    self.cords(0, -1)
                else:
                    self.cords(0, 1)
            else:
                self.jump = False
                self.jump1 = False


a = Player('priz', abc)


def main():
    size = width, height = 1100, 700
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    a.jump_act()
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
        screen.fill(pygame.Color("BLACK"))
        abc.draw(screen)
        abc.update(screen)
        pygame.display.flip()
    pygame.quit()


main()

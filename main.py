import pygame

pygame.init()
abc = pygame.sprite.Group()


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
        self.update_jump = 1
        self.jump1 = False
        self.jump = False
        self.left = False
        self.right = False
        self.update1 = 0
    def left_act(self):
        self.left = not self.left

    def right_act(self):
        self.right = not self.right

    def cords(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def attack(self):
        pass

    def jump_act(self):
        print('activate jump')
        if not self.jump1:
            self.update_jump = 1
            self.jump = -1 * (self.update_jump) - 130
            self.jump1 = True

    def update(self, *args):
        self.update1 +=1
        if self.update1 == 4:
            self.update1 = 0
            if self.jump1:
                if self.jump < 130 - 1:
                    self.jump += self.update_jump
                    if self.jump < 0:
                        self.cords(0, -1 * (self.update_jump))
                    else:
                        self.cords(0, self.update_jump)
                else:
                    print(self.rect.y)
                    self.jump = False
                    self.jump1 = False
            if self.left:
                self.cords(-1, 0)
            if self.right:
                self.cords(1, 0)


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
                    a.left_act()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    a.right_act()
                if event.key == pygame.K_z:
                    # атака
                    pass
                if event.key == pygame.K_x:
                    # Супер атака(способности)
                    pass
                if event.key == pygame.K_c:
                    # блок(90% урона будет блокировано)
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    a.left_act()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    a.right_act()

        screen.fill(pygame.Color("BLACK"))
        abc.draw(screen)
        abc.update(screen)
        pygame.display.flip()
    pygame.quit()


main()

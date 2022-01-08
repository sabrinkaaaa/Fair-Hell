import pygame

FPS = 150
size = width, height = 1100, 700
pygame.init()
abc = pygame.sprite.Group()
clock = pygame.time.Clock()
hps = pygame.sprite.Group()


class Hotbar_hp:
    def __init__(self, max_hp, flag):
        self.max_hp = max_hp
        self.hp = max_hp + 1 - 1
        self.flag = flag

    def draw(self, screen):
        print(1)
        if self.flag:
            pygame.draw.line(screen, (255, 0, 0), *[(10, 30), (510, 30)], 15)
            print(2)
        else:
            pygame.draw.line(screen, (255, 0, 0), *[(590, 30), (1090, 30)], 15)



b = Hotbar_hp(300, True)
c = Hotbar_hp(300, False)


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
        self.max_hp = 300
        if self.pers == 'priz':
            self.viz = False
        self.spos = 20
        self.update_jump = 1
        self.jump1 = False
        self.jump = False
        self.left = False
        self.right = False

    def left_act(self):
        self.left = not self.left

    def right_act(self):
        self.right = not self.right

    def cords(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def hp_return(self):
        return self.hp

    def hp_red(self, hp):
        self.hp -= hp

    def attack(self):
        pass

    def jump_act(self):
        print('activate jump')
        if not self.jump1:
            self.update_jump = 1
            self.jump = -1 * (self.update_jump) - 130
            self.jump1 = True

    def update(self, *args):
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
        if self.left and self.rect.x > 0:
            self.cords(-1, 0)
        if self.right and self.rect.x < width - 100:
            self.cords(1, 0)


a = Player('priz', abc)


def main():
    size = width, height = 1100, 700
    screen = pygame.display.set_mode(size)
    running = True
    b.draw(screen)
    c.draw(screen)
    pygame.display.update()
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

        pygame.draw.rect(screen, (0, 0, 0), (0, 50, width, height))
        abc.draw(screen)
        abc.update(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()

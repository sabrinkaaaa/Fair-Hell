import pygame

FPS = 150
size = width, height = 1100, 700
pygame.init()
abc = pygame.sprite.Group()
clock = pygame.time.Clock()
hps = pygame.sprite.Group()
spos = pygame.sprite.Group()


class Croc_spos(pygame.sprite.Sprite):
    def __init__(self, x, y, storona, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/water1.png')
        self.image = pygame.transform.scale(self.image, (100, 20))
        self.rect = self.image.get_rect()

        self.storona = storona
        self.rect.x = x
        self.rect.y = y
        print(345, self.rect.x, self.rect.y)

    def update(self, *args):
        if self.rect.x > 1200:
            self.kill()
        print(321)
        coords = d.get_cords()
        if coords[0] + 100 > self.rect.x:
            pass
        print(self.rect.x)
        self.rect.x += 1



class Hotbar_hp:
    def __init__(self, max_hp, flag):
        self.max_hp = max_hp
        self.hp = max_hp + 1 - 1
        self.flag = flag

    def draw(self, screen):
        hp = self.hp / self.max_hp
        hp = round(hp, 2)
        draw = 500 * hp
        if self.flag:
            pygame.draw.line(screen, (255, 0, 0), *[(10, 30), (draw + 10, 30)], 15)
        else:
            pygame.draw.line(screen, (255, 0, 0), *[((1090 - draw), 30), (1090, 30)], 15)

    def hp_red(self, hp):
        self.hp = hp


b = Hotbar_hp(300, True)
c = Hotbar_hp(300, False)


class Player(pygame.sprite.Sprite):
    def __init__(self, pers, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/mario.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.attack2 = False
        self.attack1 = 0

        self.pers = pers  # 'argo''peop''priz''diav'
        self.rect.x, self.rect.y = 110, 525
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
        h = d.get_cords()
        udar = self.rect.x + 100
        if udar - 75 < h[0] < udar + 50:
            d.hp_red(20)
            self.attack2 = True
            self.dis()

    def attack_act(self):
        self.attack2 = True

    def jump_act(self):
        print('activate jump')
        if not self.jump1:
            self.update_jump = 5
            self.jump = -1 * (self.update_jump) - 300
            self.jump1 = True

    def get_cords(self):
        return self.rect.x, self.rect.y

    def dis(self):
        if self.attack2:
            a = self.get_cords()
            self.image = pygame.image.load('data/mario_attack.jpg')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = a[0], a[1]
        else:
            a = self.get_cords()
            self.image = pygame.image.load('data/mario.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = a[0], a[1]

    def update(self, *args):
        if self.attack1 == FPS and self.attack2:
            self.attack2 = False
            self.attack1 = 0
            self.dis()
        elif self.attack2:
            self.attack1 += 1
        b.hp_red(self.hp)
        if self.jump1:
            if self.jump < 300 - self.update_jump:
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

    def sposop(self):
        if self.pers == 'argo':
            print(123)
            a = self.get_cords()
            Croc_spos(a[0], a[1], 1, spos)

    def prover(self):
        h = d.get_cords()
        udar = self.rect.x + 100
        print(udar - 75 < h[0] < udar + 50, 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/luiji.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 900, 525
        self.hp = 300
        self.max_hp = 300
        self.update_jump = 1
        self.jump1 = False
        self.jump = False
        self.left = False
        self.right = False

    def hp_red(self, hp):
        self.hp -= hp

    def update(self, *args):
        c.hp_red(self.hp)

    def cords(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_cords(self):
        return self.rect.x, self.rect.y

    def attack(self):
        h = a.get_cords()
        udar = self.rect.x - 100
        print(udar - 50, udar + 75)
        if udar - 50 < h[0] < udar + 75:
            a.hp_red(20)
            self.attack2 = True
            # self.dis()

    def attack_act(self):
        self.attack2 = True

    def prover(self):
        h = a.get_cords()
        udar = self.rect.x - 100
        print(udar - 50 < h[0] < udar + 75, 1)


a = Player('argo', abc)
d = Enemy(abc)


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
                    a.attack()
                if event.key == pygame.K_x:
                    a.sposop()
                if event.key == pygame.K_c:
                    d.attack()
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    a.left_act()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    a.right_act()
        screen.fill((0, 0, 0))
        b.draw(screen)
        c.draw(screen)
        spos.draw(screen)
        spos.update(screen)

        abc.draw(screen)
        abc.update(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


main()

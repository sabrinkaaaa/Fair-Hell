import random

import pygame

Game = 0


def reolad():
    a.hp_norm()
    d.hp_norm()
    a.rt()
    d.rt()
    a.reload()
    d.reload()


def proverka(screen):
    aa = a.hp_return()
    dd = d.hp_return()
    if aa <= 0 and not dd <= 0:
        font = pygame.font.Font(None, 72)
        text = font.render("You Lose!!!", True, (0, 100, 0))
        place = text.get_rect(center=(200, 150))
        screen.blit(text, (550, 350))
        Game = 1
        return 2
    elif dd <= 0 and not aa <= 0:
        font = pygame.font.Font(None, 72)
        text1 = font.render("You win!!!", True, (0, 100, 0))
        place = text1.get_rect(center=(200, 150))
        screen.blit(text1, (550, 350))
        Game = 2
        return 1
    return 0


class Intelect:
    def __init__(self):
        self.intelect = [0, 0, 0, 'atc', 'bl', 'le', 'ri', 'ju']
        self.time_mozg = 0
        self.spis = 0
        random.shuffle(self.intelect)

    def imp(self):
        self.time_mozg += 1
        if self.time_mozg == FPS // 2:
            if self.intelect[self.spis] == 'atc':
                d.attack()
            elif self.intelect[self.spis] == 'le':
                d.left_act()
            elif self.intelect[self.spis] == 'ju':
                d.jump_act()
            elif self.intelect[self.spis] == 'ri':
                d.right_act()
            elif self.intelect[self.spis] == 'le':
                pass
            self.spis += 1
            self.time_mozg = 0
            if self.spis == 6:
                self.spis = 0
                random.shuffle(self.intelect)
                print(self.intelect)


class Fone(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/bolota13.jpg')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Croc_spos(pygame.sprite.Sprite):
    def __init__(self, x, y, storona, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/water1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (100, 20))
        self.rect = self.image.get_rect()

        self.storona = storona
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):

        if self.rect.x > 1200:
            self.kill()
        coords = d.get_cords()
        if (coords[0] - 110 < self.rect.x < coords[0] + 50) and \
                self.rect.y + 15 > coords[1] > self.rect.y - 20:
            d.hp_red(20)
            self.kill()
        self.rect.x += 1
        if d.hp_return() <= 0:
            self.kill()


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


class Player(pygame.sprite.Sprite):
    def __init__(self, pers, *group):
        super().__init__(*group)
        self.image = pygame.image.load('data/argonianin.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.attack2 = False
        self.attack1 = 0
        self.attact3 = 0
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
        self.hp_def = True

    def rt(self):
        self.hp_def = True

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
        if self.hp_def:
            self.hp -= hp

    def attack(self):
        if not self.attack2:
            h = d.get_cords()
            udar = self.rect.x + 100
            if udar - 75 < h[0] < udar + 50:
                d.hp_red(20)
                self.attack2 = True
                self.attact3 += 1
                self.dis()

    def hp_norm(self):
        self.hp = self.max_hp

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

    def reload(self):
        self.rect.x = 110

    def dis(self):
        if self.attack2:
            a = self.get_cords()
            self.image = pygame.image.load('data/argonianin_attak.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = a[0], a[1]
        else:
            a = self.get_cords()
            self.image = pygame.image.load('data/argonianin.png')
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

        if self.attact3 >= 3:
            self.attact3 = 0
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
        self.image = pygame.image.load('data/monstr_battle.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 900, 525
        self.attack3 = 0
        self.hp = 300
        self.max_hp = 300
        self.update_jump = 1
        self.jump1 = False
        self.jump = False
        self.left = False
        self.right = False
        self.left1 = 50
        self.right1 = 50
        self.hod = False
        self.hp_def = True

    def hp_red(self, hp):
        if self.hp_def:
            self.hp -= hp

    def hp_return(self):
        return self.hp

    def mozg(self, arrg):
        if arrg == 'atc':
            self.attack()
        elif arrg == 'le':
            self.left_act()
        elif arrg == 'ri':
            self.right_act()
        elif arrg == 'ju':
            self.jump = True

    def update(self, *args):
        c.hp_red(self.hp)
        mozg.imp()
        if self.jump1:
            if self.jump < 300 - self.update_jump:
                self.jump += self.update_jump
                if self.jump < 0:
                    self.cords(0, -1 * (self.update_jump))
                else:
                    self.cords(0, self.update_jump)
            else:
                self.jump = False
                self.jump1 = False
        if self.left and self.rect.x > 0:
            if self.left1 == 0:
                self.left = False
                self.left1 = 50
            self.cords(-1, 0)
            self.left1 -= 1
        if self.right and self.rect.x < width - 100:
            if self.right1 == 0:
                self.right = False
                self.right1 = 50
            self.cords(1, 0)
            self.right1 -= 1

    def cords(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_cords(self):
        return self.rect.x, self.rect.y

    def hp_norm(self):
        self.hp = self.max_hp

    def rt(self):
        self.hp_def = True

    def reload(self):
        self.rect.x = 900

    def jump_act(self):
        print('activate jump1')
        if not self.jump1:
            self.update_jump = 5
            self.jump = -1 * (self.update_jump) - 300
            self.jump1 = True

    def attack(self):
        h = a.get_cords()
        udar = self.rect.x - 100
        if udar - 50 < h[0] < udar + 75:
            if self.attack3 == 3:
                a.hp_red(150)
                self.attack3 = 0
            a.hp_red(50)
            self.attack2 = True
            self.attack3 += 1

            # self.dis()

    def attack_act(self):
        self.attack2 = True

    def left_act(self):
        if not self.right:
            self.left = True

    def right_act(self):
        if not self.left:
            self.right = True


FPS = 150
size = width, height = 1100, 700
pygame.init()
abc = pygame.sprite.Group()
clock = pygame.time.Clock()
hps = pygame.sprite.Group()
spos = pygame.sprite.Group()

fon = pygame.sprite.Group()
fon1 = Fone(fon)

b = Hotbar_hp(300, True)
c = Hotbar_hp(300, False)

a = Player('argo', abc)
d = Enemy(abc)
mozg = Intelect()


def battle():
    stop = 0
    stop1 = True
    screen = pygame.display.set_mode(size)
    running = True
    prov = proverka(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if stop == 400 and prov == 2:
                prov = 0
                reolad()
                print(1234)
                stop = 0
            if stop == 400 or not stop1:
                running = False
                prov = 0
                stop = 0
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
                    # блок
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    a.left_act()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    a.right_act()
        if prov != 0:
            a.hp_def = False
            d.hp_def = False
        else:
            a.rt()
            d.rt()
        fon.draw(screen)
        prov = proverka(screen)
        b.draw(screen)
        c.draw(screen)
        spos.draw(screen)
        abc.draw(screen)
        spos.update(screen)
        abc.update(screen)
        mozg.imp()
        clock.tick(FPS)
        pygame.display.flip()
        if prov == 1 or prov == 2:
            stop += 1
        if prov == 1:
            stop1 = False
        if stop == 400 and prov == 2:
            reolad()
            stop = 0

        pygame.display.flip()
    #pygame.quit()

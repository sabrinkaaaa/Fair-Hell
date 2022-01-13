import os
import pygame
import sys
import random
import pickle

width = 1100
height = 700
flag = 0
all_sprites_cloud = pygame.sprite.Group()
all_sprites_menu = pygame.sprite.Group()
running = True
f = 0


# сохранение заметки
def save_file():
    global flag
    # ключ
    date_save = {"save": flag}
    # создание txt файла
    with open("conf.txt", "wb") as dump_out:
        pickle.dump(date_save, dump_out)


# распаковка предыдущей заметки
def read_file():
    global flag
    # если txt файл не был создан
    try:
        # распаковка txt файла
        with open('conf.txt', 'rb') as dump_in:
            date_load = pickle.load(dump_in)
            flag = date_load["save"]
    except:
        print("Нет")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class New_game(pygame.sprite.Sprite):
    global running
    image = load_image("new_game.png")
    image = pygame.transform.scale(image, (350, 200))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = New_game.image
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 350
        self.rect = self.image.get_rect()
        self.rect.center = (550, 350)
        self.speedx = 0

    def update(self, *args):
        self.rect.center = (550, 350)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.rect.center = (550, 550)


    def new_update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.rect.center = (0, 0)


class Continue(pygame.sprite.Sprite):
    image = load_image("continue.png")
    image = pygame.transform.scale(image, (350, 200))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Continue.image
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 150
        self.rect = self.image.get_rect()
        self.rect.center = (550, 150)
        self.speedx = 0

    def update(self, *args):
        self.rect.center = (550, 150)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.rect.center = (-550, -150)

    def new_update(self):
        self.rect.center = (-550, -150)
        pygame.display.update()


class Exite(pygame.sprite.Sprite):
    global running
    image = load_image("exite.png")
    image = pygame.transform.scale(image, (350, 200))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Exite.image
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 550
        self.rect = self.image.get_rect()
        self.rect.center = (550, 550)
        self.speedx = 0

    def update(self, *args):
        global running
        self.rect.center = (550, 550)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            running = False


class Cloud(pygame.sprite.Sprite):
    global f
    image = load_image("cloud1.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Cloud.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-300, width)
        self.rect.y = random.randrange(-150, height)
        self.speedx = 0

    def update(self):
        if f == 0:
            self.rect = self.rect.move(random.randrange(3) - 1,
                                       random.randrange(3) - 1)
        elif f > 0:
            self.rect = self.rect.move(random.randrange(50) - 1,
                                       random.randrange(50) - 1)

    def new_update(self):
        self.rect = self.rect.move(random.randrange(50) - 1,
                                   random.randrange(50) - 1)
        pygame.display.update()


class Cloud_2(pygame.sprite.Sprite):
    global f
    image = load_image("cloud4.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Cloud_2.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-300, width)
        self.rect.y = random.randrange(-150, height)
        self.speedx = 0

    def update(self):
        if f == 0:
            self.rect = self.rect.move(random.randrange(3) - 1,
                                       random.randrange(3) - 1)
        elif f > 0:
            self.rect = self.rect.move(random.randrange(50) - 1,
                                       random.randrange(50) - 1)

    def new_update(self):
        self.rect = self.rect.move(random.randrange(50) - 1,
                                    random.randrange(50) - 1)
        pygame.display.update()


def main():
    ex = Exite(pygame.sprite.Group())
    new_game = New_game(pygame.sprite.Group())
    cloud_2 = Cloud_2(pygame.sprite.Group())
    cloud_1 = Cloud(pygame.sprite.Group())
    pygame.init()

    global running
    global f

    # вставляем фон
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Изображение")

    # настройки фона
    bg_surf = pygame.image.load('app.bmp')
    bg_rect = bg_surf.get_rect(
        bottomright=(width, height))

    # настройки текста
    font = pygame.font.Font(None, 72)
    text = font.render("Hello Wold", True, (0, 100, 0))
    place = text.get_rect(center=(200, 150))

    # вставляем фон
    screen.blit(bg_surf, bg_rect)

    # вставляем текст
    screen.blit(text, place)

    # ЗДЕСЬ ПОЯВЛЯЕТСЯ МЕНЮ

    for _ in range(1):
        New_game(all_sprites_menu)
        Continue(all_sprites_menu)
        Exite(all_sprites_menu)

    # ЗДЕСЬ ПОЯВЛЯЮТСЯ ОБЛАКА

    for _ in range(30):
        Cloud(all_sprites_cloud)
        Cloud_2(all_sprites_cloud)

    while running:
        # ЗДЕСЬ ПОЯВЛЯЛИСЬ ВСЕ ОБЪЕКТЫ
        screen.blit(bg_surf, bg_rect)

        all_sprites_cloud.draw(screen)
        all_sprites_cloud.update()

        all_sprites_menu.draw(screen)
        all_sprites_menu.update()
        # screen.blit(text, place)
        # pygame.draw.rect(screen, (255, 255, 255, 127), (375, 450, 350, 200), 0)
        # pygame.draw.rect(screen, (0, 0, 255), (375, 250, 350, 200))
        # pygame.draw.rect(screen, (255, 0, 0), (375, 50, 350, 200))

        """for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 375 < event.pos[0] < 725 and 450 < event.pos[1] < 650:
                    ex.update(event)
                #print("Сука, у  меня эта хуита пол ёбаного дня не работала")
                elif 375 < event.pos[0] < 725 and 250 < event.pos[1] < 450:
                    running = False
                elif 375 < event.pos[0] < 725 and 50 < event.pos[1] < 250:
                    flag = 1
                    save_file()
                    running = False

            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_z:
                    pass
                if event.key == pygame.K_x:
                    pass
                if event.key == pygame.K_c:
                    pass
                if event.key == pygame.K_v:
                    pass"""

        pygame.display.update()

        pygame.time.delay(30)
    print("hhhhhhhhh")
    f += 1
    oblako = 0
    running = True
    while running:
        # ЗДЕСЬ ПОЯВЛЯЛИСЬ ВСЕ ОБЪЕКТЫ
        screen.blit(bg_surf, bg_rect)

        if oblako < 70:
            for i in range(70):
                screen.blit(bg_surf, bg_rect)

                all_sprites_cloud.update()
                all_sprites_cloud.draw(screen)

                cloud_2.new_update()
                cloud_1.new_update()
                pygame.display.update()
                oblako += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        pygame.time.delay(30)


    pygame.quit()


main()

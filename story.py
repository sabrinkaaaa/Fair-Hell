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


def character_selection():
    pass


def main():
    global running
    global f

    # вставляем фон
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Изображение")

    # настройки фона
    bg_surf = pygame.image.load('app.bmp')
    bg_rect = bg_surf.get_rect(
        bottomright=(width, height))

    while running:
        screen.blit(bg_surf, bg_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

        pygame.time.delay(30)
    pygame.quit()


main()
import pygame

def main():
    pygame.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
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
                    pass


    pygame.quit()
main()

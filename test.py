import pygame
import random
import duck_code

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DUCK_BACK = (59, 202, 255)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, x, y, filename):
        """Constructor function"""
        # Call the parent constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        self.image = pygame.image.load(filename).convert()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        #  boarders for walls, reset player, play bump sound
        if self.rect.x in range(1060, 1085):
            self.rect.x -= 25
        if self.rect.x in range(-5, 0):
            self.rect.x += 25
        if self.rect.y in range(-5, 0):
            self.rect.y += 25
        if self.rect.y in range(480, 505):
            self.rect.y -= 25


# Initialize Pygame
#  Loading sounds

pygame.init()
game_background = pygame.image.load("game_background.jpg")
duck_hit = pygame.mixer.Sound("duck_hit.wav")
player_click = pygame.mixer.Sound("shot_gun.ogg")

# Set the height and width of the screen
screen_width = 1280
screen_height = 1024
screen = pygame.display.set_mode([screen_width, screen_height])

# Starting score and font settings
font = pygame.font.Font(None, 36)
score = 0

# This is a list of every sprite.
all_sprites_list = pygame.sprite.Group()
duck_list = pygame.sprite.Group()
duck_hit_list = pygame.sprite.Group()


"""DUCKS"""
for i in range(5):
    # This represents a block
    ducks = duck_code.Duck("duck1.png")

    ducks.rect.x = random.randrange(screen_width)
    ducks.rect.y = random.randrange(50, 350)
    # Add the block to the list of objects
    duck_list.add(ducks)
    all_sprites_list.add(ducks)

"""PLAYER"""
player_image = pygame.image.load("crosshair.png")
player_image.set_colorkey(WHITE)

# Loop until the user clicks the close button.
    done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0


# Hide the mouse cursor
pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            blocks_hit_list = pygame.sprite.spritecollide(mouse, duck_list, True)
            score += 100
            print(score)
            player_click.play()
            # --- Game logic should go here

            # --- Screen-clearing code goes here

            # Here, we clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.

            # If you want a background image, replace this clear with blit'ing the
            # background image.
    screen.blit(game_background, [0, 0])
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    screen.blit(player_image, [x, y])

    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.

    all_sprites_list.draw(screen)
    duck_list.update()
    # Showing scoreboard
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
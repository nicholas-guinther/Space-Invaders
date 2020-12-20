import pygame

# Use this code to initialize pygame
pygame.init()

# This line creates the screen
screen = pygame.display.set_mode((800, 600))

# Window Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('spaceship1.png')
player_x = 370
player_y = 480


def player():
    screen.blit(player_img, (player_x, player_y))


# Main Game Loop
running = True
while running:
    # RGB Value
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()

# Importing Necessary Modules
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Rectangular Sprites")

# Clock to control frame rate
clock = pygame.time.Clock()

# Sprite 1 (controlled by the player)
player = pygame.Rect(100, 100, 50, 50)  # x, y, width, height

# Sprite 2 (static)
static_sprite = pygame.Rect(300, 200, 50, 50)  # x, y, width, height

# Movement speed for the player
player_speed = 5

# Game loop control flag
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Prevent the player from moving out of bounds
    if player.left < 0:
        player.left = 0
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

    # Drawing everything
    screen.fill((0, 0, 0))  # Clear the screen with a black background
    pygame.draw.rect(screen, (255, 255, 255), player)  # Draw the player sprite
    pygame.draw.rect(screen, (255, 255, 255), static_sprite)  # Draw the static sprite

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
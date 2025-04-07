# Importing Necessary Libraries
import pygame
import random

# Initialise Pygame
pygame.init()

# Custom event ID's for colour change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colours using pygame.Color
# Background Colour
BLUE = pygame.Color('Blue')
LIGHTBLUE = pygame.Color('LightBlue')
DARKBLUE = pygame.Color('DarkBlue')

# Sprite Colours
YELLOW = pygame.Color('Yellow')
MAGENTA = pygame.Color('Magenta')
ORANGE = pygame.Color('Orange')
WHITE = pygame.Color('White')

# Sprite Class representing the moving object
class Sprite(pygame.sprite.Sprite):
    # Constructor method
    def __init__(self, color, height, width):
        # Call to the parent's class (Sprite) constructor
        super().__init__()
        # Create the sprite's surface with dimensions and colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        # Set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Method to update the sprite's position
    def update(self):
        # Move the sprite by its velocity
        self.rect.move_ip(self.velocity)
        # Flag to track if the sprite hits a boundary
        boundary_hit = False
        # Check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]

        # Check for collision with top or bottom boundaries and reverse the direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        # If a boundary was hit, trigger both events
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    # Function to change the sprite's colour
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

# Function to change the background colour
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])


# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 380)
# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title
pygame.display.set_caption('Colourful Bounce')
# Set the initial background colour
bg_color = BLUE

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
    # Event handling loop
    for event in pygame.event.get():
        # If the window close button is clicked, exit the game
        if event.type == pygame.QUIT:
            exit = True
        # If the sprite colour change event is triggered, change the colour of the sprite
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        # If the background colour change event is triggered, change the background colour
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # Update all the sprites
    all_sprites_list.update()
    # Fill the screen with the current background colour
    screen.fill(bg_color)
    # Draw all the sprites to the screen
    all_sprites_list.draw(screen)

    # Refresh the display
    pygame.display.flip()
    # Limit the frame rate to 240 fps
    clock.tick(240)

# Uninitialize all the pygame modules and close the window
pygame.quit()
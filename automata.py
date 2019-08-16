import pygame
import math
from game_of_life import World
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Reactive Diffusion")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

eater = [(5,5), (6,5), (7,5), (7,4), (6,3), (13,23), (13,22), (13,21), (12,23),
         (11,23), (10,23), (9,22), (9, 20), (12,20), (26,25), (26,24), (27,24),
         (28,25), (28,26), (28,27), (29,27)]
exploder = [(21,23), (21,24), (21,25), (21,26), (21,27), (25,23), (25,24), (25,25), (25,26), (25,27), (23,23), (23, 27)]
world = World(exploder)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    for x, y in world.live_cells():
        # screen.set_at((x, y), BLACK)
        pygame.draw.rect(screen, BLACK, [10 * x, 10 * y, 10, 10])

    world = world.next_iteration()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

pygame.quit()

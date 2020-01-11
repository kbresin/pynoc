import pygame
from pygame import *
import random
import time

#Initialize pygame
pygame.init()

projectName = 'NoC Intro Gaussian'

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLACK_A10 = (0,0,0,10)

GAME_WINDOW = display.set_mode((900,400))

#Create Window
display.set_caption(projectName)
GAME_WINDOW.fill(COLOR_WHITE)
display.update()

game_running = True
WIDTH, HEIGHT = pygame.display.get_surface().get_size()

def monteCarlo():
#    We do this “forever” until we find a qualifying random value.
    while True:
        #Pick a random value.
        r1 = random.random();

        # Assign a probability.
        probability = r1;

        # Pick a second random value.
        r2 = random.random();

        # Does it qualify? If so, we’re done!
        if r2 < probability:
          return r1
        else:
          print("rejecting", r1, "less than", r2)
def nextMonteCarlo():
    sd = WIDTH
    mean = 10
    return monteCarlo() * sd + mean

r = 16
half_r = int(r/2)

COLOR_BLACK_A10 = (0,0,0,10)

dot = pygame.Surface((r*2,r*2), pygame.SRCALPHA)  # the size of your rect
#dot.set_alpha(10)                # alpha level
pygame.draw.circle(dot, COLOR_BLACK_A10, (r,r), r)

#--------------------------------------------------------#
# Game Loop
while game_running:
# Check for events
  x = nextMonteCarlo()
 # pygame.draw.circle(GAME_WINDOW, COLOR_BLACK_A10, (int(x), 180), r)
  GAME_WINDOW.blit(dot, (int(x),180))    # (0,0) are the top-left coordinates

  display.update()

  for event in pygame.event.get():
# Exit loop on quit
    if event.type == QUIT:
        game_running = False

 # time.sleep(0.02)

#End of main game Loop
#--------------------------------------------------------#
# Clean up game
pygame.quit()

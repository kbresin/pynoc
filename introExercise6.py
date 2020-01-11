import pygame
from pygame import *
import random
import time
from lib.Vector import Vector

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

def edgeCheck(v):
  if (v.x > WIDTH):
      v.x = 0
  if (v.x < 0):
      v.x = WIDTH
  if (v.y > HEIGHT):
      v.y = 0
  if (v.y < 0):
      v.y = HEIGHT

def weightedRandom():
    max = 10
#    We do this “forever” until we find a qualifying random value.
    while True:
        #Pick a random value.
        r1 = random.randint(0,max);

        # Assign a probability.
        probability = r1*r1;

        # Pick a second random value.
        r2 = random.randint(0,max*max);

        # Does it qualify? If so, we’re done!
        if r2 < probability:
          return random.randint(-r1, r1)
        else:
          print("rejecting", r1, "less than", r2)

r = 1
#dot.set_alpha(10)                # alpha level


pos = Vector(int(WIDTH/2),int(HEIGHT/2))

#--------------------------------------------------------#
# Game Loop
while game_running:
# Check for events
  xstep = weightedRandom()
  ystep = weightedRandom()
  step = Vector(xstep,ystep)
  lastPos = pos.copy()
  pos.add(step)
  pygame.draw.line(GAME_WINDOW, COLOR_BLACK, lastPos.coords(), pos.coords(), r)

  display.update()g
  edgeCheck(pos)

  for event in pygame.event.get():
# Exit loop on quit
    if event.type == QUIT:
        game_running = False

  time.sleep(0.02)

#End of main game Loop
#--------------------------------------------------------#
# Clean up game
pygame.quit()

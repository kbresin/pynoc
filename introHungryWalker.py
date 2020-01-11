import pygame
from pygame import *
from lib.Vector import Vector
import time
import random

#Initialize pygame
pygame.init()

projectName = 'NoC Intro Hungry Walker'
print("This walker prioritizes white squares over black")

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)

GAME_WINDOW = display.set_mode((900,400))

#Create Window
display.set_caption(projectName)
GAME_WINDOW.fill(COLOR_WHITE)
display.update()

game_running = True
WIDTH, HEIGHT = pygame.display.get_surface().get_size()

pos = Vector(int(WIDTH/2),int(HEIGHT/2))
posVel = Vector(1,3.3)

def edgeCheck(v):
  if (v.x > WIDTH):
      v.x = 0
  if (v.x < 0):
      v.x = WIDTH
  if (v.y > HEIGHT):
      v.y = 0
  if (v.y < 0):
      v.y = HEIGHT

def randomWalk():
    # 8 1 2
    # 7 0 3
    # 6 5 4
    x = 0
    y = 0
    choice = random.randint(1,8)
#    print(choice)
    if choice == 1:
      y -= 1
    elif choice == 2:
      x += 1
      y -= 1
    elif choice == 3:
      x += 1
    elif choice == 4:
      x += 1
      y += 1
    elif choice == 5:
      y += 1
    elif choice == 6:
      y += 1
      x -= 1
    elif choice == 7:
      x -= 1
    elif choice == 8:
      x -= 1
      y -= 1
    return Vector(x,y)

# TODO do edgeChecking if x or y is 0 or HEIGH/WIDTH
def findAdjacentColor(display, x,y, targetColor):
#    print("fac called with:", x, y)
#   todo handle out of bounds
    foundPixels = []
    for xinc in [-1, 0, 1]:
        for yinc in [-1, 0, 1]:
            if xinc != 0 or yinc != 0:
                tx = x+xinc
                ty = y+yinc
                pixelColor = display.get_at((tx, ty))[:3]
                if pixelColor == targetColor:
                    foundPixels.append((tx, ty))
#                else:
#                    print(pixelColor, "doesn't match", targetColor)
#    print("returning",foundPixels)
#    time.sleep(5)
    return foundPixels

# r = 16
r = 1
#--------------------------------------------------------#
# Game Loop
while game_running:
# Check for events
  pygame.draw.circle(GAME_WINDOW, COLOR_BLACK, pos.coords(), 0)
  display.update()

  for event in pygame.event.get():
# Exit loop on quit
    if event.type == QUIT:
        game_running = False

#  pygame.draw.circle(GAME_WINDOW, COLOR_BLACK, (pos.pixels()), r )
#  pos.add(randomWalk())
  whitePixels = findAdjacentColor(GAME_WINDOW, int(pos.x), int(pos.y), COLOR_WHITE)
  whitePixelsFound = len(whitePixels)
  if whitePixelsFound > 0:
    choice = random.randint(0,whitePixelsFound-1)
    newCoords = whitePixels[choice]
    pos.set(newCoords[0], newCoords[1])
  else:
      pos.add(randomWalk())
      print("random walking")
  edgeCheck(pos)
  time.sleep(0.1)
#  print(random.randint(1,4))


#End of main game Loop
#--------------------------------------------------------#
# Clean up game
pygame.quit()

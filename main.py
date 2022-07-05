import pygame
import time
import math
from player import *
from utils import *

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)




BACKGROUND = scale_image(pygame.image.load("imgs/background.jpg"), 1)

ASTEROID = scale_image(pygame.image.load("imgs/asteroid.jpg"), 1)


WIN = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Space Shooter")

FPS = 60

clock = pygame.time.Clock()

images = [(BACKGROUND, (0, 0)), (ASTEROID, (0, 0))]

run = True
player = Player()

while run:
    clock.tick(FPS)
    draw(WIN, images)
    player.draw(WIN)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moving_up = False
    moving_down = False
    moving_left = False
    moving_right = False

    if keys[pygame.K_a]:
        moving_left = True
        player.move_horizontal(left=True)

    elif keys[pygame.K_d]:
        moving_right = True
        player.move_horizontal(right=True)

    if keys[pygame.K_w]:
        moving_up = True
        player.move_vertical(up=True)

    elif keys[pygame.K_s]:
        moving_down = True
        player.move_vertical(down=True)

    if not moving_right and not moving_left:
        player.stop_horizontal()

    if not moving_down and not moving_up:
        player.stop_vertical()


    player.update()


pygame.quit()
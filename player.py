import math

import pygame
from utils import *

class Player:
    MAX_SPEED = 7
    IMG = scale_image(pygame.image.load("imgs/player.png"), 1)
    ACCELERATION = 0.3
    DECELERATION = 0.15
    CENTER = (1366/2, 768/2)

    def __init__(self):
        self.ver_speed = 0
        self.hor_speed = 0

        self.angle = -90
        self.img = self.IMG
        self.x, self.y = self.CENTER

    def draw(self, win):
        rotate_image(win, self.img, (self.x, self.y), self.angle)

    def move_vertical(self, up=False, down=False):
        if up:
            self.ver_speed = max(self.ver_speed - self.ACCELERATION, -self.MAX_SPEED)
        if down:
            self.ver_speed = min(self.ver_speed + self.ACCELERATION, self.MAX_SPEED)

        self.y += self.ver_speed

    def move_horizontal(self, right=False, left=False):
        if right:
            self.hor_speed = min(self.hor_speed + self.ACCELERATION, self.MAX_SPEED)
        if left:
            self.hor_speed = max(self.hor_speed - self.ACCELERATION, -self.MAX_SPEED)

        self.x += self.hor_speed


    def update(self):
        pos = pygame.mouse.get_pos()
        off_x, off_y = self.IMG.get_rect().center
        obj_pos = self.x+off_x, self.y+off_y
        angle = follow_mouse(pos, obj_pos)
        if angle != -90:
            self.angle = angle

    def stop_vertical(self):
        if self.ver_speed > 0:
            self.ver_speed = max(self.ver_speed - self.DECELERATION, 0)
        elif self.ver_speed < 0:
            self.ver_speed = min(self.ver_speed + self.DECELERATION, 0)

        self.y += self.ver_speed

    def stop_horizontal(self):
        if self.hor_speed > 0:
            self.hor_speed = max(self.hor_speed - self.DECELERATION, 0)
        elif self.hor_speed < 0:
            self.hor_speed = min(self.hor_speed + self.DECELERATION, 0)

        self.x += self.hor_speed


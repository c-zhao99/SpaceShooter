import math

import pygame

def scale_image(image, factor):
    size = round(image.get_width() * factor), round(image.get_height() * factor)
    return pygame.transform.scale(image, size)

def rotate_image(win, image, top_left_corner, angle):
    rotated = pygame.transform.rotate(image, angle)
    rectangle = rotated.get_rect(center=image.get_rect(topleft=top_left_corner).center)
    win.blit(rotated, rectangle.topleft)

def follow_mouse(mouse_pos, obj_pos):
    obj_x, obj_y = obj_pos
    mouse_x, mouse_y = mouse_pos

    angle = 0

    # 1° quadrant
    if mouse_x > obj_x and mouse_y < obj_y:
        cos = mouse_x - obj_x
        hypotenuse = math.sqrt((math.pow(mouse_x - obj_x, 2)) + (math.pow(obj_y - mouse_y, 2)))
        radians = math.acos(cos/hypotenuse)
        angle = math.degrees(radians)

    # 2° quadrant
    elif mouse_x < obj_x and mouse_y < obj_y:
        cos = obj_x - mouse_x
        hypotenuse = math.sqrt((math.pow(obj_x - mouse_x, 2)) + (math.pow(obj_y - mouse_y, 2)))
        radians = math.acos(cos/hypotenuse)
        angle = math.degrees(radians)

        angle = 180 - angle

    # 3° quadrant
    elif mouse_x < obj_x and mouse_y > obj_y:
        cos = obj_x - mouse_x
        hypotenuse = math.sqrt((math.pow(obj_x - mouse_x, 2)) + (math.pow(mouse_y - obj_y, 2)))
        radians = math.acos(cos / hypotenuse)
        angle = math.degrees(radians)

        angle += 180

    # 4° quadrant
    elif mouse_x > obj_x and mouse_y > obj_y:
        cos = mouse_x - obj_x
        hypotenuse = math.sqrt((math.pow(mouse_x - obj_x, 2)) + (math.pow(mouse_y - obj_y, 2)))
        radians = math.acos(cos/hypotenuse)
        angle = math.degrees(radians)

        angle = 360 - angle

    return angle-90



# coding: utf-8

import pygame

from math import *

pygame.font.init()

PINK  = (255,   0, 150)
WHITE = (255, 255, 255)

def draw(eq, plane_size=(800, 800), continuity=0.005, color=PINK):
    w, h, hw, hh = (*plane_size, plane_size[0] / 2, plane_size[1] / 2)

    t = 0
    
    func = eq[3:].strip()

    font = pygame.font.SysFont("freesans", 15)

    plane = pygame.display.set_mode(size=plane_size)

    while True:
        pygame.display.flip()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return None

        pygame.draw.line(plane, WHITE, (hw, h), (hw, 0))
        pygame.draw.line(plane, WHITE, (0, hh), (w, hh))

        value = eval(func)
        cx = cos(t) * value
        cy = sin(t) * value

        pygame.draw.circle(plane, color, (cx + hw, -1 * cy + hh), 1)

        text = font.render(f"drawing the point (cartesian) : {(cx, cy)}", False, WHITE)
        plane.blit(pygame.Surface(text.get_size()), (20, 0))
        plane.blit(text, (0, 0))

        t += continuity






def draw_parametric(eq1, eq2, plane_size=(800, 800), continuity=0.001, color=PINK):
    w, h, hw, hh = (*plane_size, plane_size[0] / 2, plane_size[1] / 2)

    t = 0

    rfunc = eq1[3:].strip()
    tfunc = eq2[3:].strip()
    
    font = pygame.font.SysFont("freesans", 15)

    plane = pygame.display.set_mode(size=plane_size)

    while True:
        pygame.display.flip()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return None

        pygame.draw.line(plane, WHITE, (hw, h), (hw, 0))
        pygame.draw.line(plane, WHITE, (0, hh), (w, hh))

        rvalue = eval(rfunc)
        tvalue = eval(tfunc)

        cx = cos(tvalue) * rvalue
        cy = sin(tvalue) * rvalue

        pygame.draw.circle(plane, color, (cx + hw, -1 * cy + hh), 1)

        text = font.render(f"drawing the point (cartesian) : {(cx, cy)}", False, WHITE)
        plane.blit(pygame.Surface(text.get_size()), (20, 0))
        plane.blit(text, (0, 0))

        t += continuity

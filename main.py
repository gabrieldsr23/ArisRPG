import random, pygame, sys
from pygame.locals import *
import menu

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

FPS = 30
global DISPLAYSURF

pygame.init()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Ari's RPG")

state = 0
def main():
    if state == 0:
        menu.menu(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT, FPS)
    return state


if __name__ == "__main__":
    main()
import pygame, sys, time
from pygame.locals import *
from player import *

#WINDOWWIDTH = 800
#WINDOWHEIGTH = 600

#pygame.init()

def test_map(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGTH, FPS):

    FPSCLOCK = pygame.time.Clock()

    GREEN = (0, 200, 50)

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))


    menu_song = pygame.mixer.music.load("audio/Forest3.mp3")
    pygame.mixer.music.play(-1, 0.0)

    walk_song = pygame.mixer.Sound("audio/walk_in_grass.wav")
    walk_song.set_volume(0.2)

    player = Player()
    player.rect.x = 300  # go to x
    player.rect.y = 400  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    player_speed = 7

    spell = 0
    while True:
        DISPLAYSURF.fill(GREEN)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                m_pos = pygame.mouse.get_pos()
                player.attack(DISPLAYSURF)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player.move(player_speed,walk_song)

        player_list.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__=="__main__":
    test_map()
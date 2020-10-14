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

    player = Player()
    player.rect.x = 300  # go to x
    player.rect.y = 400  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    spell = 0
    while True:
        DISPLAYSURF.fill(GREEN)

        move_tick = 0
        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and player.rect.x < 740:
                walk_song.play()
                move_tick = 10
                player.rect.x += 10
            elif keys[pygame.K_LEFT] and player.rect.x > 0:
                walk_song.play()
                move_tick = 10
                player.rect.x -= 10
            elif keys[pygame.K_UP] and player.rect.y > 10:
                walk_song.play()
                move_tick = 10
                player.rect.y -= 10
            elif keys[pygame.K_DOWN] and player.rect.y < 490:
                walk_song.play()
                move_tick = 10
                player.rect.y += 10

            if move_tick > 0:
                move_tick -= 1

            if event.type == pygame.K_1:
                spell = 1

            if event.type == pygame.MOUSEBUTTONUP:
                m_pos = pygame.mouse.get_pos()
                pos0 = (player.rect.x+50, player.rect.y-100)
                if spell == 1:
                    player.attack(pos0, m_pos)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        player_list.draw(DISPLAYSURF)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__=="__main__":
    test_map()
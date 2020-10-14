import pygame, sys, time
from pygame.locals import *

#WINDOWWIDTH = 800
#WINDOWHEIGTH = 600

#pygame.init()

def menu(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGTH, FPS):

    FPSCLOCK = pygame.time.Clock()

    GRAY = (120, 120, 120)
    PURPLE = (70, 0, 40)
    BLACK = (0, 0, 0)

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))

    menu_font = pygame.font.Font('freesansbold.ttf', 32)

    play_button_surface = menu_font.render(' Jogar ', True, BLACK, GRAY)
    play_button_rect = play_button_surface.get_rect()
    play_button_rect.center = (400, 300)

    set_button_surface = menu_font.render(' Configurações ', True, BLACK, GRAY)
    set_button_rect = play_button_surface.get_rect()
    set_button_rect.center = (330, 350)

    quit_button_surface = menu_font.render(' Sair ', True, BLACK, GRAY)
    quit_button_rect = play_button_surface.get_rect()
    quit_button_rect.center = (412, 400)

    menu_song = pygame.mixer.music.load("audio/menu-background.mp3")
    pygame.mixer.music.play(-1, 0.0)
    quit_song = pygame.mixer.Sound('audio/quit-song.wav')

    while True:
        DISPLAYSURF.fill(PURPLE)
        DISPLAYSURF.blit(play_button_surface,play_button_rect)
        DISPLAYSURF.blit(quit_button_surface, quit_button_rect)
        DISPLAYSURF.blit(set_button_surface, set_button_rect)


        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                m_pos = pygame.mouse.get_pos()
                if (m_pos[0] > 358 and m_pos[0] < 440) and (m_pos[1] > 385 and m_pos[1] < 425):
                    pygame.mixer.music.stop()
                    quit_song.play()
                    time.sleep(1.3)
                    pygame.quit()
                    sys.exit()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__=="__main__":
    menu()
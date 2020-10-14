import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/avatar_fire.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def attack(self,display):
        spell1_img = pygame.image.load("images/Fireball.png")
        display.blit(spell1_img,(self.rect.x+50,self.rect.y))


    def move(self,player_speed,walk_song):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and self.rect.x < 740:
            walk_song.play()
            self.rect.x += player_speed
        elif keys[pygame.K_a] and self.rect.x > 0:
            walk_song.play()
            self.rect.x -= player_speed
        elif keys[pygame.K_w] and self.rect.y > 10:
            walk_song.play()
            self.rect.y -= player_speed
        elif keys[pygame.K_s] and self.rect.y < 490:
            walk_song.play()
            self.rect.y += player_speed


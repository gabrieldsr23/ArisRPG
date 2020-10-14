import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("images/avatar_fire.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def attack(self,pos0,posF):
        spell1 = pygame.image.load("images/Fireball.png")
        spell1.images.append(spell1)
        spell1.image = spell1.images[0]
        spell1.rect = spell1.image.get_rect()
        spell1.rect.x = pos0[0]
        spell1.rect.y = pos0[1]
        if pos0[0] > posF[0] and pos0[1] > posF[1]:
            spell1.image.fill(0,0,0,0)
        else:
            spell1.rect.x += 10
            spell1.rect.y += 10



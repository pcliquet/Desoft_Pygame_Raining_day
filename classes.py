from os import kill
from pygame.display import update
import pygame
from assets import *
from config import *
import random


class Mapa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = -200
        self.rect.y = -720
        self.speedx = 0 
        self.speedy = 0 

    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
            
        if self.rect.right < 662:
            self.rect.right = 662
        
        if self.rect.right > 7000:
            self.rect.right = 7000

        if self.rect.top > 398:
            self.rect.top = 398

        if self.rect.top < -2696:
            self.rect.top = -2696


class Player(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 360
        self.speedx = 0
        self.speedy = 0
        # self.mask = img


    def pick_up (self):
        pass

class Raio(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(0, 2000)

class Madeira(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(504, 3598)
        self.speedx = 0
        self.speedy = 0

    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy

class Pedra(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(504, 3598)
        self.speedx = 0
        self.speedy = 0
    
    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
    

class Gota(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1290)
        self.rect.y = random.randint(0, 720)
        self.speedx = random.randint(-1, 2)
        self.speedy = random.randint(-1, 2)

    def update(self):
        self.rect.x += 100
        self.rect.y += 100
        # if self.rect.top > 720:
        #     kill()

#posição vai aparecer só quando o personagem terminar de pegar todos os objetos no mapa (implementar posição ainda)
class casa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = img
    def update(self):
        pass
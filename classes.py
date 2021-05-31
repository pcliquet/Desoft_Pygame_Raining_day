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
            
        if self.rect.right < x_size:
            self.rect.right = 1290
        
        if self.rect.left > 0:
            self.rect.left = 0

        if self.rect.top > 0:
            self.rect.top = 0

        if self.rect.bottom < y_size:
            self.rect.bottom = y_size

class Player(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 360
        self.speedx = 0
        self.speedy = 0
    
    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
            
        if self.rect.right > 1365:
            self.rect.right = 1365
        
        if self.rect.left < -75:
            self.rect.left = -75

        if self.rect.top < -60:
            self.rect.top = -60

        if self.rect.bottom > 790:
            self.rect.bottom = 790

class Raio(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(0, 2000)

class Madeira(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(0, 2000)
    
    def update(self):
        pass

class Pedra(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(0, 2000)
    
    def update(self):
        pass
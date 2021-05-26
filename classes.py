from pygame.display import update
import pygame
from assets import *
<<<<<<< HEAD

class Mapa(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = mapa_img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -720
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
       

        # Mantem dentro da tela
        if self.rect.right < x_size:
            self.rect.right = 1290
        if self.rect.left > 0:
            self.rect.left = 0
        if self.rect.top > 0:
            self.rect.top = 0
=======
from config import *


class Mapa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = mapa_img
        self.rect = self.img.get_rect()
        self.rect.x = -10
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

class player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = player_img
        self.rect = self.img.get_rect()
        self.rect.x = 520
        self.rect.y = 360
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

>>>>>>> a8a616f4bb30c8988c7707f4283bd5916348807d
        if self.rect.bottom < y_size:
            self.rect.bottom = y_size
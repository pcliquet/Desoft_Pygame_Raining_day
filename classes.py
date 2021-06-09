from os import kill
from pygame.display import update
import pygame
from assets import *
from config import *
from pygame.transform import flip
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
        self.y_i = -720
        self.x_i = -200

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
    def __init__(self,imgs):
        pygame.sprite.Sprite.__init__(self)
        self.imageIndex = 1
        self.imgDelay = 0
        self.imgs = imgs
        self.image = imgs[self.imageIndex]
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 360
        self.speedx = 0
        self.speedy = 0


    def update(self):
        
        image = self.imgs[self.imageIndex]
        self.imgDelay += 1
        if self.speedx != 0 or self.speedy != 0:
            if self.imgDelay % 5 == 0:
                self.imageIndex = (self.imageIndex + 1) % len(self.imgs)
                self.image = self.imgs[self.imageIndex]
                self.rect = self.image.get_rect()
                self.rect.x = 520
                self.rect.y = 360
        
        else:
            self.image = self.imgs[0]
     
    def pick_up (self):
        pass

class Poça(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 4000)
        self.rect.y = random.randint(504, 1220)
        self.speedx = 0
        self.speedy = 0
        self.x_i = self.rect.x
        self.y_i = self.rect.y
        self.delta_x = self.rect.x - self.x_i
        self.delta_y = self.rect.y - self.y_i
        self.max_y = self.rect.y
        self.max_x = self.rect.x



    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        self.delta_y = self.rect.y - self.y_i
        self.delta_x = self.rect.x - self.x_i


        if self.delta_y >= 1180:
            self.delta_y = 1180
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_y <= -1976:
            self.delta_y = -1976
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_x >= 800:
            self.delta_x = 800
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x

        if self.delta_x <= -5538:
            self.delta_x = -5538
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x

class Madeira(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-200, 6200)
        self.rect.y = random.randint(-720, 2480)
        self.speedx = 0
        self.speedy = 0
        self.movimento_y = True
        self.x_i = self.rect.x
        self.y_i = self.rect.y
        self.delta_x = self.rect.x - self.x_i
        self.delta_y = self.rect.y - self.y_i
        self.max_y = self.rect.y
        self.max_x = self.rect.x


    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        self.delta_y = self.rect.y - self.y_i
        self.delta_x = self.rect.x - self.x_i


        if self.delta_y >= 1180:
            self.delta_y = 1180
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_y <= -1976:
            self.delta_y = -1976
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_x >= 800:
            self.delta_x = 800
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x

        if self.delta_x <= -5538:
            self.delta_x = -5538
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x



class Pedra(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-200, 6200)
        self.rect.y = random.randint(-720, 2480)
        self.speedx = 0
        self.speedy = 0
        self.x_i = self.rect.x
        self.y_i = self.rect.y
        self.delta_x = self.rect.x - self.x_i
        self.delta_y = self.rect.y - self.y_i
        self.max_y = self.rect.y
        self.max_x = self.rect.x


    def update (self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        self.delta_y = self.rect.y - self.y_i
        self.delta_x = self.rect.x - self.x_i


        if self.delta_y >= 1180:
            self.delta_y = 1180
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_y <= -1976:
            self.delta_y = -1976
            self.max_y =  self.delta_y + self.y_i
            self.rect.y = self.max_y

        if self.delta_x >= 800:
            self.delta_x = 800
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x

        if self.delta_x <= -5538:
            self.delta_x = -5538
            self.max_x = self.delta_x + self.x_i
            self.rect.x = self.max_x






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
        self.rect.x += 50
        self.rect.y += 50
        if self.rect.top == 720:
            self.kill()

#posição vai aparecer só quando o personagem terminar de pegar todos os objetos no mapa (implementar posição ainda)
class casa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = img
    def update(self):
        pass
import pygame
import os
from os import path
from config import *

map_dir = path.join(path.dirname(__file__), 'assets/img/map')
mapa_img = pygame.image.load(path.join(map_dir, 'Map001.png'))
mapa_img = pygame.transform.scale(mapa_img,(6400,1900))

#mapa_img = pygame.transform.scale(mapa_img,(100,100))


player_dir = path.join(path.dirname(__file__),'assets/img/char')
player_img = pygame.image.load(path.join(player_dir, 'char_1.png'))
player_img = pygame.transform.scale(player_img,(200,200))

madeira_dir = path.join(path.dirname(__file__), 'assets/img/items/madeira')
madeira_img = pygame.image.load(path.join(madeira_dir, 'madeira.png'))
madeira_img = pygame.transform.scale(madeira_img, (200, 200))

gota_dir = path.join(path.dirname(__file__), 'assets/img/items/gota')
gota_img = pygame.image.load(path.join(gota_dir, 'gota.png'))
gota_img = pygame.transform.scale(gota_img, (7, 7)) 


pedra_dir = path.join(path.dirname(__file__), 'assets/img/items/pedra')
pedra_img = pygame.image.load(path.join(pedra_dir, 'pedra.png'))
pedra_img = pygame.transform.scale(pedra_img, (50, 50)) 

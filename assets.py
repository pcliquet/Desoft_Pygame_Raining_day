import pygame
import os
from os import path
from config import *

map_dir = path.join(path.dirname(__file__), 'assets/img/map')
mapa_img = pygame.image.load(path.join(map_dir, 'Map001.png'))
mapa_img = pygame.transform.scale(mapa_img,(2580,1440))
#mapa_img = pygame.transform.scale(mapa_img,(100,100))

player_dir = path.join(path.dirname(__file__),'assets/img/char')
player_img = pygame.image.load(path.join(player_dir, 'char_1.png'))
player_img = pygame.transform.scale(player_img,(200,200))
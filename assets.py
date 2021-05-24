import pygame
import pathlib
from path import os

map_dir = path.join(path.dirname(__file__), 'assets/img/map')
mapa_img = pygame.image.load(path.join(map_dir, 'Map001.png')).convert()
mapa_img = pygame.transform.scale(mapa_img,(2580,1440))

import pygame
import os
from os import path
from config import *

pygame.font.init()
map_dir = path.join(path.dirname(__file__), 'assets/img/map')
mapa_img = pygame.image.load(path.join(map_dir, 'Map001.png'))
mapa_img = pygame.transform.scale(mapa_img,(6400,3200))

#mapa_img = pygame.transform.scale(mapa_img,(100,100))


player_dir = path.join(path.dirname(__file__),'assets/img/char')
player_img = pygame.image.load(path.join(player_dir, 'char_1.png'))
player_img = pygame.transform.scale(player_img,(200,200))

madeira_dir = path.join(path.dirname(__file__), 'assets/img/items/madeira')
madeira_img = pygame.image.load(path.join(madeira_dir, 'madeira.png'))
madeira_img = pygame.transform.scale(madeira_img, (75, 75))

gota_dir = path.join(path.dirname(__file__), 'assets/img/items/gota')
gota_img = pygame.image.load(path.join(gota_dir, 'gota.png'))
gota_img = pygame.transform.scale(gota_img, (7, 7)) 

pedra_dir = path.join(path.dirname(__file__), 'assets/img/items/pedra')
pedra_img = pygame.image.load(path.join(pedra_dir, 'pedra.png'))
pedra_img = pygame.transform.scale(pedra_img, (50, 50)) 

casa_dir = path.join(path.dirname(__file__), 'assets/img/items/casa')
casa_img = pygame.image.load(path.join(casa_dir, 'casa.png'))
casa_img = pygame.transform.scale(casa_img, (50, 50))

raio_dir = path.join(path.dirname(__file__), 'assets/img/items/raio')
raio_img = pygame.image.load(path.join(raio_dir, 'raio_3.png'))
raio_img = pygame.transform.scale(raio_img, (100, 100))


visao_dir = path.join(path.dirname(__file__), 'assets/img/items/visao')
visao_img_1 = pygame.image.load(path.join(visao_dir, 'camera_01.png'))
visao_img_1 = pygame.transform.scale(visao_img_1, (1390, 750))

visao_dir = path.join(path.dirname(__file__), 'assets/img/items/visao')
visao_img_2 = pygame.image.load(path.join(visao_dir, 'camera_02.png'))
visao_img_2 = pygame.transform.scale(visao_img_2, (1390, 750))

visao_dir = path.join(path.dirname(__file__), 'assets/img/items/visao')
visao_img_3 = pygame.image.load(path.join(visao_dir, 'camera_03.png'))
visao_img_3 = pygame.transform.scale(visao_img_3, (1390, 800))

poça_dir = path.join(path.dirname(__file__), 'assets/img/items/poca')
poça_img = pygame.image.load(path.join(poça_dir, 'poca.png'))
poça_img = pygame.transform.scale(poça_img, (100, 100))

mar_dir = path.join(path.dirname(__file__), 'assets/img/items/mar')
mar_img = pygame.image.load(path.join(mar_dir, 'mar.png'))
mar_img = pygame.transform.scale(mar_img, (1290, 720))


font_dir = path.join(path.dirname(__file__), 'assets/img/fonte')
font_img = pygame.font.Font((path.join(font_dir, 'PressStart2P.ttf')),28)
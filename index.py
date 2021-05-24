import pygame
from config import *
from assets import *


pygame.init()


#Display
window = pygame.display.set_mode((x_size, y_size))

while game == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0

    window.blit(mapa_img, (0,0))
    pygame.display.update()


pygame.quit() 
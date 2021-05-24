import pygame
from config import *
from assets import *
from classes import *

pygame.init()


#Display
window = pygame.display.set_mode((x_size, y_size))
pygame.display.set_caption('Hello World!')


#conversor para imagem vetorizada
mapa_img.convert()
player_img.convert()

all_sprites = pygame.sprite.Group()

mapa_mov = Mapa(mapa_img)



all_sprites.add(mapa_mov)


while game == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                mapa_mov.speedx += 3
            elif event.key == pygame.K_RIGHT:
                mapa_mov.speedx -= 3
            elif event.key == pygame.K_UP:
                mapa_mov.speedy += 3
            elif event.key == pygame.K_DOWN:
                mapa_mov.speedy -= 3
            elif event.key == pygame.K_q:
                mapa_mov.shoot()
      

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                mapa_mov.speedx -= 3
            if event.key == pygame.K_RIGHT:
                mapa_mov.speedx += 3
            if event.key == pygame.K_UP:
                mapa_mov.speedy -= 3
            if event.key == pygame.K_DOWN:
                mapa_mov.speedy += 3      
    all_sprites.update()
    print(mapa_mov.rect.bottom)
    mapa_mov.update()      
    
    window.fill(PRETO)
    #window.blit(mapa_img, (0,0))
    all_sprites.draw(window)
    window.blit(player_img, (520,360))
    pygame.display.update()
    

pygame.quit() 
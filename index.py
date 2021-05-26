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

#################################
mapa_mov = Mapa(mapa_img)
player_mov = Player(player_img)

all_sprites.add(mapa_mov)
#all_sprites.add(player_mov)


while game == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0

####################################################################################################################################################################
#Teste para verificar posições
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_mov.speedx -= 5
                mapa_mov.speedx += 10
            elif event.key == pygame.K_RIGHT:
                mapa_mov.speedx -= 10
                player_mov.speedx += 5
            elif event.key == pygame.K_UP:
                mapa_mov.speedy += 10
                player_mov.speedy -= 5
            elif event.key == pygame.K_DOWN:
                mapa_mov.speedy -= 10
                player_mov.speedy += 5
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
        # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                
                mapa_mov.speedx -= 10
                player_mov.speedx += 5
            if event.key == pygame.K_RIGHT:
                mapa_mov.speedx += 10
                player_mov.speedx -= 5
            if event.key == pygame.K_UP:
                mapa_mov.speedy -= 10
                player_mov.speedy += 5
            if event.key == pygame.K_DOWN:
                mapa_mov.speedy += 10
                player_mov.speedy -= 5 
            ###########################################################################################################################











        ###########################################################################################################################################################
        #Verifica a posição do mapa
        # if mapa_mov.rect.left == 0 or mapa_mov.rect.left == -2710:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player_mov.speedx -= 5
        #             mapa_mov.speedx += 0
        #         elif event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx -= 0
        #             player_mov.speedx += 5
        #         elif event.key == pygame.K_UP:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5
        #         elif event.key == pygame.K_DOWN:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #     # Verifica se soltou alguma tecla.
        #     if event.type == pygame.KEYUP:
        #     # Dependendo da tecla, altera a velocidade.
        #         if event.key == pygame.K_LEFT:
                    
        #             mapa_mov.speedx -= 0
        #             player_mov.speedx += 5
        #         if event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx += 0
        #             player_mov.speedx -= 5
        #         if event.key == pygame.K_UP:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #         if event.key == pygame.K_DOWN:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5 
        # else:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player_mov.speedx -= 0
        #             mapa_mov.speedx += 10
        #         elif event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx -= 10
        #             player_mov.speedx += 0
        #         elif event.key == pygame.K_UP:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 0
        #         elif event.key == pygame.K_DOWN:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 0
        # # Verifica se soltou alguma tecla.
        #     if event.type == pygame.KEYUP:
        #     # Dependendo da tecla, altera a velocidade.
        #         if event.key == pygame.K_LEFT:
                    
        #             mapa_mov.speedx -= 10
        #             player_mov.speedx += 0
        #         if event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx += 10
        #             player_mov.speedx -= 0
        #         if event.key == pygame.K_UP:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 0
        #         if event.key == pygame.K_DOWN:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 0






        # if player_mov.rect.left < 520 or player_mov.rect.left > 520:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player_mov.speedx -= 5
        #             mapa_mov.speedx += 0
        #         elif event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx -= 0
        #             player_mov.speedx += 5
        #         elif event.key == pygame.K_UP:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5
        #         elif event.key == pygame.K_DOWN:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #     # Verifica se soltou alguma tecla.
        #     if event.type == pygame.KEYUP:
        #     # Dependendo da tecla, altera a velocidade.
        #         if event.key == pygame.K_LEFT:
                    
        #             mapa_mov.speedx -= 0
        #             player_mov.speedx += 5
        #         if event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx += 0
        #             player_mov.speedx -= 5
        #         if event.key == pygame.K_UP:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #         if event.key == pygame.K_DOWN:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5 
        
        #Verifica posição do personagem            
        # if player_mov.rect.left >= 520 :
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player_mov.speedx -= 0
        #             mapa_mov.speedx += 10
        #         elif event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx -= 10
        #             player_mov.speedx += 0
        #         elif event.key == pygame.K_UP:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5
        #         elif event.key == pygame.K_DOWN:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #     # Verifica se soltou alguma tecla.
        #     if event.type == pygame.KEYUP:
        #     # Dependendo da tecla, altera a velocidade.
        #         if event.key == pygame.K_LEFT:
                    
        #             mapa_mov.speedx -= 0
        #             player_mov.speedx += 5
        #         if event.key == pygame.K_RIGHT:
        #             mapa_mov.speedx += 0
        #             player_mov.speedx -= 5
        #         if event.key == pygame.K_UP:
        #             mapa_mov.speedy -= 10
        #             player_mov.speedy += 5
        #         if event.key == pygame.K_DOWN:
        #             mapa_mov.speedy += 10
        #             player_mov.speedy -= 5 



            # Dependendo da tecla, altera a velocidade.
            
           
      
        
    
    print(player_mov.rect.left)
    #print(mapa_mov.rect.left)
    all_sprites.update()
    #print(player_mov.speedx)
    #print(mov_px, mov_py)
    
    
    window.fill(PRETO)
    
    all_sprites.draw(window)
    #window.blit(player_img, (520,360))
    pygame.display.update()
    
pygame.quit()
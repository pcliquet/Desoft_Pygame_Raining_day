import pygame
from config import *
from assets import *
from classes import *
pygame.init()

#Display
window = pygame.display.set_mode((x_size, y_size))
pygame.display.set_caption('Raining Day')


pos_p = {
    'x':520,'y': 560, 'm_x': 0, 'm_y': 0, 'c_x': 0, 'c_y': 0
}
pos_m = {
    'x':0,'y': 0
}
pos_pedra = {
    'x':0,'y':0,'x_i':0,'y_i': 0 
}

#conversor para imagem vetorizada
mapa_img.convert()
player_img.convert()
gota_img.convert()
madeira_img.convert()
raio_img.convert()



all_sprites = pygame.sprite.Group()
all_pedras = pygame.sprite.Group()
all_madeira = pygame.sprite.Group()
#################################
mapa_mov = Mapa(mapa_img)
player_mov = Player(player_img)



all_sprites.add(mapa_mov)
all_sprites.add(player_mov)



for m in range(30):
    madeira = Madeira(madeira_img)
    all_madeira.add(madeira)
for f in range(30):
    pedrita = Pedra(pedra_img)
    all_pedras.add(pedrita)



while game == 1:

    for i in range(20): 
        gota_c = Gota(gota_img)
        all_sprites.add(gota_c)


    # pedrita.rect.y = mapa_mov.speedy
    # pedrita.rect.x = mapa_mov.speedx

    pos_p['x'] = player_mov.rect.left
    pos_p['y'] = player_mov.rect.bottom

    #Condições iniciais
    pos_m['x'] = mapa_mov.rect.left
    pos_m['y'] = mapa_mov.rect.bottom


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0

        #[Movimenta o mapa]

        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_LEFT:
                mapa_mov.speedx += 13
                for madeira in all_madeira:
                    madeira.speedx += 13
                for pedra in all_pedras:
                    pedra.speedx += 13

            if event.key == pygame.K_RIGHT:
                mapa_mov.speedx -= 13
                for madeira in all_madeira:
                    madeira.speedx -= 13
                for pedra in all_pedras:
                    pedra.speedx -= 13

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mapa_mov.speedx -= 13
                for madeira in all_madeira:
                    madeira.speedx -= 13
                for pedra in all_pedras:
                    pedra.speedx -= 13

            if event.key == pygame.K_RIGHT:
                mapa_mov.speedx += 13
                for madeira in all_madeira:
                    madeira.speedx += 13
                for pedra in all_pedras:
                    pedra.speedx += 13
    
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                mapa_mov.speedy += 13
                for madeira in all_madeira:
                    madeira.speedy += 13
                for pedra in all_pedras:
                    pedra.speedy += 13

            if event.key == pygame.K_DOWN:
                mapa_mov.speedy -= 13
                for madeira in all_madeira:
                    madeira.speedy -= 13
                for pedra in all_pedras:
                    pedra.speedy -= 13

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                mapa_mov.speedy -= 13
                for madeira in all_madeira:
                    madeira.speedy -= 13
                for pedra in all_pedras:
                    pedra.speedy -= 13
    
            if event.key == pygame.K_DOWN:
                mapa_mov.speedy += 13
                for madeira in all_madeira:
                    madeira.speedy += 13
                for pedra in all_pedras:
                    pedra.speedy += 13


    #pick = pygame.sprite.groupcollide(player_mov,all_madeira,all_pedras,True)

    # if madeira.colliderect() in player_mov.colliderect():
    #     madeira.kill()
    
    colisao_madeira = pygame.sprite.spritecollide(player_mov, all_madeira, True)
    # if len(colisao_madeira) > 0:
    #     print('sim')
    # else:
    #     print('não')
     
    colisao_pedra = pygame.sprite.spritecollide(player_mov, all_pedras, True)
    # if len(colisao_pedra) > 0:
    #     print('sim')

################################################################################################################        

    #print(mapa_mov.speedx)
    print(pos_m)
    #print(p_p_x)
    #print(pm_x)
    all_sprites.update()
    all_madeira.update()
    all_pedras.update()
    #print(mapa_mov.speedy)
    #print(mov_px, mov_py)

    window.fill(PRETO)
    #window.blit(mar_img,(0,0))
    
    all_sprites.draw(window)
    all_pedras.draw(window)
    all_madeira.draw(window)
    # window.blit(visao_img,(0,0))
    pygame.display.update()

pygame.quit()
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
all_sprites = pygame.sprite.Group()

#################################
mapa_mov = Mapa(mapa_img)
player_mov = Player(player_img)
pedrita = Pedra(pedra_img)


all_sprites.add(mapa_mov)
all_sprites.add(player_mov)
all_sprites.add(pedrita)


while game == 1:

    for i in range(20): 
        gota_c = Gota(gota_img)
        all_sprites.add(gota_c)

    

    pos_p['x'] = player_mov.rect.left
    pos_p['y'] = player_mov.rect.bottom

    #Condições iniciais
    pos_m['x'] = mapa_mov.rect.right
    pos_m['y'] = mapa_mov.rect.top


    pos_pedra['x_i'] = pedrita.rect.x
    pos_pedra['y_i'] = pedrita.rect.y





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0

        #[Movimenta o mapa]
        if pos_p['x'] == 520:
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx += 13

                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx -= 13
  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx -= 13

                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx += 13
       
        if pos_p['y'] == 560: 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP:
                    mapa_mov.speedy += 13

                if event.key == pygame.K_DOWN:
                    mapa_mov.speedy -= 13
   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mapa_mov.speedy -= 13
        
                if event.key == pygame.K_DOWN:
                    mapa_mov.speedy += 13
         
       
        #[Movimenta o personagem em X]
        # if pos_m['x'] == 4000 or pos_m['x'] == 1290:
        
        
        #     if pos_m['x'] == 4000:
        #         pos_p['c_x'] = 0
        #     if pos_m['x'] == 1290:
        #         pos_p['c_x'] = 1
        #     if event.type == pygame.KEYDOWN:    
        #         if event.key == pygame.K_LEFT:
        #             player_mov.speedx -= 10
        #             pos_p['m_x'] = 1
        #         if event.key == pygame.K_RIGHT:
        #             player_mov.speedx += 10
        #             pos_p['m_x'] = 1

        #     if event.type == pygame.KEYUP: 
        #         if event.key == pygame.K_LEFT and pos_p['m_x'] == 1:
        #             player_mov.speedx += 10
        #             pos_p['m_x'] = 0
        #         if event.key == pygame.K_RIGHT and pos_p['m_x'] == 1:
        #             player_mov.speedx -= 10 
        
        
        # #[Movimenta o Personagem em Y]      
        # if pos_m['y'] == 0 or pos_m['y'] == -1280:
        
        #     if pos_m['y'] == 0:
        #         pos_p['c_y'] = 0
        #     if pos_m['y'] == -1280:
        #         pos_p['c_y'] = 1
        #     if event.type == pygame.KEYDOWN:     
        #         if event.key == pygame.K_UP:
        #             player_mov.speedy -= 10
        #             pos_p['m_y'] = 1
        #         if event.key == pygame.K_DOWN:
        #             player_mov.speedy += 10
        #             pos_p['m_y'] = 1

        #     if event.type == pygame.KEYUP: 
        #         if event.key == pygame.K_UP and pos_p['m_y'] == 1:
        #             player_mov.speedy += 10
        #             pos_p['m_y'] == 0
        #         if event.key == pygame.K_DOWN and pos_p['m_y'] == 1:
        #             player_mov.speedy -= 10 
        #             pos_p['m_y'] == 0

                  
################################################################################################################        
        
    #print(mapa_mov.speedx)
    print(pos_m,pos_pedra)
    #print(p_p_x)
    #print(pm_x)
    all_sprites.update()
    #print(mapa_mov.speedy)
    #print(mov_px, mov_py)
    
    
    window.fill(PRETO)
    
    all_sprites.draw(window)
    #window.blit(gota_c)
    #window.blit(player_img, (520,360))
    pygame.display.update()
    
pygame.quit()
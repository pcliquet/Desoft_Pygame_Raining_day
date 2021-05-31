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

#conversor para imagem vetorizada
mapa_img.convert()
player_img.convert()
all_sprites = pygame.sprite.Group()

#################################
mapa_mov = Mapa(mapa_img)
player_mov = Player(player_img)

all_sprites.add(mapa_mov)
all_sprites.add(player_mov)


while game == 1:

    pos_p['x'] = player_mov.rect.left
    pos_p['y'] = player_mov.rect.bottom
    pos_m['x'] = mapa_mov.rect.right
    pos_m['y'] = mapa_mov.rect.top

    # if pos_p['x'] > 520 and pos_p['c_x'] == 0:
    #     player_mov.speedx = 0
    #     player_mov.rect.left = 520
    #     pos_p['m_x'] = 0
    #     pos_m['x'] == 3999
    # elif pos_p['x'] <= 520 and pos_p['c_x'] == 1:
    #     player_mov.speedx = 0
    #     player_mov.rect.left = 520
    #     pos_p['m_x'] = 0
    #     pos_m['x'] == 1291
    #     pos_p['c_x'] == 0
    # elif pos_p['c_y'] == 1 and pos_p['y'] >= 560:
    #     player_mov.speedy = 0
    #     player_mov.rect.bottom = 560
    #     pos_p['m_y'] = 0
    #     pos_p['c_y'] = 0
    #     pos_m['y'] = -1 
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0


       

        if pos_m['x'] == 4000 or pos_m['x'] == 1290:
            if pos_m['x'] == 1290:
                pos_p['c_x'] = 1
            if pos_m['x'] == 4000:
                pos_p['c_x'] = 0
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    player_mov.speedx -= 8
                    pos_p['m_x'] = 1
                if event.key == pygame.K_RIGHT:
                    player_mov.speedx += 8
                    pos_p['m_x'] = 1
                if event.key == pygame.K_UP:
                    mapa_mov.speedy += 10

                if event.key == pygame.K_DOWN:
                    mapa_mov.speedy -= 10
                

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT and pos_p['m_x'] == 1:
                    player_mov.speedx += 8
                    pos_p['m_x'] = 0
                if event.key == pygame.K_RIGHT and pos_p['m_x'] == 1:
                    player_mov.speedx -= 8 
                    pos_p['m_x'] = 0
                if event.key == pygame.K_UP:
                        mapa_mov.speedy -= 10

                if event.key == pygame.K_DOWN:
                    mapa_mov.speedy += 10
            
        

###############################################################################################################        
        if pos_m['y'] == 0 or pos_m['y'] == -1280:
            if pos_m['y'] == 0:
                pos_p['c_y'] = 1
            if pos_m['y'] == -1280:
                pos_p['c_y'] = 0

            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx += 10
                    
                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx -= 10
                    
                if event.key == pygame.K_UP:
                    player_mov.speedy -= 8
                    pos_p['m_y'] = 1
                if event.key == pygame.K_DOWN:
                    player_mov.speedy += 8
                    pos_p['m_y'] = 1

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_UP and pos_p['m_y'] == 1:
                    player_mov.speedy += 8
                    pos_p['m_y'] == 0
                if event.key == pygame.K_DOWN and pos_p['m_y'] == 1:
                    player_mov.speedy -= 8 
                    pos_p['m_y'] == 0
                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx -= 10
                 
                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx += 10
                  
################################################################################################################        
        if pos_p['x'] == 520:
            if pos_p['c_x'] == 0 :
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_LEFT:
                        mapa_mov.speedx += 10
                        #player_mov.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        mapa_mov.speedx -= 10

                    
        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        mapa_mov.speedx -= 10
                        
                    if event.key == pygame.K_RIGHT:
                        mapa_mov.speedx += 10
                            
                        
            if pos_p['c_y'] == 0: 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_UP:
                        mapa_mov.speedy += 10

                    if event.key == pygame.K_DOWN:
                        mapa_mov.speedy -= 10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mapa_mov.speedy -= 10

                    if event.key == pygame.K_DOWN:
                        mapa_mov.speedy += 10
    #print(mapa_mov.speedx)
    print(pos_p)
    #print(p_p_x)
    #print(pm_x)
    all_sprites.update()
    #print(mapa_mov.speedy)
    #print(mov_px, mov_py)
    
    
    window.fill(PRETO)
    
    all_sprites.draw(window)
    #window.blit(player_img, (520,360))
    pygame.display.update()
    
pygame.quit()
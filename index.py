import pygame
from config import *
from assets import *
from classes import *
import assets
from init_screen import *
from tela_final import *
from won_screen import *
pygame.mixer.init()
pygame.mixer.music.load(intro_m)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops = True)

effect = pygame.mixer.Sound(beber_sound)
effect_2 = pygame.mixer.Sound(pick_sound)

def game_screen(window):

    #Velocidade
    velocidade_i = 25

    #contador
    conta = 0
    conta_2 = 0

    #Vida
    lives = 3
    game = 1
    fase = 1
    current_time = 0 
    time = 30*1000
    #conversor para imagem vetorizada
    mapa_img.convert()
    player_img.convert()
    gota_img.convert()
    madeira_img.convert()
    poça_img.convert()
    casa = casa_img.convert()


    #escala na tela
    madeira_img_2 = pygame.transform.scale(madeira_img, (40, 40))
    pedra_img_2 = pygame.transform.scale(pedra_img, (40, 40))




    #criação de grupos de sprites
    all_sprites = pygame.sprite.Group()
    all_pedras = pygame.sprite.Group()
    all_madeira = pygame.sprite.Group()
    all_poça = pygame.sprite.Group()
    all_gotas = pygame.sprite.Group()



    #Declarando objetos
    mapa_mov = Mapa(mapa_img)
    player_mov = Player(player_imgs)



    all_sprites.add(mapa_mov)
    all_sprites.add(player_mov)




    #velocidades dos objetos
    velocidade = velocidade_i
    velocidade_x = velocidade_i
    velocidade_y = velocidade_i
    velocidade_items_x = velocidade_i
    velocidade_items_y = velocidade_i



    #Gerando madeiras no mapa
    for m in range(35):
        madeira = Madeira(madeira_img)
        all_madeira.add(madeira)


    #Gerando pedras no mapa
    for f in range(35):
        pedrita = Pedra(pedra_img)
        all_pedras.add(pedrita)


    for p in range(2):
        poça_mov = Poça(poça_img)
        all_poça.add(poça_mov)
    #Chuva

    game = 1
    while game == 1:

        for i in range(10): 
            gota_c = Gota(gota_img)
            all_gotas.add(gota_c)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = 0

            #[Movimenta o mapa]
            if event.type == pygame.KEYDOWN:
                velocidade_x = velocidade_i

                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx += velocidade_x
                    player_mov.speedx = mapa_mov.speedx
    
                    for madeira in all_madeira:
                        madeira.speedx += velocidade_items_x
                    for pedra in all_pedras:
                        pedra.speedx += velocidade_items_x
                    for poça in all_poça:
                        poça.speedx += velocidade_items_x

                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx -= velocidade_x
                    player_mov.speedx = mapa_mov.speedx
                    for madeira in all_madeira:
                        madeira.speedx -= velocidade_items_x
                    for pedra in all_pedras:
                        pedra.speedx -= velocidade_items_x
                    for poça in all_poça:
                        poça.speedx -= velocidade_items_x

            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_LEFT:
                    mapa_mov.speedx -= velocidade_x
                    player_mov.speedx = mapa_mov.speedx
                    for madeira in all_madeira:
                        madeira.speedx -= velocidade_items_x
                    for pedra in all_pedras:
                        pedra.speedx -= velocidade_items_x
                    for poça in all_poça:
                        poça.speedx -= velocidade_items_x

                if event.key == pygame.K_RIGHT:
                    mapa_mov.speedx += velocidade_x
                    player_mov.speedx = mapa_mov.speedx
                    for madeira in all_madeira:
                        madeira.speedx += velocidade_items_x
                    for pedra in all_pedras:
                        pedra.speedx += velocidade_items_x
                    for poça in all_poça:
                        poça.speedx += velocidade_items_x


            if event.type == pygame.KEYDOWN: 
                velocidade_y = velocidade_i
                       
                if event.key == pygame.K_UP:
                    mapa_mov.speedy += velocidade_y
                    player_mov.speedy = mapa_mov.speedy  
                    for madeira in all_madeira:
                        madeira.speedy += velocidade_items_y
                    for pedra in all_pedras:
                        pedra.speedy += velocidade_items_y
                    for poça in all_poça:
                        poça.speedy += velocidade_items_y

                if event.key == pygame.K_DOWN:
                    
                    mapa_mov.speedy -= velocidade_y
                    player_mov.speedy = mapa_mov.speedy  
                    for madeira in all_madeira:
                        madeira.speedy -= velocidade_items_y
                    for pedra in all_pedras:
                        pedra.speedy -= velocidade_items_y
                    for poça in all_poça:
                        poça.speedy -= velocidade_items_y

            if event.type == pygame.KEYUP: 
                
                if event.key == pygame.K_UP:
                    mapa_mov.speedy -= velocidade_y
                    player_mov.speedy = mapa_mov.speedy
                    for madeira in all_madeira:
                        madeira.speedy -= velocidade_items_y
                    for pedra in all_pedras:
                        pedra.speedy -= velocidade_items_y
                    for poça in all_poça:
                        poça.speedy -= velocidade_items_y

                if event.key == pygame.K_DOWN:
                    mapa_mov.speedy += velocidade_y
                    player_mov.speedy = mapa_mov.speedy  
                    for madeira in all_madeira:
                        madeira.speedy += velocidade_items_y
                    for pedra in all_pedras:
                        pedra.speedy += velocidade_items_y
                    for poça in all_poça:
                        poça.speedy += velocidade_items_y


        
        colisao_madeira = pygame.sprite.spritecollide(player_mov, all_madeira, True)
        for madeira in colisao_madeira:
            effect_2.play()
            conta += len(colisao_madeira)
            if conta > 30:
                conta = 30
        
        
        colisao_pedra = pygame.sprite.spritecollide(player_mov, all_pedras, True)
        for colis in colisao_pedra:
            effect_2.play()
            conta_2 += len(colisao_pedra)
            if conta_2 >30:
                conta_2 = 30 

        colisao_poça = pygame.sprite.spritecollide(player_mov, all_poça, True)
        for poca in colisao_poça:
            lives+= len(colisao_poça)
            effect.play()


        all_sprites.update()
        all_madeira.update()
        all_pedras.update()
        all_poça.update()
        all_gotas.update()
        
        #tempo
        clock.tick(30)
        
        current_time = pygame.time.get_ticks()
        if current_time > time:
            time = 2*time
            lives -= 1

        window.fill(PRETO)
        
        all_sprites.draw(window)
        all_pedras.draw(window)
        all_madeira.draw(window)
        all_gotas.draw(window)
        all_poça.draw(window)

        #Sanidade
        if lives <= 5:
            window.blit(visao_img_1,(-80,0))
        if lives == 2:
            window.blit(visao_img_2,(-80,0))
        if lives == 1:
            window.blit(visao_img_3,(-100,0))
        # if lives == 7:
        #     window.blit(casa_img,(520,560))


        if conta >= 30 and conta_2 >=30:
            lives = 7
            window.blit(casa,(520,560))
            return WIN
        window.blit(madeira_img_2,(20,680))
        window.blit(pedra_img_2,(150,680))
        #colocar tela de ganho



        #madeira
        text_surface = font_img.render("{:02d}".format(conta), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (100, 690)
        window.blit(text_surface, text_rect)

        #pedra
        text_surface = font_img.render("{:02d}".format(conta_2), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (220, 690)
        window.blit(text_surface, text_rect)
        
        #vida
        text_surface = font_img.render(chr(9829) * lives, True, (110, 30, 120))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (1200, 690)
        window.blit(text_surface, text_rect)

    #colocar tela de game over + agradecimentos
        if lives == 0:
            game = 0
        pygame.display.update()
    return TELAFINAL

pygame.init()
pygame.font.init()
window = pygame.display.set_mode((x_size, y_size))
pygame.display.set_caption('Raining Day')

clock = pygame.time.Clock() 

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == TELAFINAL:
        state = tela_final(window)
    elif state == WIN:
        state = won_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados



import pygame
from assets import * 
from config import *
def tela_instrucoes(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    running = True
    while running:
            # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        font = pygame.font.SysFont('Algerian', 80)
        font2 = pygame.font.SysFont('Cooperplate Gothic Bold', 40)
        text2 = font2.render("Pressione qualquer tecla para finalizar ou pressione 'Q' para recomeçar", False, (0, 0, 0)) 
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    state = GAME
                    return GAME
                else:
                    state = DONE
                    running = False
                    pygame.quit() 
        # A cada loop, redesenha o fundo e os sprites
        window.fill((255, 255, 255))
        window.blit(instrucoes_img, (0, 0))
        
        
        window.blit(text2, ((180), (10)))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return QUIT

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *

pygame.init()
pygame.mixer.init()

import pygame
# from index import *
from config import *
from init_screen import * 


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((x_size, y_size))
pygame.display.set_caption('Raining Day')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = index(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utiliz


#         if state == TELAGANHADOR:
#             for event in pygame.event.get():
#                 # Verifica se foi fechado.
#                 if event.type == pygame.QUIT:
#                     state = DONE
#                 if event.type == pygame.KEYUP:
#                     # Dependendo da tecla, altera o estado do jogador.
#                     if event.key == pygame.K_ESCAPE:
#                         state = DONE
#                     if event.key == ord('r'): #
#                         window.fill((255, 255, 255))
#                         return INICIO

#             window.fill((255, 255, 255))
#             window.blit(assets[BGGANHADOR], (0, 0))
#             pygame.display.flip()


#         if state == TELAFINAL:
#             font3 = pygame.font.SysFont('Algerian', 100)
#             text3 = font3.render("GAME OVER", False, (255, 255, 255))
#             font4 = pygame.font.SysFont('Cooperplate Gothic Bold', 40)
#             text4 = font4.render("Pressione a tecla 'R' para retornar ao inicio do jogo.", False, (255, 255, 255))
#             # Processa os eventos (mouse, teclado, botão, etc).
#             for event in pygame.event.get():
#                 # Verifica se foi fechado.
#                 if event.type == pygame.QUIT:
#                     state = DONE
#                 if event.type == pygame.KEYUP:
#                     # Dependendo da tecla, altera o estado do jogador.
#                     if event.key == ord('r'): 
#                         window.fill((255, 255, 255))
#                         return INICIO
                        
#             window.fill((255, 255, 255))
#             window.blit(assets[GAMEOVER], (0, 0))
#             window.blit(text3, ((LARGURA/2 - 300), (ALTURA/2 - 50)))
#             window.blit(text4, ((LARGURA/2 - 350), (ALTURA/2 + 200)))
#             pygame.display.flip()
# INICIO = 0
# TELAINSTRUCOES = 1
# TELA1 = 2
# TELA2 = 3
# TELA3 = 4
# TELA4 = 5
# TELAFINAL = 6
# TELAGANHADOR = 7  
# DONE = 8
# RESTART = 9
# state = INICIO
# while state != DONE:
#     if state == INICIO:
#         state = game_screen(window)
#         print(f"Reiniciar {state}")
#     else:
#         state = DONE

# # ===== Finalização =====
# pygame.quit()















# # ----- Gera tela principal
# window = pygame.display.set_mode((x_size, y_size))
# pygame.display.set_caption('Raining Day')

# index(window) # Executa a função principal do jogo

# pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


# ----- Gera tela principal
# window = pygame.display.set_mode((x_size, y_size))
# pygame.display.set_caption('Tela Inicial')

# state = INIT
# while state != QUIT:
#     if state == INIT:
#         state = init_screen(window)
#     elif state == GAME:
#         state = game_screen(window)
#     else:
#         state = QUIT

# tela_principal = True 
# while tela_principal:
#         fundo = pygame.image.load('assets/img/init/tela_inicial.png').convert()
#         window.blit(fundo, (0,0))
#         tela_principal=False

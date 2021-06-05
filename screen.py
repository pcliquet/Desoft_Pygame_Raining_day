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

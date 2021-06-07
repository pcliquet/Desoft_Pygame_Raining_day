# if state == TELAFINAL:
    #         font3 = pygame.font.SysFont('Algerian', 100)
    #         text3 = font3.render("GAME OVER", False, (255, 255, 255))
    #         font4 = pygame.font.SysFont('Cooperplate Gothic Bold', 40)
    #         text4 = font4.render("Pressione a tecla 'R' para retornar ao inicio do jogo.", False, (255, 255, 255))
    #         # Processa os eventos (mouse, teclado, botão, etc).
    #         for event in pygame.event.get():
    #             # Verifica se foi fechado.
    #             if event.type == pygame.QUIT:
    #                 state = DONE
    #             if event.type == pygame.KEYUP:
    #                 # Dependendo da tecla, altera o estado do jogador.
    #                 if event.key == ord('r'): 
    #                     window.fill((255, 255, 255))
    #             return INIT
                        
    #         window.fill((255, 255, 255))
    #         window.blit(assets[lose_img], (0, 0))
    #         window.blit(text3, ((x_size/2 - 300), (y_size/2 - 50)))
    #         window.blit(text4, ((x_size/2 - 350), (y_size/2 + 200)))
    #         pygame.display.flip()
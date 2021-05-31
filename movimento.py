if event.type == pygame.KEYDOWN:
            

            #Movimento para esquerda
            if event.key == pygame.K_LEFT:

                if mapa_mov.rect.right == 4000:
                    mapa_mov.speedx = 0
                    pm_x = 1
               
                else:
                    mapa_mov.speedx += 10

                if mapa_mov.rect.right == 4000 and pm_x == 1:
                    player_mov.speedx -= 5
                    mapa_mov.speedx = 0
                
                

            #movimento para direita
            elif event.key == pygame.K_RIGHT:
                
                if mapa_mov.rect.left == -2710:
                    mapa_mov.speedx = 0
                    pm_x = 1
                else:
                    mapa_mov.speedx -= 10
                    
                if mapa_mov.rect.left == -2710 and pm_x == 1:
                    player_mov.speedx += 5

            #movimento para cima
            elif event.key == pygame.K_UP:
                if mapa_mov.rect.top == 0:
                    mapa_mov.speedy = 0
                else:
                    mapa_mov.speedy += 10



            #Movimento para baixo
            elif event.key == pygame.K_DOWN:
                if mapa_mov.rect.bottom == 720:
                    mapa_mov.speedy = 0
                else:
                    mapa_mov.speedy -= 10
    



        if event.type == pygame.KEYUP:
       
            #Movimento para esquerda
            if event.key == pygame.K_LEFT:

                if mapa_mov.rect.right >= 3980:
                    mapa_mov.speedx = 0

                elif mapa_mov.rect.right >= 3990 and pm_x == 1:
                    player_mov.speedx += 5

                else:
                    mapa_mov.speedx -= 10
                    

            #Movimento para direita
            if event.key == pygame.K_RIGHT:

                if mapa_mov.rect.left == -2710:
                    mapa_mov.speedx = 0

                else:
                    mapa_mov.speedx += 10

                if mapa_mov.rect.left == -2710 and pm_x == 1:
                    player_mov.speedx -= 5



            #Movimento para cima
            if event.key == pygame.K_UP:
                if mapa_mov.rect.top == 0:
                    mapa_mov.speedy = 0
                else:
                    mapa_mov.speedy -= 10


            #Movimento para baixo    
            if event.key == pygame.K_DOWN:
                if mapa_mov.rect.bottom == 720:
                    mapa_mov.speedy = 0
                else:
                    mapa_mov.speedy += 10
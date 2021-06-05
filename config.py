from os import path
#Tamanho da tela
x_size = 1290   
y_size = 720
mp_sizex = 2580
mp_sizey = 1440


#Estatus do jogo
game = 1
fase = 1


#Fill
PRETO = (0, 0, 0)


p_p_x = 0
p_p_y = 0
p_m_x = 1
p_m_y = 1


#tela 
FPS = 60 
INIT = 0
GAME = 1
QUIT = 2

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'telas')
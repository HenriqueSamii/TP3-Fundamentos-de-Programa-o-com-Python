#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)
import pygame

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

def circulo_azul():
    posicaoX = larguraTela//2
    posicaoY = alturaTela//2
    diametro = 100
    pygame.draw.circle(tela, BLUE, [posicaoX, posicaoY], diametro//2)


treminou = False

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            treminou = True
    

    pygame.display.update()

    tela.fill(BLACK)
    circulo_azul()

    clock.tick(50)

pygame.display.quit()
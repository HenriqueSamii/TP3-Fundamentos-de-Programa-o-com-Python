#Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios a cada vez que o usuário clicar na tela.
#  A ponta superior da estrela deve estar situada onde o usuário clicou. (código e printscreen)
import pygame
from random import randint

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

def estrela(X=0,Y=0, tamanho = 100):
    alturaTopo = 0
    alturaMedio = tamanho
    alturaFuno = 2.4*tamanho
    pygame.draw.polygon(tela, WHITE, [[tamanho*1.50+X, alturaTopo+Y], [tamanho*2+X, alturaMedio+Y], [tamanho*3+X, alturaMedio+Y], [tamanho*2.2+X, tamanho*1.5+Y], [tamanho*3+X, alturaFuno+Y], [tamanho*1.5+X, tamanho*1.6+Y], [0+X, alturaFuno+Y], [tamanho*0.8+X, tamanho*1.5+Y],[0+X, alturaMedio+Y], [tamanho+X, alturaMedio+Y]], 0)


treminou = False

posicaoX = larguraTela//2-150
posicaoY = alturaTela//2-150
tamanhoEstrela = 100

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicaoClickada = pygame.mouse.get_pos()
            tamanhoEstrela =randint(10, 100)
            posicaoX = posicaoClickada[0]-tamanhoEstrela*1.50
            posicaoY = posicaoClickada[1]
            #tamanhoEstrela =randint(10, 100)
        if event.type == pygame.QUIT:
            treminou = True
    

    pygame.display.update()
    clock.tick(50)
    
    tela.fill(BLACK)
    estrela(posicaoX,posicaoY,tamanhoEstrela)

pygame.display.quit()
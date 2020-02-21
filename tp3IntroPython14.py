#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro da tela.
#  Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada. (código e printscreen)
import pygame

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

tamanho = 50

def quadrado(X,Y):
    pygame.draw.rect(tela, WHITE, [X, Y, tamanho,tamanho])


treminou = False

posicaoX = larguraTela//2-tamanho//2
posicaoY = alturaTela//2-tamanho//2

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicaoClickada = pygame.mouse.get_pos()
            posicaoX = posicaoClickada[0]
            posicaoY = posicaoClickada[1]
        if event.type == pygame.QUIT:
            treminou = True
    

    pygame.display.update()
    clock.tick(50)
    
    tela.fill(BLACK)
    quadrado(posicaoX,posicaoY)

pygame.display.quit()
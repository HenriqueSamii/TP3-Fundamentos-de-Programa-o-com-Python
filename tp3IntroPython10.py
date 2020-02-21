#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
#  O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
import pygame

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

tamanho = 100
distanciaMovimento = 5

def quadrado_vermelho(X,Y):
    pygame.draw.rect(tela, RED, [X, Y, tamanho,tamanho])


treminou = False

posicaoX = larguraTela//2-tamanho//2
posicaoY = alturaTela//2-tamanho//2

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
                if posicaoX >=larguraTela-100:
                    pass
                else:
                    posicaoX += distanciaMovimento
            elif event.key == pygame.K_LEFT or event.key ==pygame.K_a:
                if posicaoX<=0:
                    pass
                else:
                    posicaoX -=distanciaMovimento
            elif event.key == pygame.K_UP or event.key ==pygame.K_w:
                if posicaoY<=0:
                    pass
                else:
                    posicaoY -=distanciaMovimento
            elif event.key == pygame.K_DOWN or event.key ==pygame.K_s:
                if posicaoY >=alturaTela-100:
                    pass
                else:
                    posicaoY +=distanciaMovimento
        if event.type == pygame.QUIT:
            treminou = True
    

    pygame.display.update()

    tela.fill(BLACK)
    quadrado_vermelho(posicaoX,posicaoY)

    clock.tick(50)

pygame.display.quit()
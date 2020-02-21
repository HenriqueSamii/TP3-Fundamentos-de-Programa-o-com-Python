#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo verde de 100 px de diâmetro no centro da tela que se inicie o movimento da esquerda para a direita.
#  Sempre que chegar em alguma extremidade, o círculo deve trocar a direção e aumentar a velocidade em 1. (código e printscreen)
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

tamanho = 100//2
distanciaMovimento = 10

def circulo_azul(X,Y):
    pygame.draw.circle(tela, GREEN, [X, Y], tamanho)


treminou = False

posicaoX = larguraTela//2
posicaoY = alturaTela//2

movimento = True
velocidade = 10

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
                movimento = True
            elif event.key == pygame.K_LEFT or event.key ==pygame.K_a:
                movimento = False
            elif event.key == pygame.K_UP or event.key ==pygame.K_w:
                if posicaoY<=tamanho:
                    pass
                else:
                    posicaoY -=distanciaMovimento
            elif event.key == pygame.K_DOWN or event.key ==pygame.K_s:
                if posicaoY >= alturaTela-tamanho:
                    pass
                else:
                    posicaoY +=distanciaMovimento
        if event.type == pygame.QUIT:
            treminou = True
    

    pygame.display.update()
    clock.tick(50)

    if movimento == True:
        posicaoX +=velocidade
    elif movimento ==False:
        posicaoX -=velocidade

    tela.fill(BLACK)
    if posicaoX <= tamanho:
        velocidade +=1
        movimento =True
    elif posicaoX >= larguraTela-tamanho:
        velocidade +=1
        movimento =False
    print(velocidade)
    circulo_azul(posicaoX,posicaoY)

pygame.display.quit()
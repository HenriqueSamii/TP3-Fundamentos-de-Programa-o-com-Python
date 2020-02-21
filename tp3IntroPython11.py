#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela que se move da esquerda para a direita.
#  Sempre que chegar na extremidade direita, o círculo deve voltar à extremidade esquerda, retomando o movimento da esquerda para a direita. (código e printscreen)
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

tamanho = 100//2
distanciaMovimento = 10

def circulo_azul(X,Y):
    pygame.draw.circle(tela, BLUE, [X, Y], tamanho)


treminou = False

posicaoX = larguraTela//2
posicaoY = alturaTela//2

while not treminou:
    #Capturar Eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key ==pygame.K_d:
                posicaoX += distanciaMovimento
            elif event.key == pygame.K_LEFT or event.key ==pygame.K_a:
                posicaoX -=distanciaMovimento
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

    tela.fill(BLACK)
    if posicaoX < tamanho:
        circulo_azul(larguraTela+posicaoX,posicaoY)
        circulo_azul(posicaoX,posicaoY)
        if posicaoX<=-tamanho:
            posicaoX = larguraTela-tamanho
    elif posicaoX > alturaTela-tamanho:
        circulo_azul(posicaoX,posicaoY)
        circulo_azul(posicaoX-larguraTela,posicaoY)
        if posicaoX>=larguraTela+tamanho:
            posicaoX = 0+tamanho
    else:
        circulo_azul(posicaoX,posicaoY)

    clock.tick(50)

pygame.display.quit()
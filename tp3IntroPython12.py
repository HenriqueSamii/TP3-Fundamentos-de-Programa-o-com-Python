#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo amarelo de 100 px de diâmetro no centro da tela que se move sempre em
#  velocidade permanente na direção que o usuário indicar através das teclas.
#  Similar ao item anterior, sempre que chegar em uma extremidade, o círculo deve voltar à extremidade oposta e continuar o com a última direção que o usuário indicou. (código e printscreen)
import pygame

larguraTela = 800
alturaTela = 600

tela  = pygame.display.set_mode([larguraTela,alturaTela])

pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

tamanho = 100//2
distanciaMovimento = 10

def circulo_azul(X,Y):
    pygame.draw.circle(tela, YELLOW, [X, Y], tamanho)


treminou = False

posicaoX = larguraTela//2
posicaoY = alturaTela//2

movimento = "Movimento vai ser alterado para True ou False"
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

pygame.display.quit()
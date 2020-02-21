#Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação. Tal modificação consiste em incluir o aumento da velocidade da bola.
#  O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)
import pygame, random
#constantes
LARGURA_TELA  = 400
ALTURA_TELA   = 300
FPS           = 200
LARGURA_LINHA = 10
PALETA_TAMANHO= 50
PALETA_OFFSET = 20
#cores
PRETO  = (0,0,0)
BRANCO = (255,255,255)

global placar
placar = 0

def desenha_arena():
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, ((0,0), (LARGURA_TELA, ALTURA_TELA)), LARGURA_LINHA * 2)
    pygame.draw.line(tela, BRANCO, ((LARGURA_TELA/2),0), ((LARGURA_TELA/2), ALTURA_TELA), (LARGURA_LINHA // 4))

def desenha_bola(bola): #espera um rect
    pygame.draw.rect(tela, BRANCO, bola)

def desenha_paleta(paleta): #espera um rect
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA: #trava embaixo
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    elif paleta.top < LARGURA_LINHA: #trava em cima
        paleta.top = LARGURA_LINHA
    pygame.draw.rect(tela, BRANCO, paleta)

def move_bola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX
    bola.y += bolaDirY
    return bola

def verifica_colisao(bola, bolaDirX, bolaDirY):
    global placar
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
        if bola.right == (LARGURA_TELA - LARGURA_LINHA):
            placar += 100
        if bola.left == (LARGURA_LINHA):
            placar -= 100
        
    return bolaDirX, bolaDirY

def cpu(bola, bolaDirX, paleta2):
    
    nao_jogar = random.randint(0,3)

    if bolaDirX == 1 and nao_jogar != 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -= 1
    return paleta2

def imprime_placar(placar):
    font = pygame.font.SysFont('Arial',24)
    text = font.render('Placar:'+str(placar),1, BRANCO)
    tela.blit(text, (LARGURA_LINHA,LARGURA_LINHA))

def verifica_colisao_bola(bola, paleta1, paleta2, bolaDirX):
    global placar
    #jogador acertou
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        placar -= 1
        return -1
    else:
        return 1

def main():
    #motores
    pygame.init()
    #gerando a tela
    global tela
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    #gerando o clock
    FPS_CLOCK = pygame.time.Clock()
    #loop do jogo
    
    #posicoes iniciais
    bolaX = LARGURA_TELA // 2 - LARGURA_LINHA // 2
    bolaY = ALTURA_TELA // 2 - LARGURA_LINHA // 2
    jogadorUm_posicao   = (ALTURA_TELA - PALETA_TAMANHO) // 2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) // 2
    
    #alterar a posicao da bola
    bolaDirX = -1
    bolaDirY = -1
    
    #criando os rects
    paleta1 = pygame.Rect(PALETA_OFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETA_OFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    bola    = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA) 
    #desenho das pos. iniciais
    desenha_arena()
    desenha_paleta(paleta1)
    desenha_paleta(paleta2)
    desenha_bola(bola)
    
    terminou = False
    while not terminou:        
        
        #refresh no desenho
        pygame.display.update()
        
        desenha_arena()
        desenha_paleta(paleta1)
        desenha_paleta(paleta2)
        desenha_bola(bola)
        
        bola = move_bola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verifica_colisao(bola, bolaDirX, bolaDirY)
        paleta2 = cpu(bola, bolaDirX, paleta2)
        bolaDirX = bolaDirX * verifica_colisao_bola(bola, paleta1, paleta2, bolaDirX)
        
        if bolaDirX <= -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
            if bolaDirX < 0:
                bolaDirX -= 1
            else:
                bolaDirX += 1
            if bolaDirY < 0:
                bolaDirY -= 1
            else:
                bolaDirY += 1
            print(bolaDirX)
            print(bolaDirY)
        #if bola.colliderect(paleta1) or bola.colliderect(paleta2) :
        #    bolaDirX = bolaDirX * -1
        #print(bola)
        
        imprime_placar(placar)
        
        #checar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.MOUSEMOTION:
                mouseX, mouseY = event.pos
                paleta1.y = mouseY
                
        #setar framerate
        FPS_CLOCK.tick(FPS)

    pygame.display.quit()
    pygame.quit()

if __name__ == '__main__':
    main()
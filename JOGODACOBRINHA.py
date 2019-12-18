import pygame
from random import randrange


# definição de cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

pygame.init()

# definindo a dimensão da tela de exibição
largura = 320
altura = 240
# criação da cobrinha
tamanho = 10
#FPS
relogio = pygame.time.Clock()

# criando a tela de exibição
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO DA COBRINHA')
# inserindo texto
font = pygame.font.SysFont(None, 15)

def texto(msg,cor):
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [largura/10, altura/2])

# definindo funções
def cobra (CobraXY):
    for XY in CobraXY:
    # desenhando a cobrinha
        pygame.draw.rect(tela, verde, [XY[0], XY[1], tamanho, tamanho])
    # desenhando a maçã
def maca(pos_x, pos_y):
        pygame.draw.rect(tela, vermelho, [pos_x, pos_y, tamanho, tamanho])

def jogo():
    # criando o loop que ao clicar no 'x' da tela, faz fechar o jogo
    sair = True
    # definindo fim de jogo
    fimdejogo = False
    # definindo as posições
    pos_x =randrange(0,largura-tamanho,10)
    pos_y =randrange(0,altura-tamanho,10)
    maca_x =randrange(0,largura-tamanho,10)
    maca_y =randrange(0,altura-tamanho,10)
    # definindo a velocidade
    velocidade_x=0
    velocidade_y=0
    # definindo corescimento e comprimento da cobra
    CobraXY = []
    CobraComp = 1

    while sair:
# definindo as teclas que continuam ou finalizam ou jogo
        while fimdejogo:
            tela.fill(preto)
            texto('Fim de jogo, para continuar tecle C ou S para sair', branco)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sair = False
                   fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()

                    if event.key == pygame.K_s:
                           sair = False 
                           fimdejogo = False               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
    # definindo posição e velocidade
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho

        # preenchendo o fundo com preto
        tela.fill((preto))
        # definindo o que o programa deve fazer com a velocidade
        pos_x+=velocidade_x
        pos_y+=velocidade_y

        # cobra comendo a maçã
        if pos_x == maca_x and pos_y == maca_y:
            maca_x =randrange(0,largura-tamanho,10)
            maca_y =randrange(0,altura-tamanho,10)
            CobraComp += 1

        # bordas
        if pos_x > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x= largura-tamanho
        if pos_y > altura:
            pos_y = 0
        if pos_y < 0:
            pos_y= altura-tamanho

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True

        # chamando função cobra
        cobra(CobraXY)
 
        # chamando a função maçã
        maca(maca_x, maca_y)
        pygame.display.update()
        pygame.display.flip()
        relogio.tick(15)
        
# chamando função jogo       
jogo ()
pygame.quit()

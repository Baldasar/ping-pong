import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Ping Pong")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (200, 200, 200)

# FPS
clock = pygame.time.Clock()
fps = 60

# Posição e tamanho das barras dos jogadores
largura_barra = 10
altura_barra = 100
posicao_barra_jogador1 = [30, altura_tela // 2 - altura_barra // 2]
posicao_barra_jogador2 = [largura_tela - largura_barra - 30, altura_tela // 2 - altura_barra // 2]
velocidade_barra = 10

# Bola
tamanho_bola = 10
posicao_bola = [largura_tela // 2, altura_tela // 2]
velocidade_bola = [random.choice([-4, 4]), random.choice([-4, 4])]

# Variáveis do jogo
pontuacao_jogador1 = 0
pontuacao_jogador2 = 0
geracao = 1
bolas = 1
rodando = True

# Fonte para o texto
fonte = pygame.font.Font(None, 36)

# Função para exibir o texto
def exibir_texto(texto, x, y):
    superficie_texto = fonte.render(texto, True, branco)
    tela.blit(superficie_texto, (x, y))

# Função para desenhar a linha pontilhada no meio
def linha_pontilhada():
    for y in range(0, altura_tela, 20):  # Desenha segmentos pontilhados
        pygame.draw.line(tela, branco, (largura_tela // 2, y), (largura_tela // 2, y + 10), 2)

# Loop do jogo
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação das barras
    teclas = pygame.key.get_pressed()

    # Jogador 1 (barra à esquerda)
    if teclas[pygame.K_w] and posicao_barra_jogador1[1] > 0:
        posicao_barra_jogador1[1] -= velocidade_barra
    if teclas[pygame.K_s] and posicao_barra_jogador1[1] < altura_tela - altura_barra:
        posicao_barra_jogador1[1] += velocidade_barra

    # Jogador 2 (barra à direita)
    if teclas[pygame.K_UP] and posicao_barra_jogador2[1] > 0:
        posicao_barra_jogador2[1] -= velocidade_barra
    if teclas[pygame.K_DOWN] and posicao_barra_jogador2[1] < altura_tela - altura_barra:
        posicao_barra_jogador2[1] += velocidade_barra

    # Movimentação da bola
    posicao_bola[0] += velocidade_bola[0]
    posicao_bola[1] += velocidade_bola[1]

    # Colisão com as paredes
    if posicao_bola[0] <= 0 or posicao_bola[0] >= largura_tela - tamanho_bola:
        velocidade_bola[0] = -velocidade_bola[0]
    if posicao_bola[1] <= 0 or posicao_bola[1] >= altura_tela - tamanho_bola:
        velocidade_bola[1] = -velocidade_bola[1]

    # Colisão com as barras
    if (
        posicao_barra_jogador1[1] <= posicao_bola[1] + tamanho_bola <= posicao_barra_jogador1[1] + altura_barra
        and posicao_barra_jogador1[0] <= posicao_bola[0] <= posicao_barra_jogador1[0] + largura_barra
    ):
        velocidade_bola[0] = -velocidade_bola[0]
        pontuacao_jogador1 += 1  # Incrementa a pontuação do jogador 1

    if (
        posicao_barra_jogador2[1] <= posicao_bola[1] + tamanho_bola <= posicao_barra_jogador2[1] + altura_barra
        and posicao_barra_jogador2[0] <= posicao_bola[0] <= posicao_barra_jogador2[0] + largura_barra
    ):
        velocidade_bola[0] = -velocidade_bola[0]
        pontuacao_jogador2 += 1  # Incrementa a pontuação do jogador 2

    # Caso a bola passe da barra (um dos jogadores perde)
    if posicao_bola[0] < 0:  # Jogador 2 ganha ponto
        pontuacao_jogador2 += 1
        posicao_bola = [largura_tela // 2, altura_tela // 2]
        velocidade_bola = [random.choice([-4, 4]), random.choice([-4, 4])]

    if posicao_bola[0] > largura_tela:  # Jogador 1 ganha ponto
        pontuacao_jogador1 += 1
        posicao_bola = [largura_tela // 2, altura_tela // 2]
        velocidade_bola = [random.choice([-4, 4]), random.choice([-4, 4])]

    # Atualização da tela
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (*posicao_barra_jogador1, largura_barra, altura_barra))
    pygame.draw.rect(tela, branco, (*posicao_barra_jogador2, largura_barra, altura_barra))
    pygame.draw.ellipse(tela, cinza, (*posicao_bola, tamanho_bola, tamanho_bola))

    # Desenhar a linha pontilhada no meio
    linha_pontilhada()

    # Exibir a pontuação centralizada
    exibir_texto(str(pontuacao_jogador1), largura_tela * 0.25 - fonte.size(str(pontuacao_jogador1))[0] // 2, 10)
    exibir_texto(str(pontuacao_jogador2), largura_tela * 0.75 - fonte.size(str(pontuacao_jogador2))[0] // 2, 10)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

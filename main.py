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

# Posição e tamanho do jogador
largura_barra = 100
altura_barra = 10
posicao_barra = [largura_tela // 2 - largura_barra // 2, altura_tela - 20]
velocidade_barra = 10

# Bola
tamanho_bola = 10
posicao_bola = [largura_tela // 2, altura_tela // 2]
velocidade_bola = [random.choice([-4, 4]), random.choice([-4, 4])]

# Variáveis do jogo
pontuacao = 0
geracao = 1
bolas = 1
rodando = True

# Fonte para o texto
fonte = pygame.font.Font(None, 36)

# Função para exibir o texto
def exibir_texto(texto, x, y):
    superficie_texto = fonte.render(texto, True, branco)
    tela.blit(superficie_texto, (x, y))

# Loop do jogo
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação da barra
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and posicao_barra[0] > 0:
        posicao_barra[0] -= velocidade_barra
    if teclas[pygame.K_RIGHT] and posicao_barra[0] < largura_tela - largura_barra:
        posicao_barra[0] += velocidade_barra

    # Movimentação da bola
    posicao_bola[0] += velocidade_bola[0]
    posicao_bola[1] += velocidade_bola[1]

    # Colisão com as paredes
    if posicao_bola[0] <= 0 or posicao_bola[0] >= largura_tela - tamanho_bola:
        velocidade_bola[0] = -velocidade_bola[0]
    if posicao_bola[1] <= 0:
        velocidade_bola[1] = -velocidade_bola[1]

    # Colisão com a barra
    if (
        posicao_barra[1] <= posicao_bola[1] + tamanho_bola <= posicao_barra[1] + altura_barra
        and posicao_barra[0] <= posicao_bola[0] <= posicao_barra[0] + largura_barra
    ):
        velocidade_bola[1] = -velocidade_bola[1]
        pontuacao += 1  # Incrementa a pontuação ao acertar a barra

    # Caso a bola passe da barra (o jogador perde)
    if posicao_bola[1] > altura_tela:
        bolas += 1  # Incrementa o número de bolas perdidas
        pontuacao = 0  # Reseta o score ao perder
        geracao += 1  # Incrementa a geração
        
        # Reseta a posição da bola para o centro
        posicao_bola = [largura_tela // 2, altura_tela // 2]
        
        # Reseta a velocidade da bola
        velocidade_bola = [random.choice([-4, 4]), -abs(random.choice([-4, -3, -5]))]

    # Atualização da tela
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (*posicao_barra, largura_barra, altura_barra))
    pygame.draw.ellipse(tela, cinza, (*posicao_bola, tamanho_bola, tamanho_bola))

    # Exibir texto
    exibir_texto(f"Geração: {geracao}, Score: {pontuacao}, Ball: {bolas}", 10, 10)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

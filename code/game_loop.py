import pygame
import random
import sys
from pathlib import Path
from const import *
from drawing import desenhar_cobra, exibir_pontuacao, exibir_fps

CAMINHO_RAIZ = Path(__file__).parent.parent
CAMINHO_ASSETS = CAMINHO_RAIZ / "assets"


def musica_game():
    try:
        pygame.mixer.music.load(CAMINHO_ASSETS / 'musica.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    except pygame.error as e:
        print(f"Não foi possível carregar o arquivo de música do jogo: {e}")


def rodar_jogo(tela, assets):
    pygame.mixer.music.stop()
    musica_game()
    pos_x, pos_y = LARGURA_TELA / 2, ALTURA_TELA / 2
    delta_x, delta_y = TAMANHO_BLOCO, 0
    direcao_atual = 'CIMA'
    corpo_cobra = [[[pos_x, pos_y], direcao_atual]]
    comprimento_cobra = 1
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    relogio = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direcao_atual != 'DIREITA':
                    direcao_atual = 'ESQUERDA'
                elif event.key == pygame.K_d and direcao_atual != 'ESQUERDA':
                    direcao_atual = 'DIREITA'
                elif event.key == pygame.K_w and direcao_atual != 'BAIXO':
                    direcao_atual = 'CIMA'
                elif event.key == pygame.K_s and direcao_atual != 'CIMA':
                    direcao_atual = 'BAIXO'

        if direcao_atual == 'DIREITA':
            delta_x, delta_y = TAMANHO_BLOCO, 0
        elif direcao_atual == 'ESQUERDA':
            delta_x, delta_y = -TAMANHO_BLOCO, 0
        elif direcao_atual == 'CIMA':
            delta_x, delta_y = 0, -TAMANHO_BLOCO
        elif direcao_atual == 'BAIXO':
            delta_x, delta_y = 0, TAMANHO_BLOCO

        pos_x += delta_x
        pos_y += delta_y

        if not (0 <= pos_x < LARGURA_TELA and 0 <= pos_y < ALTURA_TELA) or [pos_x, pos_y] in [p for p, d in
                                                                                              corpo_cobra]:
            assets['som_gameover'].play()
            return {'acao': 'GAME_OVER', 'pontuacao': comprimento_cobra - 1}

        nova_cabeca = [[pos_x, pos_y], direcao_atual]
        corpo_cobra.append(nova_cabeca)
        if len(corpo_cobra) > comprimento_cobra: del corpo_cobra[0]

        if pos_x == comida_x and pos_y == comida_y:
            comprimento_cobra += 1
            assets['som_comida'].play()
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

        tela.fill(PRETO)
        tela.blit(assets['imagem_maca'], (comida_x, comida_y))
        desenhar_cobra(tela, corpo_cobra, assets)
        exibir_pontuacao(tela, comprimento_cobra - 1, assets)
        exibir_fps(tela, relogio.get_fps(), assets)
        pygame.display.update()
        relogio.tick(VELOCIDADE_JOGO)

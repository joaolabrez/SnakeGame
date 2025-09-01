import pygame
import random
import sys
from pathlib import Path
from const import *
from drawing import desenhar_cobra, exibir_pontuacao, exibir_fps, desenhar_pausa

CAMINHO_RAIZ = Path(__file__).parent.parent
CAMINHO_ASSETS = CAMINHO_RAIZ / "assets"


def musica():
    try:
        pygame.mixer.music.load(CAMINHO_ASSETS / 'musica.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    except pygame.error as e:
        print(f"Erro ao carregar musica.wav: {e}")


def rodar_jogo(tela, assets):
    musica()

    pos_x, pos_y = LARGURA_TELA / 2, ALTURA_TELA / 2
    delta_x, delta_y = TAMANHO_BLOCO, 0
    direcao_atual = 'DIREITA'
    corpo_cobra = [[[pos_x, pos_y], direcao_atual]]
    comprimento_cobra = 1
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    relogio = pygame.time.Clock()

    jogo_pausado = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jogo_pausado = not jogo_pausado

                if not jogo_pausado:
                    if event.key == pygame.K_a and direcao_atual != 'DIREITA':
                        direcao_atual = 'ESQUERDA'
                    elif event.key == pygame.K_d and direcao_atual != 'ESQUERDA':
                        direcao_atual = 'DIREITA'
                    elif event.key == pygame.K_w and direcao_atual != 'BAIXO':
                        direcao_atual = 'CIMA'
                    elif event.key == pygame.K_s and direcao_atual != 'CIMA':
                        direcao_atual = 'BAIXO'

        if not jogo_pausado:
            if direcao_atual == 'DIREITA':
                delta_x, delta_y = TAMANHO_BLOCO, 0
            elif direcao_atual == 'ESQUERDA':
                delta_x, delta_y = -TAMANHO_BLOCO, 0
            elif direcao_atual == 'CIMA':
                delta_x, delta_y = 0, -TAMANHO_BLOCO
            elif direcao_atual == 'BAIXO':
                delta_x, delta_y = 0, TAMANHO_BLOCO

            pos_x += delta_x;
            pos_y += delta_y

            if not (0 <= pos_x < LARGURA_TELA and 0 <= pos_y < ALTURA_TELA) or [pos_x, pos_y] in [p for p, d in
                                                                                                  corpo_cobra]:
                assets['som_gameover'].play()
                pygame.mixer.music.stop()  # <-- PARA A MÚSICA AQUI
                return {'acao': 'GAME_OVER', 'pontuacao': comprimento_cobra - 1}

            nova_cabeca = [[pos_x, pos_y], direcao_atual]
            corpo_cobra.append(nova_cabeca)
            if len(corpo_cobra) > comprimento_cobra: del corpo_cobra[0]

            if pos_x == comida_x and pos_y == comida_y:
                comprimento_cobra += 1;
                assets['som_comida'].play()
                comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
                comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

        tela.fill(PRETO)
        tela.blit(assets['imagem_maca'], (comida_x, comida_y))
        desenhar_cobra(tela, corpo_cobra, assets)
        exibir_pontuacao(tela, comprimento_cobra - 1, assets)
        exibir_fps(tela, relogio.get_fps(), assets)

        if jogo_pausado:
            desenhar_pausa(tela, assets)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: pygame.quit(); sys.exit()
                    if event.key == pygame.K_m:
                        pygame.mixer.music.stop()  # <-- PARA A MÚSICA AQUI
                        return {'acao': 'VOLTAR_MENU'}
                    if event.key == pygame.K_ESCAPE: jogo_pausado = False

        pygame.display.update()
        relogio.tick(VELOCIDADE_JOGO)

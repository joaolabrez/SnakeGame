import pygame
import random
import sys
from const import *
from drawing import desenhar_cobra, exibir_pontuacao, exibir_fps, desenhar_pausa


def rodar_jogo(tela, assets):
    pygame.mixer.music.play(loops=-1)

    pos_x, pos_y = LARGURA_TELA / 2, ALTURA_TELA / 2
    delta_x, delta_y = 0, 0
    direcao_atual = 'DIREITA'
    corpo_cobra = [[(pos_x, pos_y), direcao_atual]]
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
                # --- LÓGICA DA MÚSICA E PAUSA ALTERADA AQUI ---
                if event.key == pygame.K_ESCAPE:
                    jogo_pausado = not jogo_pausado
                    if jogo_pausado:
                        pygame.mixer.music.pause()  # Pausa a música
                    else:
                        pygame.mixer.music.unpause()  # Retoma a música

                if jogo_pausado:
                    # 'Q' agora volta para o menu (antes era 'M')
                    if event.key == pygame.K_q:
                        pygame.mixer.music.stop()
                        return {'acao': 'VOLTAR_MENU'}
                    # 'E' agora retoma o jogo (antes era 'ESC')
                    if event.key == pygame.K_e:
                        jogo_pausado = False
                        pygame.mixer.music.unpause()
                else:  # Se o jogo NÃO estiver pausado
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

            pos_x += delta_x
            pos_y += delta_y

            cabeca_pos = (pos_x, pos_y)

            if not (0 <= pos_x < LARGURA_TELA and 0 <= pos_y < ALTURA_TELA) or cabeca_pos in [p for p, d in
                                                                                              corpo_cobra]:
                assets['som_gameover'].play()
                pygame.mixer.music.stop()
                return {'acao': 'GAME_OVER', 'pontuacao': comprimento_cobra - 1}

            nova_cabeca = [cabeca_pos, direcao_atual]
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

        if jogo_pausado:
            desenhar_pausa(tela, assets)

        pygame.display.update()
        relogio.tick(VELOCIDADE_JOGO)
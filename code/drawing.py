import pygame

from const import *

from const import LARGURA_TELA, ALTURA_TELA


def desenhar_cobra(tela, corpo_da_cobra, assets):
    imagens_cobra = assets['imagens_cobra']
    cabeca_pos, cabeca_dir = corpo_da_cobra[-1]
    if cabeca_dir == 'CIMA':
        tela.blit(imagens_cobra['cabeca_cima'], cabeca_pos)
    elif cabeca_dir == 'BAIXO':
        tela.blit(imagens_cobra['cabeca_baixo'], cabeca_pos)
    elif cabeca_dir == 'ESQUERDA':
        tela.blit(imagens_cobra['cabeca_esquerda'], cabeca_pos)
    elif cabeca_dir == 'DIREITA':
        tela.blit(imagens_cobra['cabeca_direita'], cabeca_pos)

    if len(corpo_da_cobra) > 1:
        rabo_pos, rabo_dir = corpo_da_cobra[0]
        prox_pos, prox_dir = corpo_da_cobra[1]
        if prox_pos[1] < rabo_pos[1]:
            tela.blit(imagens_cobra['rabo_baixo'], rabo_pos)
        elif prox_pos[1] > rabo_pos[1]:
            tela.blit(imagens_cobra['rabo_cima'], rabo_pos)
        elif prox_pos[0] < rabo_pos[0]:
            tela.blit(imagens_cobra['rabo_direita'], rabo_pos)
        elif prox_pos[0] > rabo_pos[0]:
            tela.blit(imagens_cobra['rabo_esquerda'], rabo_pos)

    for i in range(1, len(corpo_da_cobra) - 1):
        pos_atual, dir_atual = corpo_da_cobra[i]
        pos_prox, dir_prox = corpo_da_cobra[i + 1]
        if dir_atual == dir_prox:
            if dir_atual in ['CIMA', 'BAIXO']:
                tela.blit(imagens_cobra['corpo_vertical'], pos_atual)
            else:
                tela.blit(imagens_cobra['corpo_horizontal'], pos_atual)
        else:
            if dir_atual == 'CIMA' and dir_prox == 'DIREITA':
                tela.blit(imagens_cobra['curva_cima_direita'], pos_atual)
            elif dir_atual == 'DIREITA' and dir_prox == 'BAIXO':
                tela.blit(imagens_cobra['curva_direita_baixo'], pos_atual)
            elif dir_atual == 'BAIXO' and dir_prox == 'ESQUERDA':
                tela.blit(imagens_cobra['curva_baixo_esquerda'], pos_atual)
            elif dir_atual == 'ESQUERDA' and dir_prox == 'CIMA':
                tela.blit(imagens_cobra['curva_esquerda_cima'], pos_atual)

            elif dir_atual == 'CIMA' and dir_prox == 'ESQUERDA':
                tela.blit(imagens_cobra['curva_cima_esquerda_inv'], pos_atual)
            elif dir_atual == 'ESQUERDA' and dir_prox == 'BAIXO':
                tela.blit(imagens_cobra['curva_esquerda_baixo_inv'], pos_atual)
            elif dir_atual == 'BAIXO' and dir_prox == 'DIREITA':
                tela.blit(imagens_cobra['curva_baixo_direita_inv'], pos_atual)
            elif dir_atual == 'DIREITA' and dir_prox == 'CIMA':
                tela.blit(imagens_cobra['curva_direita_cima_inv'], pos_atual)


def exibir_pontuacao(tela, pontos, assets):
    texto = assets['fonte_pontuacao'].render(f"Score: {pontos}", True, BRANCO)
    tela.blit(texto, texto.get_rect(topleft=(10, 10)))


def exibir_fps(tela, fps, assets):
    texto = assets['fonte_fps'].render(f"FPS: {int(fps)}", True, BRANCO)
    tela.blit(texto, texto.get_rect(topright=(LARGURA_TELA - 10, 10)))


def exibir_mensagem(tela, msg, cor, y_deslocamento, assets, fonte_tipo='menu'):
    if fonte_tipo == 'titulo':
        fonte = assets['fonte_titulo']
    else:
        fonte = assets['fonte_menu']
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, texto.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_deslocamento)))


def desenhar_pausa(tela, assets):
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    tela.blit(overlay, (0, 0))

    exibir_mensagem(tela, "JOGO PAUSADO", VERDE, -80, assets, fonte_tipo='titulo')
    exibir_mensagem(tela, "ESC - Continuar", BRANCO, 20, assets)
    exibir_mensagem(tela, "M - Voltar ao Menu", BRANCO, 70, assets)
    exibir_mensagem(tela, "Q - Sair do Jogo", BRANCO, 120, assets)

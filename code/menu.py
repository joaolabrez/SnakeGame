import pygame
import sys
from pathlib import Path
from const import *
from drawing import exibir_mensagem
from game_loop import rodar_jogo
from database import ler_scores, atualizar_scores


def tela_de_scores(tela, assets):
    while True:
        score_total, ultima_partida = ler_scores()
        tela.fill(PRETO)
        exibir_mensagem(tela, "PLACAR GERAL", VERMELHO, -120, assets, fonte_tipo='titulo')
        exibir_mensagem(tela, f"Score Total: {score_total}", BRANCO, -40, assets)
        exibir_mensagem(tela, f"Ultima Partida: {ultima_partida}", BRANCO, 20, assets)
        exibir_mensagem(tela, "M - Voltar ao Menu", BRANCO, 100, assets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m or event.key == pygame.K_ESCAPE: return


def tela_de_menu(tela, assets):
    while True:
        score_total, ultima_partida = ler_scores()
        tela.fill(PRETO)
        exibir_mensagem(tela, "SNAKE GAME", VERMELHO, -120, assets, fonte_tipo='titulo')
        exibir_mensagem(tela, "E - Iniciar", BRANCO, 60, assets)
        exibir_mensagem(tela, "S - Score", BRANCO, 110, assets)  # Usando S como você personalizou
        exibir_mensagem(tela, "Q - Sair", BRANCO, 160, assets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q): pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    resultado = rodar_jogo(tela, assets)
                    if resultado['acao'] == 'GAME_OVER':
                        pontos_da_partida = resultado['pontuacao']
                        atualizar_scores(pontos_da_partida)
                        tela_de_game_over(tela, pontos_da_partida, assets)
                if event.key == pygame.K_s:
                    tela_de_scores(tela, assets)


def tela_de_game_over(tela, pontuacao_final, assets):
    while True:
        tela.fill(PRETO)
        exibir_mensagem(tela, "GAME OVER", VERMELHO, -50, assets, fonte_tipo='titulo')
        exibir_mensagem(tela, f"Score da Partida: {pontuacao_final}", BRANCO, 20, assets)
        exibir_mensagem(tela, "E - Jogar de Novo", BRANCO, 80, assets)
        exibir_mensagem(tela, "M - Menu Principal", BRANCO, 120, assets)
        exibir_mensagem(tela, "Q - Sair", BRANCO, 160, assets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q): pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m: return
                if event.key == pygame.K_e:
                    resultado = rodar_jogo(tela, assets)
                    if resultado['acao'] == 'GAME_OVER':
                        pontos_da_partida = resultado['pontuacao']
                        atualizar_scores(pontos_da_partida)
                        pontuacao_final = pontos_da_partida
                    elif resultado['acao'] == 'VOLTAR_MENU':
                        return

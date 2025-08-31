import pygame
import sys
from pathlib import Path
from const import *
from drawing import exibir_mensagem
from game_loop import rodar_jogo

CAMINHO_RAIZ = Path(__file__).parent.parent
CAMINHO_ASSETS = CAMINHO_RAIZ / "assets"


def musica():
    try:
        pygame.mixer.music.load(CAMINHO_ASSETS / 'musica.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    except pygame.error as e:
        print(f"Erro ao carregar musica.wav: {e}")


def tela_de_menu(tela, assets):
    pygame.mixer.music.stop()
    musica()
    while True:
        tela.fill(PRETO)
        exibir_mensagem(tela, "SNAKE GAME", VERDE, -80, assets, fonte_tipo='titulo')
        exibir_mensagem(tela, "E - Iniciar", BRANCO, 20, assets)
        exibir_mensagem(tela, "Q - Sair", BRANCO, 70, assets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                resultado = rodar_jogo(tela, assets)
                if resultado['acao'] == 'GAME_OVER':
                    tela_de_game_over(tela, resultado['pontuacao'], assets)
                elif resultado['acao'] == 'VOLTAR_MENU':
                    pygame.mixer.music.stop()
                    musica()


def tela_de_game_over(tela, pontuacao_final, assets):
    pygame.mixer.music.stop()
    while True:
        tela.fill(PRETO)
        exibir_mensagem(tela, "GAME OVER", VERMELHO, -50, assets, fonte_tipo='titulo')
        exibir_mensagem(tela, f"Score: {pontuacao_final}", BRANCO, 20, assets)
        exibir_mensagem(tela, "E - Jogar de Novo", BRANCO, 80, assets)
        exibir_mensagem(tela, "Q - Sair", BRANCO, 120, assets)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                resultado = rodar_jogo(tela, assets)
                if resultado['acao'] == 'GAME_OVER':
                    pontuacao_final = resultado['pontuacao']
                    pygame.mixer.music.stop()
                elif resultado['acao'] == 'VOLTAR_MENU':
                    return

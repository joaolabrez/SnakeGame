# menu.py
import pygame
import sys
from pathlib import Path
from const import *
from drawing import exibir_mensagem
from game_loop import rodar_jogo

# --- Lógica para encontrar a pasta de assets ---
CAMINHO_RAIZ = Path(__file__).parent.parent
CAMINHO_ASSETS = CAMINHO_RAIZ / "assets"

def musica_menu():
    try:
        pygame.mixer.music.load(CAMINHO_ASSETS / 'musica_menu.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    except pygame.error as e:
        print(f"Erro ao carregar musica_menu.wav: {e}")

# --- SUA NOVA FUNÇÃO DE MÚSICA DE FINAL ---
def musica_ending():
    try:
        # Carrega o seu novo arquivo de música
        pygame.mixer.music.load(CAMINHO_ASSETS / 'musica_end.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
    except pygame.error as e:
        print(f"Erro ao carregar musica_end.wav: {e}")

def tela_de_menu(tela, assets):
    musica_menu() # Toca a música do menu ao iniciar
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
                pontuacao = rodar_jogo(tela, assets)
                tela_de_game_over(tela, pontuacao, assets)

def tela_de_game_over(tela, pontuacao_final, assets):
    pygame.mixer.music.stop() # Para a música do jogo
    musica_ending()
    pygame.mixer.music.set_volume(0.3)
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
                # Ao jogar de novo, ele roda o jogo e atualiza a tela de game over com a nova pontuação
                nova_pontuacao = rodar_jogo(tela, assets)
                pontuacao_final = nova_pontuacao
                pygame.mixer.music.stop()
                musica_ending()
                pygame.mixer.music.set_volume(0.3)
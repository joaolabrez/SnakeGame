# menu.py
import pygame
import sys
from const import *
from drawing import exibir_mensagem
from game_loop import rodar_jogo

def musica_menu():
    # Se você tiver uma música de menu, descomente as linhas abaixo
    # pygame.mixer.music.load('./assets/musica_menu.wav')
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    pass # Remova essa linha se descomentar acima

def musica_ending():
    # Se você tiver uma música de final, descomente as linhas abaixo
    # pygame.mixer.music.load('./assets/musica_ending.wav')
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.3)
    pass # Remova essa linha se descomentar acima

def tela_de_menu(tela):
    # No seu código original, você tinha uma função "musica()"
    # Vou chamar a de menu aqui, mas você pode ajustar
    musica_menu()
    while True:
        tela.fill(PRETO)
        exibir_mensagem(tela, "SNAKE GAME", VERDE, -80, fonte_titulo)
        exibir_mensagem(tela, "E - Iniciar", BRANCO, 20)
        exibir_mensagem(tela, "Q - Sair", BRANCO, 70)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                pontuacao = rodar_jogo(tela)
                tela_de_game_over(tela, pontuacao)

def tela_de_game_over(tela, pontuacao_final):
    musica_ending()
    while True:
        tela.fill(PRETO)
        exibir_mensagem(tela, "GAME OVER", VERMELHO, -50, fonte_titulo)
        exibir_mensagem(tela, f"Score: {pontuacao_final}", BRANCO, 20)
        exibir_mensagem(tela, "E - Jogar de Novo", BRANCO, 80)
        exibir_mensagem(tela, "Q - Sair", BRANCO, 120)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                # Ao jogar de novo, ele sai do loop de game over e volta para o loop do menu
                return
# main.py
import pygame
import sys
from const import LARGURA_TELA, ALTURA_TELA
from menu import tela_de_menu


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('SNAKE GAME')

    # O jogo começa aqui, na tela de menu
    while True:
        tela_de_menu(tela)


if __name__ == '__main__':
    main()
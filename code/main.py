import pygame
import sys
from const import LARGURA_TELA, ALTURA_TELA
from assets import carregar_assets
from menu import tela_de_menu
from database import setup_database


def main():
    pygame.init()
    pygame.mixer.init()

    setup_database()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('SNAKE GAME by Joao')

    assets = carregar_assets()
    if not assets:
        pygame.quit()
        sys.exit()

    while True:
        tela_de_menu(tela, assets)


if __name__ == '__main__':
    main()

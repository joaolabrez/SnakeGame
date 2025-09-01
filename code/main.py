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
    pygame.display.set_caption('Snake Game')

    assets = carregar_assets()
    if not assets:
        print("Falha ao carregar assets. Encerrando.")
        pygame.quit()
        sys.exit()

    pygame.mixer.music.load(assets['musica_fundo'])
    pygame.mixer.music.set_volume(0.4)

    while True:
        tela_de_menu(tela, assets)


if __name__ == '__main__':
    main()

import pygame
import sys
from pathlib import Path
from const import TAMANHO_BLOCO


def carregar_assets():
    CAMINHO_RAIZ = Path(__file__).parent.parent
    CAMINHO_ASSETS = CAMINHO_RAIZ / "assets"

    assets = {}
    try:
        assets['fonte_titulo'] = pygame.font.Font(CAMINHO_ASSETS / "PressStart2P-Regular.ttf", 40)
        assets['fonte_pontuacao'] = pygame.font.Font(CAMINHO_ASSETS / "PressStart2P-Regular.ttf", 14)
        assets['fonte_menu'] = pygame.font.Font(CAMINHO_ASSETS / "PressStart2P-Regular.ttf", 20)
        assets['fonte_fps'] = pygame.font.Font(CAMINHO_ASSETS / "PressStart2P-Regular.ttf", 14)

        assets['som_comida'] = pygame.mixer.Sound(CAMINHO_ASSETS / "crunch.wav")
        assets['som_gameover'] = pygame.mixer.Sound(CAMINHO_ASSETS / "game_over.wav")

        assets['imagem_maca'] = pygame.transform.scale(pygame.image.load(CAMINHO_ASSETS / "maca.png").convert_alpha(),
                                                       (TAMANHO_BLOCO, TAMANHO_BLOCO))

        imagens_cobra = {
            'cabeca_cima': pygame.transform.scale(pygame.image.load(CAMINHO_ASSETS / 'cabeca_cima.png').convert_alpha(),
                                                  (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_baixo': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'cabeca_baixo.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_direita': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'cabeca_direita.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_esquerda': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'cabeca_esquerda.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_cima': pygame.transform.scale(pygame.image.load(CAMINHO_ASSETS / 'rabo_cima.png').convert_alpha(),
                                                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_baixo': pygame.transform.scale(pygame.image.load(CAMINHO_ASSETS / 'rabo_baixo.png').convert_alpha(),
                                                 (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_direita': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'rabo_direita.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_esquerda': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'rabo_esquerda.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'corpo_vertical': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'corpo_vertical.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'corpo_horizontal': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'corpo_horizontal.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),

            # Curvas Normais (sentido horário)
            'curva_direita_baixo': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_sup_right.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_baixo_esquerda': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_sup_left.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_esquerda_cima': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_low_left.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_cima_direita': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_low_right.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),

            # Curvas Invertidas (sentido anti-horário)
            'curva_direita_cima_inv': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_low_right_inv.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_cima_esquerda_inv': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_low_left_inv.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_esquerda_baixo_inv': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_sup_left_inv.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_baixo_direita_inv': pygame.transform.scale(
                pygame.image.load(CAMINHO_ASSETS / 'curva_sup_right_inv.png').convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        }
        assets['imagens_cobra'] = imagens_cobra

    except Exception as e:
        print(f"Erro fatal ao carregar um asset: {e}. Verifique se você criou as 4 imagens com final '_inv'.")
        return None

    return assets

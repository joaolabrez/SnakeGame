import pygame
from const import TAMANHO_BLOCO
from utils import resource_path


def carregar_assets():
    assets = {}
    try:
        assets['fonte_titulo'] = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 40)
        assets['fonte_pontuacao'] = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 14)
        assets['fonte_menu'] = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
        assets['fonte_fps'] = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 14)

        assets['som_comida'] = pygame.mixer.Sound(resource_path("assets/crunch.wav"))
        assets['som_gameover'] = pygame.mixer.Sound(resource_path("assets/game_over.wav"))

        assets['musica_fundo'] = resource_path("assets/musica.wav")

        assets['imagem_maca'] = pygame.transform.scale(
            pygame.image.load(resource_path("assets/maca.png")).convert_alpha(),
            (TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

        imagens_cobra = {
            'cabeca_cima': pygame.transform.scale(
                pygame.image.load(resource_path("assets/cabeca_cima.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_baixo': pygame.transform.scale(
                pygame.image.load(resource_path("assets/cabeca_baixo.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_direita': pygame.transform.scale(
                pygame.image.load(resource_path("assets/cabeca_direita.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'cabeca_esquerda': pygame.transform.scale(
                pygame.image.load(resource_path("assets/cabeca_esquerda.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_cima': pygame.transform.scale(
                pygame.image.load(resource_path("assets/rabo_cima.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_baixo': pygame.transform.scale(
                pygame.image.load(resource_path("assets/rabo_baixo.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_direita': pygame.transform.scale(
                pygame.image.load(resource_path("assets/rabo_direita.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'rabo_esquerda': pygame.transform.scale(
                pygame.image.load(resource_path("assets/rabo_esquerda.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'corpo_vertical': pygame.transform.scale(
                pygame.image.load(resource_path("assets/corpo_vertical.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'corpo_horizontal': pygame.transform.scale(
                pygame.image.load(resource_path("assets/corpo_horizontal.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_direita_baixo': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_sup_right.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_baixo_esquerda': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_sup_left.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_esquerda_cima': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_low_left.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_cima_direita': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_low_right.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_direita_cima_inv': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_low_right_inv.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_cima_esquerda_inv': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_low_left_inv.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_esquerda_baixo_inv': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_sup_left_inv.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_baixo_direita_inv': pygame.transform.scale(
                pygame.image.load(resource_path("assets/curva_sup_right_inv.png")).convert_alpha(),
                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        }
        assets['imagens_cobra'] = imagens_cobra
    except Exception as e:
        print(f"Erro fatal ao carregar um asset: {e}.")
        return None
    return assets
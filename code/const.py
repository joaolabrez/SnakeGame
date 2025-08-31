# config.py
import pygame
import sys

pygame.init()
pygame.mixer.init()

# --- Constantes Principais ---
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_BLOCO = 20
VELOCIDADE_JOGO = 15

# --- Carregamento de Assets ---
try:
    fonte_titulo = pygame.font.Font("assets/PressStart2P-Regular.ttf", 40)
    fonte_pontuacao = pygame.font.Font("assets/PressStart2P-Regular.ttf", 14)
    fonte_menu = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
    fonte_fps = pygame.font.Font("assets/PressStart2P-Regular.ttf", 14)
    som_comida = pygame.mixer.Sound("assets/crunch.wav")
    som_gameover = pygame.mixer.Sound("assets/game_over.wav")
    imagem_maca = pygame.transform.scale(pygame.image.load("assets/maca.png").convert_alpha(),
                                         (TAMANHO_BLOCO, TAMANHO_BLOCO))

    imagens_cobra = {
        'cabeca_cima': pygame.transform.scale(pygame.image.load('assets/cabeca_cima.png').convert_alpha(),
                                              (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'cabeca_baixo': pygame.transform.scale(pygame.image.load('assets/cabeca_baixo.png').convert_alpha(),
                                               (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'cabeca_direita': pygame.transform.scale(pygame.image.load('assets/cabeca_direita.png').convert_alpha(),
                                                 (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'cabeca_esquerda': pygame.transform.scale(pygame.image.load('assets/cabeca_esquerda.png').convert_alpha(),
                                                  (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'rabo_cima': pygame.transform.scale(pygame.image.load('assets/rabo_cima.png').convert_alpha(),
                                            (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'rabo_baixo': pygame.transform.scale(pygame.image.load('assets/rabo_baixo.png').convert_alpha(),
                                             (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'rabo_direita': pygame.transform.scale(pygame.image.load('assets/rabo_direita.png').convert_alpha(),
                                               (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'rabo_esquerda': pygame.transform.scale(pygame.image.load('assets/rabo_esquerda.png').convert_alpha(),
                                                (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'corpo_vertical': pygame.transform.scale(pygame.image.load('assets/corpo_vertical.png').convert_alpha(),
                                                 (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'corpo_horizontal': pygame.transform.scale(pygame.image.load('assets/corpo_horizontal.png').convert_alpha(),
                                                   (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_direita_baixo': pygame.transform.scale(pygame.image.load('assets/curva_sup_right.png').convert_alpha(),
                                                      (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_baixo_esquerda': pygame.transform.scale(pygame.image.load('assets/curva_sup_left.png').convert_alpha(),
                                                       (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_esquerda_cima': pygame.transform.scale(pygame.image.load('assets/curva_low_left.png').convert_alpha(),
                                                      (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_cima_direita': pygame.transform.scale(pygame.image.load('assets/curva_low_right.png').convert_alpha(),
                                                     (TAMANHO_BLOCO, TAMANHO_BLOCO)),
    }
    # Verifica se as imagens invertidas existem antes de carregar
    # Isso evita erros se você ainda não as criou
    try:
        imagens_cobra.update({
            'curva_direita_cima_inv': pygame.transform.scale(
                pygame.image.load('assets/curva_low_right_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_cima_esquerda_inv': pygame.transform.scale(
                pygame.image.load('assets/curva_low_left_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_esquerda_baixo_inv': pygame.transform.scale(
                pygame.image.load('assets/curva_sup_left_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
            'curva_baixo_direita_inv': pygame.transform.scale(
                pygame.image.load('assets/curva_sup_right_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        })
    except pygame.error:
        print(
            "Aviso: Imagens de curva invertidas ('_inv') não encontradas. As curvas para esquerda podem não parecer perfeitas.")

except Exception as e:
    print(f"Erro fatal ao carregar um asset: {e}.")
    pygame.quit()
    sys.exit()
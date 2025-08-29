import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições de Cores e Tela
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
LARGURA_TELA = 600
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Jogo da Cobrinha')

# Configurações do Jogo
TAMANHO_BLOCO = 20
VELOCIDADE_JOGO = 15
relogio = pygame.time.Clock()

try:
    fonte_titulo = pygame.font.Font("PressStart2P-Regular.ttf", 40)
    fonte_pontuacao = pygame.font.Font("PressStart2P-Regular.ttf", 28)
    fonte_menu = pygame.font.Font("PressStart2P-Regular.ttf", 20)
except pygame.error:
    print("Arquivo da fonte não encontrado! Usando fontes padrão.")
    fonte_titulo = pygame.font.SysFont("comicsansms", 50)
    fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)
    fonte_menu = pygame.font.SysFont("bahnschrift", 25)


def exibir_pontuacao(pontos):
    valor = fonte_pontuacao.render(str(pontos), True, BRANCO)
    retangulo_texto = valor.get_rect(center=(LARGURA_TELA / 2, 30))
    tela.blit(valor, retangulo_texto)


def desenhar_cobra(tamanho_bloco, corpo_da_cobra):
    for segmento in corpo_da_cobra:
        pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])


def exibir_mensagem(msg, cor, y_deslocamento=0, fonte=fonte_menu):  # Adicionamos um parâmetro para escolher a fonte
    texto = fonte.render(msg, True, cor)
    retangulo_texto = texto.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_deslocamento))
    tela.blit(texto, retangulo_texto)


# TELA DE MENU
def tela_de_menu():
    menu_ativo = True
    while menu_ativo:
        tela.fill(PRETO)

        # Desenha o título do jogo
        exibir_mensagem("SNAKE", VERDE, -80, fonte_titulo)

        # Desenha as opções
        exibir_mensagem("E - Iniciar Jogo", BRANCO, 20)
        exibir_mensagem("Q - Sair", BRANCO, 70)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Se apertar 'E'
                    rodar_jogo()  # Começa o jogo
                if event.key == pygame.K_q:  # Se apertar 'Q'
                    pygame.quit()
                    sys.exit()


def rodar_jogo():
    """Contém o loop principal e a lógica do jogo."""
    game_over = False
    game_close = False
    pos_x = LARGURA_TELA / 2
    pos_y = ALTURA_TELA / 2
    delta_x = 0
    delta_y = 0
    corpo_cobra = []
    comprimento_cobra = 1
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(TAMANHO_BLOCO)
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(TAMANHO_BLOCO)

    while not game_over:
        while game_close:
            tela.fill(PRETO)
            exibir_mensagem("GAME OVER", VERMELHO, y_deslocamento=-50)
            exibir_mensagem("E - Jogar de Novo", BRANCO, y_deslocamento=50)
            exibir_mensagem("Q - Sair", BRANCO,
                            y_deslocamento=90)
            exibir_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        rodar_jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and delta_x == 0:
                    delta_x = -TAMANHO_BLOCO
                    delta_y = 0
                elif event.key == pygame.K_d and delta_x == 0:
                    delta_x = TAMANHO_BLOCO
                    delta_y = 0
                elif event.key == pygame.K_w and delta_y == 0:
                    delta_y = -TAMANHO_BLOCO
                    delta_x = 0
                elif event.key == pygame.K_s and delta_y == 0:
                    delta_y = TAMANHO_BLOCO
                    delta_x = 0

        if pos_x >= LARGURA_TELA or pos_x < 0 or pos_y >= ALTURA_TELA or pos_y < 0:
            game_close = True

        pos_x += delta_x
        pos_y += delta_y
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        cabeca_cobra = [pos_x, pos_y]
        corpo_cobra.append(cabeca_cobra)

        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_close = True

        desenhar_cobra(TAMANHO_BLOCO, corpo_cobra)
        exibir_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comprimento_cobra += 1

        relogio.tick(VELOCIDADE_JOGO)

    pygame.quit()
    sys.exit()

tela_de_menu()
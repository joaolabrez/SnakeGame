import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('SNAKE GAME by Joao')

TAMANHO_BLOCO = 20
VELOCIDADE_JOGO = 15
relogio = pygame.time.Clock()

try:
    # --- Carregamento de assets ---
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
        # Curvas Normais (sentido horário)
        'curva_direita_baixo': pygame.transform.scale(pygame.image.load('assets/curva_sup_right.png').convert_alpha(),
                                                      (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_baixo_esquerda': pygame.transform.scale(pygame.image.load('assets/curva_sup_left.png').convert_alpha(),
                                                       (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_esquerda_cima': pygame.transform.scale(pygame.image.load('assets/curva_low_left.png').convert_alpha(),
                                                      (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_cima_direita': pygame.transform.scale(pygame.image.load('assets/curva_low_right.png').convert_alpha(),
                                                     (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        # Curvas Invertidas (sentido anti-horário)
        'curva_direita_cima_inv': pygame.transform.scale(
            pygame.image.load('assets/curva_low_right_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_cima_esquerda_inv': pygame.transform.scale(
            pygame.image.load('assets/curva_low_left_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_esquerda_baixo_inv': pygame.transform.scale(
            pygame.image.load('assets/curva_sup_left_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
        'curva_baixo_direita_inv': pygame.transform.scale(
            pygame.image.load('assets/curva_sup_right_inv.png').convert_alpha(), (TAMANHO_BLOCO, TAMANHO_BLOCO)),
    }
except Exception as e:
    print(
        f"Erro ao carregar um asset: {e}. Verifique se você criou as 4 imagens com final '_inv' e as salvou na pasta 'assets'.")
    pygame.quit()
    sys.exit()


def exibir_pontuacao(pontos):
    texto = fonte_pontuacao.render(f"Score: {pontos}", True, BRANCO)
    tela.blit(texto, texto.get_rect(topleft=(10, 10)))


def exibir_fps(fps):
    texto = fonte_fps.render(f"FPS: {int(fps)}", True, BRANCO)
    tela.blit(texto, texto.get_rect(topright=(LARGURA_TELA - 10, 10)))

def tela_de_game_over(pontuacao_final):

    while True:
        tela.fill(PRETO)
        exibir_mensagem("GAME OVER", VERMELHO, -50, fonte_titulo)
        exibir_mensagem(f"Score: {pontuacao_final}", BRANCO, 20, fonte_menu)
        exibir_mensagem("E - Jogar de Novo", BRANCO, 80, fonte_menu)
        exibir_mensagem("Q - Sair", BRANCO, 120, fonte_menu)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                rodar_jogo() # Reinicia o jogo e sai desta tela


def musica():
    pygame.mixer.music.load('./assets/musica.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

def desenhar_cobra(corpo_da_cobra):
    # Lógica de cabeça e rabo (correta)
    cabeca_pos, cabeca_dir = corpo_da_cobra[-1]
    if cabeca_dir == 'CIMA':
        tela.blit(imagens_cobra['cabeca_cima'], cabeca_pos)
    elif cabeca_dir == 'BAIXO':
        tela.blit(imagens_cobra['cabeca_baixo'], cabeca_pos)
    elif cabeca_dir == 'ESQUERDA':
        tela.blit(imagens_cobra['cabeca_esquerda'], cabeca_pos)
    elif cabeca_dir == 'DIREITA':
        tela.blit(imagens_cobra['cabeca_direita'], cabeca_pos)
    if len(corpo_da_cobra) > 1:
        rabo_pos, rabo_dir = corpo_da_cobra[0]
        prox_pos, prox_dir = corpo_da_cobra[1]
        if prox_pos[1] < rabo_pos[1]:
            tela.blit(imagens_cobra['rabo_baixo'], rabo_pos)
        elif prox_pos[1] > rabo_pos[1]:
            tela.blit(imagens_cobra['rabo_cima'], rabo_pos)
        elif prox_pos[0] < rabo_pos[0]:
            tela.blit(imagens_cobra['rabo_direita'], rabo_pos)
        elif prox_pos[0] > rabo_pos[0]:
            tela.blit(imagens_cobra['rabo_esquerda'], rabo_pos)

    # Lógica do Corpo e Curvas (IMPLEMENTANDO SUA IDEIA CORRETAMENTE)
    for i in range(1, len(corpo_da_cobra) - 1):
        pos_atual, dir_atual = corpo_da_cobra[i]
        pos_prox, dir_prox = corpo_da_cobra[i + 1]

        if dir_atual == dir_prox:  # É um segmento reto
            if dir_atual in ['CIMA', 'BAIXO']:
                tela.blit(imagens_cobra['corpo_vertical'], pos_atual)
            else:
                tela.blit(imagens_cobra['corpo_horizontal'], pos_atual)
        else:  # É uma curva
            # Lógica para curvas no sentido horário (imagens normais)
            if dir_atual == 'CIMA' and dir_prox == 'DIREITA':
                tela.blit(imagens_cobra['curva_cima_direita'], pos_atual)
            elif dir_atual == 'DIREITA' and dir_prox == 'BAIXO':
                tela.blit(imagens_cobra['curva_direita_baixo'], pos_atual)
            elif dir_atual == 'BAIXO' and dir_prox == 'ESQUERDA':
                tela.blit(imagens_cobra['curva_baixo_esquerda'], pos_atual)
            elif dir_atual == 'ESQUERDA' and dir_prox == 'CIMA':
                tela.blit(imagens_cobra['curva_esquerda_cima'], pos_atual)

            # Lógica para curvas no sentido anti-horário (imagens invertidas)
            elif dir_atual == 'CIMA' and dir_prox == 'ESQUERDA':
                tela.blit(imagens_cobra['curva_cima_esquerda_inv'], pos_atual)
            elif dir_atual == 'ESQUERDA' and dir_prox == 'BAIXO':
                tela.blit(imagens_cobra['curva_esquerda_baixo_inv'], pos_atual)
            elif dir_atual == 'BAIXO' and dir_prox == 'DIREITA':
                tela.blit(imagens_cobra['curva_baixo_direita_inv'], pos_atual)
            elif dir_atual == 'DIREITA' and dir_prox == 'CIMA':
                tela.blit(imagens_cobra['curva_direita_cima_inv'], pos_atual)


def exibir_mensagem(msg, cor, y_deslocamento=0, fonte=fonte_menu):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, texto.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_deslocamento)))


def tela_de_menu():
    musica()
    while True:
        tela.fill(PRETO)
        exibir_mensagem("SNAKE GAME", VERDE, -80, fonte_titulo)
        exibir_mensagem("E - Iniciar", BRANCO, 20)
        exibir_mensagem("Q - Sair", BRANCO, 70)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit();
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                rodar_jogo()


def rodar_jogo():
    pygame.mixer.music.stop()
    musica()
    pos_x, pos_y = LARGURA_TELA / 2, ALTURA_TELA / 2
    delta_x, delta_y = TAMANHO_BLOCO, 0
    direcao_atual = 'DIREITA'
    corpo_cobra = [[[pos_x, pos_y], direcao_atual]]
    comprimento_cobra = 1
    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direcao_atual != 'DIREITA':
                    direcao_atual = 'ESQUERDA'
                elif event.key == pygame.K_d and direcao_atual != 'ESQUERDA':
                    direcao_atual = 'DIREITA'
                elif event.key == pygame.K_w and direcao_atual != 'BAIXO':
                    direcao_atual = 'CIMA'
                elif event.key == pygame.K_s and direcao_atual != 'CIMA':
                    direcao_atual = 'BAIXO'

        if direcao_atual == 'DIREITA':
            delta_x, delta_y = TAMANHO_BLOCO, 0
        elif direcao_atual == 'ESQUERDA':
            delta_x, delta_y = -TAMANHO_BLOCO, 0
        elif direcao_atual == 'CIMA':
            delta_x, delta_y = 0, -TAMANHO_BLOCO
        elif direcao_atual == 'BAIXO':
            delta_x, delta_y = 0, TAMANHO_BLOCO

        pos_x += delta_x
        pos_y += delta_y

        # --- LÓGICA DE GAME OVER ATUALIZADA ---
        if not (0 <= pos_x < LARGURA_TELA and 0 <= pos_y < ALTURA_TELA) or [pos_x, pos_y] in [p for p, d in corpo_cobra]:
            som_gameover.play()
            tela_de_game_over(comprimento_cobra - 1) # Chama a nova tela de game over
            return # Sai da função rodar_jogo

        nova_cabeca = [[pos_x, pos_y], direcao_atual]
        corpo_cobra.append(nova_cabeca)
        if len(corpo_cobra) > comprimento_cobra: del corpo_cobra[0]

        if pos_x == comida_x and pos_y == comida_y:
            comprimento_cobra += 1
            som_comida.play()
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / TAMANHO_BLOCO) * TAMANHO_BLOCO

        tela.fill(PRETO)
        tela.blit(imagem_maca, (comida_x, comida_y))
        desenhar_cobra(corpo_cobra)
        exibir_pontuacao(comprimento_cobra - 1)
        exibir_fps(relogio.get_fps())
        pygame.display.update()
        relogio.tick(VELOCIDADE_JOGO)


tela_de_menu()
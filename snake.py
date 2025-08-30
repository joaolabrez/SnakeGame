import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)
LARGURA_TELA = 600
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('SNAKE GAME')

TAMANHO_BLOCO = 20
VELOCIDADE_JOGO = 15
relogio = pygame.time.Clock()

try:
    # ALTERAÇÃO: Adicionado 'assets/'
    fonte_titulo = pygame.font.Font("assets/PressStart2P-Regular.ttf", 40)
    # ALTERAÇÃO: Adicionado 'assets/'
    fonte_pontuacao = pygame.font.Font("assets/PressStart2P-Regular.ttf", 28)
    # ALTERAÇÃO: Adicionado 'assets/'
    fonte_menu = pygame.font.Font("assets/PressStart2P-Regular.ttf", 20)
except pygame.error:
    print("Arquivo da fonte não encontrado! Usando fontes padrão.")
    fonte_titulo = pygame.font.SysFont("comicsansms", 50)
    fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)
    fonte_menu = pygame.font.SysFont("bahnschrift", 25)

try:
    # ALTERAÇÃO: Adicionado 'assets/'
    som_comida = pygame.mixer.Sound("assets/crunch.wav")
    # ALTERAÇÃO: Adicionado 'assets/'
    som_gameover = pygame.mixer.Sound("assets/game_over.wav")
except pygame.error:
    print("Arquivos de som não encontrados! O jogo rodará sem som.")
    som_comida = type('DummySound', (), {'play': lambda: None})()
    som_gameover = type('DummySound', (), {'play': lambda: None})()

try:
    # ALTERAÇÃO: Adicionado 'assets/'
    imagem_maca_original = pygame.image.load("assets/maca.png").convert_alpha()
    imagem_maca = pygame.transform.scale(imagem_maca_original, (TAMANHO_BLOCO, TAMANHO_BLOCO))
except pygame.error:
    print("Imagem 'maca.png' não encontrada! A comida será um quadrado vermelho.")
    imagem_maca = None

try:
    # ALTERAÇÃO: Adicionado 'assets/'
    imagem_background_original = pygame.image.load("assets/background.png").convert()
    imagem_background = pygame.transform.scale(imagem_background_original, (LARGURA_TELA, ALTURA_TELA))
except (pygame.error, FileNotFoundError):
    print("Imagem 'background.png' não encontrada! O fundo será preto.")
    imagem_background = None

try:
    # ALTERAÇÃO: Adicionado 'assets/' a cada caminho de imagem da cobra
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
    }
except (pygame.error, FileNotFoundError):
    print("Erro ao carregar as imagens da cobra! Verifique os nomes dos arquivos. A cobra será verde.")
    imagens_cobra = None


def exibir_pontuacao(pontos):
    valor = fonte_pontuacao.render(str(pontos), True, BRANCO)
    retangulo_texto = valor.get_rect(center=(LARGURA_TELA / 2, 30))
    tela.blit(valor, retangulo_texto)


def desenhar_cobra(tamanho_bloco, corpo_da_cobra, imagem_cabeca, imagem_rabo):
    cabeca = corpo_da_cobra[-1]
    if imagem_cabeca:
        tela.blit(imagem_cabeca, (cabeca[0], cabeca[1]))
    else:
        pygame.draw.rect(tela, VERDE, [cabeca[0], cabeca[1], tamanho_bloco, tamanho_bloco])

    if len(corpo_da_cobra) > 1:
        rabo = corpo_da_cobra[0]
        if imagem_rabo:
            tela.blit(imagem_rabo, (rabo[0], rabo[1]))
        else:
            pygame.draw.rect(tela, VERDE, [rabo[0], rabo[1], tamanho_bloco, tamanho_bloco])

    for segmento in corpo_da_cobra[1:-1]:
        pygame.draw.rect(tela, VERDE, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])


def exibir_mensagem(msg, cor, y_deslocamento=0, fonte=fonte_menu):
    texto = fonte.render(msg, True, cor)
    retangulo_texto = texto.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + y_deslocamento))
    tela.blit(texto, retangulo_texto)


def tela_de_menu():
    menu_ativo = True
    while menu_ativo:
        if imagem_background:
            tela.blit(imagem_background, (0, 0))
        else:
            tela.fill(PRETO)

        exibir_mensagem("SNAKE GAME", VERDE, -80, fonte_titulo)
        exibir_mensagem("E - Iniciar", BRANCO, 20)
        exibir_mensagem("Q - Sair", BRANCO, 70)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    rodar_jogo()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def rodar_jogo():
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

    direcao_atual = 'DIREITA'

    while not game_over:
        while game_close:
            if imagem_background:
                tela.blit(imagem_background, (0, 0))
            else:
                tela.fill(PRETO)
            exibir_mensagem("GAME OVER", VERMELHO, y_deslocamento=-50)
            exibir_mensagem("E - Jogar de Novo", BRANCO, y_deslocamento=50)
            exibir_mensagem("Q - Sair", BRANCO, y_deslocamento=90)
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
                    delta_x = -TAMANHO_BLOCO;
                    delta_y = 0;
                    direcao_atual = 'ESQUERDA'
                elif event.key == pygame.K_d and delta_x == 0:
                    delta_x = TAMANHO_BLOCO;
                    delta_y = 0;
                    direcao_atual = 'DIREITA'
                elif event.key == pygame.K_w and delta_y == 0:
                    delta_y = -TAMANHO_BLOCO;
                    delta_x = 0;
                    direcao_atual = 'CIMA'
                elif event.key == pygame.K_s and delta_y == 0:
                    delta_y = TAMANHO_BLOCO;
                    delta_x = 0;
                    direcao_atual = 'BAIXO'

        if pos_x >= LARGURA_TELA or pos_x < 0 or pos_y >= ALTURA_TELA or pos_y < 0:
            som_gameover.play();
            game_close = True

        pos_x += delta_x
        pos_y += delta_y

        if imagem_background:
            tela.blit(imagem_background, (0, 0))
        else:
            tela.fill(PRETO)

        if imagem_maca:
            tela.blit(imagem_maca, (comida_x, comida_y))
        else:
            pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])

        cabeca_cobra = [pos_x, pos_y]
        corpo_cobra.append(cabeca_cobra)

        if len(corpo_cobra) > comprimento_cobra: del corpo_cobra[0]
        for segmento in corpo_cobra[:-1]:
            if segmento == cabeca_cobra: som_gameover.play(); game_close = True

        imagem_cabeca_final = None
        imagem_rabo_final = None

        if imagens_cobra:
            if direcao_atual == 'CIMA':
                imagem_cabeca_final = imagens_cobra['cabeca_cima']
            elif direcao_atual == 'BAIXO':
                imagem_cabeca_final = imagens_cobra['cabeca_baixo']
            elif direcao_atual == 'ESQUERDA':
                imagem_cabeca_final = imagens_cobra['cabeca_esquerda']
            elif direcao_atual == 'DIREITA':
                imagem_cabeca_final = imagens_cobra['cabeca_direita']

            # --- LÓGICA DO RABO (TODAS AS DIREÇÕES INVERTIDAS) ---
            if len(corpo_cobra) > 1:
                rabo = corpo_cobra[0]
                segundo_segmento = corpo_cobra[1]  # O segmento logo depois do rabo

                # Se o segundo segmento está à direita do rabo, o rabo aponta para a ESQUERDA
                # Mas como seus arquivos parecem invertidos, pedimos o da DIREITA
                if segundo_segmento[0] > rabo[0]:
                    imagem_rabo_final = imagens_cobra['rabo_direita']  # INVERTIDO
                # Se o segundo segmento está à esquerda do rabo, o rabo aponta para a DIREITA
                # Mas como seus arquivos parecem invertidos, pedimos o da ESQUERDA
                elif segundo_segmento[0] < rabo[0]:
                    imagem_rabo_final = imagens_cobra['rabo_esquerda']  # INVERTIDO
                # Se o segundo segmento está abaixo do rabo, o rabo aponta para CIMA
                # Mas como seus arquivos parecem invertidos, pedimos o de BAIXO
                elif segundo_segmento[1] > rabo[1]:
                    imagem_rabo_final = imagens_cobra['rabo_baixo']  # INVERTIDO
                # Se o segundo segmento está acima do rabo, o rabo aponta para BAIXO
                # Mas como seus arquivos parecem invertidos, pedimos o de CIMA
                elif segundo_segmento[1] < rabo[1]:
                    imagem_rabo_final = imagens_cobra['rabo_cima']  # INVERTIDO

        desenhar_cobra(TAMANHO_BLOCO, corpo_cobra, imagem_cabeca_final, imagem_rabo_final)

        exibir_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comprimento_cobra += 1
            som_comida.play()

        relogio.tick(VELOCIDADE_JOGO)

    pygame.quit()
    sys.exit()


tela_de_menu()
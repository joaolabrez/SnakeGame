import sqlite3
from pathlib import Path

CAMINHO_RAIZ = Path(__file__).parent.parent
NOME_DB = CAMINHO_RAIZ / "snake_score.db"


def setup_database():
    """Cria o banco de dados e a tabela com as duas colunas de score."""
    conn = sqlite3.connect(NOME_DB)
    cursor = conn.cursor()

    # Adicionamos a coluna 'score_ultima_partida'
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS pontuacao
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY,
                       score_total
                       INTEGER
                       NOT
                       NULL,
                       score_ultima_partida
                       INTEGER
                       NOT
                       NULL
                   )
                   ''')

    cursor.execute('SELECT count(*) FROM pontuacao')
    if cursor.fetchone()[0] == 0:
        # Insere o registro inicial com ambos os scores zerados
        cursor.execute('INSERT INTO pontuacao (score_total, score_ultima_partida) VALUES (0, 0)')

    conn.commit()
    conn.close()


def ler_scores():
    """Lê ambos os scores (total e última partida) do banco de dados."""
    try:
        conn = sqlite3.connect(NOME_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT score_total, score_ultima_partida FROM pontuacao WHERE id = 1')
        resultado = cursor.fetchone()
        conn.close()
        # Retorna uma tupla (score_total, score_ultima_partida)
        return resultado if resultado else (0, 0)
    except sqlite3.Error as e:
        print(f"Erro ao ler o banco de dados: {e}")
        return (0, 0)


def atualizar_scores(pontos_da_partida):
    """Salva a pontuação da partida e adiciona ao total."""
    try:
        score_total_anterior, _ = ler_scores()
        novo_total = score_total_anterior + pontos_da_partida

        conn = sqlite3.connect(NOME_DB)
        cursor = conn.cursor()

        # Atualiza ambas as colunas de uma vez
        cursor.execute('''
                       UPDATE pontuacao
                       SET score_total          = ?,
                           score_ultima_partida = ?
                       WHERE id = 1
                       ''', (novo_total, pontos_da_partida))

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o banco de dados: {e}")

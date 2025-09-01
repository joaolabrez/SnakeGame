import sqlite3
from utils import resource_path

NOME_DB = resource_path("snake_score.db")

def setup_database():
    conn = sqlite3.connect(NOME_DB)
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS pontuacao
                   (id INTEGER PRIMARY KEY,
                    score_total INTEGER NOT NULL,
                    score_ultima_partida INTEGER NOT NULL)
                   ''')
    cursor.execute('SELECT count(*) FROM pontuacao')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO pontuacao (score_total, score_ultima_partida) VALUES (0, 0)')
    conn.commit()
    conn.close()

def ler_scores():
    try:
        conn = sqlite3.connect(NOME_DB)
        cursor = conn.cursor()
        cursor.execute('SELECT score_total, score_ultima_partida FROM pontuacao WHERE id = 1')
        resultado = cursor.fetchone()
        conn.close()
        return resultado if resultado else (0, 0)
    except sqlite3.Error as e:
        print(f"Erro ao ler o banco de dados: {e}")
        return (0, 0)

def atualizar_scores(pontos_da_partida):
    try:
        score_total_anterior, _ = ler_scores()
        novo_total = score_total_anterior + pontos_da_partida
        conn = sqlite3.connect(NOME_DB)
        cursor = conn.cursor()
        cursor.execute('''
                       UPDATE pontuacao
                       SET score_total = ?, score_ultima_partida = ?
                       WHERE id = 1
                       ''', (novo_total, pontos_da_partida))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o banco de dados: {e}")
import sqlite3


def criar_tabela_alunos():
    conn = sqlite3.connect('notas_enem.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, linguagens REAL, humanas REAL, natureza REAL, matematica REAL, redacao REAL, media REAL, status TEXT)''')
    conn.commit()
    conn.close()

def inserir_dados_aluno(notas, media, status):
    conn = sqlite3.connect('notas_enem.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (linguagens, humanas, natureza, matematica, redacao, media, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (notas[0], notas[1], notas[2], notas[3], notas[4], media, status))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabela_alunos()

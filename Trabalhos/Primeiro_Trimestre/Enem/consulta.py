import sqlite3


def consultar_alunos():
    conn = sqlite3.connect('notas_enem.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

if __name__ == "__main__":
    alunos = consultar_alunos()
    for aluno in alunos:
        print(aluno)

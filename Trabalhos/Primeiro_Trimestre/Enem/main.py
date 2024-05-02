import sqlite3

def calcular_media_enem(linguagens, humanas, natureza, matematica, redacao):
    notas = [linguagens, humanas, natureza, matematica, redacao]

    if any(nota < 0 or nota > 1000 for nota in notas):
        print("Por favor, insira notas válidas (entre 0 e 1000).")
        return

    if redacao == 0:
        print("A nota da redação não pode ser zero. O aluno está reprovado.")
        return

    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 450 else "Reprovado"

    mensagem = f"Sua média final no ENEM é: {media:.2f}\nStatus: {status}"
    print(mensagem)

    inserir_dados_aluno(linguagens, humanas, natureza, matematica, redacao, media, status)

def criar_tabela_alunos():
    conn = sqlite3.connect('notas_enem.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, linguagens REAL, humanas REAL, natureza REAL, matematica REAL, redacao REAL, media REAL, status TEXT)''')
    conn.commit()
    conn.close()

def inserir_dados_aluno(linguagens, humanas, natureza, matematica, redacao, media, status):
    conn = sqlite3.connect('notas_enem.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (linguagens, humanas, natureza, matematica, redacao, media, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (linguagens, humanas, natureza, matematica, redacao, media, status))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabela_alunos()
    calcular_media_enem(
        float(input("Digite a nota de Linguagens: ")),
        float(input("Digite a nota de Humanas: ")),
        float(input("Digite a nota de Natureza: ")),
        float(input("Digite a nota de Matemática: ")),
        float(input("Digite a nota de Redação: "))
    )

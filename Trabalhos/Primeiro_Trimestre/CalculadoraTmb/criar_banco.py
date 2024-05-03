import sqlite3


def criar_banco_dados():
    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       sexo TEXT,
                       idade INTEGER,
                       peso REAL,
                       altura REAL,
                       tmb REAL)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco_dados()
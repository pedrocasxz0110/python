import sqlite3


def consultar_usuarios():
    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def exibir_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

def main():
    usuarios = consultar_usuarios()
    exibir_usuarios(usuarios)

if __name__ == "__main__":
    main()

import sqlite3


def calcular_tmb():
    
      sexo = input("Digite o sexo (M/F): ").upper()
      idade = int(input("Digite a idade em anos: "))
      peso = float(input("Digite o peso em kg: "))
      altura = float(input("Digite a altura em cm: "))

      if sexo not in ['M', 'F']:
          print("Sexo inválido. Digite M para masculino ou F para feminino.")
          return

      if sexo == 'M':
          tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
      else:
          tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

      print(f"Sua Taxa Metabólica Basal (TMB) é: {tmb:.2f} calorias por dia.")
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
      cursor.execute('''INSERT INTO usuarios (sexo, idade, peso, altura, tmb) VALUES (?, ?, ?, ?, ?)''',(sexo, idade, peso, altura, tmb))
      conn.commit()
      conn.close()

calcular_tmb()



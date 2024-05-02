import sqlite3

def calcular_imc(nome, peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.
    Retorna o IMC, status de peso e mensagem indicando o status de peso da pessoa.
    """

    if peso <= 0 or altura <= 0:
        return "Por favor, insira um valor válido para peso e altura.", None

    imc = peso / (altura ** 2)

    if imc < 18.5:
        status = "Abaixo do peso"
    elif imc < 25:
        status = "Peso normal"
    elif imc < 30:
        status = "Sobrepeso"
    elif imc < 35:
        status = "Obesidade grau I"
        perda_peso = peso * 0.20
    elif imc < 40:
        status = "Obesidade grau II"
        perda_peso = peso * 0.30
    else:
        status = "Obesidade grau III"
        perda_peso = peso * 0.40

    if imc >= 35:
        mensagem = f"Você está com {status}. Para voltar ao peso ideal, você precisa perder {perda_peso:.2f} quilos."
    else:
        mensagem = f"Seu IMC é {imc:.2f}. Você está {status}."

    return mensagem, imc

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, peso REAL, altura REAL, imc REAL)''')

while True:
    try:
        nome = input("Digite seu nome: ")
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        resultado, imc = calcular_imc(nome, peso, altura)
        if imc is not None:
            print(resultado)

            # Inserir os dados do usuário no banco de dados
            cursor.execute("INSERT INTO usuarios (nome, peso, altura, imc) VALUES (?, ?, ?, ?)", (nome, peso, altura, imc))
            conn.commit()

            break
        else:
            print(resultado)
    except ValueError:
        print("Por favor, insira um valor numérico para peso e altura.")

# Fechar a conexão com o banco de dados
conn.close()








#sqlite3.connect('dados_usuarios.db') - Esta linha de código cria uma conexão com o banco de dados SQLite chamado 'dados_usuarios.db'. Se o arquivo do banco de dados já existir, ele será aberto. Se não existir, um novo arquivo com esse nome será criado no mesmo diretório onde o seu código Python está sendo executado. A função connect() do módulo sqlite3 retorna um objeto de conexão que representa a conexão com o banco de dados.

###conn.cursor(): Esta linha de código cria um objeto de cursor que você pode usar para executar operações SQL no banco de dados. O cursor é obtido a partir do objeto de conexão que criamos anteriormente. Um cursor é como uma "alavanca" que você usa para interagir com o banco de dados: você executa comandos SQL através do cursor e ele retorna resultados para você. Você pode pensar nele como uma "posição" em seu banco de dados, permitindo que você mova e interaja com os dados armazenados nele.

###Cursor.execute(): Este é um método utilizado para executar uma instrução SQL no banco de dados SQLite. Ele recebe como argumento uma string contendo a instrução SQL que deseja executar.

#CREATE TABLE IF NOT EXISTS usuarios: Esta é a instrução SQL para criar uma tabela chamada usuarios, se ela ainda não existir. A cláusula IF NOT EXISTS garante que a tabela só será criada se ainda não existir no banco de dados.

#cursor.execute("INSERT INTO usuarios (nome, peso, altura, imc) VALUES (?, ?, ?, ?)", (nome, peso, altura, imc)): cursor.execute(): Este método é usado para executar uma instrução SQL no banco de dados através do cursor. Ele recebe dois argumentos: a instrução SQL a ser executada e os valores a serem inseridos na instrução SQL.

#"INSERT INTO usuarios (nome, peso, altura, imc) VALUES (?, ?, ?, ?)": Esta é uma instrução SQL de inserção de dados na tabela usuarios. Ela indica que você está inserindo valores nas colunas nome, peso, altura e imc da tabela usuarios. O uso de ? como marcador de posição indica que os valores a serem inseridos serão fornecidos separadamente.

#(nome, peso, altura, imc): Este é um tuplo contendo os valores a serem inseridos nas colunas da tabela usuarios. Os valores são passados como argumentos para a instrução SQL, substituindo os marcadores de posição ? na ordem em que aparecem na instrução SQL. Por exemplo, o valor nome será inserido na primeira posição ?, peso na segunda posição ?, e assim por diante.

#Essa linha de código executa uma instrução SQL de inserção de dados na tabela usuarios, com os valores fornecidos nas variáveis nome, peso, altura e imc.

#conn.commit(): Este método é usado para confirmar as alterações feitas no banco de dados desde a última operação de commit. Quando você executa operações que modificam o banco de dados, como inserções, atualizações ou exclusões, essas mudanças são temporárias até que você as confirme com um commit.
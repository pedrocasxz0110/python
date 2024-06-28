class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0

    def verificar_situacao(self):
      media = self.calcular_media()
      if media >= 6.0:
          return "Aprovado"
      else:
          return "Reprovado"


lista_alunos = []

while True:
    nome_aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    if nome_aluno.lower()=="fim":
        break

    matricula_aluno = input("Digite a matricula do aluno: ")
    
# Lê as notas do aluno

    notas_do_aluno = []

    while True:
        nota = input("Digite uma nota (ou 'fim' para encerrar): ")      
        if nota.lower() == "fim":
            break
        notas_do_aluno.append(float(nota))
        
    aluno = Aluno(nome_aluno, matricula_aluno, notas_do_aluno)
    lista_alunos.append(aluno)
    
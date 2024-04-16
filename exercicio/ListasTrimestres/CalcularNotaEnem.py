def calcular_media_enem():
    while True:
        linguagens = float(input("Digite a nota de Linguagens: "))
        ciencias_humanas = float(input("Digite a nota de Ciências Humanas: "))
        ciencias_natureza = float(input("Digite a nota de Ciências da Natureza: "))
        matematica = float(input("Digite a nota de Matemática: "))
        redacao = float(input("Digite a nota de Redação: "))

        if not (0 <= linguagens <= 1000) or not (0 <= ciencias_humanas <= 1000) \
                or not (0 <= ciencias_natureza <= 1000) or not (0 <= matematica <= 1000) \
                or not (0 <= redacao <= 1000):
            print("Por favor, insira notas válidas entre 0 e 1000.")
            continue

        media = (linguagens + ciencias_humanas + ciencias_natureza + matematica + redacao) / 5

        if media >= 450:
            print(f"Média final: {media:.2f}")
            print("Status de aprovação: Aprovado para o Prouni e Fies.")
        else:
            print(f"Média final: {media:.2f}")
            print("Status de aprovação: Reprovado para o Prouni e Fies.")
            
        break

calcular_media_enem()

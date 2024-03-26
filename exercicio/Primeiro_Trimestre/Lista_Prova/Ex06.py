def soma_tres_numeros(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado = soma_tres_numeros(numero1, numero2, numero3)
print("A soma dos três números é:", resultado)

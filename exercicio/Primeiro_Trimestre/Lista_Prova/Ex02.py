numero = int(input("Digite um número menor 100: "))
if numero>=100:
    print("O número digitado é maior que 100")
else:
    dezena = numero//10
    unidade=numero%10
soma_digitos=dezena+unidade
print("A soma dos dígitos de", numero, "é igual a", soma_digitos)

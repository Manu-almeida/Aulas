while True:
    numero = int(input("Digite um numero positivo: "))

    if numero < 0:
        print("O número deve ser POSITIVO")
        continue
    else:
        print("Parabéns o número é POSITIVO")
    break

#correção
numero = int(input("Digite um numero positivo: "))
while numero <= 0:
    print("Valor inválido")
    nuemero = int(input("Digite um numero positivo: "))
    print(f"Voce digitou: {numero}")
# Recebe três números inteiros como entrada
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Verifica se os números estão em ordem crescente
if numero1 < numero2 < numero3:
    print("crescente")
else:
    print("não está em ordem crescente")

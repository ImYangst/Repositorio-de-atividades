import random

def rolar_dados(numero):

    valor = random.randint(1,numero)

    print(f"Rodando um dado d{numero}")
    print(f"Resultado: {valor}")

numero = int(input("Insira o valor do dado:\n>>> "))

rolar_dados(numero)
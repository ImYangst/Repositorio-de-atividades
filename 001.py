import random

opcoes = ["pedra", "papel", "tesoura"]

opcao_computador = random.choice(opcoes)

opcao_normalizada = input("Digite sua jogada (Pedra, papel ou tesoura)\n>>> ").lower()

print(f"Você escolheu: {opcao_normalizada}")
print(f"O computador escolheu: {opcao_computador}")

if opcao_normalizada == opcao_computador:
    print(f"Empate! Ambos escolheram {opcao_normalizada}")
elif opcao_normalizada == "pedra":
    if opcao_computador == "tesoura":
        print("Parabéns! Pedra quebra tesoura!")
    else:
        print("Que pena! Não foi dessa vez.")
elif opcao_normalizada == "papel":
    if opcao_computador == "pedra":
        print("Parabéns! Papel cobre a pedra!")
    else:
        print("Que pena! Não foi dessa vez.")
elif opcao_normalizada == "tesoura":
    if opcao_computador == "papel":
        print("Parabéns! Tesoura corta o papel!")
    else:
        print("Que pena! Não foi dessa vez.")
else:
    print("Opção inválida!")
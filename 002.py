import time

def print_velha(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\n")


def print_pontuação(pontuação):
    print("\t--------------------------------")
    print("\t              Pontuação        ")
    print("\t--------------------------------")

    jogadores = list(pontuação.keys())
    print(f"\t    {jogadores[0]}\t    {pontuação[jogadores[0]]}")
    print(f"\t    {jogadores[1]}\t    {pontuação[jogadores[1]]}")

    print("\t--------------------------------\n")

def checar_vitória(pos_jogador, jogador_atual):
    solucoes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in solucoes:
        if all(y in pos_jogador[jogador_atual] for y in x):
            return True
    return False

def empate(pos_jogador):
    if len(pos_jogador['X']) + len(pos_jogador['O']) == 9:
        return True
    return False

def jogo(jogador_atual):
    values = [' ' for x in range(9)]

    pos_jogador = {'X':[], 'O':[]}

    while True:
        print_velha(values)

        try:
            print("Vez de ", jogador_atual, "Qual posição deseja jogar?\n>>> ", end="")
            jogada = int(input())
        except ValueError:
            print("Valor inválido!!! Tente novamente.")
            continue

        if jogada < 1 or jogada > 9:
            print("Valor inválido!!! Tente novamente")
            continue

        if values[jogada-1] != ' ':
            print("Posição já ocupada. Tente novamente!!")
            continue

        values[jogada-1] = jogador_atual

        pos_jogador[jogador_atual].append(jogada)

        if checar_vitória(pos_jogador, jogador_atual):
            print_velha(values)
            print(f"Jogador {jogador_atual}, venceu o jogo!!")
            print("\n")
            time.sleep(2)
            return jogador_atual
        
        if empate(pos_jogador):
            print_velha(values)
            print("Empate!")
            print("\n")
            return 'E'
        
        if jogador_atual == 'X':
            jogador_atual = 'O'
        else:
            jogador_atual = 'X'

if __name__ == "__main__":

    print("Jogador 1")
    jogador1 = input("Escreva seu nome:\n>>> ")
    print("\n")

    print("Jogador 2")
    jogador2 = input("Escreva seu nome:\n>>> ")
    print("\n")

    jogador_atual = jogador1

    escolha_jogador = {'X' : "", 'O' : ""}

    opcoes = ['X' , 'O']

    pontuação = {jogador1: 0, jogador2: 0}
    print_pontuação(pontuação)

    while True:
        print(f"Vez de {jogador_atual} escolher!" )
        print("Escolha 1 para X")
        print("Escolha 2 para O")
        print("Escolha 3 para Sair")
        
        try:
            escolha = int(input())
        except ValueError:
            print("Valor inválido!! Tente novamente\n")
            continue

        if escolha == 1:
            escolha_jogador['X'] = jogador_atual
            if jogador_atual == jogador1:
                escolha_jogador['O'] = jogador2
            else:
                escolha_jogador['O'] = jogador1
        elif escolha == 2:
            escolha_jogador['O'] = jogador_atual
            if jogador_atual == jogador1:
                escolha_jogador['X'] = jogador2
            else:
                escolha_jogador['X'] = jogador1
        elif escolha == 3:
            print("Pontuação final")
            print_pontuação(pontuação)
            break
        else:
            print("Escolha inexistente!!!! Tente novamente.")

        vencedor = jogo(opcoes[escolha-1])

        if vencedor != 'E':
            jogador_vencedor = escolha_jogador[vencedor]
            pontuação[jogador_vencedor] = pontuação[jogador_vencedor] + 1

        print_pontuação(pontuação)

        if jogador_atual == jogador1:
            jogador_atual = jogador2
        else:
            jogador_atual = jogador1
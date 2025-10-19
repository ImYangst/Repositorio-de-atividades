import time
import os

class Tarefa:
    def __init__(self, descricao, status = 'pendente'):
        self.descricao = descricao
        self.status = status
    def concluir(self):
        self.status = "concluido"
    def __str__(self):
        return f"[{self.status}] -> [{self.descricao}]"

tarefas = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_tarefas():
    arquivo = 'tarefas.txt'
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            infos = f.read().splitlines()
            lista_objetos = []
            for linha_atual in infos:
                descricao,status = linha_atual.split(';')
                tarefa1 = Tarefa(descricao,status)
                lista_objetos.append(tarefa1)
            return lista_objetos
    else:
        print("Nenhuma tarefa para ser carregada")
        return []

def salvar_tarefa(tarefas):
    with open('tarefas.txt', "w") as f:
        for item in tarefas:
            descricao = item.descricao
            status = item.status
            f.write(f"{descricao};{status}\n")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada")
        time.sleep(1.5)
    else:
        for indice, item in enumerate(tarefas):
            print(f"{indice + 1}.{item}")
        time.sleep(2)

def concluir_tarefas(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        time.sleep(1)
        concluir_num = int(input("Coloque um número:\n>>> "))
        indice = concluir_num - 1
        objeto_tarefa = tarefas[indice]
        objeto_tarefa.concluir()
        print("Tarefa concluida com sucesso!!")
        time.sleep(1)
    except ValueError:
        print("Erro! Entrada invalida")
        time.sleep(1)
    except IndexError:
        print("Erro! Essa tarefa não existe")
        time.sleep(1)

def adicionar_tarefas(tarefas):
    descricao = input("Informe nova tarefa:\n>>> ")
    nova_tarefa = Tarefa(descricao)
    tarefas.append(nova_tarefa)
    time.sleep(1)

info = carregar_tarefas()

while True:
    limpar_tela()
    print("-----------tarefas----------")
    print("[1] Para adiconar nova tarefa")
    print("[2] Para listar tarefas existentes")
    print("[3] Para concluir sua tarefa")
    print("[4] Para sair do programa")
    escolha = int(input("insira o numero desejado:\n>>> "))
    match escolha:
        case 1: 
            print("Opção escolhida: Adicionar nova tarefa.")
            adicionar_tarefas(info)
            salvar_tarefa(info)
        case 2:
            print("Opção escolhida: Listar tarefas.")
            listar_tarefas(info)
        case 3:
            print("Opção escolhida: Concluir tarefas.")
            concluir_tarefas(info)
            salvar_tarefa(info)
        case 4:
            print("Opção escolhida: Sair.")
            break

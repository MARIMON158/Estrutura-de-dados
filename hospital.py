
#TRABALHO ESTRUTURA DE DADOS MARIANA


class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor.upper()
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, novo_nodo):
        if self.head is None:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if self.head is None or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").strip().upper()
        numero = input("Informe o número do cartão: ").strip()

        try:
            numero = int(numero)
        except:
            print("Número inválido.")
            return

        novo_nodo = Nodo(numero, cor)
        if self.head is None:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)
        else:
            print("Cor inválida.")

    def imprimirListaEspera(self):
        atual = self.head
        print("Lista -> ", end="")
        while atual:
            print(f"[{atual.cor},{atual.numero}]", end=" ")
            atual = atual.proximo
        print()

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
        else:
            print(f"Atendendo o paciente cartão cor {self.head.cor} e número {self.head.numero}")
            self.head = self.head.proximo
            
fila = ListaEncadeada()

while True:
    print("1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - sair")
    opcao = input(">>")

    if opcao == '1':
        fila.inserir()
    elif opcao == '2':
        fila.imprimirListaEspera()
    elif opcao == '3':
        fila.atenderPaciente()
    elif opcao == '4':
        break
    else:
        continue

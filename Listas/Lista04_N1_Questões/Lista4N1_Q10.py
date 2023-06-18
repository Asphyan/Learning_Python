class Node:
    def __init__(self, data):
        self.data = data
        self.proximo = None
        self.anterior = None


class ListaEncadeadaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def esta_vazia(self):
        return self.inicio is None

    def inserir_no_inicio(self, data):
        novo_no = Node(data)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no

    def inserir_no_final(self, data):
        novo_no = Node(data)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no

    def remover_do_inicio(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return
        data = self.inicio.data
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        return data

    def remover_do_final(self):
        if self.esta_vazia():
            print("A lista está vazia. Não é possível remover elementos.")
            return
        data = self.fim.data
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        return data

    def exibir(self):
        if self.esta_vazia():
            print("A lista está vazia.")
        else:
            atual = self.inicio
            while atual:
                print(atual.data, end=" ")
                atual = atual.proximo
            print()


# Criação de uma lista encadeada dupla
lista = ListaEncadeadaDupla()

lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_inicio(1)

lista.inserir_no_final(4)
lista.inserir_no_final(5)
lista.inserir_no_final(6)

print("Lista original:")
lista.exibir()

lista.remover_do_inicio()
print("Após remover do início:")
lista.exibir()

lista.remover_do_final()
print("Após remover do final:")
lista.exibir()

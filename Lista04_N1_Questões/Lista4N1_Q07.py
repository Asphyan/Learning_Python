class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_inicio(self, dado):
        novo_no = No(dado)

        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no

    def inserir_final(self, dado):
        novo_no = No(dado)

        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def remover_inicio(self):
        if self.primeiro is None:
            return None

        no_removido = self.primeiro
        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

        return no_removido.dado

    def remover_final(self):
        if self.primeiro is None:
            return None

        no_atual = self.primeiro
        no_anterior = None

        while no_atual.proximo is not None:
            no_anterior = no_atual
            no_atual = no_atual.proximo

        if no_anterior is None:
            self.primeiro = None
            self.ultimo = None
        else:
            no_anterior.proximo = None
            self.ultimo = no_anterior

        return no_atual.dado

    def exibir_lista(self):
        no_atual = self.primeiro

        while no_atual is not None:
            print(no_atual.dado, end=" -> ")
            no_atual = no_atual.proximo

        print("None")


# Exemplo de uso:
lista = ListaEncadeada()

lista.inserir_inicio(3)
lista.inserir_inicio(2)
lista.inserir_inicio(1)
lista.inserir_final(4)
lista.inserir_final(5)

lista.exibir_lista()  # Saída: 1 -> 2 -> 3 -> 4 -> 5 -> None

lista.remover_inicio()
lista.remover_final()

lista.exibir_lista()  # Saída: 2 -> 3 -> 4 -> None

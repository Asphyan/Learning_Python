class Fila:
    def __init__(self):
        self.fila = []

    def inserir(self, elemento):
        self.fila.append(elemento)

    def remover(self):
        if not self.vazia():
            return self.fila.pop(0)
        else:
            print("A fila está vazia.")

    def mostrar(self):
        if not self.vazia():
            print("Fila:", self.fila)
        else:
            print("A fila está vazia.")

    def frente(self):
        if not self.vazia():
            return self.fila[0]
        else:
            print("A fila está vazia.")

    def vazia(self):
        return len(self.fila) == 0
    
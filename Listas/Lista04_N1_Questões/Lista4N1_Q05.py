class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0

    def inserir(self, elemento):
        if self.tamanho() == self.capacidade - 1:
            print("A fila está cheia.")
        else:
            self.fila[self.fim] = elemento
            self.fim = (self.fim + 1) % self.capacidade

    def remover(self):
        if self.tamanho() == 0:
            print("A fila está vazia.")
        else:
            elemento = self.fila[self.inicio]
            self.fila[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.capacidade
            return elemento

    def vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        if self.fim >= self.inicio:
            return self.fim - self.inicio
        else:
            return self.capacidade - self.inicio + self.fim

fila = FilaCircular(5)

fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
fila.remover()

print("Elementos da fila:")
while not fila.vazia():
    print(fila.remover())

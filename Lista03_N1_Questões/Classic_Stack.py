# Criando uma Pilha simples.

class Pilha:
    def __init__(self):
        self.itens = []
    
    def vazia(self):
        return len(self.itens) == 0
    
    def empilhar(self, itens):
        return self.itens.append(itens)
    
    def top(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None
    
    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None
    def tamanho(self):
        return len(self.itens)


pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

print(pilha.tamanho())
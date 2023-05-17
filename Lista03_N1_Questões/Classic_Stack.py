class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        if not self.is_empty():
            return self.pilha.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.pilha[-1]
        return None

    def is_empty(self):
        return len(self.pilha) == 0
    
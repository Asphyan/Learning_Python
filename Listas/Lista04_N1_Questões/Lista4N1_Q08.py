class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def criar_lista_encadeada_inversa(numeros):
    head = None
    for numero in numeros:
        novo_no = Node(numero)
        novo_no.next = head
        head = novo_no
    return head


def exibir_lista_encadeada(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


numeros = input("Digite os números inteiros separados por espaço: ").split()
numeros = [int(numero) for numero in numeros]

head = criar_lista_encadeada_inversa(numeros)

print("Lista encadeada em ordem inversa:")
exibir_lista_encadeada(head)

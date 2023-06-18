class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.next = None


class Cliente:
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo


class ListaClientes:
    def __init__(self):
        self.head = None

    def inserir_cliente(self, cliente):
        novo_no = Node(cliente)
        novo_no.next = self.head
        self.head = novo_no

    def remover_cliente(self, nome):
        if self.head is None:
            print("A lista está vazia. Não é possível remover cliente.")
            return

        if self.head.cliente.nome == nome:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        while current and current.cliente.nome != nome:
            previous = current
            current = current.next

        if current:
            previous.next = current.next
        else:
            print("Cliente não encontrado.")

    def pesquisar_cliente(self, nome):
        current = self.head
        while current:
            if current.cliente.nome == nome:
                return current.cliente
            current = current.next
        return None

    def exibir_tabela(self):
        if self.head is None:
            print("A lista está vazia.")
            return

        print("Nome\t\tNúmero da Conta\tSaldo")
        print("==============================================")
        current = self.head
        while current:
            cliente = current.cliente
            print(f"{cliente.nome}\t\t{cliente.numero_conta}\t\t{cliente.saldo}")
            current = current.next
        print()


# Criação da lista de clientes
lista_clientes = ListaClientes()

cliente1 = Cliente("João", 1001, 5000)
cliente2 = Cliente("Maria", 1002, 3000)
cliente3 = Cliente("Pedro", 1003, 2000)

lista_clientes.inserir_cliente(cliente1)
lista_clientes.inserir_cliente(cliente2)
lista_clientes.inserir_cliente(cliente3)

# Exibição da tabela de clientes
print("Lista de clientes:")
lista_clientes.exibir_tabela()

# Remoção de um cliente
lista_clientes.remover_cliente("Maria")

print("Lista de clientes após remover 'Maria':")
lista_clientes.exibir_tabela()

# Pesquisa de um cliente
cliente_pesquisado = lista_clientes.pesquisar_cliente("Pedro")
if cliente_pesquisado:
    print("Cliente encontrado:")
    print("Nome:", cliente_pesquisado.nome)
    print("Número da Conta:", cliente_pesquisado.numero_conta)
    print("Saldo:", cliente_pesquisado.saldo)
else:
    print("Cliente não encontrado.")


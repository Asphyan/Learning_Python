from Classic_Queue_Q01 import Fila

fila = Fila()

while True:
    print("\n--- Menu ---")
    print("1. Adicionar número na fila")
    print("2. Remover número da fila")
    print("3. Tamanho da fila")
    print("4. Mostrar fila")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero = int(input("Digite o número a ser adicionado na fila: "))
        fila.inserir(numero)
        print("Número adicionado na fila.")

    elif opcao == "2":
        numero_removido = fila.remover()
        if numero_removido is not None:
            print("Número removido da fila:", numero_removido)

    elif opcao == "3":
        tamanho = fila.tamanho()
        print("Tamanho da fila:", tamanho)

    elif opcao == "4":
        fila.mostrar()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

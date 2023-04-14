'''
Crie um cadastro de pessoas que permita:
cadastrar;
Editar;
Mostar/Pesquisar;
Excluir;
'''
import os

print('\nBem vindo ao cadastro!\n')
print('Aqui você poderá fazer o cadastro de pessoas com seus dados específicos.')

while True:
    print('O que gostaria de fazer?\n\n1 - Cadastrar.\t2 - Editar.\n3 - Pesquisar.\t4 - Excluir.\n5 - Encerrar.\n')
    entry = int(input('Digite aqui: '))
    os.system('cls')

    if entry == 1:
        lista = int(
            input('Digite o tamanho da lista de pessoas que deseja adicionar: '))
        dados = []
        os.system('cls')

        for i in range(lista):
            print(f'{i+1}° Pessoa da lista\n')
            nome = input('Digite seu nome: ')
            idade = int(input('Digite sua idade: '))
            email = input('Digite seu e-mail: ')
            '''
            Os dois parenteses indicam que está sendo armazenado como uma tupla,
            porque no Python é necessário agrupar múltiplos valores em uma tupla, 
            antes de passá-los como um único argumento para a função
            '''
            dados.append((nome, idade, email))
            os.system('cls')
    elif entry == 2:
        # Recebe o índice para ser buscado na matriz dados.
        index = int(
            input('Digite o índice do do número da pessoa que deseja editar: '))
        os.system('cls')
        # Verifica se o índice é menor que o número de itens da matriz, e abre o índice indicado pelo usuário.
        if index < len(dados):
            print(f'{index+1}° pessoa da lista está disponível para edição.\n')
            print(f'Nome: {dados[index][0]}')
            print(f'Idade: {dados[index][1]}')
            print(f'E-mail: {dados[index][2]}')

            print('\nAbaixo segue os inputs para atualização dos dados.\n')

            nome = input('Digite o novo nome: ')
            idade = int(input('Digite a nova idade: '))
            email = input('Digite o novo E-mail: ')
            # Armazena as novas informações no indice.
            dados[index] = [nome, idade, email]
            os.system('cls')
    elif entry == 3:
        print('Informe como deseja realizar a pesquisa:\n\n1 - Índice.\t2 - Nome.\t3 - Mostrar toda a lista.')
        search = int(input('Digite aqui: '))
        os.system('cls')
        if search == 1:
            index = int(input('Digite o ídice que deseja buscar: '))
            if index < len(dados):
                print(f'{index+1}° pessoa da lista é:\n')
                print(f'Nome: {dados[index][0]}')
                print(f'Idade: {dados[index][1]}')
                print(f'E-mail: {dados[index][2]}')
                os.system('cls')
        if search == 2:
            nome = input('Digite o nome que deseja buscar: ')
            for i in range(len(dados)):
                if dados[i][0] == nome:
                    print(f'Dados relacionados ao nome: {nome}')
                    print(f'Nome: {dados[i][0]}')
                    print(f'Idade: {dados[i][1]}')
                    print(f'E-mail: {dados[i][2]}')
                    os.system('cls')
        if search == 3:
            for dados in dados:
                print(f'Nome: {dados[0]}')
                print(f'Idade: {dados[1]}')
                print(f'E-mail: {dados[2]}')
                print('----------')
    elif entry == 5:
        print('Programa encerrado.')
        break

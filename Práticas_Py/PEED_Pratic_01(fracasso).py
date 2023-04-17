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
    print('O que gostaria de fazer?\n\n1 - Cadastrar(Nova lista).\n2 - Editar.\t3 - Pesquisar.\n4 - Excluir.\t5 - Encerrar.\n')
    entry = int(input('Digite aqui: '))
    os.system('cls')

    if entry == 1:
        lista = int(input('Digite o tamanho da lista de pessoas que deseja adicionar: '))
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
        print('O que gostaria de fazer?\n\n1 - Adicionar novo item a lista.\t2 - Editar um existente.\n')
        edit = int(input('Digite aqui: '))
        os.system('cls')
        if edit == 1:
            lista = int(input('Digite a quantidade de pessoas que deseja adicionar: '))
            dados2 = []
            os.system('cls')

            for i in range(lista):
                print(f'{i+1}° Pessoa da lista\n')
                nome = input('Digite seu nome: ')
                idade = int(input('Digite sua idade: '))
                email = input('Digite seu e-mail: ')
                dados2.append((nome, idade, email))
                dados = dados + dados2
                os.system('cls')
            print ('Lista atualizada!\n')
            for dados in dados:
                print(f'Nome: {dados[0]}')
                print(f'Idade: {dados[1]}')
                print(f'E-mail: {dados[2]}')
                print('----------')

        if edit == 2:
            # Recebe o índice para ser buscado na matriz dados.
            index = int(input('Digite o índice do do número da pessoa que deseja editar: '))
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
            dados[index] = (nome, idade, email)
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
    elif entry == 4:
        '''
         'enumerate()' é usada para iterar sobre uma sequência e gerar pares de valores,
          cada um consistindo em um índice e um elemento correspondente da sequência.
        '''
        for indice, i in enumerate(dados):
                print(f'{indice}\n')
                print(f'Nome: {dados[0]}')
                print(f'Idade: {dados[1]}')
                print(f'E-mail: {dados[2]}')
                print('----------')
        delete = int(input('Digite o índice da lista que deseja excluir: '))
        del dados[i] # 'del' remove o item na posição que o usuário informar.
        if delete >= 0:
            print('Item excluído com sucesso!')
    elif entry == 5:
        print('Programa encerrado.')
        break

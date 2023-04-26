'''
Crie um cadastro de pessoas que permita:
cadastrar;
Editar;
Mostar/Pesquisar;
Excluir;
'''
import os

dados = {}


def cadastro():
    try:
        lista = int(input('Quantas pessoas vai cadastrar?.: '))
        os.system('cls')
        for i in range(lista):
            print(f'{i+1}° pessoa a cadastrar\n')
            nome = input('Digite seu nome: ')
            idade = int(input('Digite sua idade: '))
            email = input('Digite seu email: ')
            dado = {'Nome': nome, 'Idade': idade, 'E-mail': email}
            dados[nome] = dado
            os.system('cls')
            print('Cadastro efetuado com sucesso!\n')
    except ValueError:
        print('O valor digitado é inválido!')


def editar():
    nome = input('Nome da pessoa que gostaria de editar: ')
    if nome in dados:
        # 'dado' irá armazenar e atualizar itens específicos solicitados do dicionário.
        # Além de ser usado para acessar uma linha específica do dicionário.
        dado = dados[nome]
        print('Escolha o que gostaria de editar: ')
        print('1 - Nome')
        print('2 - Idade')
        print('3 - E-mail')
        op = int(input('Escolha uma das opções acima: '))
        if op == 1:
            novo_nome = input('Novo nome: ')
            dado['nome'] = novo_nome
            # "pop" é usado para remover o item com a chave antiga e retornar o valor associado a essa chave.
            # Já que o item chave desse dicionário está sendo nome.
            dados[novo_nome] = dados.pop(nome)
            print('Nome alterado com sucesso!!!')
        elif op == 2:
            nova_idade = int(input('Nova idade: '))
            dado['Idade'] = nova_idade
        elif op == 3:
            novo_email = input('Novo E-mail: ')
            dado['E-mail'] = novo_email
        else:
            print('Nome não encontrado!')


def pesquisar():
    print('Escolha uma das opções abaixo:\n')
    print('1 - Mostrar todos os cadastros.')
    print('2 - Pesquisar nome específico.')
    op = int(input('\nDigite aqui: '))
    os.system('cls')
    if op == 1:
        # 'items()' é usado para obter uma lista dos pares chave-valor do dicionário.
        #  Em cada iteração do loop, o nome da chave é atribuído à variável nome, e o valor correspondente é atribuído à variável dado.
        for nome, dado in dados.items():
            print('Nome: ', dado['Nome'])
            print('Idade: ', dado['Idade'])
            print('E-mail: ', dado['E-mail'])
            print('----------')
    if op == 2:
        nome = input('Digite o nome que deseja perquisar: ')
        if nome in dados:
            dado = dados[nome]
            print('\nNome:', dado['Nome'])
            print('Idade:', dado['Idade'])
            print('Email:', dado['E-mail'])
        else:
            print('Nome não encontrado!')


def excluir():
    for nome, dado in dados.items():
        print('Nome: ', dado['Nome'])
        print('Idade: ', dado['Idade'])
        print('E-mail: ', dado['E-mail'])
        print('----------')
    try:
        nome = input('\nDigite o nome que deseja excluir: ')
        os.system('cls')
        if nome in dados:
            del dados[nome]
            print('Item excluído com sucesso!')
        else:
            print('Nome não encontrado!')
    except ValueError:
        print('O valor digitado é inválido!')


while True:
    print('\nBem vindo ao cadastro!\n')
    print('Aqui você poderá fazer o cadastro de pessoas com seus dados específicos.')

    print('Escolha uma das opções abaixo:\n')
    print('1 - Cadastro')
    print('2 - Editar')
    print('3 - Pesquisar')
    print('4 - Exluir')
    print('5 - Encerrar')

    try:
        option = int(input('\nDigite a opção escolhida: '))
        os.system('cls')
        if option == 1:
            cadastro()
        elif option == 2:
            editar()
        elif option == 3:
            pesquisar()
        elif option == 4:
            excluir()
        elif option == 5:
            print('Programa Encerrado!')
            break
        else:
            print('Número inválido!')
    except ValueError:
        print('O valor digitado é inválido!')

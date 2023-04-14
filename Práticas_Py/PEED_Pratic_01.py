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
            dados.append(nome, idade, email)
            os.system('cls')
    if entry == 2:
    if entry == 5:
        print('Programa encerrado.')
        break

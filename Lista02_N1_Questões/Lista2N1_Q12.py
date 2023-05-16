'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
Em seguida, verifique se o nome 'Maria' está presente na tupla.
'''

lista = []

print('Digite 3 Nomes')

for i in range(3):
    nome = input(f'Digite o {i+1}° nome: ')
    lista.append(nome)

tt = tuple(lista)

if 'Maria' in tt:
    print('Maria está presente na tupla')
else:
    print('Maria não está presente na tupla')

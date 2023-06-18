'''
Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, retorne os elementos de índice par da lista.
'''

lista = []

print('Digte 10 números')

for i in range(10):
    num = float(input(f'Digite o {i+1}° número: '))
    lista.append(num)

print('\nNúmeros apenas de índice par.\n')

for i in range(0, len(lista), 2):
    print('----------')
    print(lista[i])

print('----------')

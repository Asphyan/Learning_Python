'''
Peça para o usuário digitar 10 números e crie uma lista com esses números. 
Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.
'''

lista = []

print('Digite 10 números.\n')

for i in range(10):
    num = float(input(f'Digite o {i+1}° número: '))
    lista.append(num)

nova_lista = []

for i in lista:
    i = i * 2
    nova_lista.append(i)

print('')
print(lista,'\n')
print(nova_lista)

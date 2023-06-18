'''
Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, adicione esses números à lista utilizando um loop for.
'''

lista = []

for i in range(10):
    num = float(input(f'Digite o {i+1}° número: '))
    lista.append(num)

print(lista)

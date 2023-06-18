'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, verifique se o número 3 está presente no conjunto.
'''

conj = set([])

print('Digite 5 números.')

for i in range(5):
    num = float(input(f'Digite o {i+1}° número: '))
    conj.add(num)

if 3 in conj:
    print('o número três está presente no conjunto.')
else:
    print('o número três não está presente no conjunto.')
    
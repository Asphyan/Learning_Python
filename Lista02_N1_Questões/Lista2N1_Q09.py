'''
Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
Em seguida, remova todos os números pares do conjunto.
'''

conj = set([])

print('Digite 10 números\n')
for i in range(10):
    num = float(input(f'Digite o {1+i}° número: '))
    if num % 2 != 0:
        conj.add(num)

print(conj)

# Uma segunda maneira.

conj = set([])

print('Digite 10 números\n')
for i in range(10):
    num = float(input(f'Digite o {1+i}° número: '))
    conj.add(num)

impares = set([])
for i in conj:
    if i % 2 != 0:
        impares.add(i)

print(impares)

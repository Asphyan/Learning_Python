lista = int(input('Digite a quantidade de itens da lista: '))

impares = []

for i in range(0, lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num % 2 != 0:
        impares.append(num)

print(impares)

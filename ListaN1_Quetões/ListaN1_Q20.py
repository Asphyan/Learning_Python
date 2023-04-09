# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.

lista = int(input('Digite o tamanho da lista: '))

numeros = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    numeros.append(num)

# 'reverse=True' é usado para inverter a ordem dá lista.
# 'reverse=True' vem como padrão definido como False.
# Não faço a menor ideia do por que do 'T'/'F' ser obrigatoriamente maiúsculo.
decrescente = sorted(numeros, reverse=True)

print ('Ordem do usuário: ', numeros)
print ('Ordem decrescente: ', decrescente)

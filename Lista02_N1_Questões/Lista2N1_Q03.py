'''
Crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e adicione esses dados ao dicionário.
Em seguida, peça para o usuário adicionar mais uma chave e um valor e adicione esses dados ao dicionário também.
'''

dic = {}

print('Criador de dicionário em Python.\n')

print('Primeiro digite sua chave.')
chave = input('Digite aqui: ')
num = int(input('Digite um número: '))
dic[chave] = num

print('Digite uma segunda chave.')
chave2 = input('Digite aqui: ')
num2 = int(input('Digite um número: '))
dic[chave2] = num2

print(dic)

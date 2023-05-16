'''
Crie um dicionário vazio. 
Peça para o usuário digitar as chaves e os valores desse dicionário.
Em seguida, retorne o valor da chave 'idade'.
'''

dic = {}

print('Criador de dicionário em Python.\n')

quant = int(input('Digite quantas chave/valor quer adicionar: '))

for i in range(quant):
    chave = input('Digite sua chave: ')
    valor = float(input('Digite um número: '))
    dic[chave] = valor

dic['idade'] = int(input('(Chave idade) digite sua idade: '))
idade = dic['idade']

print('sua idade é',idade)

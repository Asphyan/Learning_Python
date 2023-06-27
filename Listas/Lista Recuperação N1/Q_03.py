'''
Uma loja deseja calcular o desconto a ser aplicado em um produto segundo a idade do cliente. 
Se o cliente tiver menos de 21 anos, o desconto será de 15%. 
Caso contrário, o desconto será de 10%. 
Escreva uma função em Python chamada "calcular_desconto" que recebe a idade do cliente como parâmetro e 
retorna o valor do desconto a ser aplicado.
'''

def calcular_desconto(idade, idade_min):
    if idade < idade_min:
        print(f'Desconto de 15%!!! (menores de {idade_min})')
    else:
        print(f'Desconto de 10%!!! (maiores de {idade_min})')

print('## Verificador de descontos ##')

idade = int(input('Informe sua idade: '))

calcular_desconto(idade, 21)

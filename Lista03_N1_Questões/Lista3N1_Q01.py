'''
Escreva um programa que leia uma expressão matemática na forma de string e 
utilize uma pilha para verificar se os parênteses estão balanceados.
'''

def verificador(expressao):
    
    pilha = []
    
    for item in expressao:
        if item == '(':
            pilha.append(item)
        elif item == ')':
            if len(pilha) == 0:
                return False
            pilha.pop()
    
    return len(pilha) == 0

expressao = input("Digite uma expressão: ")

if verificador(expressao):
    print("Estão balanceados.")
else:
    print("Não estão desbalanceados.")

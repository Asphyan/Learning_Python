from Classic_Queue_Q01 import Fila

def verifica_palindromo(frase):
    fila = []

    for caractere in frase:
        fila.append(caractere)

    inverso = []

    while len(fila) > 0:
        inverso.append(fila.pop())

    inverso_frase = ''.join(inverso)
    frase = frase.replace(" ", "")

    if frase == inverso_frase:
        return True
    else:
        return False


frase = input("Digite uma frase: ").lower()

if verifica_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
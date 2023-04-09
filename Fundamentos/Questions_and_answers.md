# Nível Básico #

# A - Qual a função da palavra-chave print em Python?

R: Usamos a função print para mostrar dados na tela dos usuários, através do terminal. Além disso, é muito comum em nosso dia a dia de Desenvolvedor utilizá-lo como forma de inspecionar o código, também chamado de Debug.

# B - Qual é a sintaxe básica para imprimir uma mensagem na tela usando o print?

R: print('O que será mostrado na tela')

# C - Como se define uma variável em Python?

R: Para declaração de variáveis, no Python é um processo simples. Basta definir o nome da variável e, em seguida, atribuir o valor desejável. Em Python, os tipos de dados, para atribuir um número digitado pelo usuário em uma variável, é necessário especificar se o número é inteiro ou real.

Ex1.: x = int(input('Digite sua variável'))
Ex2.: y = 10

# D - Quais são os tipos de dados básicos em Python?

R:  Inteiro (int)
    Ponto Flutuante ou Decimal (float)
    Tipo Complexo (complex)
    String (str)
    Boolean (bool)
    List (list)
    Tuple (tuple)
    Dictionary (dic)

# E - Qual é a diferença entre números inteiros (int) e números de ponto flutuante (float) em Python?

R: Em Python, números inteiros (int) são números inteiros sem casas decimais, positivos ou negativos. Eles são representados sem ponto decimal. Por exemplo, 1, 2, 3, -4 são inteiros. Eles são úteis para representar contagens, índices, identificadores, entre outros.

Já os números de ponto flutuante (float) em Python são números que possuem uma parte fracionária representada por um ponto decimal. Por exemplo, 1.0, 3.14, -2.5 são float. Eles são úteis para representar números reais e operações matemáticas que envolvem frações, como cálculos envolvendo dinheiro, medidas físicas, entre outros.

# F - Como se realiza uma operação matemática em Python?

R: Para realizar uma operação matemática em Python, você pode usar os operadores aritméticos padrão:

-- Adição (+): adiciona dois valores.
-- Subtração (-): subtrai dois valores.
-- Multiplicação (*): multiplica dois valores.
-- Divisão (/): divide um valor pelo outro, retornando um float.
-- Divisão inteira (//): divide um valor pelo outro, retornando um int (resultado arredondado para baixo).
-- Resto da divisão (%): retorna o resto da divisão entre dois valores.
-- Potência (**): eleva um valor à potência de outro valor.

Ex.: a = 10
     b = 5
     c = b + a
     print('c')

# G - Como se realiza a concatenação de strings em Python?

R: A concatenação de strings em Python é a união de duas ou mais strings em uma única string. Para concatenar strings em Python, você pode usar o operador de adição (+) ou o método join().

Usando o operador de adição (+):

nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo) # Output: "João Silva"

Neste exemplo, as variáveis "nome" e "sobrenome" contêm as strings "João" e "Silva", respectivamente. Ao usar o operador de adição (+), estamos concatenando as duas strings e adicionando um espaço em branco entre elas.

Usando o método join():

palavras = ["Isso", "é", "um", "exemplo"]
frase = " ".join(palavras)
print(frase) # Output: "Isso é um exemplo"

Neste exemplo, temos uma lista de strings "palavras" que contém as palavras "Isso", "é", "um" e "exemplo". Usando o método join(), estamos concatenando as strings da lista e adicionando um espaço em branco entre elas. Observe que o método join() é chamado na string que será usada como separador (neste caso, um espaço em branco).

É importante notar que as strings em Python são imutáveis, o que significa que você não pode modificar uma string existente. Em vez disso, ao concatenar strings, você está criando uma nova string que contém as strings originais. Por isso, é recomendável usar o método join() para concatenar grandes quantidades de strings, pois é mais eficiente do que usar o operador de adição (+) em um loop.


# ============================================================
# LISTAS E LOOPS — REFERÊNCIA RÁPIDA PARA A PROVA
# ============================================================
# LISTA: estrutura que guarda vários valores em sequência.
#   Sintaxe: minha_lista = [valor1, valor2, valor3]
#   Índice positivo começa em 0 (primeiro elemento = [0])
#   Índice negativo: [-1] = último, [-2] = penúltimo, etc.
#
# MÉTODOS PRINCIPAIS DE LISTA:
#   lista.append(x)   → adiciona x no FINAL da lista
#   lista.remove(x)   → remove a PRIMEIRA ocorrência de x
#   lista.sort()      → ordena a lista em ordem crescente (in-place)
#   lista.reverse()   → inverte a ordem (in-place)
#   lista.index(x)    → retorna o índice da PRIMEIRA ocorrência de x
#   lista + lista2    → concatena duas listas em uma nova lista
#   len(lista)        → retorna o número de elementos
#   sum(lista)        → soma todos os valores numéricos
#   max(lista)        → retorna o maior valor
#   min(lista)        → retorna o menor valor
#   list(range(a,b))  → cria lista de inteiros de a até b-1
# ============================================================

# 1 - Crie uma lista frutas contendo as seguintes frutas: "maçã", "banana", "laranja", "uva".
frutas = ["maçã", "banana", "laranja", "uva"]
# Criamos uma lista com 4 strings. Cada elemento fica em uma posição (índice).

# 2 - Imprima o primeiro e o último elemento da lista.
frutas[0]   # índice 0 = primeiro elemento → "maçã"
frutas[-1]  # índice -1 = último elemento  → "uva"

# 3 - Adicione a fruta "manga" ao final da lista.
frutas.append("manga")
# .append() insere o valor passado no FINAL da lista.
# Agora frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# 4 - Remova a fruta "banana" da lista.
frutas.remove("banana")
# .remove() busca o valor e remove a primeira ocorrência encontrada.
# Não usa índice — usa o próprio valor como argumento.

# 5 - Substitua "laranja" por "abacaxi".
frutas[1] = "abacaxi"
# Acesso por índice à esquerda do '=' faz substituição no lugar.
# frutas[1] era "laranja" → agora é "abacaxi"
frutas

# 6 Crie uma lista numeros contendo os números de 1 a 10.
nums = list(range(1,11))
# range(1, 11) gera os inteiros de 1 até 10 (o segundo parâmetro é EXCLUSIVO).
# list() converte o range para uma lista Python real.

# 7 Calcule e imprima a soma de todos os números da lista.
sum(nums)
# sum() percorre a lista e soma todos os elementos. Retorna o total.

# 8 - Encontre e imprima o maior e o menor número da lista.
max(nums)  # retorna o maior valor da lista
min(nums)  # retorna o menor valor da lista

# 9 - Inverta a ordem dos elementos na lista e imprima a lista invertida.
nums.reverse()
# .reverse() inverte a lista IN-PLACE (modifica a própria lista, não cria nova).
# Agora nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(nums)


# 10 - Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

# 11 - Ordene a lista cidades em ordem alfabética.
cidades.sort()
# .sort() ordena IN-PLACE em ordem crescente (alfabética para strings).
cidades

# 12 - Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append("Porto Alegre")

# 13 - Encontre o índice da cidade "Curitiba" na lista.
cidades.index("Curitiba")
# .index("Curitiba") retorna a posição numérica onde "Curitiba" está na lista.
# ATENÇÃO: a lista foi ordenada, então o índice pode ser diferente do original.

# 14 - Remova a cidade "Rio de Janeiro" da lista.
cidades.remove("Rio de Janeiro")

# 15 - Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# 16 - Concatene lista1 e lista2 em uma nova lista lista3.
lista3 = lista1 + lista2
# O operador '+' entre listas cria uma NOVA lista com todos os elementos de ambas.
# lista3 = [1, 2, 3, 4, 5, 6]

#17 - Imprima lista3.
print(lista3)

# 18 - Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].
animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

# 19 - Concatene as duas listas em uma nova lista todos_animais.
todos_animais = animais_domesticos + animais_selvagens
# todos_animais = ["cachorro", "gato", "coelho", "leão", "tigre", "urso"]

# 20 - Imprima todos animais
print(todos_animais)

# 21 - Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
nomes = ["Ana", "Pedro", "Maria", "João"]

# ============================================================
# LOOP FOR — percorre cada elemento de uma lista/sequência
# Sintaxe:
#   for variavel in lista:
#       bloco_de_codigo
#
# A variável recebe cada elemento da lista, um por vez.
# O bloco indentado (4 espaços) é executado para cada elemento.
# ============================================================

# 22 - Utilize um loop for para imprimir cada nome da lista.
for nome in nomes:
    # 'nome' assume cada valor: "Ana", depois "Pedro", "Maria", "João"
    print(nome)

#---------------------------------------------------
# 23 - Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.

nomes_maiusculos = []
# Criamos uma lista vazia para acumular os resultados.

for nome in nomes:
    nome_maiusculo = nome.upper()       # .upper() converte a string para MAIÚSCULAS
    nomes_maiusculos.append(nome_maiusculo)  # adiciona o resultado na nova lista

print(nomes_maiusculos)
# Resultado: ["ANA", "PEDRO", "MARIA", "JOÃO"]

#---------------------------------------------------
# 24 - Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares.

numeros = list(range(1,21))   # lista de 1 a 20
numeros_par = []              # lista acumuladora para os pares

for numero in numeros:
    if numero%2 == 0:
        # '%' é o operador módulo (resto da divisão).
        # numero % 2 == 0 significa "o resto de dividir por 2 é zero" → é par.
        numeros_par.append(numero)  # só adiciona se for par

print(numeros_par)

#---------------------------------------------------
# 25 - Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.

numeros_quadrado = []   # lista acumuladora

for numero in numeros:
    numero_quadrado = numero**2          # '**' é o operador de potência. 3**2 = 9
    numeros_quadrado.append(numero_quadrado)

print(numeros_quadrado)

#---------------------------------------------------
# 26 - Crie uma lista palavras contendo: "python", "java", "c", "javascript". Utilize um loop for para imprimir o tamanho (número de letras) de cada palavra.

palavras = ["python", "java", "c", "javascript"]

for palavra in palavras:
    palavra_len = len(palavra)   # len() retorna o número de caracteres da string
    print(f"{palavra}: {palavra_len} letras")
    # f-string: permite inserir variáveis dentro de {} dentro da string.
    # Sintaxe: f"texto {variavel} texto"

#---------------------------------------------------
# 27 - Crie uma lista idades contendo [12, 18, 25, 40, 60]. Utilize um loop for para imprimir "maior de idade" se a idade for >= 18 ou "menor de idade" se for < 18.

idades = [12, 18, 25, 40, 60]

for idade in idades:
    if idade<18:
        # Condição verdadeira para menores de 18
        print(f"{idade}: Menor de idade")
    else:
        # else cobre todos os outros casos (18 ou mais)
        print(f"{idade}: Maior de idade")

#---------------------------------------------------
# 28 - Crie uma lista notas contendo [5.5, 7.0, 8.3, 4.9, 6.2]. Utilize um loop for para contar quantos alunos estão aprovados (nota >= 7) e quantos estão reprovados (nota < 7).

notas = [5.5, 7.0, 8.3, 4.9, 6.2]

for nota in notas:
    if nota<7:
        print(f"{nota}: Reprovado")
    else:
        print(f"{nota}: Aprovado")

#---------------------------------------------------
# 29 - Crie uma lista compras com ["arroz", "feijão", "batata", "carne"]. Utilize um loop for para imprimir cada item precedido da frase "Preciso comprar: ".

compras = ["arroz", "feijão", "batata", "carne"]

for compra in compras:
    print(f"Preciso comprar {compra}")
    # f-string concatena o texto fixo com o valor da variável 'compra'

#---------------------------------------------------
# ============================================================
# LOOP WHILE — repete enquanto a condição for verdadeira
# Sintaxe:
#   while condição:
#       bloco_de_codigo
#
# ATENÇÃO: a variável de controle precisa ser atualizada dentro
# do loop para que a condição eventualmente seja falsa,
# evitando loop infinito.
# ============================================================

# 30 - Escreva um programa que use um loop while para imprimir os números de 1 a 10.

num = 1   # variável de controle: começa em 1

while num <=10:
    # Continua enquanto num for menor ou igual a 10
    print(num)
    num = num + 1   # incrementa num a cada iteração (sem isso, loop infinito)

#---------------------------------------------------
# 31 - Usando um loop while, peça para o usuário digitar um número inteiro. O programa deve parar quando o usuário digitar o número 0.

num = int(input("Digite um número inteiro: "))
# input() lê texto do teclado. int() converte para inteiro.

while num != 0:
    # '!=' significa "diferente de". Continua enquanto num for diferente de 0.
    num = int(input("Digite outro número inteiro: "))
else:
    # O bloco 'else' do while executa quando a condição se torna falsa.
    print("Você digitou o número 0")

#---------------------------------------------------
# 32 - Utilize um loop while para calcular a soma dos números de 1 a 100.

num = 0       # variável de controle (começa em 0)
num_sum = 0   # acumulador da soma (começa em 0)

while num <= 100:
    num_sum = num_sum + num   # acumula: soma o valor atual de num ao total
    num = num + 1             # avança para o próximo número

print(num_sum)   # resultado: 5050

#---------------------------------------------------
# 33 - Peça para o usuário adivinhar um número secreto (por exemplo, 7). Use um loop while para continuar pedindo até que ele acerte.

num = 0   # valor inicial diferente do segredo para entrar no loop

while num != 7:
    # Continua pedindo enquanto o usuário não digitar 7
    num = int(input("Digite um número: "))
else:
    print("Você acertou")

#---------------------------------------------------
# 34 - Crie um loop while que imprima todos os números pares de 2 até 20.

num = 2   # começa em 2 (primeiro par)

while num <= 20:
    print(num)
    num = num + 2   # incrementa de 2 em 2 para pular os ímpares

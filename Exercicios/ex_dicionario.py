# ============================================================
# DICIONÁRIOS — REFERÊNCIA RÁPIDA PARA A PROVA
# ============================================================
# DICIONÁRIO: estrutura de chave → valor. Como uma tabela de consulta.
#   Sintaxe: meu_dict = {"chave1": valor1, "chave2": valor2}
#   Acesso:  meu_dict["chave1"]       → retorna valor1
#   Chaves podem ser strings ou inteiros. Valores podem ser qualquer coisa.
#
# MÉTODOS PRINCIPAIS DE DICIONÁRIO:
#   dict["nova_chave"] = valor        → ADICIONA ou ATUALIZA uma chave
#   dict["chave"] = novo_valor        → ALTERA o valor de uma chave existente
#   dict.pop("chave")                 → REMOVE a chave e retorna o valor
#   dict.get("chave", padrão)         → retorna o valor ou 'padrão' se não existir
#                                       (não dá KeyError como dict["chave"])
#   dict.items()                      → retorna pares (chave, valor) para iterar
#   dict.keys()                       → retorna só as chaves
#   dict.values()                     → retorna só os valores
#   len(dict)                         → número de pares chave-valor
#   sum(dict.values())                → soma de todos os valores numéricos
#
# DICIONÁRIO ANINHADO: valor de uma chave é outro dicionário.
#   turma["Ana"]["notas"]             → acessa a lista de notas de Ana
# ============================================================

# Exercício 1

aluno = {
    'nome': 'Vinícius Tanno',
    'idade': 19,
    'curso': 'Administração'
}
# Criamos um dicionário com 3 chaves: 'nome', 'idade', 'curso'.
# Aspas simples ou duplas funcionam da mesma forma nas chaves.

print(f"{aluno['nome']}\n{aluno['idade']}\n{aluno['curso']}")
# Acessamos cada valor usando a chave entre colchetes.
# '\n' é o caractere de nova linha (pula linha na impressão).

#---------------------------------------------
# Exercício 2

produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}

produto['marca'] = 'Logitech'   # ADICIONA nova chave 'marca' com valor 'Logitech'
produto['preco'] = 320.00       # ATUALIZA o valor da chave 'preco' (era 350, vira 320)
produto['estoque'] -= 2         # '-=' é atalho para: produto['estoque'] = produto['estoque'] - 2
produto.pop('marca')            # REMOVE a chave 'marca' e seu valor do dicionário

print(produto)

#---------------------------------------------
# Exercício 3

notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

soma = 0                          # acumulador da soma
for nome, nota in notas.items():
    # .items() retorna cada par como uma tupla (chave, valor).
    # Aqui desempacotamos: 'nome' recebe a chave, 'nota' recebe o valor.
    print(f"{nome}: {nota}")
    soma += nota                  # '+=' acumula: soma = soma + nota

media = soma / len(notas)
# len(notas) retorna a quantidade de pares no dicionário (4 aqui).
print(f"Média: {media:.2f}")
# :.2f formata o float com 2 casas decimais.

#---------------------------------------------
# Exercício 4

numeros = {"a": 10, "b": 20, "c": 30}
soma_total = sum(numeros.values())
# .values() retorna apenas os valores do dicionário (10, 20, 30).
# sum() soma todos eles.

print(soma_total)

#---------------------------------------------
# Exercício 5

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}   # dicionário vazio para contar frequências

for item in lista:
    frequencia[item] = frequencia.get(item, 0) + 1
    # .get(item, 0): tenta buscar a chave 'item'.
    #   - Se a chave EXISTE → retorna o valor atual.
    #   - Se NÃO EXISTE → retorna 0 (o padrão que passamos).
    # Somamos +1 ao resultado para contar mais uma ocorrência.
    # Na primeira vez que "maçã" aparece: get("maçã", 0) → 0 → frequencia["maçã"] = 1
    # Na segunda vez: get("maçã", 0) → 1 → frequencia["maçã"] = 2

print(frequencia)

#---------------------------------------------
# Exercício 6

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_filtrados = {}   # dicionário que vai receber só os caros

for produto, preco in produtos.items():
    # Iteramos sobre cada par (produto, preço) do dicionário
    if preco > 50:
        # Só adicionamos ao novo dicionário se o preço for maior que 50
        produtos_filtrados[produto] = preco

print(produtos_filtrados)
# Resultado: {"mochila": 80, "notebook": 3000}

#---------------------------------------------
# Exercício 7

tradutor = {
    "apple": "maçã",
    "book": "livro",
    "deal": "acordo",
    "growth": "crescimento"
}

palavra = input("Digite uma palavra em inglês: ").lower()
# .lower() converte para minúsculas, para que "Apple" e "apple" funcionem igual.
print(tradutor.get(palavra, "Palavra não encontrada"))
# .get(palavra, "Palavra não encontrada"):
#   - Se a palavra EXISTE no dicionário → retorna a tradução.
#   - Se NÃO EXISTE → retorna "Palavra não encontrada" (sem dar erro).

#---------------------------------------------
# Exercício 8

lista_compras = {}   # começa vazio

lista_compras["Câmera"] = 1   # ADICIONA "Câmera" com quantidade 1
lista_compras["Iluminação"] = 2   # ADICIONA "Iluminação" com quantidade 2
lista_compras["Iluminação"] = 4   # ATUALIZA "Iluminação" para quantidade 4 (sobrescreve o 2)
lista_compras.pop("Câmera")       # REMOVE "Câmera" do dicionário

print(lista_compras)
# Resultado: {"Iluminação": 4}

#---------------------------------------------
# Exercício 9
# DICIONÁRIO ANINHADO: cada valor é outro dicionário.
# Para acessar: turma["Ana"]["idade"] → 17
#               turma["Ana"]["notas"] → [8, 9, 7]

turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

turma["Lucas"] = {"idade": 20, "notas": [7, 8, 9]}
# ADICIONA um novo aluno: a chave "Lucas" com um dicionário como valor.

maior_media = 0     # guarda a maior média encontrada até agora
melhor_aluno = ""   # guarda o nome do aluno com maior média

for aluno, dados in turma.items():
    # 'aluno' = nome (chave), 'dados' = dicionário interno (valor)
    media = sum(dados['notas']) / len(dados['notas'])
    # dados['notas'] → lista de notas. sum() soma. len() conta. Divisão = média.
    print(f"{aluno}: Média {media:.1f}")

    if media > maior_media:
        # Se a média atual é maior que o melhor registrado até agora:
        maior_media = media     # atualiza o melhor valor
        melhor_aluno = aluno    # atualiza o nome do melhor aluno

print(f"Melhor aluno: {melhor_aluno}")

#---------------------------------------------
# Exercício 10
# FUNÇÕES com dicionário global: permitem organizar operações em blocos reutilizáveis.

funcionarios = {}   # dicionário global para armazenar os funcionários

def cadastrar_funcionario(nome, cargo, salario):
    # 'def' define uma função. Os parâmetros são os dados que ela recebe.
    funcionarios[nome] = {"Cargo": cargo, "Salário": salario}
    # Usa o nome como chave e um dicionário com cargo e salário como valor.

def consultar_funcionario(nome):
    return funcionarios.get(nome, "Funcionário não encontrado no sistema.")
    # .get() tenta buscar o nome. Se não existir, retorna a mensagem padrão.
    # 'return' devolve o resultado para quem chamou a função.

cadastrar_funcionario("Rafael", "Gestor de Tráfego", 4500)
# Chama a função passando os 3 argumentos. Cria funcionarios["Rafael"].
cadastrar_funcionario("Mendes", "Produtor de Conteúdo", 4500)

print(consultar_funcionario("Rafael"))
# Chama a função de consulta. Como "Rafael" existe, retorna o dicionário dele.

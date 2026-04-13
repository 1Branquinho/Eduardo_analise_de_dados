"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
# Importa a biblioteca pandas com o apelido 'pd'.
# Usaremos 'pd.' para chamar todas as funções do pandas.

dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}
# Dicionário de listas: cada chave é o nome de uma coluna,
# cada lista é os valores daquela coluna.
# Todas as listas devem ter o mesmo tamanho (6 elementos aqui).

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)
# pd.DataFrame(dicionário) converte o dicionário em tabela (DataFrame).
# As chaves viram nomes de colunas, os valores viram as linhas.

# b) Mostre as 5 primeiras linhas
df_vendas.head()
# .head() exibe as primeiras 5 linhas (padrão). Use .head(n) para n linhas.
# Útil para visualizar a estrutura do DataFrame.

# c) Mostre o formato (linhas, colunas)
df_vendas.shape
# Retorna uma tupla: (número_de_linhas, número_de_colunas)
# Ex: (6, 4) → 6 linhas e 4 colunas

# d) Mostre os tipos de dados das colunas
df_vendas.dtypes
# Exibe o tipo de cada coluna: int64, float64, object (texto), etc.


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:

# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas[["mes", "vendas"]]
# Passando uma LISTA de nomes entre [[]] seleciona múltiplas colunas.
# Retorna um novo DataFrame com apenas essas colunas.

# b) Mostre somente a primeira linha
df_vendas.iloc[0]
# .iloc[índice] seleciona uma linha pelo número do índice (posição).
# iloc[0] = primeira linha. iloc[-1] = última linha.
# O resultado é uma Série (coluna transposta).

# c) Mostre as linhas de indice 2 ate 4
df_vendas.iloc[2:5]
# Slicing com iloc: [início:fim] → inclui início, EXCLUI fim.
# iloc[2:5] retorna as linhas nos índices 2, 3 e 4.


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:

# a) Filtre vendas acima de 12000
df_vendas[df_vendas['vendas']>12000]
# df_vendas['vendas']>12000 → cria uma Série booleana (True/False por linha).
# df_vendas[...] → passa essa série como máscara, mantendo só as linhas True.

# b) Filtre apenas a filial "Centro"
df_vendas[df_vendas["filial"]=="Centro"]
# Filtro de igualdade: mantém apenas linhas onde filial é exatamente "Centro".

# c) Filtre vendas acima de 11000 na filial "Norte"
df_vendas[(df_vendas["filial"]=="Norte") & (df_vendas["vendas"]>11000)]
# FILTRO DUPLO com '&' (E lógico): ambas as condições precisam ser verdadeiras.
# IMPORTANTE: cada condição DEVE estar entre parênteses quando usar '&' ou '|'.


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:

# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket médio"] = df_vendas["vendas"]/df_vendas["clientes"]
# Atribuição de nova coluna: df["nova_coluna"] = expressão
# A divisão é feita elemento a elemento entre as duas colunas.

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta batida"] = df_vendas["vendas"]>=13000
# Comparação cria uma coluna booleana: True onde vendas >= 13000, False caso contrário.

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas[['filial', 'mes', 'ticket_medio', 'meta_batida']]
# Seleciona as 4 colunas indicadas para visualização.


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:

# a) Calcule total de vendas por filial
vendas_filial = df_vendas.groupby("filial")["vendas"].sum()
# groupby("filial") → agrupa as linhas pelo valor da coluna "filial"
# ["vendas"]        → dentro de cada grupo, opera sobre a coluna "vendas"
# .sum()            → soma os valores de cada grupo
# Resultado: Série com índice = nome da filial, valor = total de vendas
vendas_filial

# b) Calcule media de clientes por mes
df_vendas.groupby("mes")["clientes"].mean()
# Agrupa por mês e calcula a média de clientes em cada mês.

# c) Descubra a filial com maior total de vendas
vendas_filial.idxmax()
# .idxmax() retorna o ÍNDICE (nome) do elemento com maior valor.
# Aqui retorna o nome da filial com mais vendas.


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:

# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas_decrescente = df_vendas.sort_values(by='vendas', ascending=False)
# .sort_values(by='coluna', ascending=False) → ordena do maior para o menor.
# ascending=True  → crescente (menor para maior, padrão).
# ascending=False → decrescente (maior para menor).
# Não modifica o original; retorna novo DataFrame.

# b) Pegue os 3 maiores resultados de vendas
df_vendas_decrescente[0:3]
# Slicing: pega os 3 primeiros do DataFrame já ordenado de forma decrescente.
# Equivalente a .head(3)

# c) Mostre um ranking com "filial", "mes", "vendas"
df_vendas_decrescente[['filial', 'mes', 'vendas']]
# Seleciona só as 3 colunas relevantes do DataFrame ordenado.


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):

# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
resumo_filial = df_vendas.groupby("filial").agg({
    "vendas": "sum",
    "ticket médio": "mean",
    "clientes": "sum"
}).rename(columns={
    "vendas": "total_vendas",
    "ticket médio": "media_ticket_medio",
    "clientes": "total_clientes"
})
# .agg({"coluna": "função"}) → aplica FUNÇÕES DIFERENTES para cada coluna.
# Equivalente a fazer vários groupby separados de uma vez.
# .rename(columns={"nome_atual": "nome_novo"}) → renomeia colunas do resultado.
resumo_filial

# 2) Ordene o resumo por total_vendas (desc)
resumo_filial.sort_values(by="total_vendas", ascending=False)

# 3) Exiba qual filial teve melhor desempenho geral
melhor_filial = resumo_filial.index[0]
# Depois do sort_values() acima, a primeira posição (índice 0) é a filial com maior total.
# .index retorna o índice do DataFrame (nomes das filiais aqui).
melhor_filial


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]
# Estrutura: LISTA contendo UM dicionário.
# O dicionário tem chaves "Column A/B/C" e os valores são LISTAS de números.
# Para acessar: dados_list_dict[0]["Column A"] → [1, 2, 3]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
type(dados_list_dict)
# Retorna: <class 'list'> → é uma lista (o container mais externo é [])

# 2. Qual é o tipo do primeiro elemento?
type(dados_list_dict[0])
# dados_list_dict[0] → primeiro (e único) elemento da lista
# Retorna: <class 'dict'> → o elemento é um dicionário

# 3. Como acessar a lista da "Column A"?
dados_list_dict[0]["Column A"]
# [0]           → acessa o primeiro elemento da lista (o dicionário)
# ["Column A"]  → acessa o valor da chave "Column A" dentro do dicionário
# Retorna: [1, 2, 3]

# 4. Como acessar o segundo elemento da "Column C"?
dados_list_dict[0]["Column C"][1]
# [0]          → primeiro elemento da lista (o dicionário)
# ["Column C"] → acessa a lista [7, 8, 9]
# [1]          → segundo elemento da lista (índice 1) → retorna 8


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
import pandas as pd

df_dados = pd.DataFrame(dados_list_dict[0])
# dados_list_dict[0] é um dicionário de listas → formato ideal para criar DataFrame.
# Chaves viram nomes de colunas, listas viram os valores das colunas.
df_dados

# 2. Mostre:

#    - shape
df_dados.shape
# Retorna (3, 3): 3 linhas e 3 colunas (A, B, C)

#    - tipos das colunas
df_dados.dtypes
# Exibe o tipo de cada coluna (int64 aqui, pois são números inteiros)

# 3. Calcule:
#    - soma de cada coluna
df_dados.sum()
# Sem argumento → soma cada coluna verticalmente (padrão axis=0)
# Retorna: Column A=6, Column B=15, Column C=24

#    - média de cada coluna
df_dados.mean()
# Calcula a média de cada coluna.


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
df_dados["Total"] = df_dados.sum(axis=1)
# axis=1 → opera na direção HORIZONTAL (soma cada linha entre colunas).
# axis=0 → opera na direção VERTICAL (padrão, soma cada coluna).
# Para cada linha: Total = Column A + Column B + Column C
df_dados

# 2. Crie coluna "Media" = média por linha
df_dados["Média"] = df_dados.mean(axis=1)
# axis=1 → calcula a média de cada linha (entre as colunas).
df_dados

# 3. Filtre linhas onde Total > 10
df_dados[df_dados["Total"]<=10]
# Mantém apenas as linhas onde a coluna "Total" é menor ou igual a 10.


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
dicionarios = df_dados.to_dict(orient="records")
# to_dict(orient="records") → cada linha vira um dicionário separado.
# Resultado: [{"Column A": 1, "Column B": 4, ...}, {"Column A": 2, ...}, ...]
# Usado quando se quer enviar dados como JSON ou iterar linha por linha.
dicionarios

#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
lista = df_dados.to_dict(orient="list")
# to_dict(orient="list") → cada coluna vira uma lista.
# Resultado: {"Column A": [1, 2, 3], "Column B": [4, 5, 6], ...}
# Usado para reconstruir o DataFrame ou processar coluna por coluna.
lista

# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.


# RESOLVA AQUI:


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
lista_a = df_dados["Column A"].to_list()
# .to_list() converte a Série (coluna do DataFrame) em uma lista Python comum.
lista_a

# 2. Multiplique cada elemento da lista por 10.
lista_a_10 = []
for num in lista_a:
    num = num*10
    lista_a_10.append(num)
# Loop que multiplica cada número por 10 e adiciona na nova lista.
lista_a_10

# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.
df_dados["Column A x10"] = lista_a_10
# Atribui a lista diretamente como nova coluna. O pandas alinha pelo índice.
df_dados


# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]
# Lista de dicionários: cada dicionário é uma linha/registro.
# Formato direto para criar DataFrame com pd.DataFrame(dados).


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
type(dados)
# Retorna: <class 'list'> — é uma lista de dicionários

# 2. Quantos registros existem?
len(dados)
# len() retorna o número de elementos na lista = número de registros (5 aqui)

# 3. Quais são as chaves do primeiro dicionário?
list(dados[0].keys())
# dados[0] → primeiro dicionário da lista
# .keys() → retorna as chaves do dicionário
# list() → converte para lista para visualizar melhor

# 4. Liste todos os países existentes (sem repetição).
paises = []   # lista acumuladora
for dado in dados:
    if dado["nome_pais"] not in paises:
        # 'not in' verifica se o valor NÃO está na lista ainda.
        # Só adiciona se ainda não foi adicionado (evita duplicatas).
        paises.append(dado["nome_pais"])
paises


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)
# pd.DataFrame(lista_de_dicts) → cada dicionário vira uma linha, chaves viram colunas.

# 2. Mostre shape, tipos e primeiras linhas
df.shape   # → (5, 8): 5 linhas, 8 colunas
df.dtypes  # → tipos de cada coluna (int64, object, etc.)
df.head()  # → primeiras 5 linhas para visualização

# 3. Converta a coluna periodo para datetime
pd.to_datetime(df["periodo"])
# pd.to_datetime() converte strings de data ("2023-01") para o tipo datetime do pandas.
# Necessário para usar operações de data como .dt.year, .dt.month.
df


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros

# 1. Filtre apenas Brasil
df[df["nome_pais"] == "Brasil"]
# Mantém apenas linhas onde nome_pais é "Brasil"

# 2. Filtre apenas Produto A
df[df["descricao"] == "Produto A"]
# Mantém apenas linhas onde descricao é "Produto A"

# 3. Filtre valor > 4000
df[df["valor"] > 4000]
# Mantém apenas linhas com valor maior que 4000

# 4. Combine Brasil + Produto A
df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")]
# Filtro duplo: nome_pais = "Brasil" E descricao = "Produto A"
# Ambas as condições precisam ser verdadeiras (operador &)


# Exercício 4 – Ordenação

# 1. Ordene por valor crescente
df.sort_values(by="valor", ascending=True)
# ascending=True = do menor para o maior (padrão)

# 2. Ordene por valor decrescente
df.sort_values(by="valor", ascending=False)
# ascending=False = do maior para o menor

# 3. Ordene por periodo e depois por valor
df.sort_values(by=["periodo", "valor"], ascending=[True, True])
# Ordenação múltipla: primeiro por "periodo", depois por "valor" dentro do mesmo período.
# Cada critério pode ter sua própria direção na lista ascending=[].


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples

# 1. Total exportado por país
df.groupby("nome_pais")["valor"].sum()
# Agrupa por país e soma os valores de cada grupo.

# 2. Total exportado por produto
df.groupby("id_produto")["valor"].sum()
# Agrupa por id_produto e soma os valores de cada grupo.

# 3. Média por país
df.groupby("nome_pais")["valor"].mean()
# Agrupa por país e calcula a média dos valores.

# 4. Quantidade de operações por país
df.groupby("nome_pais").size()
# .size() conta o número de LINHAS em cada grupo (contagem bruta de registros).
# Diferente de .count() que conta valores não nulos por coluna.


# Exercício 6 – GroupBy Múltiplo

# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem
df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])
# groupby com LISTA de colunas → agrupa por múltiplos níveis.
# .agg(["sum", "mean", "count"]) → aplica várias funções ao mesmo tempo.
# Resultado: tabela com índice múltiplo (país + produto) e colunas sum/mean/count.

# Explique em comentário o que essa tabela representa
# A tabela mostra, para cada combinação de país + produto:
# - sum: total exportado
# - mean: valor médio por operação
# - count: número de operações registradas


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor
pivot_produto = df.pivot_table(index='periodo', columns='descricao', values='valor', aggfunc='sum')
# pivot_table() cria uma tabela cruzada (como tabela dinâmica do Excel):
#   index   = o que vai nas LINHAS (períodos)
#   columns = o que vai nas COLUNAS (nomes dos produtos)
#   values  = os valores a exibir (coluna 'valor')
#   aggfunc = como agregar se houver múltiplos valores ('sum', 'mean', etc.)
pivot_produto

# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

# RESOLVA AQUI:
df['ano'] = df['periodo'].dt.year
# .dt.year extrai apenas o ANO de uma coluna datetime.
# ATENÇÃO: a coluna 'periodo' precisa ter sido convertida para datetime antes.
df['mes'] = df['periodo'].dt.month
# .dt.month extrai apenas o MÊS como número inteiro (1 a 12).
df['valor_mil'] = df['valor'] / 1000
# Divide todos os valores por 1000, criando nova coluna em milhares.

# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela
# A tabela mostra o total exportado por cada país em cada período.
# Valores NaN (nulo) indicam que aquele país não teve exportação naquele período.

# RESOLVA AQUI:
pais = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
pais


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

# RESOLVA AQUI:
df['periodo'] = pd.to_datetime(df['periodo'])
# Converte a coluna 'periodo' de string para datetime.
# IMPORTANTE: precisa fazer isso ANTES de usar .dt.year ou .dt.month.
df['ano'] = df['periodo'].dt.year     # extrai o ano
df['mes'] = df['periodo'].dt.month    # extrai o mês
df['valor_mil'] = df['valor'] / 1000  # valor em milhares

df = df.sort_values(by=['descricao', 'periodo'])
# Ordena por produto e data antes de calcular crescimento percentual.
# Essencial para que o cálculo de variação seja feito na ordem correta.
df['crescimento'] = df.groupby('descricao')['valor'].pct_change()
# .pct_change() calcula a variação percentual em relação à linha ANTERIOR do grupo.
# groupby('descricao') → calcula dentro de cada produto separadamente.
# Resultado: (valor_atual - valor_anterior) / valor_anterior
df


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

# RESOLVA AQUI:
df.isnull().sum()
# .isnull() → cria DataFrame booleano: True onde valor é nulo (NaN).
# .sum()    → soma True=1 por coluna → total de nulos em cada coluna.

df[df["valor"]<0]
# Filtra linhas onde o valor é negativo.
# Se retornar DataFrame vazio, não há valores negativos.

df.duplicated().sum()
# .duplicated() → marca True nas linhas que são duplicatas (cópia de linha anterior).
# .sum()        → conta o número de duplicatas.

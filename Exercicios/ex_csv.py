
# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

# ============================================================
# REFERÊNCIA RÁPIDA — MÉTODOS USADOS NESTE ARQUIVO
# ============================================================
# CARREGAR CSV:
#   pd.read_csv("arquivo.csv")         → lê CSV e cria DataFrame
#
# EDA (EXPLORAÇÃO INICIAL):
#   df.shape                           → (nº linhas, nº colunas)
#   df.dtypes                          → tipos de cada coluna
#   df.isnull().sum()                  → nulos por coluna
#   df["col"].unique()                 → valores únicos da coluna
#   df["col"].mean() / .max() / .min() → estatísticas
#   df["col"].std()                    → desvio padrão
#
# SELEÇÃO:
#   df[["col1","col2"]]                → múltiplas colunas
#   df.nsmallest(n, "col")             → n menores valores
#   df["col"].between(a, b)            → valores entre a e b (inclusivo)
#   df.loc[filtro, ["col1","col2"]]    → filtro + seleção de colunas juntos
#
# MISSING VALUES:
#   df["col"].isnull().sum()           → conta nulos da coluna
#   df.dropna(subset=["col"])          → remove linhas nulas na coluna
#   df.fillna(valor)                   → preenche nulos com 'valor'
#
# GROUPBY:
#   df.groupby("col")["val"].mean()    → média por grupo
#   resultado.idxmax()                 → índice do maior valor
#   resultado.sort_values(ascending=False).head(n) → top n
#
# GRÁFICO:
#   serie.plot(kind="line", marker="o", figsize=(10,5), color="darkblue")
# ============================================================


# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================


import pandas as pd
df = pd.read_csv("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/notas.csv")
# pd.read_csv() lê o arquivo CSV e cria um DataFrame.
# Cada linha do CSV vira uma linha do DataFrame, cada coluna do cabeçalho vira uma coluna.

#----------------------------------------------
# Exercício 1 – Conhecendo o Dataset

# 1. Quantas linhas e colunas existem?
df.shape
# Retorna tupla (linhas, colunas). Ex: (2000, 9) → 2000 registros, 9 colunas.

# 2. Quais são os tipos de dados?
df.dtypes
# Exibe o tipo de cada coluna: int64 (inteiro), float64 (decimal), object (texto/string).

# 3. Existe coluna com valores ausentes?
df.isnull().sum()
# .isnull() → cria DataFrame booleano (True = nulo).
# .sum()    → soma True=1 por coluna → quantos nulos em cada coluna.

# 4. Qual é o período de anos disponível?
df.loc[:,"year"].unique()
# .loc[:, "year"] → seleciona TODAS as linhas (:) da coluna "year".
# .unique() → retorna apenas os valores distintos (sem repetição).

# 5. Quantos países diferentes existem?
df.loc[:,"country"].sum()
# ATENÇÃO: .sum() em coluna de texto (object) concatena as strings, não conta.
# Para contar países únicos, o correto seria: df["country"].nunique()

#----------------------------------------------
# Exercício 2 – Estatísticas Gerais

# 1. Média do score
df["score"].mean()
# Calcula a média aritmética de todos os scores do dataset.

# 2. Maior score
df["score"].max()
# Retorna o maior valor de score no dataset.

# 3.Menor score
df["score"].min()
# Retorna o menor valor de score no dataset.

# 4. Média do score por ano
df.groupby("year")["score"].mean()
# Agrupa as linhas por ano e calcula a média de score em cada grupo.

# 5. Desvio padrão do score
df["score"].std()
# Desvio padrão = mede a dispersão dos dados em torno da média.
# Valor alto = dados muito variados; valor baixo = dados próximos da média.


# ============================================================
# FILTROS E SELEÇÕES
# ============================================================


#----------------------------------------------
# Exercício 3 – Top Universidades

# 1. Mostre as 10 melhores universidades do mundo (menor world_rank)
top_10 = df.nsmallest(10, "world_rank")
# .nsmallest(n, "coluna") → retorna as n linhas com os MENORES valores da coluna.
# Aqui: as 10 linhas com menor world_rank (rank 1 é melhor).
top_10["institution"]
# Seleciona só a coluna "institution" do resultado filtrado.

# 2. Mostre as 5 melhores universidades do Brasil (se existirem)
brazil = df[df["country"] == "Brazil"]
# Filtra apenas as linhas onde country é "Brazil".
brazil_5 = brazil.nsmallest(5, "world_rank")
# Dentro das universidades brasileiras, pega as 5 com menor world_rank.
brazil_5["institution"]

# 3. Mostre universidades com score maior que 90
top_90 = df[df["score"]>90]
# Filtro: mantém apenas linhas com score maior que 90.
top_90["institution"]

# 4. Mostre universidades dos EUA com score maior que 80
top_80 = df[df["score"]>80]
# Primeiro filtra por score > 80 (sem restrição de país).
top_80_EUA = top_80[top_80["country"] == "USA"]
# Depois filtra dentro do resultado anterior: só os EUA.
# Equivalente ao filtro duplo com &:
# df[(df["score"] > 80) & (df["country"] == "USA")]
top_80_EUA["institution"]

#----------------------------------------------
# Exercício 4 – Seleção Avançada

# 1. Mostre apenas as colunas: institution,
# country e score
df[["institution", "country", "score"]]
# Lista de colunas em [[]] → retorna DataFrame apenas com essas colunas.

# 2. Mostre universidades entre rank 50 e 100
top_50_100 = df[(df["score"]>=50) & (df["score"]<=100)]
# Filtro duplo: score >= 50 E score <= 100.
top_50_100 = df[df["score"].between(50, 100)]
# .between(a, b) é equivalente ao filtro duplo acima (mais legível).
# Ambos os extremos são INCLUSIVOS.
top_50_100["institution"]

# 3. Mostre universidades cujo país é "United Kingdom"
uk = df[df["country"] == "United Kingdom"]
# Filtro de igualdade exata (case-sensitive: "United Kingdom" ≠ "united kingdom").
uk["institution"]


# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================


#----------------------------------------------
# Exercício 5 – Valores Ausentes

# 1. Quantos valores nulos existem na coluna broad_impact?
null_broad_impact = df["broad_impact"].isnull().sum()
# Conta o número de valores nulos (NaN) na coluna "broad_impact".
null_broad_impact

# 2. Qual percentual do dataset é nulo?
null_percentage = 100*(null_broad_impact/df.shape[0])
# df.shape[0] → número total de linhas.
# (nulos / total) * 100 → percentual de nulos.
print(f"O percentual do dataset que é nulo é {null_percentage:.2f}%")

# 3. Remova linhas com broad_impact nulo
df_without_null = df.dropna(subset=["broad_impact"])
# .dropna(subset=["coluna"]) → remove apenas as linhas onde "coluna" é nula.
# Sem 'subset', removeria qualquer linha com qualquer nulo.
# Retorna novo DataFrame; o original 'df' não é alterado.
df_without_null

# 4. Preencha valores nulos com a média
df_X = df.fillna(df["broad_impact"].mean())
# .fillna(valor) → substitui todos os NaN pelo valor passado.
# Aqui usamos a média da própria coluna como valor de preenchimento.
df_X

# 5. Compare a média antes e depois do preenchimento
df_mean = df["broad_impact"].mean()
# Média original (ignorando nulos — .mean() ignora NaN por padrão).
df_mean_X = df_X["broad_impact"].mean()
# Média após preenchimento com a média → deve ser idêntica (preenchimento com média não altera a média).
print(f"A média antes era {df_mean:.2f}, depois do preenchimento ficou {df_mean_X:.2f}")


# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================


# Exercício 6 – Análise por País

# 1. Média do score por país
df_countries = df.groupby("country")["score"].mean()
# Agrupa por país e calcula a média de score em cada grupo.
df_countries

# 2. País com maior média de score
df_countries.idxmax()
# .idxmax() → retorna o ÍNDICE (nome do país) com maior valor na Série.

# 3. Quantidade de universidades por país
institution_country = df.groupby("country")["institution"].count()
# .count() conta valores não nulos em cada grupo.
# Resultado: número de registros (universidades) por país.

# 4. Top 10 países com mais universidades
institution_country.sort_values(ascending=False).head(10)
# .sort_values(ascending=False) → ordena do maior para o menor.
# .head(10) → pega os 10 primeiros (maior número de universidades).


# Exercício 7 – Análise por Ano

# 1. Média do score por ano
year_mean = df.groupby("year")["score"].mean()
# Agrupa por ano e calcula a média de score em cada ano.
year_mean

# 2. Qual ano teve maior média?
year_mean.idxmax()
# Retorna o ano (índice) com a maior média de score.

# 3. Faça um gráfico da evolução do score médio ao longo do tempo
year_mean.plot(kind="line", marker="o", figsize=(10,5),color="darkblue")
# .plot() gera um gráfico diretamente da Série.
# kind="line"      → tipo de gráfico (linha)
# marker="o"       → marca cada ponto com um círculo
# figsize=(10,5)   → tamanho da figura em polegadas (largura, altura)
# color="darkblue" → cor da linha

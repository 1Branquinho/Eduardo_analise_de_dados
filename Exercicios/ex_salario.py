# ============================================================
# PANDAS COM EXCEL — REFERÊNCIA RÁPIDA PARA A PROVA
# ============================================================
# PANDAS: biblioteca Python para análise de dados.
#   import pandas as pd  → importa com o apelido 'pd'
#
# CARREGAR ARQUIVO:
#   pd.read_csv("arquivo.csv")    → lê CSV e cria DataFrame
#   pd.read_excel("arquivo.xlsx") → lê Excel e cria DataFrame
#
# EXPLORAÇÃO BÁSICA (EDA):
#   df.shape       → tupla (nº_linhas, nº_colunas)
#   df.dtypes      → tipo de dado de cada coluna
#   df.head(n)     → primeiras n linhas (padrão 5)
#   df.describe()  → estatísticas descritivas das colunas numéricas
#
# SELEÇÃO DE COLUNA:
#   df["coluna"]               → retorna uma Série (coluna inteira)
#   df[["col1", "col2"]]       → retorna DataFrame com as colunas indicadas
#
# ESTATÍSTICAS DE COLUNA:
#   df["col"].mean()   → média
#   df["col"].max()    → maior valor
#   df["col"].min()    → menor valor
#   df["col"].count()  → contagem de valores não nulos
#   df["col"].nunique()→ contagem de valores ÚNICOS (sem repetição)
#
# FILTRO (retorna só as linhas que satisfazem a condição):
#   df[df["col"] == "valor"]          → igualdade
#   df[df["col"] > número]            → maior que
#   df[(condição1) & (condição2)]     → E lógico (ambas verdadeiras)
#   df[(condição1) | (condição2)]     → OU lógico
#
# GROUPBY (agrupa por coluna e aplica função):
#   df.groupby("col_grupo")["col_valor"].mean()   → média por grupo
#   df.groupby("col_grupo")["col_valor"].sum()    → soma por grupo
#   resultado.idxmax()  → retorna o ÍNDICE (nome do grupo) com maior valor
#   resultado.idxmin()  → retorna o ÍNDICE com menor valor
# ============================================================

import pandas as pd

df = pd.read_excel("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/salary.xlsx")
# pd.read_excel() lê o arquivo Excel e retorna um DataFrame.
# O caminho completo do arquivo deve estar correto.
df

# 1 - Quantas linhas e quantas colunas tem o dataset?
df.shape
# Retorna uma tupla: (número_de_linhas, número_de_colunas)
# Ex: (100, 8) → 100 linhas e 8 colunas

# 2 - Qual a média salarial? Qual é o maior salário? O menor salário?
salary_mean = df["salary"].mean()
# df["salary"] → seleciona a coluna "salary" (uma Série).
# .mean() → calcula a média dos valores da coluna.
# Guardamos em 'salary_mean' para reutilizar depois.
df["salary"].max()   # retorna o maior valor da coluna salary
df["salary"].min()   # retorna o menor valor da coluna salary

# 3 - Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
df[["job_title", "salary", "company_location", "company_size", "remote_ratio"]]
# Passando uma LISTA de colunas entre [[]] retorna um novo DataFrame
# com somente essas colunas. (duplo colchete = selecionar múltiplas colunas)

# 4 - Qual é o maior e menor salário de um "Data Scientist"? Onde fica essas empresas?
df[df["job_title"] == "Data Scientist"].max()
# df[df["job_title"] == "Data Scientist"] → FILTRA apenas as linhas onde job_title é "Data Scientist"
# .max() → retorna o máximo de cada coluna das linhas filtradas
df[df["job_title"] == "Data Scientist"].min()
# .min() → retorna o mínimo de cada coluna das linhas filtradas

# 5 - Qual a profissão com a maior média salarial? E a menor?
salary_job = df.groupby("job_title")["salary"].mean()
# groupby("job_title") → agrupa todas as linhas pelo valor de "job_title"
# ["salary"]           → dentro de cada grupo, seleciona a coluna "salary"
# .mean()              → calcula a média salarial de cada grupo
# Resultado: uma Série onde o índice = nome da profissão, valor = média salarial
salary_job.idxmax()   # idxmax() → retorna o NOME (índice) da profissão com MAIOR média
salary_job.idxmin()   # idxmin() → retorna o NOME (índice) da profissão com MENOR média

# 6 - Quais as profissões com a média salarial maior que a média geral?
job_over_mean = salary_job[salary_job > salary_mean]
# Filtramos a Série 'salary_job' mantendo apenas os grupos onde
# a média do grupo é maior que a média geral (salary_mean calculada no ex. 2).

# 7 - Qual a localização com maior média salarial?
salary_loc = df.groupby("employee_residence")["salary"].mean()
# Agrupa por localização do funcionário e calcula média salarial por local.
salary_loc.idxmax()
# Retorna o código da localização com maior média salarial.

# 8 - Quais as profissões que existem no Brasil (BR)?
df["job_title"][df["company_location"] == "BR"]
# df["company_location"] == "BR" → cria um filtro booleano (True/False por linha)
# df["job_title"][filtro]        → aplica o filtro na coluna "job_title"
# Resultado: lista de profissões cujas empresas ficam no Brasil

# 9 - Qual a média salarial no Brasil?
df["salary"][df["company_location"] == "BR"].mean()
# Filtra a coluna "salary" apenas para linhas do Brasil, depois calcula a média.

# 10 - Quantas profissões existem no Brasil?
df["job_title"][df["company_location"] == "BR"].count()
# .count() → conta o número de valores não nulos (quantidade de registros filtrados)

# 11 - Qual a profissão que mais ganha no Brasil? (Considerando média salarial)
salary_job_BR = df[df["company_location"] == "BR"].groupby("job_title")["salary"].mean()
# Primeiro filtramos só o Brasil: df[df["company_location"] == "BR"]
# Depois agrupamos por profissão e calculamos a média salarial de cada uma.
salary_job_BR.idxmax()
# Retorna o nome da profissão com maior média salarial no Brasil.

# 12 - Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
df[(df["company_location"] == "US") & (df["company_size"] == "L")]["job_title"].nunique()
# Filtro com DUAS condições combinadas com '&' (E lógico).
# IMPORTANTE: cada condição deve estar entre parênteses quando usar '&' ou '|'.
# .nunique() → conta quantos valores ÚNICOS (distintos) existem na coluna filtrada.
# Diferente de .count() que conta tudo (incluindo repetições).

# 13 - Qual é a média salarial das empresas médias (M) na Canada (CA)?
df[(df["company_location"] == "CA") & (df["company_size"] == "M")]["salary"].mean()
# Filtro duplo: localização = CA E tamanho = M.
# Depois seleciona a coluna "salary" e calcula a média.

# 14 - Qual é o país com mais profissões? E qual é o com menos?
df.groupby("company_location")["job_title"].nunique()
# Agrupa por localização e conta o número de profissões únicas em cada país.
# Para o país com MAIS: adicionar .idxmax()
# Para o país com MENOS: adicionar .idxmin()

# 15 - Quem ganha mais que trabalha remoto, presencial ou híbrido?
# Na maioria dessas bases: 0 = Presencial, 50 = Híbrido, 100 = 100% Remoto
salary_ratio = df.groupby("remote_ratio")["salary"].mean()
# Agrupa pela coluna "remote_ratio" (0, 50 ou 100) e calcula média salarial.
salary_ratio.idxmax()
# Retorna o valor de remote_ratio (0, 50 ou 100) com maior média salarial.

# 16 - Qual o país com maior numero de profissões trabalhando 100% remoto?
remote_countries = df[df["remote_ratio"] == 100].groupby("company_location")["job_title"].nunique()
# Passo 1: filtra só as linhas com remote_ratio == 100 (100% remoto)
# Passo 2: agrupa por país (company_location)
# Passo 3: conta o número de profissões únicas em cada país
remote_countries.idxmax()
# Retorna o código do país com mais profissões 100% remotas.

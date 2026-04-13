"""
===========================================================
QUESTÕES DE REVISÃO – AP1
===========================================================
Tópicos cobertos:
  1. Python Básico (Listas e Dicionários)
  2. Carregando e Explorando Dados (CSV e Excel)
  3. Filtros e Seleções
  4. Cálculos e Novas Colunas
  5. Agrupamentos (GroupBy)
  6. Ranking e Ordenação
  7. APIs (Laboratório de Finanças – BCB)

Datasets utilizados:
  - exercicios/titanic.csv
  - exercicios/notas.csv
  - exercicios/salary.xlsx

APIs utilizadas:
  - BCB (Banco Central do Brasil) – PTAX Dólar
  - ViaCEP
  - BrasilAPI (Bancos)
  - IBGE (Estados)
===========================================================
"""

import pandas as pd
import requests
# pandas: biblioteca de análise de dados (tabelas/DataFrames).
# requests: biblioteca para fazer requisições HTTP a APIs.

# Caminhos dos arquivos (ajuste se necessário)
PATH_TITANIC = "exercicios/titanic.csv"
PATH_NOTAS   = "exercicios/notas.csv"
PATH_SALARY  = "exercicios/salary.xlsx"
# Variáveis com os caminhos dos arquivos: facilita a reutilização e evita digitar o caminho toda hora.


# ===========================================================
# PARTE 1 – PYTHON BÁSICO (Listas e Dicionários)
# ===========================================================

# ----------------------------------------------------------
# Questão 1
# Crie um dicionário chamado 'aluno' com as chaves:
# 'nome', 'idade' e 'curso'. Preencha com seus próprios dados.
# Depois, imprima cada valor usando as chaves.
# ----------------------------------------------------------

# RESOLVA AQUI:
aluno = {
    "nome": "Vinicius Tanno",
    "idade": 19,
    "curso": "Administração"
}
# Dicionário criado com 3 chaves. Valores: string, inteiro, string.
print(aluno["nome"])    # Acessa o valor da chave "nome"
print(aluno["idade"])   # Acessa o valor da chave "idade"
print(aluno["curso"])   # Acessa o valor da chave "curso"


# ----------------------------------------------------------
# Questão 2
# Dado o dicionário abaixo, faça as operações indicadas:
produtos = {
    "caneta": 2.50,
    "mochila": 120.00,
    "caderno": 35.00,
    "notebook": 4500.00
}
# a) Adicione o produto "mouse" com preço 89.90
# b) Altere o preço da "caneta" para 3.00
# c) Remova o produto "mochila"
# d) Imprima o dicionário final
# ----------------------------------------------------------

# RESOLVA AQUI:
produtos["mouse"] = 89.90       # a) ADICIONA nova chave "mouse" com valor 89.90
produtos["caneta"] = 3.00       # b) ATUALIZA o valor de "caneta" (sobrescreve 2.50 com 3.00)
produtos.pop("mochila")         # c) REMOVE a chave "mochila" e seu valor do dicionário
print(produtos)                 # d) Imprime o dicionário com as alterações aplicadas


# ----------------------------------------------------------
# Questão 3
# Dado o dicionário de notas abaixo, calcule e imprima
# a média da turma usando um loop for.
notas_turma = {
    "Alice":   8.5,
    "Bruno":   7.0,
    "Carla":   9.2,
    "Daniel":  6.8,
    "Eduarda": 7.5
}
# ----------------------------------------------------------

# RESOLVA AQUI:
soma = 0
# Acumulador: inicia em 0 e vai somando cada nota.
for nome, nota in notas_turma.items():
    # .items() retorna cada par (chave, valor) do dicionário.
    # 'nome' recebe a chave (nome do aluno), 'nota' recebe o valor (nota).
    soma += nota
    # '+=' é atalho para: soma = soma + nota

media = soma / len(notas_turma)
# len(notas_turma) → conta quantas entradas o dicionário tem (5 alunos aqui).
print(f"Média da turma: {media:.2f}")
# :.2f → formata o float com 2 casas decimais.


# ----------------------------------------------------------
# Questão 4
# Dado o dicionário abaixo, crie um NOVO dicionário chamado
# 'caros' contendo apenas os produtos com preço ACIMA de 50.
catalogo = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
# ----------------------------------------------------------

# RESOLVA AQUI:
caros = {}
# Dicionário vazio que vai receber apenas os produtos caros.
for produto, preco in catalogo.items():
    # Itera sobre cada par (produto, preço) do catálogo.
    if preco > 50:
        # Condição: só adiciona ao novo dicionário se preço > 50.
        caros[produto] = preco

print(caros)
# Resultado: {"mochila": 80, "notebook": 3000}


# ----------------------------------------------------------
# Questão 5
# Dado o dicionário aninhado abaixo, adicione o aluno "Lucas"
# com idade 20 e notas [7, 8, 9]. Em seguida, calcule e
# imprima a média de cada aluno e diga quem tem a maior média.
turma = {
    "Ana":     {"idade": 17, "notas": [8, 9, 7]},
    "Pedro":   {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
# DICIONÁRIO ANINHADO: o valor de cada chave é outro dicionário.
# turma["Ana"] → {"idade": 17, "notas": [8, 9, 7]}
# turma["Ana"]["notas"] → [8, 9, 7]
# ----------------------------------------------------------

# RESOLVA AQUI:
turma["Lucas"] = {"idade": 20, "notas": [7, 8, 9]}
# ADICIONA um novo aluno: chave "Lucas" com dicionário como valor.

maior_media   = 0    # rastreia a maior média encontrada até agora
melhor_aluno  = ""   # rastreia o nome do aluno com maior média

for aluno_nome, dados in turma.items():
    # 'aluno_nome' = chave (nome), 'dados' = valor (dicionário interno)
    med = sum(dados["notas"]) / len(dados["notas"])
    # sum(dados["notas"]) → soma as notas do aluno.
    # len(dados["notas"]) → quantidade de notas.
    # Divisão → média.
    print(f"{aluno_nome}: Média {med:.1f}")
    if med > maior_media:
        # Se a média atual supera o melhor registrado:
        maior_media  = med          # atualiza o melhor valor
        melhor_aluno = aluno_nome   # atualiza o nome do melhor

print(f"Melhor aluno: {melhor_aluno}")


# ===========================================================
# PARTE 2 – CARREGANDO E EXPLORANDO DADOS
# ===========================================================

# ----------------------------------------------------------
# Questão 6
# Carregue o arquivo titanic.csv em um DataFrame chamado df_titanic.
# Responda:
# a) Quantas linhas e colunas existem?
# b) Quais são os tipos de dados de cada coluna?
# c) Existem valores nulos em alguma coluna?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_titanic = pd.read_csv(PATH_TITANIC)
# pd.read_csv() lê o CSV e cria o DataFrame automaticamente.
# PATH_TITANIC é a variável com o caminho definida no início do arquivo.

print(df_titanic.shape)           # a) Retorna (nº_linhas, nº_colunas)
print(df_titanic.dtypes)          # b) Tipo de cada coluna: int64, float64, object
print(df_titanic.isnull().sum())  # c) Conta nulos por coluna (0 = sem nulos)


# ----------------------------------------------------------
# Questão 7
# Carregue o arquivo notas.csv em um DataFrame chamado df_notas.
# Responda:
# a) Quantos anos diferentes aparecem na coluna 'year'?
# b) Qual é a média da coluna 'score'?
# c) Qual é o desvio padrão de 'score'?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_notas = pd.read_csv(PATH_NOTAS)

print(df_notas["year"].nunique())   # a) .nunique() conta valores ÚNICOS (sem repetição)
print(df_notas["score"].mean())     # b) .mean() calcula a média aritmética da coluna
print(df_notas["score"].std())      # c) .std() calcula o desvio padrão da coluna


# ----------------------------------------------------------
# Questão 8
# Carregue o arquivo salary.xlsx em um DataFrame chamado df_salary.
# Responda:
# a) Quantas linhas e colunas existem?
# b) Qual é o maior salário registrado?
# c) Qual é o menor salário registrado?
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary = pd.read_excel(PATH_SALARY)
# pd.read_excel() para arquivos .xlsx (Excel).

print(df_salary.shape)              # a) (nº_linhas, nº_colunas)
print(df_salary["salary"].max())    # b) maior valor da coluna "salary"
print(df_salary["salary"].min())    # c) menor valor da coluna "salary"


# ===========================================================
# PARTE 3 – FILTROS E SELEÇÕES
# ===========================================================

# ----------------------------------------------------------
# Questão 9  (Dataset: titanic.csv)
# a) Filtre apenas as passageiras do sexo feminino.
# b) Quantos passageiros sobreviveram? (Survived == 1)
# c) Quantos homens sobreviveram?
# d) Quantos passageiros têm "John" no nome?
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
feminino = df_titanic[df_titanic["Sex"] == "female"]
# Filtro simples: mantém apenas linhas onde Sex é "female".
print(feminino)

# b)
sobreviventes = df_titanic[df_titanic["Survived"] == 1]["PassengerId"].nunique()
# Passo 1: filtra linhas onde Survived == 1 (sobreviveu).
# Passo 2: seleciona coluna "PassengerId".
# Passo 3: .nunique() conta IDs únicos = número de passageiros distintos que sobreviveram.
print(f"{sobreviventes} passageiros sobreviveram")

# c)
homens_sobrev = df_titanic[(df_titanic["Sex"] == "male") & (df_titanic["Survived"] == 1)]["PassengerId"].nunique()
# Filtro duplo: sexo masculino E sobreviveu.
# Ambas as condições devem ser verdadeiras (&).
print(f"{homens_sobrev} homens sobreviveram")

# d)
johns = df_titanic[df_titanic["Name"].str.contains("John")]["PassengerId"].nunique()
# .str.contains("John") → True para nomes que contêm "John" em qualquer posição.
print(f"{johns} passageiros têm 'John' no nome")


# ----------------------------------------------------------
# Questão 10  (Dataset: notas.csv)
# a) Mostre apenas as colunas 'institution', 'country' e 'score'.
# b) Filtre universidades com score maior que 80.
# c) Filtre universidades dos EUA ("USA") com score maior que 80.
# d) Mostre as 10 melhores universidades (menor world_rank).
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
print(df_notas[["institution", "country", "score"]])
# [[lista de colunas]] → retorna DataFrame com somente essas 3 colunas.

# b)
top_80 = df_notas[df_notas["score"] > 80]
# Filtro: mantém linhas com score maior que 80.
print(top_80["institution"])

# c)
top_80_eua = df_notas[(df_notas["score"] > 80) & (df_notas["country"] == "USA")]
# Filtro duplo: score > 80 E país = "USA".
print(top_80_eua["institution"])

# d)
top_10 = df_notas.nsmallest(10, "world_rank")
# .nsmallest(10, "world_rank") → retorna as 10 linhas com MENORES world_rank.
# world_rank 1 = melhor universidade, então menor = melhor.
print(top_10["institution"])


# ----------------------------------------------------------
# Questão 11  (Dataset: salary.xlsx)
# a) Crie um df com apenas as colunas:
#    job_title, salary, company_location, company_size, remote_ratio
# b) Filtre profissões no Brasil ("BR").
# c) Filtre profissões nos EUA ("US") em empresas grandes ("L").
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
df_sal_reduzido = df_salary[["job_title", "salary", "company_location", "company_size", "remote_ratio"]]
# Seleciona apenas as 5 colunas especificadas, ignorando as demais.
print(df_sal_reduzido)

# b)
brasil_sal = df_salary[df_salary["company_location"] == "BR"]
# Filtra linhas onde a empresa fica no Brasil (código "BR").
print(brasil_sal["job_title"])

# c)
eua_grandes = df_salary[(df_salary["company_location"] == "US") & (df_salary["company_size"] == "L")]
# Filtro duplo: localização = "US" E tamanho = "L" (Large = grande).
print(eua_grandes["job_title"].nunique())
# .nunique() → quantas profissões DIFERENTES existem nesse filtro.


# ----------------------------------------------------------
# Questão 12  (Dataset: notas.csv)
# Use .loc para selecionar linhas onde o país é "Brazil"
# e mostre apenas as colunas 'institution' e 'score'.
# (Dica: filtro = df_notas["country"] == "Brazil")
# ----------------------------------------------------------

# RESOLVA AQUI:
filtro_br = df_notas["country"] == "Brazil"
# Cria uma Série booleana: True para linhas onde country = "Brazil".
df_brazil = df_notas.loc[filtro_br, ["institution", "score"]]
# .loc[filtro, colunas]: seleciona LINHAS pelo filtro E COLUNAS pela lista.
# Mais explícito que o filtro simples — melhor para combinar filtro + seleção de colunas.
print(df_brazil)


# ----------------------------------------------------------
# Questão 13  (Dataset: notas.csv)
# Use .str.contains() para filtrar universidades cujo nome
# contenha "Technology" (sem diferenciar maiúsculas/minúsculas).
# ----------------------------------------------------------

# RESOLVA AQUI:
filtro_tech = df_notas["institution"].str.contains("Technology", case=False)
# .str.contains("Technology") → True para nomes que contêm "Technology".
# case=False → ignora maiúsculas/minúsculas ("technology", "TECHNOLOGY" também passam).
df_tech = df_notas[filtro_tech]
# Aplica o filtro booleano ao DataFrame.
print(df_tech[["institution", "country", "score"]])


# ===========================================================
# PARTE 4 – CÁLCULOS E NOVAS COLUNAS
# ===========================================================

# ----------------------------------------------------------
# Questão 14  (Dataset: salary.xlsx)
# Crie uma nova coluna chamada 'salary_k' que representa
# o salário em milhares (salary / 1000).
# ----------------------------------------------------------

# RESOLVA AQUI:
df_salary["salary_k"] = df_salary["salary"] / 1000
# df["nova_coluna"] = expressão → cria nova coluna com operação sobre coluna existente.
# Cada valor de "salary" é dividido por 1000.
print(df_salary[["job_title", "salary", "salary_k"]].head())
# .head() → exibe as primeiras 5 linhas para verificar o resultado.


# ----------------------------------------------------------
# Questão 15  (Dataset: notas.csv)
# a) Qual a média, máximo e mínimo da coluna 'score'?
# b) Quantos valores nulos existem na coluna 'broad_impact'?
# c) Preencha os nulos de 'broad_impact' com a média da coluna.
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
print(f"Média:  {df_notas['score'].mean():.2f}")   # média com 2 casas decimais
print(f"Máximo: {df_notas['score'].max()}")         # maior valor
print(f"Mínimo: {df_notas['score'].min()}")         # menor valor

# b)
print(f"Nulos em broad_impact: {df_notas['broad_impact'].isnull().sum()}")
# .isnull() → True onde o valor é NaN.
# .sum() → soma os True (contagem de nulos).

# c)
df_notas["broad_impact"] = df_notas["broad_impact"].fillna(df_notas["broad_impact"].mean())
# .fillna(valor) → substitui NaN pelo valor passado.
# Usamos a própria média da coluna como valor de preenchimento.
# Boa prática: preencher com média não altera a média geral da coluna.


# ----------------------------------------------------------
# Questão 16  (Dataset: titanic.csv)
# Crie uma nova coluna chamada 'sobreviveu_texto' que contém
# "Sim" quando Survived == 1 e "Não" caso contrário.
# (Dica: use df.apply() ou np.where / condição com assign)
# ----------------------------------------------------------

# RESOLVA AQUI:
df_titanic["sobreviveu_texto"] = df_titanic["Survived"].apply(lambda x: "Sim" if x == 1 else "Não")
# .apply(função) → aplica a função em CADA valor da coluna, linha por linha.
# lambda x: "Sim" if x == 1 else "Não"
#   → função anônima (lambda): recebe x, retorna "Sim" se x==1, senão "Não".
#   → equivalente a uma função if/else para cada célula.
print(df_titanic[["Name", "Survived", "sobreviveu_texto"]].head())


# ===========================================================
# PARTE 5 – AGRUPAMENTOS (GROUPBY)
# ===========================================================

# ----------------------------------------------------------
# Questão 17  (Dataset: notas.csv)
# a) Calcule a média do score por país.
# b) Qual país tem a maior média de score?
# c) Quantas universidades cada país tem?
# d) Top 5 países com mais universidades.
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
media_pais = df_notas.groupby("country")["score"].mean()
# groupby("country") → agrupa linhas pelo país.
# ["score"].mean()   → calcula a média de score dentro de cada grupo.
print(media_pais)

# b)
print(f"País com maior média: {media_pais.idxmax()}")
# .idxmax() → retorna o ÍNDICE (nome do país) com o maior valor na Série.

# c)
count_pais = df_notas.groupby("country")["institution"].count()
# .count() → conta quantas linhas (universidades) existem em cada grupo.
print(count_pais)

# d)
print(count_pais.sort_values(ascending=False).head(5))
# .sort_values(ascending=False) → ordena do maior para o menor.
# .head(5) → pega os 5 primeiros (top 5 países com mais universidades).


# ----------------------------------------------------------
# Questão 18  (Dataset: salary.xlsx)
# a) Qual profissão tem a maior média salarial?
# b) Qual profissão tem a menor média salarial?
# c) Quais profissões têm média salarial ACIMA da média geral?
# d) Qual a média salarial no Brasil ("BR")?
# ----------------------------------------------------------

# RESOLVA AQUI:
media_geral = df_salary["salary"].mean()
# Calcula a média salarial de TODOS os registros (sem filtro).

# a) e b)
media_prof = df_salary.groupby("job_title")["salary"].mean()
# Agrupa por profissão e calcula a média salarial de cada uma.
print(f"Maior média: {media_prof.idxmax()}")   # profissão com maior média
print(f"Menor média: {media_prof.idxmin()}")   # profissão com menor média

# c)
acima_media = media_prof[media_prof > media_geral]
# Filtra a Série 'media_prof': mantém só as profissões com média > media_geral.
print(acima_media)

# d)
media_br = df_salary[df_salary["company_location"] == "BR"]["salary"].mean()
# Passo 1: filtra linhas do Brasil.
# Passo 2: seleciona coluna "salary".
# Passo 3: calcula a média.
print(f"Média salarial no Brasil: {media_br:.2f}")


# ----------------------------------------------------------
# Questão 19  (Dataset: salary.xlsx)
# a) Qual modalidade (remote_ratio) paga mais em média?
#    (0 = Presencial, 50 = Híbrido, 100 = Remoto)
# b) Qual país tem o maior número de profissões trabalhando
#    100% remoto?
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
media_remoto = df_salary.groupby("remote_ratio")["salary"].mean()
# Agrupa pelos valores de remote_ratio (0, 50 ou 100) e calcula a média salarial.
print(f"Modalidade com maior média: {media_remoto.idxmax()}")
# .idxmax() → retorna o valor de remote_ratio com maior média (0, 50 ou 100).

# b)
remoto_pais = df_salary[df_salary["remote_ratio"] == 100].groupby("company_location")["job_title"].nunique()
# Passo 1: filtra apenas trabalhadores 100% remotos.
# Passo 2: agrupa por país.
# Passo 3: conta profissões únicas por país.
print(f"País com mais profissões 100% remotas: {remoto_pais.idxmax()}")


# ----------------------------------------------------------
# Questão 20  (Dataset: notas.csv)
# a) Calcule a média do score por ano.
# b) Qual ano teve a maior média de score?
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
media_ano = df_notas.groupby("year")["score"].mean()
# Agrupa por ano e calcula a média de score de cada ano.
print(media_ano)

# b)
print(f"Ano com maior média: {media_ano.idxmax()}")
# .idxmax() retorna o ANO (índice) com a maior média de score.


# ===========================================================
# PARTE 6 – RANKING E ORDENAÇÃO
# ===========================================================

# ----------------------------------------------------------
# Questão 21  (Dataset: notas.csv)
# a) Ordene o DataFrame pelo score de forma DECRESCENTE.
# b) Crie uma coluna 'rank_score' que rankeia as universidades
#    pelo score (1 = maior score).
# c) Mostre as 5 primeiras linhas após a ordenação.
# ----------------------------------------------------------

# RESOLVA AQUI:
# a) e c)
df_notas_ord = df_notas.sort_values("score", ascending=False)
# .sort_values("score", ascending=False) → ordena pelo score do maior para o menor.
print(df_notas_ord[["institution", "score"]].head(5))
# .head(5) → primeiras 5 linhas (as 5 universidades com maior score).

# b)
df_notas["rank_score"] = df_notas["score"].rank(ascending=False)
# .rank(ascending=False) → rank 1 = maior valor (melhor universidade).
# ascending=True → rank 1 = menor valor.
# A nova coluna "rank_score" é adicionada ao DataFrame original.
print(df_notas[["institution", "score", "rank_score"]].head())


# ----------------------------------------------------------
# Questão 22  (Dataset: salary.xlsx)
# a) Ordene o DataFrame pelo salary de forma DECRESCENTE.
# b) Mostre as 10 profissões mais bem pagas (sem repetição).
# ----------------------------------------------------------

# RESOLVA AQUI:
# a)
df_sal_ord = df_salary.sort_values("salary", ascending=False)
# Ordena por salary do maior para o menor.
print(df_sal_ord[["job_title", "salary"]].head(10))

# b)
top_10_prof = df_sal_ord["job_title"].drop_duplicates().head(10)
# .drop_duplicates() → remove linhas com valores repetidos na coluna.
# Depois .head(10) pega as 10 primeiras profissões únicas (sem repetição).
print(top_10_prof)


# ----------------------------------------------------------
# Questão 23  (Dataset: notas.csv)
# Mostre as 5 melhores universidades do Brasil.
# (Dica: filtre por country == "Brazil" e ordene por world_rank)
# ----------------------------------------------------------

# RESOLVA AQUI:
df_br_univ = df_notas[df_notas["country"] == "Brazil"]
# Filtra apenas as universidades do Brasil.
top5_br = df_br_univ.nsmallest(5, "world_rank")
# .nsmallest(5, "world_rank") → as 5 com MENOR world_rank (melhor colocação global).
print(top5_br[["institution", "world_rank", "score"]])


# ===========================================================
# PARTE 7 – APIs (Laboratório de Finanças – BCB)
# ===========================================================

# ----------------------------------------------------------
# Questão 24
# Explique com suas palavras o que é uma API, um endpoint,
# e o que significa o status_code 200.
# ----------------------------------------------------------

"""
RESPONDA AQUI:

API (Application Programming Interface): é uma interface que permite
que dois sistemas se comuniquem e troquem dados de forma estruturada.

Endpoint: é a URL específica de um recurso dentro de uma API,
ou seja, o endereço exato de onde buscar o dado desejado.

Status_code 200: significa que a requisição foi bem-sucedida
(o servidor recebeu, processou e retornou os dados corretamente).
"""


# ----------------------------------------------------------
# Questão 25
# Complete o código abaixo para consumir a API do BCB e obter
# a cotação do dólar PTAX em 2024. Depois:
# a) Transforme a resposta em DataFrame.
# b) Converta a coluna 'valor' para float.
# c) Calcule a média, máximo e mínimo da cotação.
# ----------------------------------------------------------

# RESOLVA AQUI:
url_bcb = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"
# Endpoint da série histórica do dólar PTAX no BCB.

parametros = {
    "formato":      "json",
    "dataInicial":  "01/01/2024",
    "dataFinal":    "31/12/2024"
}
# Parâmetros de consulta: filtram o período de dados.
# O requests adiciona automaticamente na URL como query string.

response_bcb = requests.get(url_bcb, params=parametros)
# params=parametros → passa o dicionário de parâmetros para a URL.

print(f"Status: {response_bcb.status_code}")
# Verificamos o status antes de usar os dados.

if response_bcb.status_code == 200:
    # a)
    df_bcb = pd.DataFrame(response_bcb.json())
    # .json() converte JSON em lista de dicts. pd.DataFrame() transforma em tabela.
    print(df_bcb.head())

    # b)
    df_bcb["valor"] = df_bcb["valor"].astype(float)
    # .astype(float) → converte o tipo da coluna para float.
    # O BCB retorna os valores como string ("4.8970"); precisamos de número para calcular.

    # c)
    print(f"Média:  R$ {df_bcb['valor'].mean():.4f}")   # média com 4 casas decimais
    print(f"Máximo: R$ {df_bcb['valor'].max():.4f}")    # maior cotação do período
    print(f"Mínimo: R$ {df_bcb['valor'].min():.4f}")    # menor cotação do período


# ----------------------------------------------------------
# Questão 26
# Use a API do BCB para consultar a cotação do dólar em 2023.
# Qual foi o maior valor registrado e em que data ocorreu?
# (Dica: use df_bcb.loc[df_bcb['valor'].idxmax()])
# ----------------------------------------------------------

# RESOLVA AQUI:
parametros_2023 = {
    "formato":      "json",
    "dataInicial":  "01/01/2023",
    "dataFinal":    "31/12/2023"
}
# Mesmo endpoint do BCB, mas com período 2023.

response_2023 = requests.get(url_bcb, params=parametros_2023)

if response_2023.status_code == 200:
    df_2023 = pd.DataFrame(response_2023.json())
    df_2023["valor"] = df_2023["valor"].astype(float)
    # Converte para float para poder calcular o máximo.

    idx_max = df_2023["valor"].idxmax()
    # .idxmax() → retorna o ÍNDICE (número da linha) onde está o maior valor.
    linha_max = df_2023.loc[idx_max]
    # .loc[índice] → acessa a linha pelo índice retornado pelo idxmax().
    print(f"Maior cotação em 2023: R$ {linha_max['valor']:.4f} em {linha_max['data']}")


# ----------------------------------------------------------
# Questão 27
# Consulte a API do ViaCEP para o CEP 01310-100 (Av. Paulista).
# a) Verifique o status_code.
# b) Transforme o resultado em DataFrame.
# c) Mostre as colunas: cep, logradouro, bairro, localidade, uf.
# ----------------------------------------------------------

# RESOLVA AQUI:
url_cep = "https://viacep.com.br/ws/01310100/json/"
# O CEP é passado diretamente na URL (sem traço). Formato: /ws/{CEP}/json/
response_cep = requests.get(url_cep)

# a)
print(f"Status ViaCEP: {response_cep.status_code}")

if response_cep.status_code == 200:
    # b)
    df_cep = pd.DataFrame([response_cep.json()])
    # O ViaCEP retorna um ÚNICO dicionário (não lista).
    # Envolvemos em [ ] para criar um DataFrame com 1 linha.

    # c)
    print(df_cep[["cep", "logradouro", "bairro", "localidade", "uf"]])


# ----------------------------------------------------------
# Questão 28
# Consulte a lista de bancos usando a BrasilAPI.
# a) Transforme em DataFrame.
# b) Quantos bancos existem no total?
# c) Filtre os bancos cujo nome (fullName) contenha "Brasil".
# ----------------------------------------------------------

# RESOLVA AQUI:
url_bancos = "https://brasilapi.com.br/api/banks/v1"
response_bancos = requests.get(url_bancos)

if response_bancos.status_code == 200:
    # a)
    df_bancos = pd.DataFrame(response_bancos.json())
    # JSON retorna lista de dicts → pd.DataFrame() direto.

    # b)
    print(f"Total de bancos: {len(df_bancos)}")
    # len(df_bancos) = número de linhas = número de bancos.

    # c)
    df_bancos["fullName"] = df_bancos["fullName"].fillna("")
    # Preenche NaN com string vazia para evitar erro no .str.contains().
    bancos_brasil = df_bancos[df_bancos["fullName"].str.contains("Brasil", case=False)]
    # .str.contains("Brasil", case=False) → True para nomes com "Brasil" (ignora capitalização).
    print(bancos_brasil[["ispb", "name", "code"]])


# ----------------------------------------------------------
# Questão 29
# Consulte a API do IBGE para obter a lista de estados brasileiros.
# a) Transforme em DataFrame.
# b) Extraia o nome da região de cada estado (coluna 'regiao').
# c) Mostre apenas: nome, sigla e regiao_nome.
# ----------------------------------------------------------

# RESOLVA AQUI:
url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response_ibge = requests.get(url_ibge)

if response_ibge.status_code == 200:
    # a)
    df_estados = pd.DataFrame(response_ibge.json())
    # Cada estado é um dict com chaves: id, sigla, nome, regiao.
    # 'regiao' é um dicionário aninhado: {"id": ..., "sigla": ..., "nome": ...}

    # b)
    df_estados["regiao_nome"] = df_estados["regiao"].apply(
        lambda x: x.get("nome") if isinstance(x, dict) else None
    )
    # .apply(lambda x: ...) → aplica função em cada elemento da coluna "regiao".
    # lambda x: x.get("nome") → extrai o valor da chave "nome" do dict aninhado.
    # isinstance(x, dict) → verifica se é dicionário antes de chamar .get() (segurança).

    # c)
    print(df_estados[["nome", "sigla", "regiao_nome"]])


# ----------------------------------------------------------
# Questão 30 – DESAFIO INTEGRADOR
# Use a API do BCB para comparar a cotação média do dólar
# entre 2022, 2023 e 2024. Crie um DataFrame resumo com as
# colunas 'ano' e 'media_dolar' e ordene do maior para o menor.
# ----------------------------------------------------------

# RESOLVA AQUI:
anos = {
    "2022": ("01/01/2022", "31/12/2022"),
    "2023": ("01/01/2023", "31/12/2023"),
    "2024": ("01/01/2024", "31/12/2024"),
}
# Dicionário com o ano como chave e uma tupla (data_inicial, data_final) como valor.

resumo = []
# Lista acumuladora: cada item será um dict {"ano": ..., "media_dolar": ...}.

for ano, (inicio, fim) in anos.items():
    # Desempacota a tupla: 'inicio' = primeiro elemento, 'fim' = segundo.
    params = {"formato": "json", "dataInicial": inicio, "dataFinal": fim}
    res = requests.get(url_bcb, params=params)
    if res.status_code == 200:
        df_ano = pd.DataFrame(res.json())
        df_ano["valor"] = df_ano["valor"].astype(float)
        # Converte para float para calcular a média.
        media = df_ano["valor"].mean()
        resumo.append({"ano": ano, "media_dolar": round(media, 4)})
        # round(media, 4) → arredonda para 4 casas decimais.
        # Adiciona o resultado do ano na lista acumuladora.

df_resumo = pd.DataFrame(resumo).sort_values("media_dolar", ascending=False)
# pd.DataFrame(resumo) → transforma a lista de dicts em tabela.
# .sort_values("media_dolar", ascending=False) → ordena do maior para o menor.
print(df_resumo)

# ============================================================
# RESUMO COMPLETO AP1 — ANÁLISE DE DADOS
# ============================================================


import pandas as pd
import requests


# ============================================================
# PARTE 1 — LISTAS
# ============================================================

lista = [1, 2, 3, 4, 5]

lista[0]           # primeiro elemento
lista[-1]          # último elemento
lista.append(6)    # adiciona no final
lista.remove(3)    # remove a primeira ocorrência do valor 3
lista.sort()       # ordena crescente (modifica a própria lista)
lista.reverse()    # inverte a ordem (modifica a própria lista)
lista.index(2)     # retorna a posição do valor 2
lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2   # concatena → [1, 2, 3, 4]

len(lista)         # quantidade de elementos
sum(lista)         # soma de todos os elementos
max(lista)         # maior valor
min(lista)         # menor valor

list(range(1, 11)) # cria lista de 1 até 10 (o 11 é exclusivo)

# LOOP FOR — percorre cada elemento
for item in lista:
    print(item)

# FOR com filtro e acumulador
pares = []
for numero in lista:
    if numero % 2 == 0:   # % = resto da divisão. Se resto == 0, é par
        pares.append(numero)

# LOOP WHILE — repete enquanto a condição for verdadeira
num = 1
while num <= 10:
    print(num)
    num += 1   # SEMPRE atualizar a variável, senão loop infinito


# ============================================================
# PARTE 2 — DICIONÁRIOS
# ============================================================

d = {"nome": "Ana", "idade": 20, "curso": "Adm"}

d["nome"]                 # acessa o valor da chave "nome"
d["cidade"] = "SP"        # adiciona nova chave
d["idade"] = 21           # atualiza valor de chave existente
d.pop("cidade")           # remove a chave "cidade"
d.get("nome", "vazio")    # retorna o valor ou "vazio" se não existir (sem erro)
d.items()                 # retorna pares (chave, valor) para iterar
d.keys()                  # retorna só as chaves
d.values()                # retorna só os valores
len(d)                    # número de pares chave-valor
sum(d.values())           # soma todos os valores (se forem numéricos)

# ITERAR sobre dicionário
for chave, valor in d.items():
    print(chave, valor)

# CONTAR frequência de elementos com dicionário
lista = ["maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    frequencia[item] = frequencia.get(item, 0) + 1
# get(item, 0) → retorna o valor atual ou 0 se ainda não existe
# +1 → incrementa a contagem

# DICIONÁRIO ANINHADO — valor é outro dicionário
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
}
turma["Ana"]["notas"]    # acessa a lista de notas de Ana
turma["Ana"]["notas"][0] # acessa o primeiro elemento da lista de notas


# ============================================================
# PARTE 3 — PANDAS
# ============================================================

# --- CARREGAR DADOS ---
df = pd.read_csv("arquivo.csv")
df = pd.read_excel("arquivo.xlsx")

# Criar DataFrame a partir de dicionário
dados = {"col1": [1, 2, 3], "col2": [4, 5, 6]}
df = pd.DataFrame(dados)

# --- EXPLORAÇÃO INICIAL ---
df.shape           # (nº linhas, nº colunas)
df.dtypes          # tipo de dado de cada coluna
df.head(5)         # primeiras 5 linhas
df.describe()      # estatísticas descritivas das colunas numéricas
df.isnull().sum()  # quantidade de nulos por coluna
df["col"].unique()    # valores únicos da coluna
df["col"].nunique()   # quantidade de valores únicos (sem repetição)

# --- SELEÇÃO ---
df["coluna"]               # uma coluna → retorna Série
df[["col1", "col2"]]       # múltiplas colunas → retorna DataFrame
df.iloc[0]                 # primeira linha pelo número do índice
df.iloc[2:5]               # linhas 2, 3 e 4 (o 5 é exclusivo)
df.loc[filtro, ["col1"]]   # filtro de linhas + seleciona colunas ao mesmo tempo

# --- FILTROS ---
df[df["col"] == "valor"]          # igualdade exata
df[df["col"] != "valor"]          # diferente
df[df["col"] > 80]                # maior que
df[df["col"] >= 80]               # maior ou igual

# Filtro duplo com & (E) ou | (OU) — CADA CONDIÇÃO ENTRE PARÊNTESES
df[(df["col1"] == "Brasil") & (df["col2"] > 10)]    # ambas verdadeiras
df[(df["col1"] == "Brasil") | (df["col1"] == "EUA")] # qualquer uma verdadeira

df[df["col"].str.contains("texto", case=False, na=False)]
# str.contains → True se a string contiver o texto
# case=False   → ignora maiúscula/minúscula
# na=False     → trata nulos como False (evita erro)

df[df["col"].between(50, 100)]
# between(a, b) → equivale a: (col >= 50) & (col <= 100), ambos inclusivos

# --- ESTATÍSTICAS ---
df["col"].mean()    # média
df["col"].max()     # máximo
df["col"].min()     # mínimo
df["col"].sum()     # soma
df["col"].std()     # desvio padrão
df["col"].count()   # contagem de valores não-nulos
df["col"].nunique() # quantidade de valores únicos

# Top N valores
df.nsmallest(10, "col")  # 10 linhas com os menores valores
df.nlargest(10, "col")   # 10 linhas com os maiores valores

# --- CRIAR/MODIFICAR COLUNAS ---
df["nova"] = df["col1"] / df["col2"]   # operação entre colunas
df["passou"] = df["nota"] >= 7         # coluna booleana (True/False)
df["rank"] = df["col"].rank(ascending=False)  # rank 1 = maior valor

# --- ORDENAÇÃO ---
df.sort_values(by="col", ascending=False)              # decrescente
df.sort_values(by=["col1", "col2"], ascending=[True, False])  # múltiplos critérios

# --- GROUPBY ---
df.groupby("col")["valor"].mean()    # média por grupo
df.groupby("col")["valor"].sum()     # soma por grupo
df.groupby("col")["valor"].max()     # máximo por grupo
df.groupby("col")["valor"].count()   # contagem por grupo
df.groupby("col").size()             # nº de linhas por grupo (inclui tudo)

resultado = df.groupby("col")["valor"].mean()
resultado.idxmax()   # retorna o NOME do grupo com maior valor
resultado.idxmin()   # retorna o NOME do grupo com menor valor

# GroupBy com múltiplas colunas e múltiplas funções ao mesmo tempo
df.groupby(["col1", "col2"])["valor"].agg(["sum", "mean", "count"])

# --- MISSING VALUES (VALORES NULOS) ---
df.isnull().sum()                  # conta nulos por coluna
df.dropna(subset=["col"])          # remove linhas com nulo na coluna especificada
df.fillna(0)                       # substitui todos os nulos por 0
df.fillna(df["col"].mean())        # substitui nulos pela média da coluna

# --- PIVOT TABLE ---
df.pivot_table(
    index="col_linha",      # o que vai nas linhas
    columns="col_coluna",   # o que vai nas colunas
    values="col_valor",     # valores a exibir
    aggfunc="sum"           # função de agregação: sum, mean, count...
)

# --- CONVERSÕES ---
df.to_dict(orient="records")  # DataFrame → lista de dicionários [{}, {}, ...]
df.to_dict(orient="list")     # DataFrame → dicionário de listas {"col": [...]}
df["col"].to_list()           # Série (coluna) → lista Python comum

df["col"] = pd.to_datetime(df["col"])  # converte string para data
df["col"].dt.year                       # extrai o ano
df["col"].dt.month                      # extrai o mês

df["col"] = df["col"].astype(float)    # converte tipo da coluna para float


# ============================================================
# PARTE 4 — APIs COM REQUESTS
# ============================================================

# --- FLUXO BÁSICO (sem parâmetros, sem token) ---

url = "https://brasilapi.com.br/api/banks/v1"
# URL = endereço do endpoint (cada API tem o seu)

response = requests.get(url)
# Envia a requisição HTTP GET para o servidor
# Retorna um objeto com: .status_code, .json(), .text

print(response.status_code)
# 200 → OK, deu certo
# 400 → Bad Request (requisição errada)
# 401 → Unauthorized (token inválido ou ausente)
# 404 → Not Found (endpoint não existe)
# 500 → Server Error (erro no servidor)

if response.status_code == 200:          # só usa os dados se deu certo
    dados = response.json()
    # .json() converte o JSON (texto) em estrutura Python (dict ou lista)

    # SE o JSON for uma LISTA de dicionários → [ {}, {}, {} ]
    df = pd.DataFrame(dados)

    # SE o JSON for UM ÚNICO dicionário → { "chave": "valor", ... }
    df = pd.DataFrame([dados])           # o [ ] é obrigatório aqui


# --- COM PARÂMETROS (filtragem via URL) ---

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"

params = {
    "formato": "json",
    "dataInicial": "01/01/2024",
    "dataFinal": "31/12/2024"
}
# Dicionário de parâmetros: cada chave é o nome do filtro que a API aceita
# O requests monta a URL automaticamente assim:
# .../dados?formato=json&dataInicial=01/01/2024&dataFinal=31/12/2024

response = requests.get(url, params=params)
# params=params → passa o dicionário de filtros para a requisição

if response.status_code == 200:
    df = pd.DataFrame(response.json())
    df["valor"] = df["valor"].astype(float)  # converter string → número
    print(df["valor"].mean())


# --- COM TOKEN (autenticação por chave) ---

url = "https://api.football-data.org/v4/areas"

headers = {
    "X-Auth-Token": "seu_token_aqui"
    # "X-Auth-Token" é o nome do cabeçalho que ESSA API específica exige
    # Outras APIs podem usar: "Authorization", "X-RapidAPI-Key", etc.
    # O valor é o token que você recebeu ao se cadastrar na API
}
# Headers são informações extras enviadas junto com a requisição
# O token viaja "escondido" nos headers, não aparece na URL

response = requests.get(url, headers=headers)

if response.status_code == 200:
    dados = response.json()
    df = pd.DataFrame(dados)


# --- COM PARÂMETROS + TOKEN AO MESMO TEMPO ---

url = "https://api.exemplo.com/dados"

params = {
    "cidade": "Brasilia",
    "pais": "BR"
}

headers = {
    "X-RapidAPI-Key": "seu_token_aqui",
    "X-RapidAPI-Host": "api.exemplo.com"
}

response = requests.get(url, params=params, headers=headers)
# params  → filtros que aparecem na URL
# headers → credenciais e metadados que ficam escondidos

if response.status_code == 200:
    dados = response.json()
    df = pd.DataFrame(dados.get("data", []))
    # .get("data", []) → acessa a chave "data" do dict
    #                    se não existir, retorna lista vazia []
    # Muitas APIs envolvem os dados numa chave como "data", "value", "results"


# ============================================================
# ARMADILHAS COMUNS — FIQUE ATENTO
# ============================================================

# ❌ ERRADO — selecionar múltiplas colunas sem lista dupla
# df["col1", "col2"]

# ✅ CERTO
df[["col1", "col2"]]

# ❌ ERRADO — JSON dict único sem o [ ]
# pd.DataFrame({"cep": "01310-100", "rua": "Av. Paulista"})

# ✅ CERTO
pd.DataFrame([{"cep": "01310-100", "rua": "Av. Paulista"}])

# ❌ ERRADO — filtro duplo sem parênteses em cada condição
# df[df["col1"] == "A" & df["col2"] > 10]

# ✅ CERTO
df[(df["col1"] == "A") & (df["col2"] > 10)]

# ❌ ERRADO — contar únicos com count() (conta repetidos também)
# df["col"].count()

# ✅ CERTO para valores únicos
df["col"].nunique()

# ❌ ERRADO — somar coluna de texto com sum() (concatena strings)
# df["nome"].sum()

# ✅ CERTO para contar ou verificar únicos em texto
df["nome"].count()    # conta não-nulos
df["nome"].nunique()  # conta valores distintos

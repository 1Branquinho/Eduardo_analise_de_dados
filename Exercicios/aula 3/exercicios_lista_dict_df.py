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
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
# b) Mostre as 5 primeiras linhas
# c) Mostre o formato (linhas, colunas)
# d) Mostre os tipos de dados das colunas

# RESOLUCAO:
df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas.head())
print(df_vendas.shape)
print(df_vendas.dtypes)


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
# b) Mostre somente a primeira linha
# c) Mostre as linhas de indice 2 ate 4

# RESOLUCAO:
print(df_vendas[["mes", "vendas"]])
print(df_vendas.iloc[0])
print(df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
# b) Filtre apenas a filial "Centro"
# c) Filtre vendas acima de 11000 na filial "Norte"

# RESOLUCAO:
print(df_vendas[df_vendas["vendas"] > 12000])
print(df_vendas[df_vendas["filial"] == "Centro"])
print(df_vendas[(df_vendas["vendas"] > 11000) & (df_vendas["filial"] == "Norte")])


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
# b) Crie a coluna "meta_batida" com True para vendas >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"

# RESOLUCAO:
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
# b) Calcule media de clientes por mes
# c) Descubra a filial com maior total de vendas

# RESOLUCAO:
print(df_vendas.groupby("filial")["vendas"].sum())
print(df_vendas.groupby("mes")["clientes"].mean())
print(df_vendas.groupby("filial")["vendas"].sum().idxmax())


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
# b) Pegue os 3 maiores resultados de vendas
# c) Mostre um ranking com "filial", "mes", "vendas"

# RESOLUCAO:
print(df_vendas.sort_values(by="vendas", ascending=False))
print(df_vendas.nlargest(3, "vendas"))
print(df_vendas.sort_values(by="vendas", ascending=False)[["filial", "mes", "vendas"]])


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
# 2) Ordene o resumo por total_vendas (desc)
# 3) Exiba qual filial teve melhor desempenho geral

# RESOLUCAO:
summary = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)
summary = summary.sort_values(by="total_vendas", ascending=False)
print(summary)
print(f"Top Performer: {summary.index[0]}")


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
# 2. Qual é o tipo do primeiro elemento?
# 3. Como acessar a lista da "Column A"?
# 4. Como acessar o segundo elemento da "Column C"?

# RESPONDA AQUI:
print(type(dados_list_dict))
print(type(dados_list_dict[0]))
print(dados_list_dict[0]["Column A"])
print(dados_list_dict[0]["Column C"][1])


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
# 2. Mostre:
#    - shape
#    - tipos das colunas
# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna

# RESOLVA AQUI:
df1 = pd.DataFrame(dados_list_dict[0])
print(df1.shape)
print(df1.dtypes)
print(df1.sum())
print(df1.mean())


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
# 2. Crie coluna "Media" = média por linha
# 3. Filtre linhas onde Total > 10

# RESOLVA AQUI:
df1["Total"] = df1.sum(axis=1)
df1["Media"] = df1[["Column A", "Column B", "Column C"]].mean(axis=1)
print(df1[df1["Total"] > 10])


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# RESOLVA AQUI:
print(df1.to_dict(orient="records"))
print(df1.to_dict(orient="list"))


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
# 2. Multiplique cada elemento da lista por 10.
# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.

# RESOLVA AQUI:
lista_a = df1["Column A"].tolist()
lista_a_x10 = [x * 10 for x in lista_a]
df1["Column A x10"] = lista_a_x10
print(df1)


# ===========================================================
# BASE DE DADOS EXPORTAÇÃO
# ===========================================================
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


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# RESOLVA AQUI:
print(type(dados))
print(len(dados))
print(dados[0].keys())
print(list(set([d["nome_pais"] for d in dados])))


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# RESOLVA AQUI:
df = pd.DataFrame(dados)
print(df.shape, df.dtypes)
print(df.head())
df["periodo"] = pd.to_datetime(df["periodo"])


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# RESOLVA AQUI:
print(df[df["nome_pais"] == "Brasil"])
print(df[df["descricao"] == "Produto A"])
print(df[df["valor"] > 4000])
print(df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")])

print(df.sort_values(by="valor"))
print(df.sort_values(by="valor", ascending=False))
print(df.sort_values(by=["periodo", "valor"]))


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# RESOLVA AQUI:
print(df.groupby("nome_pais")["valor"].sum())
print(df.groupby("descricao")["valor"].sum())
print(df.groupby("nome_pais")["valor"].mean())
print(df.groupby("nome_pais")["valor"].count())

# GroupBy Múltiplo
summary_multiple = df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])
print(summary_multiple)


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# RESOLVA AQUI:
pivot_products = df.pivot_table(index="periodo", columns="descricao", values="valor", aggfunc="sum")
print(pivot_products)

pivot_countries = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
print(pivot_countries)


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# RESOLVA AQUI:
df["year"] = df["periodo"].dt.year
df["month"] = df["periodo"].dt.month
df["valor_mil"] = df["valor"] / 1000
df["monthly_growth"] = df.groupby("descricao")["valor"].pct_change()


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# RESOLVA AQUI:
print(df.isnull().sum())
print(df[df["valor"] < 0])
print(df.duplicated().sum())
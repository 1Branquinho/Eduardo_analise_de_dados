import pandas as pd

# -------------------------------------------------
# BLOCO 1
# -------------------------------------------------
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

df_vendas = pd.DataFrame(dados_vendas)
print(df_vendas.head())
print(df_vendas.shape)
print(df_vendas.dtypes)

# -------------------------------------------------
# BLOCO 2
# -------------------------------------------------
print(df_vendas[["mes", "vendas"]])
print(df_vendas.iloc[0])
print(df_vendas.iloc[2:5])

# -------------------------------------------------
# BLOCO 3
# -------------------------------------------------
print(df_vendas[df_vendas["vendas"] > 12000])
print(df_vendas[df_vendas["filial"] == "Centro"])
print(df_vendas[(df_vendas["vendas"] > 11000) & (df_vendas["filial"] == "Norte")])

# -------------------------------------------------
# BLOCO 4
# -------------------------------------------------
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])

# -------------------------------------------------
# BLOCO 5
# -------------------------------------------------
print(df_vendas.groupby("filial")["vendas"].sum())
print(df_vendas.groupby("mes")["clientes"].mean())
print(df_vendas.groupby("filial")["vendas"].sum().idxmax())

# -------------------------------------------------
# BLOCO 6
# -------------------------------------------------
sorted_vendas = df_vendas.sort_values("vendas", ascending=False)
print(sorted_vendas)
print(df_vendas.nlargest(3, "vendas"))
print(df_vendas[["filial", "mes", "vendas"]].sort_values("vendas", ascending=False))

# -------------------------------------------------
# BLOCO 7
# -------------------------------------------------
summary = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)
summary = summary.sort_values("total_vendas", ascending=False)
print(summary)
print(summary.index[0])

# ===========================================================
# PARTE 1 - ESTRUTURA LIST + DICT
# ===========================================================
dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]

print(type(dados_list_dict))
print(type(dados_list_dict[0]))
print(dados_list_dict[0]["Column A"])
print(dados_list_dict[0]["Column C"][1])

# EXERCICIO 2
df1 = pd.DataFrame(dados_list_dict[0])
print(df1.shape)
print(df1.dtypes)
print(df1.sum())
print(df1.mean())

# EXERCICIO 3
df1["Total"] = df1.sum(axis=1)
df1["Media"] = df1[["Column A", "Column B", "Column C"]].mean(axis=1)
print(df1[df1["Total"] > 10])

# EXERCICIO 4
print(df1.to_dict(orient="records"))
print(df1.to_dict(orient="list"))

# EXERCICIO 5
lista_a = df1["Column A"].tolist()
lista_a_10 = [x * 10 for x in lista_a]
df1["Column A x10"] = lista_a_10

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

# PARTE 1
print(type(dados))
print(len(dados))
print(dados[0].keys())
print(pd.DataFrame(dados)["nome_pais"].unique())

# PARTE 2
df = pd.DataFrame(dados)
print(df.shape, df.dtypes)
print(df.head())
df["periodo"] = pd.to_datetime(df["periodo"])

# PARTE 3
print(df[df["nome_pais"] == "Brasil"])
print(df[df["descricao"] == "Produto A"])
print(df[df["valor"] > 4000])
print(df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")])

print(df.sort_values("valor"))
print(df.sort_values("valor", ascending=False))
print(df.sort_values(["periodo", "valor"]))

# PARTE 4
print(df.groupby("nome_pais")["valor"].sum())
print(df.groupby("descricao")["valor"].sum())
print(df.groupby("nome_pais")["valor"].mean())
print(df.groupby("nome_pais").size())

multi_group = df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])
print(multi_group)

# PARTE 5
pivot_prod = df.pivot_table(index="periodo", columns="descricao", values="valor", aggfunc="sum")
print(pivot_prod)
pivot_country = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
print(pivot_country)

# PARTE 6
df["year"] = df["periodo"].dt.year
df["month"] = df["periodo"].dt.month
df["valor_mil"] = df["valor"] / 1000
df["growth"] = df.groupby("descricao")["valor"].pct_change()

# PARTE 7
print(df.isnull().sum())
print((df["valor"] < 0).any())
print(df.duplicated().sum())
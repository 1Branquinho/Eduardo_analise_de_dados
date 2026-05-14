import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxMzUyMjY0LCJpYXQiOjE3Nzg3NjAyNjQsImp0aSI6IjIzY2I3ZmRmZTE4NjRiMzU4ZmVmMDEwMmI3MTczMzUwIiwidXNlcl9pZCI6IjExOCJ9.xm_Id4FqEBio2otRltBiR8BYLQGDb4w2cqyNOWuyW6c"
headers = {"Authorization": f"Bearer {token}"}

resp_2025 = requests.get(f"{base_url}/bolsa/balanco", headers=headers, params={"ticker": "ABEV3", "ano_tri": "20254T"})
df_2025 = pd.DataFrame(resp_2025.json()[0]['balanco'])

resp_2024 = requests.get(f"{base_url}/bolsa/balanco", headers=headers, params={"ticker": "ABEV3", "ano_tri": "20244T"})
df_2024 = pd.DataFrame(resp_2024.json()[0]['balanco'])

def encontrar_contas_contabeis(df):
    ativo_circ = float(df[df["conta"]=='1.01']['valor'].iloc[0])
    passivo_circ = float(df[df["conta"]=='2.01']['valor'].iloc[0])
    passivo_n_circ = float(df[df["conta"]=='2.02']['valor'].iloc[0])
    
    filtro_arlp = df["conta"] == '1.02.01'
    arlp = float(df[filtro_arlp]['valor'].iloc[0]) if not df[filtro_arlp].empty else 0.0
    
    filtro_desc = df["descricao"].str.contains('intang.vel', case=False)
    filtro_conta = df["conta"]=='1.02.04'
    intangivel = float(df[filtro_desc & filtro_conta]['valor'].iloc[0])
    
    filtro_desc = df["descricao"].str.contains('imobilizado', case=False)
    filtro_conta = df["conta"].str.contains('1.02.03', case=False)
    imobilizado = float(df[filtro_desc & filtro_conta]['valor'].iloc[0])
    
    filtro_desc = df["descricao"].str.contains('investimento', case=False)
    filtro_conta = df["conta"].str.contains('1.02.02', case=False)
    investimento = float(df[filtro_desc & filtro_conta]['valor'].iloc[0])
    
    filtro_desc = df["descricao"].str.contains('estoque', case=False)
    estoque = float(df[filtro_desc]['valor'].iloc[0])

    filtro_desc = df["descricao"].str.contains('custo.*bens', case=False)
    filtro_conta = df["conta"].str.contains('^3.*', case=False)
    cmv = float(df[filtro_desc & filtro_conta]['valor'].iloc[0])
    
    filtro_disponibilidades = df["conta"].isin(['1.01.01', '1.01.02'])
    caixa_equivalentes = df[filtro_disponibilidades]['valor'].astype(float).sum()

    filtro_despesa = df["descricao"].str.contains('antecipada', case=False)
    despesa_antecipada = float(df[filtro_despesa]['valor'].iloc[0]) if not df[filtro_despesa].empty else 0.0

    return {
        "ativo_circ": ativo_circ,
        "passivo_circ": passivo_circ,
        "passivo_n_circ": passivo_n_circ,
        "arlp": arlp,
        "intangivel": intangivel,
        "imobilizado": imobilizado,
        "investimento": investimento,
        "estoque": estoque,
        "despesa_antecipada": despesa_antecipada,
        "caixa_equivalentes": caixa_equivalentes,
        "cmv": cmv
    }

def calcular_indicadores(d):
    return {
        'ccl': d["ativo_circ"] - d["passivo_circ"],
        'lc': d["ativo_circ"] / d["passivo_circ"],
        'lg': (d["ativo_circ"] + d["arlp"]) / (d["passivo_circ"] + d["passivo_n_circ"]),
        'ls': (d["ativo_circ"] - d["estoque"] - d["despesa_antecipada"]) / d["passivo_circ"],
        'la': d["caixa_equivalentes"] / d["passivo_circ"]
    }



dic_2024 = encontrar_contas_contabeis(df_2024)
dic_2025 = encontrar_contas_contabeis(df_2025)

resultados_contas = {"2024": dic_2024, "2025": dic_2025}
resultados_indicadores = {"2024": calcular_indicadores(dic_2024), "2025": calcular_indicadores(dic_2025)}

anos = ["2024", "2025"]

for ano in anos:
    print(f"\n### Resultados do Exercício: {ano} ###")
    print("-" * 40)
    
    print("*Contas Contábeis Base:*")
    for conta, valor in resultados_contas[ano].items():
        # Formatação para o padrão brasileiro de moeda
        print(f"  * {conta}: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        
    print("\n*Indicadores Financeiros:*")
    for indicador, valor in resultados_indicadores[ano].items():
        if indicador == 'ccl':
            print(f"  * {indicador.upper()}: R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        else:
            print(f"  * {indicador.upper()}: {valor:.4f}")
            
    print("-" * 40)
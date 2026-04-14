import pandas as pd
import requests
import numpy as np


df = pd.read_csv("ncr_ride_bookings.csv")

#1 
completed_rides = len(df[df["Booking Status"] == "Completed"])
print(f"Número de corridas Completed: {completed_rides}")

#2
total_rides = len(df)
proportion = completed_rides / total_rides
print(f"Proporção de corridas Completed: {proportion:.4f} ({proportion*100:.2f}%)")

#3
media_distance_by_vehicle = df.groupby("Vehicle Type")["Ride Distance"].mean()
print("Média de Distância por Tipo de Veículo:")
print(media_distance_by_vehicle)
#4
bikes_payment = df[df["Vehicle Type"] == "Bike"]["Payment Method"].value_counts()
most_used_payment_bikes = bikes_payment.idxmax()
print(f"Método de Pagamento mais utilizado por Bikes: {most_used_payment_bikes}")

#5
total_value_completed = df[df["Booking Status"] == "Completed"]["Booking Value"].sum()
print(f"Valor total arrecadado (Completed): {total_value_completed:.2f}")

#6
average_value_completed = df[df["Booking Status"] == "Completed"]["Booking Value"].mean()
print(f"Ticket médio (Completed): {average_value_completed:.2f}")

#7
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
dados = response.json()
dados_list = dados["value"]
df_metadata = pd.DataFrame(dados_list)
fipe_vendas = df_metadata[(df_metadata["FNTSIGLA"] == "FIPE") & 
                          (df_metadata["SERNOME"].str.contains("vendas", case=False, na=False)) &
                          (df_metadata["SERNOME"].str.contains("Brasil", case=False, na=False))]
print("Séries FIPE de vendas de imóveis no Brasil:")
print(fipe_vendas[["SERCODIGO", "SERNOME"]])

#8
if len(fipe_vendas) > 0:
    codigo_encontrado = fipe_vendas.iloc[0]["SERCODIGO"]
    print(f"Código da série encontrado: {codigo_encontrado}")
    
    
    url_valores = f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{codigo_encontrado}')"
    response_valores = requests.get(url_valores)
    dados_valores = response_valores.json()
    df_valores = pd.DataFrame(dados_valores["value"])
    
    
    df_valores_filtrado = df_valores[["VALDATA", "VALVALOR"]]
    
    
    idx_max = df_valores_filtrado["VALVALOR"].idxmax()
    data_max = df_valores_filtrado.loc[idx_max, "VALDATA"]
    valor_max = df_valores_filtrado.loc[idx_max, "VALVALOR"]
    
    print(f"Data com maior valor de vendas: {data_max}")
    print(f"Valor máximo: {valor_max}")

#9

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwNDAwMiwiaWF0IjoxNzc2MTY4MDAyLCJqdGkiOiIxZjdjMzUzMThhZmM0OTczOTU3ZGYxZDQzMWE5OTg5MSIsInVzZXJfaWQiOiIxMTgifQ.HPIVwNgPeBh2iFTfk9QjS8t6Fw2dS-V3lvlkryi-kmESEU_JWT"
params = {"ticker": "VALE3", "data_ini": "2025-01-01", "data_fim": "2025-12-31"}
response = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = response.json()
df_vale = pd.DataFrame(dados)
rendimento_vale = ((df_vale.iloc[-1]["preco"] - df_vale.iloc[0]["preco"]) / df_vale.iloc[0]["preco"]) * 100
print(f"Rendimento VALE3 em 2025: {rendimento_vale:.2f}%")

#10

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwNDAwMiwiaWF0IjoxNzc2MTY4MDAyLCJqdGkiOiIxZjdjMzUzMThhZmM0OTczOTU3ZGYxZDQzMWE5OTg5MSIsInVzZXJfaWQiOiIxMTgifQ.HPIVwNgPeBh2iFTfk9QjS8t6Fw2dS-V3lvlkryi-kmE"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"},
)
dados = response.json()
df_planilhao = pd.DataFrame(dados)
tech_companies = df_planilhao[df_planilhao["setor"] == "tecnologia"]
top_roe = tech_companies.loc[tech_companies["roe"].idxmax()]
print(top_roe[["ticker", "setor", "roe"]])

#11
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzcwNDAwMiwiaWF0IjoxNzc2MTY4MDAyLCJqdGkiOiIxZjdjMzUzMThhZmM0OTczOTU3ZGYxZDQzMWE5OTg5MSIsInVzZXJfaWQiOiIxMTgifQ.HPIVwNgPeBh2iFTfk9QjS8t6Fw2dS-V3lvlkryi-kmE"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2024-04-01"},
)
dados = response.json()
df_planilhao = pd.DataFrame(dados)
df_planilhao["rank_roc"] = df_planilhao["roc"].rank(ascending=False)
df_planilhao["rank_ey"] = df_planilhao["ey"].rank(ascending=False)
df_planilhao["magic_score"] = df_planilhao["rank_roc"] + df_planilhao["rank_ey"]
carteira_magic = df_planilhao.nsmallest(10, "magic_score")[["ticker", "magic_score"]]
print("Carteira Magic Formula (10 ações):")
print(carteira_magic)


#12
num_setores = len(carteira_magic["setor"].unique())
print(f"Número de setores na carteira: {num_setores}")

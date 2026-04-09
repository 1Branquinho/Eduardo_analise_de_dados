import requests
import pandas as pd
import yfinance as yf

url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4MTU1MjgyLCJpYXQiOjE3NzU1NjMyODIsImp0aSI6IjBkYmJkZTJlZDkwODQwNjFiZmI3N2VmMzkyZjIyMzY2IiwidXNlcl9pZCI6IjExOCJ9.N6Ev_r5DaznsUE6kuEEXbGdxJ0f_831CoqP3HUX8vPE"

resp = requests.get(
    f"{url}/bolsa/planilhao",
    headers = {"Authorization": f"Bearer {token}"},
    params = {'data_base': '2021-04-01'}
)
df_magic = pd.DataFrame(resp.json())

df_rank = df_magic[['ticker', 'roic', 'earning_yield']].copy()
df_rank['rank_roic'] = df_rank['roic'].rank(ascending=False)
df_rank['rank_ey'] = df_rank['earning_yield'].rank(ascending=False)
df_rank['rank_final'] = df_rank['rank_roic'] + df_rank['rank_ey']
top_20 = df_rank.sort_values('rank_final').head(20)

params_preco = {'ticker': 'BBSE3', 'data_ini': '2001-01-01', 'data_fim': '2026-03-26'}
resp_preco = requests.get(
    f'{url}/preco/corrigido',
    headers = {"Authorization": f"Bearer {token}"},
    params = params_preco
)
df_preco = pd.DataFrame(resp_preco.json())

p_ini = df_preco.loc[df_preco['data'] == '2021-03-22', 'fechamento'].values[0]
p_fim = df_preco.loc[df_preco['data'] == '2026-03-23', 'fechamento'].values[0]
retorno_acao = (float(p_fim) / float(p_ini)) - 1

ibov = yf.download('^BVSP', start='2021-04-01', end='2026-03-31', progress=False)
ibov_ini = ibov.loc['2021-04-01', 'Close'].item()
ibov_fim = ibov.loc['2026-03-30', 'Close'].item()
retorno_ibov = (ibov_fim / ibov_ini) - 1

print(f"Top 20 Tickers:\n{top_20['ticker'].tolist()}")
print(f"Retorno BBSE3: {retorno_acao:.2%}")
print(f"Retorno Ibovespa: {retorno_ibov:.2%}")
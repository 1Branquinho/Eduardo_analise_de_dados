"""
===========================================================
ATIVIDADE – CONSULTA DE DADOS VIA API
OBJETIVO:
- Consultar APIs públicas usando requests
- Entender estrutura JSON
- Transformar resposta em DataFrame
- Trabalhar com parâmetros e TOKENS
- Explorar dados externos
REGRAS:
- NÃO apagar os enunciados.
- Organizar o código.
- Comentar cada etapa importante.
- Mostrar os resultados com print() ou DataFrame.
===========================================================
"""
import requests
import pandas as pd
# ===========================================================
# PARTE 1 – INTRODUÇÃO
# ===========================================================
"""
O que é uma API?
API (Application Programming Interface) permite que um sistema
se comunique com outro.
Quando usamos requests.get(), estamos enviando uma requisição
HTTP para um servidor que retorna dados, geralmente em JSON.
Fluxo básico:
1. Definir URL
2. Enviar requisição
3. Verificar status_code
4. Converter para JSON
5. Transformar em DataFrame (quando necessário)
"""
# ===========================================================
# PARTE 2 – VIACEP (Consulta de CEP)
# ===========================================================
"""
Site: https://viacep.com.br/
Exemplo de consulta:
https://viacep.com.br/ws/01001000/json/

Exercícios:
1. Consulte um CEP da sua escolha.
2. Verifique o status da requisição.
3. Converta a resposta para JSON.
4. Transforme em DataFrame.
5. Mostre as principais informações.
"""
# RESOLVA AQUI:

import requests
import pandas as pd

cep = "70610-440"
url_viacep = f"https://viacep.com.br/ws/{cep}/json/"
response_viacep = requests.get(url_viacep)

print(f"Status Code: {response_viacep.status_code}")

data_viacep = response_viacep.json()
df_viacep = pd.DataFrame([data_viacep])
print(df_viacep[["cep", "logradouro", "bairro", "localidade", "uf"]])

# ===========================================================
# PARTE 3 – BRASILAPI
# ===========================================================
"""
Documentação:
https://brasilapi.com.br/docs
Exercícios:
1. Consulte a lista de bancos.
2. Transforme o resultado em DataFrame.
3. Conte quantos bancos existem.
4. Filtre bancos cujo nome contenha "Brasil".
Explique:
O que você percebe sobre a estrutura do JSON retornado?
"""
# RESOLVA AQUI:
import requests
import pandas as pd

url_banks = "https://brasilapi.com.br/api/banks/v1"
response_banks = requests.get(url_banks)
data_banks = response_banks.json()

df_banks = pd.DataFrame(data_banks)
print(f"Total banks: {len(df_banks)}")

df_brasil = df_banks[df_banks['name'].str.contains("Brasil", case=False, na=False)]
print(df_brasil.head())

# ===========================================================
# PARTE 4 – SERVIÇO DE DADOS IBGE
# ===========================================================
"""
Documentação:
https://servicodados.ibge.gov.br/api/docs/
Exercícios:
1. Consulte os estados brasileiros.
2. Transforme em DataFrame.
3. Mostre apenas:
   - nome
   - sigla
   - região
4. Pesquise como consultar dados de população.
Desafio:
Consultar a população total de um estado específico.
"""
# RESOLVA AQUI:
import requests 
import pandas as pd

url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response_ibge = requests.get(url_ibge)
data_ibge = response_ibge.json()

df_states = pd.json_normalize(data_ibge)
df_states_clean = df_states[['nome', 'sigla', 'regiao.nome']]
print(df_states_clean.head())

url_pop = "https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/35"
pop_data = requests.get(url_pop).json()
print(f"SP Population: {pop_data['projecao']['populacao']}")


import requests
import pandas as pd
import matplotlib.pyplot as plt

# ===========================================================
# PARTE 5 – IPEA DATA
# ===========================================================

metadata_url = "http://www.ipeadata.gov.br/api/odata4/Metadados('AD12_GIGP12')"
metadata_response = requests.get(metadata_url)
metadata_json = metadata_response.json()['value']
print(pd.DataFrame(metadata_json)[['SERNOME', 'SERCOMENTARIO', 'UNINOME']])

values_url = "http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='AD12_GIGP12')"
values_response = requests.get(values_url)
values_json = values_response.json()['value']
df_ipea = pd.DataFrame(values_json)
print(df_ipea.head())

# ===========================================================
# PARTE 6 – BANCO CENTRAL DO BRASIL (BCB)
# ===========================================================

bcb_url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao/resources/usuario/pesquisa/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2024'&@dataFinalCotacao='12-31-2024'&$format=json"
bcb_response = requests.get(bcb_url)
bcb_data = bcb_response.json()['value']

df_usd = pd.DataFrame(bcb_data)
df_usd['dataHoraCotacao'] = pd.to_datetime(df_usd['dataHoraCotacao'])

print(df_usd['cotacaoCompra'].mean())
print(df_usd['cotacaoCompra'].max())
print(df_usd['cotacaoCompra'].min())

df_usd.set_index('dataHoraCotacao')['cotacaoCompra'].plot()
plt.show()

# ===========================================================
# PARTE 7 – FOOTBALL-DATA.ORG
# ===========================================================

headers = {'X-Auth-Token': 'YOUR_API_KEY'}
areas_url = "https://api.football-data.org/v4/areas/"
areas_response = requests.get(areas_url, headers=headers)
df_areas = pd.DataFrame(areas_response.json()['areas'])
print(df_areas[df_areas['countryCode'] == 'BRA'])

teams_url = "https://api.football-data.org/v4/competitions/BSA/teams?season=2025"
teams_response = requests.get(teams_url, headers=headers)
df_teams = pd.DataFrame(teams_response.json()['teams'])
print(df_teams[['name', 'shortName', 'tla']])

# ===========================================================
# PARTE 8 – RAPIDAPI (NBA Example)
# ===========================================================

rapid_url = "https://free-nba.p.rapidapi.com/players"
rapid_headers = {
    "X-RapidAPI-Key": "YOUR_RAPID_KEY",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}
rapid_response = requests.get(rapid_url, headers=rapid_headers, params={"page": "0", "per_page": "25"})
df_nba = pd.json_normalize(rapid_response.json()['data'])
print(df_nba.head())

# ===========================================================
# PARTE 9 – EXPLORAÇÃO LIVRE (PokeAPI)
# ===========================================================

poke_url = "https://pokeapi.co/api/v2/pokemon?limit=100"
poke_response = requests.get(poke_url)
df_poke = pd.DataFrame(poke_response.json()['results'])
print(df_poke.describe())
print(df_poke['name'].str.upper())

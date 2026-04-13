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
# ============================================================
# REFERÊNCIA RÁPIDA — APIs COM REQUESTS
# ============================================================
# FLUXO PADRÃO PARA CONSUMIR UMA API:
#   1. import requests
#   2. url = "https://endereço-da-api"
#   3. response = requests.get(url)           → faz a requisição HTTP GET
#   4. response.status_code                   → verifica se deu certo (200 = OK)
#   5. dados = response.json()                → converte resposta JSON para dict/lista Python
#   6. df = pd.DataFrame(dados)               → transforma em tabela para análise
#
# COM PARÂMETROS (filtragem via URL):
#   params = {"chave": "valor", "data": "01/01/2024"}
#   response = requests.get(url, params=params)
#   → O requests adiciona automaticamente ?chave=valor&data=01/01/2024 na URL
#
# COM HEADERS (autenticação por token):
#   headers = {"X-Auth-Token": "meu_token_aqui"}
#   response = requests.get(url, headers=headers)
#
# CÓDIGOS DE STATUS HTTP:
#   200 → OK (sucesso)
#   400 → Bad Request (requisição errada)
#   401 → Unauthorized (token inválido ou ausente)
#   404 → Not Found (endpoint não existe)
#   500 → Server Error (erro no servidor)
#
# JSON para DATAFRAME:
#   Se JSON é uma LISTA de dicts → pd.DataFrame(dados)
#   Se JSON é um DICT único      → pd.DataFrame([dados])   ← nota o [ ]
# ============================================================

import requests
import pandas as pd
print("Lab")
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
url = "https://servicodados.ibge.gov.br/api/v1/localidades/aglomeracoes-urbanas"
# URL = endereço do endpoint da API do IBGE para aglomerações urbanas.
response = requests.get(url)
# requests.get(url) → envia uma requisição HTTP GET para o servidor.
# Retorna um objeto Response com: .status_code, .json(), .text, etc.
response.status_code
# Código de retorno: 200 = sucesso. Se não for 200, houve erro.
dados = response.json()
# .json() converte o corpo da resposta (texto JSON) em estrutura Python.
# Se for uma lista → dados é uma lista de dicts.
# Se for um objeto → dados é um dicionário.
df = pd.DataFrame(dados)
# Converte a lista de dicts em DataFrame.
df = df.loc[:, ["nome"]]
# .loc[linhas, colunas]: seleciona TODAS as linhas (:) e apenas a coluna "nome".
df


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
# 1. Consulta ao CEP da Avenida Paulista
url_viacep = "https://viacep.com.br/ws/01310100/json/"
# A API do ViaCEP usa o CEP diretamente na URL (sem parâmetros separados).
# Padrão: https://viacep.com.br/ws/{CEP}/json/
response_viacep = requests.get(url_viacep)

# 2. Verifica o status da requisição
print(f"\n[ViaCEP] Status: {response_viacep.status_code}")
# 200 = sucesso. Imprimimos para confirmar antes de tentar usar os dados.

if response_viacep.status_code == 200:
    # 3. Converte a resposta para JSON
    dados_viacep = response_viacep.json()
    # O ViaCEP retorna um ÚNICO dicionário (não uma lista).
    # Exemplo: {"cep": "01310-100", "logradouro": "Avenida Paulista", ...}

    # 4. Transforma em DataFrame (passamos como lista de dict)
    df_viacep = pd.DataFrame([dados_viacep])
    # ATENÇÃO: como é um dicionário único (não lista), envolve em [ ] para criar 1 linha.

    # 5. Mostra as principais informações
    print(df_viacep[['cep', 'logradouro', 'bairro', 'localidade', 'uf']])
    # Seleciona apenas as colunas relevantes para exibição.

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
# 1. Consulta a lista de bancos
url_brasilapi = "https://brasilapi.com.br/api/banks/v1"
response_brasilapi = requests.get(url_brasilapi)

if response_brasilapi.status_code == 200:
    # 2. Transforme o resultado em DataFrame
    df_bancos = pd.DataFrame(response_brasilapi.json())
    # O JSON da BrasilAPI já vem como LISTA de dicionários → pd.DataFrame() direto.

    # 3. Conte quantos bancos existem
    print(f"\n[BrasilAPI] Total de bancos retornados: {len(df_bancos)}")
    # len(df_bancos) = número de linhas do DataFrame = número de bancos.

    # 4. Filtre bancos cujo nome contenha "Brasil"
    # Precisamos preencher valores nulos (NaN) para evitar erros no .str.contains
    df_bancos['fullName'] = df_bancos['fullName'].fillna('')
    # .fillna('') → substitui NaN por string vazia, evitando erro no .str.contains().
    bancos_brasil = df_bancos[df_bancos['fullName'].str.contains("Brasil", case=False, na=False)]
    # .str.contains("Brasil") → True para linhas onde "Brasil" aparece no nome.
    # case=False → não diferencia maiúscula/minúscula ("brasil" também é encontrado).
    # na=False   → trata NaN como False (não dá erro se ainda houver nulos).
    print(f"Número de bancos com 'Brasil' no nome: {len(bancos_brasil)}")
    print(bancos_brasil[['ispb', 'name', 'code']].head())

# Explicação:
# A estrutura do JSON retornado é uma lista/array contendo vários objetos de dicionário.
# Cada objeto representa um banco. Quando processado pelo pandas, a lista de dicionários
# é convertida diretamente para DataFrame (chaves viram colunas).

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
# 1. Consulta os estados brasileiros
url_ibge = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
response_ibge = requests.get(url_ibge)

if response_ibge.status_code == 200:
    # 2. Transforme em DataFrame
    df_estados = pd.DataFrame(response_ibge.json())
    # JSON retorna lista de dicts com chaves: id, sigla, nome, regiao.
    # 'regiao' é um dicionário aninhado: {"id": 1, "sigla": "N", "nome": "Norte"}

    # A coluna 'regiao' contém um dicionário, precisamos extrair a sigla/nome.
    df_estados['regiao_nome'] = df_estados['regiao'].apply(lambda x: x.get('nome') if type(x) == dict else None)
    # .apply(lambda x: ...) → aplica a função em cada elemento da coluna.
    # lambda x: x.get('nome') → extrai o valor da chave 'nome' do dicionário interno.
    # type(x) == dict → verifica se é dict antes de chamar .get() (segurança).

    # 3. Mostre apenas: nome, sigla, região
    print("\n[IBGE] Estados Brasileiros:")
    print(df_estados[['nome', 'sigla', 'regiao_nome']].head())

# 4. Desafio - População total de um estado (SP - código 35)
codigo_estado_sp = "35"
# Variável 93 do agregado 6579 corresponde à população no Censo de 2022.
url_populacao = f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2022/variaveis/93?localidades=N3[{codigo_estado_sp}]"
# f-string: insere o código do estado na URL dinamicamente.
response_pop = requests.get(url_populacao)

if response_pop.status_code == 200:
    try:
        dados_pop = response_pop.json()
        serie = dados_pop[0]['resultados'][0]['series'][0]
        # Navegando pelo JSON aninhado:
        # dados_pop[0]              → primeiro elemento da lista
        # ['resultados'][0]         → primeiro resultado
        # ['series'][0]             → primeira série
        populacao_sp = serie['serie']['2022']
        nome_localidade = serie['localidade']['nome']
        print(f"População do estado de {nome_localidade} em 2022: {populacao_sp}")
    except (IndexError, KeyError):
        # try/except captura erros de índice ou chave ausente sem travar o programa.
        print("Erro ao processar dados de população.")

# ===========================================================
# PARTE 5 – IPEA DATA
# ===========================================================
"""
Documentação:
https://www.ipeadata.gov.br/api/
Exercícios:
1. Consulte os metadados de uma série.
2. Identifique:
   - nome da série
   - descrição
   - unidade
3. Consulte os valores históricos da série.
4. Transforme em DataFrame.
"""
# RESOLVA AQUI:
# 1. Consulte os metadados de uma série
import requests
import pandas as pd

url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
response.status_code
dados = response.json()
dados = dados["value"]
# A API do IPEA envolve os dados na chave "value" (padrão OData).
# Precisamos acessar essa chave para chegar na lista de resultados.
df = pd.DataFrame(dados)

# ===========================================================
# PARTE 6 – BANCO CENTRAL DO BRASIL (BCB)
# ===========================================================
"""
Dados Abertos BCB:
https://dadosabertos.bcb.gov.br/
Exemplo: Consulta PTAX
Parâmetros:
{
 "formato": "json",
 "dataInicial": "01/01/2024",
 "dataFinal": "31/12/2024"
}
Exercícios:
1. Consulte a cotação do dólar em 2024.
2. Transforme em DataFrame.
3. Calcule:
   - média
   - valor máximo
   - valor mínimo
4. Plote gráfico de linha.
"""
# RESOLVA AQUI:
# 1. Consulte a cotação do dólar em 2024
# PTAX Dolar: bcdata.sgs.1
url_bcb = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"
parametros = {
    "formato": "json",
    "dataInicial": "01/01/2024",
    "dataFinal": "31/12/2024"
}
# Dicionário de parâmetros: o requests os adiciona automaticamente na URL.
# URL final ficará: ...dados?formato=json&dataInicial=01/01/2024&dataFinal=31/12/2024
res_bcb = requests.get(url_bcb, params=parametros)
# params=parametros → passa o dicionário de parâmetros para o requests.

if res_bcb.status_code == 200:
    # 2. Transforme em DataFrame
    df_bcb = pd.DataFrame(res_bcb.json())
    # O JSON do BCB vem como lista de dicts: [{"data": "02/01/2024", "valor": "4.8970"}, ...]

    # Conversão da coluna valor de string para float para cálculos matemáticos
    df_bcb['valor'] = df_bcb['valor'].astype(float)
    # .astype(float) → converte o tipo da coluna de string (object) para float.
    # Necessário porque o BCB retorna os valores como texto, não números.

    # 3. Calcule: média, valor máximo, valor mínimo
    media = df_bcb['valor'].mean()
    val_max = df_bcb['valor'].max()
    val_min = df_bcb['valor'].min()
    print("\n[BCB] Cotação do Dólar PTAX em 2024:")
    print(f"Média: R$ {media:.4f} | Máximo: R$ {val_max:.4f} | Mínimo: R$ {val_min:.4f}")
    # :.4f → formata com 4 casas decimais (padrão para cotações cambiais).

    # 4. Plote gráfico de linha
    # Opcional caso use em IDE interativa (exige matplotlib)
    # import matplotlib.pyplot as plt
    # df_bcb['data'] = pd.to_datetime(df_bcb['data'], format='%d/%m/%Y')
    # df_bcb.plot(x='data', y='valor', title="Dólar PTAX (2024)", figsize=(8,4))
    # plt.show()

# ===========================================================
# PARTE 7 – FOOTBALL-DATA.ORG
# ===========================================================
"""
Documentação:
https://www.football-data.org/documentation/quickstart
Observação:
Essa API exige API-KEY.
Exercícios:
1. Consulte as áreas (countries).
2. Filtre o Brasil (CountryCode = "BRA").
3. Consulte competições do Brasil.
4. Consulte os times da temporada 2025.
Explique:
O que são parâmetros de consulta?
"""
# RESOLVA AQUI:
# API Exige TOKEN. Se estiver vazio o endpoint retorna um erro de Autenticação (400 Client Error).
headers_football = {
    "X-Auth-Token": "COLOQUE_AQUI_SEU_TOKEN" # Substitua pelo token real do Football-Data
}
# Headers são informações adicionais enviadas na requisição.
# "X-Auth-Token" é o cabeçalho específico que essa API usa para autenticação.

url_areas = "https://api.football-data.org/v4/areas"

# Descomente o código abaixo para testar apenas quando tiver um Token Válido
"""
res_f = requests.get(url_areas, headers=headers_football)
if res_f.status_code == 200:
    # 1. Consulta as áreas mapeadas pela API
    areas = res_f.json().get('areas', [])
    df_areas = pd.DataFrame(areas)

    # 2. Filtre o Brasil (CountryCode = "BRA")
    brasil = df_areas[df_areas['countryCode'] == "BRA"]
    print("\n[Football-Data] Filtro Brasil:")
    print(brasil)

    # 3 e 4. Consultas relacionadas a times da temporada e competições podem
    # ser feitas filtrando e buscando do objeto pai conforme endpoint /teams ou /competitions.
"""

# Explicação:
# Parâmetros de consulta (Query Parameters) são atributos passados na URL
# após o sinal de `?`, como `?season=2025`. Eles servem para filtrar ou modificar
# os dados que a API vai retornar, funcionando como um filtro de busca.

# ===========================================================
# PARTE 8 – RAPIDAPI (EXEMPLOS)
# ===========================================================
"""
Exemplos:
Tripadvisor – SearchLocation
querystring = {"query":"brasilia"}
NBA – Estatísticas de jogadores
querystring = {"game":"8133"}
Exercícios:
1. Escolha uma API do RapidAPI.
2. Faça uma consulta.
3. Transforme a resposta em DataFrame.
4. Descreva a estrutura do JSON retornado.
Desafio:
Identifique níveis aninhados no JSON.
"""
# RESOLVA AQUI:
# Exemplo fictício de pesquisa no RAPIDAPI utilizando o GeoDB Cities API.
url_rapid = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
querystring_rapid = {"namePrefix": "Brasilia", "countryIds": "BR"}
# querystring = dicionário de parâmetros de consulta passados como filtros na URL.

headers_rapid = {
	"X-RapidAPI-Key": "COLOQUE_AQUI_SEU_TOKEN",
	# Chave de autenticação da RapidAPI — necessária para todas as APIs da plataforma.
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
	# Identificador do serviço específico dentro da RapidAPI.
}

# Descomente para testar tendo a chave:
"""
res_rapid = requests.get(url_rapid, headers=headers_rapid, params=querystring_rapid)
if res_rapid.status_code == 200:
    # 2. Faça uma consulta
    dados_rapid = res_rapid.json()

    # 3. Transforme a resposta em DataFrame
    # O JSON costuma vir com uma chave "data" para a lista de resultados.
    df_rapid = pd.DataFrame(dados_rapid.get('data', []))
    print("\n[RapidAPI] Cidades Encontradas:")
    print(df_rapid.head())
"""

# 4. Explique a estrutura e níveis aninhados:
# JSON possui níveis aninhados porque as respostas organizam as informações hierarquicamente.
# Por exemplo, pode existir um campo 'metadata' geral da API por fora da lista, e uma
# lista de objetos 'data' que contém os registros, onde cada registro pode ter dicionários internos.

# ===========================================================
# PARTE 9 – EXPLORAÇÃO LIVRE
# ===========================================================
"""
Pesquise APIs públicas em:
https://github.com/public-apis/public-apis
https://apilayer.com/marketplace
https://app.balldontlie.io/
Exercícios:
1. Escolha uma API pública.
2. Consulte dados.
3. Transforme em DataFrame.
4. Faça uma pequena análise exploratória.
"""
# RESOLVA AQUI:
# 1. API escolhida: PokeAPI
url_poke = "https://pokeapi.co/api/v2/pokemon?limit=10"
# O parâmetro ?limit=10 já está na URL aqui (forma alternativa de passar parâmetros).

# 2. Consulte dados
res_poke = requests.get(url_poke)

if res_poke.status_code == 200:
    dados_poke = res_poke.json()['results']
    # O JSON da PokeAPI vem com várias chaves: count, next, previous, results.
    # ['results'] acessa apenas a lista de pokémons (o que nos interessa).

    # 3. Transforme em DataFrame
    df_poke = pd.DataFrame(dados_poke)
    # Cada pokémon é um dict com 'name' e 'url'. Vira 1 linha no DataFrame.

    print("\n[Exploração Livre - PokeAPI] Primeiros 10 Pokémons:")
    print(df_poke)

    # 4. Faça uma pequena análise exploratória
    # Vamos ver quantos caracteres o nome possui e qual a url apontada.
    df_poke['tamanho_nome'] = df_poke['name'].apply(len)
    # .apply(len) → aplica a função len() em cada elemento da coluna "name".
    # Cria nova coluna com o número de caracteres de cada nome.
    media_caracteres = df_poke['tamanho_nome'].mean()
    print(f"Média de caracteres no nome: {media_caracteres:.1f}")

# ===========================================================
# Revisão FINAL
# ===========================================================
"""
Responda:

1. O que é uma API?
R: API (Application Programming Interface) é uma interface que permite que duas aplicações se comuniquem e troquem dados livremente e de forma estruturada.

2. O que é um endpoint?
R: Um endpoint é uma exata URL final na qual os recursos procurados pela API podem ser acessados (como um endereço para a rota responsável por entregar o dado da empresa).

3. O que são parâmetros?
R: São variáveis enviadas na requisição HTTP (podendo ser por Query URL com o caractere '?') para filtrar, alinhar, paginar ou alterar o escopo do que se quer recuperar da API.

4. O que é JSON?
R: JSON (JavaScript Object Notation) é um padrão popular extremamente leve estruturado de texto para armazenar e trocar dados (sendo formado essencialmente em pares ordenados chave: valor).

5. O que é Headers?
R: Cabeçalhos (Headers) são informações extras empacotadas na troca entre cliente-servidor para passar metadados e configuração da chamada, como tokens, identificadores de browsers, codificação ou formato estipulado.

6. O que é Token?
R: Token é uma credencial ou chave (string) digital e encriptografada que prova e autentica uma identidade e sua autorização frente à API, liberando o acesso a endpoints protegidos.
"""

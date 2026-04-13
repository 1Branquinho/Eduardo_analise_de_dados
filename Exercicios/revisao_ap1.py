#-----------------------------------------------------------
# GUIA DE REVISÃO RÁPIDA — AP1
# Este arquivo é um RESUMO dos padrões mais usados na prova.
# Use como "cola estruturada" durante a avaliação.
#-----------------------------------------------------------

# PYTHON BÁSICO
#-----------------------------------------------------------

# Listas e dicionários

# Lista []
# → Coleção ordenada de valores acessada por índice numérico.
# → lista[0] = primeiro elemento, lista[-1] = último elemento.

# Dicionário {}
# → Coleção de pares chave-valor. Acesso pela chave (string ou número).

# Como pegar elementos de listas e dicionários
# Lista[0]           → acessa o PRIMEIRO elemento da lista (índice 0)
# Dicionário["Key"]  → acessa o valor da chave "Key" no dicionário

#-----------------------------------------------------------
# OBTER DADOS
#-----------------------------------------------------------

import pandas as pd
# Importa a biblioteca pandas com o apelido 'pd'.
# Necessário em qualquer script que leia/manipule dados tabulares.

df = pd.read_csv("nome.csv")
# Lê um arquivo CSV e cria um DataFrame.
# O primeiro argumento é o caminho do arquivo (relativo ou absoluto).

df = pd.read_excel("nome.xlsx")
# Lê um arquivo Excel (.xlsx) e cria um DataFrame.
# Para ler uma aba específica: pd.read_excel("nome.xlsx", sheet_name="Aba1")

#-----------------------------------------------------------
# ORGANIZAR DADOS
#-----------------------------------------------------------

# Filtrar dados

filtro = (df[df["idade"] >= 10]) & (df["nome"].str.contains("a"))     # Retorna todas as linhas com idade >= 10 e que o nome que contenha a letra "a"
# FILTRO DUPLO com & (E lógico):
#   df[df["idade"] >= 10]            → condição 1: idade maior ou igual a 10
#   df["nome"].str.contains("a")     → condição 2: nome contém a letra "a"
#   IMPORTANTE: cada condição entre parênteses quando usar & ou |

df_idade = df.loc[filtro, ["nome", "idade", "endereço"]]      # Me retorna um df com as três colunas indicadas e com as linhas após o filtro
# .loc[filtro, colunas]: seleção combinada de LINHAS (pelo filtro) + COLUNAS (lista de nomes)
# → Retorna novo DataFrame com somente as linhas filtradas e as colunas especificadas.

filtro = df["nome"].str.contains("Pedro", case=False)     #Filtro que seleciona apenas os Pedros e não considera letra maiúscula/minúscula
# .str.contains("Pedro") → True para linhas onde "nome" contém "Pedro".
# case=False → ignora diferença entre maiúscula/minúscula ("pedro", "PEDRO" também passam).

#-----------------------------------------------------------

# Rankear dados

df["Roic"].rank(ascending=False)
# .rank() → atribui uma posição/ranking para cada valor da coluna.
# ascending=False → rank 1 = MAIOR valor (ranking decrescente, do melhor para o pior).
# ascending=True  → rank 1 = menor valor.

df.sort_values(["Roic"], ascending=False)
# .sort_values() → retorna o DataFrame ordenado.
# ascending=False → do maior para o menor (decrescente).
# Pode passar lista de colunas para ordenar por múltiplos critérios.

#-----------------------------------------------------------

# Criar nova coluna

df["nova_col"] = 0
# Atribui o valor 0 a TODAS as linhas da nova coluna "nova_col".
# Também pode ser expressão: df["nova_col"] = df["col1"] + df["col2"]
# Ou booleano: df["passou"] = df["nota"] >= 7

#-----------------------------------------------------------

# Calcular - min, max, media

df["nova_col"].min()
# .min() → menor valor da coluna.
# Análogos: .max() → maior, .mean() → média, .std() → desvio padrão, .sum() → soma.

#-----------------------------------------------------------

# Agrupar dados

df.groupby("estado")["renda"].min()
# .groupby("estado")  → agrupa todas as linhas pelo valor da coluna "estado"
# ["renda"]           → dentro de cada grupo, opera sobre a coluna "renda"
# .min()              → retorna o menor valor de "renda" em cada estado
# Funções disponíveis: .min(), .max(), .mean(), .sum(), .count(), .nunique()
# Para pegar o estado com menor renda: adicionar .idxmin() ao final
# Para pegar o estado com maior renda: adicionar .idxmax() ao final

#-----------------------------------------------------------
# APIs
#-----------------------------------------------------------

# Consumir APIs

import requests
# Biblioteca para fazer requisições HTTP. Precisa estar instalada: pip install requests.

URL = "https://..."
# Endereço do endpoint da API que queremos consultar.

Response = requests.get(URL)
# Envia uma requisição HTTP GET para a URL.
# Retorna um objeto Response com atributos: .status_code, .json(), .text.

Response.status_code    # se retornou 200 é sucesso
# Código de status HTTP:
#   200 = OK (sucesso)
#   400 = Bad Request (erro na requisição)
#   401 = Unauthorized (sem autenticação ou token inválido)
#   404 = Not Found (endpoint não existe)
#   500 = Server Error (erro no servidor)

dados = Response.json()
# .json() → converte a resposta JSON para estrutura Python:
#   Lista de dicts → use pd.DataFrame(dados) diretamente.
#   Dict único     → use pd.DataFrame([dados]) (envolve em lista).

pd.DataFrame(dados)
# Converte a lista de dicionários em tabela (DataFrame).
# Cada dicionário = uma linha. Chaves do dict = nomes das colunas.

# PADRÃO COMPLETO COM PARÂMETROS:
# params = {"formato": "json", "dataInicial": "01/01/2024", "dataFinal": "31/12/2024"}
# response = requests.get(URL, params=params)
# O requests adiciona automaticamente os parâmetros na URL como query string.

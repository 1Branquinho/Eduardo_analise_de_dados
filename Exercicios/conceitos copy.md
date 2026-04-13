# RESUMO TEÓRICO — AP1 ANÁLISE DE DADOS

---

## 1. CONCEITOS GERAIS DE PROGRAMAÇÃO

**Variável**
Um "espaço na memória" com um nome, que guarda um valor. Esse valor pode mudar ao longo do programa. Por exemplo, `nome = "Ana"` cria uma variável chamada `nome` com o valor `"Ana"`.

**Tipo de dado**
Define qual tipo de informação está guardada numa variável. Os principais são: `int` (número inteiro, ex: 10), `float` (número decimal, ex: 3.14), `str` (texto, ex: "Brasil"), `bool` (verdadeiro ou falso: True/False), `list` (coleção ordenada de valores) e `dict` (coleção de pares chave → valor).

**Função**
Um bloco de código reutilizável com um nome. Você "chama" a função passando valores (argumentos) e ela pode devolver um resultado com `return`. Por exemplo, `len(lista)` chama a função `len` passando `lista` como argumento, e ela retorna o tamanho da lista.

**Índice**
A posição de um elemento dentro de uma lista. Em Python, o índice começa em 0. Ou seja, `lista[0]` é o primeiro elemento, `lista[1]` é o segundo, e `lista[-1]` é o último.

**Operador módulo (%)**
Retorna o resto de uma divisão inteira. Muito usado para verificar se um número é par ou ímpar. `10 % 2 = 0` (par, pois o resto é zero). `7 % 2 = 1` (ímpar, pois o resto é 1).

**Biblioteca / Módulo**
Um conjunto de funções e ferramentas prontas que você pode importar e usar no seu código, sem precisar criar do zero. `import pandas as pd` importa a biblioteca `pandas` com o apelido `pd`, para não precisar digitar "pandas" toda vez.

---

## 2. LISTAS E DICIONÁRIOS

**Lista**
Coleção ordenada de valores, acessada por posição numérica (índice). Pode conter qualquer tipo de dado misturado. Exemplo: `lista = [1, "Ana", True]`. O acesso é feito pela posição: `lista[0]` retorna `1`.

**Dicionário**
Coleção de pares chave → valor. O acesso é feito pela chave, não por posição numérica. Cada chave é única dentro do dicionário. Exemplo: `d = {"nome": "Ana", "idade": 20}`. O acesso é feito pela chave: `d["nome"]` retorna `"Ana"`.

**Dicionário aninhado**
Quando o valor de uma chave é outro dicionário. Precisamos encadear os acessos para chegar ao dado desejado. Exemplo: `turma["Ana"]["notas"]` primeiro acessa o dicionário de "Ana", e depois acessa a chave "notas" dentro dele.

**Método .get()**
Busca uma chave no dicionário com segurança. Se a chave não existir, retorna um valor padrão em vez de travar o programa com erro. Exemplo: `d.get("cidade", "não informado")` retorna "não informado" se a chave "cidade" não existir, em vez de lançar um KeyError.

---

## 3. PANDAS E DATAFRAMES

**DataFrame**
A estrutura principal do pandas. Pense nele como uma planilha: tem linhas, colunas e índices. Cada coluna tem um nome e um tipo de dado. É criado a partir de arquivos CSV, Excel, listas de dicionários, entre outros.

**Série (Series)**
Uma única coluna de um DataFrame. Quando você seleciona uma coluna com `df["coluna"]`, o resultado é uma Série, não um DataFrame. Para retornar um DataFrame com uma única coluna, use colchetes duplos: `df[["coluna"]]`.

**Índice do DataFrame**
Cada linha tem um número de identificação chamado índice, que começa em 0 por padrão. `df.iloc[0]` acessa a primeira linha pelo número do índice (posição). `df.loc[]` acessa pelo valor do índice, útil quando o índice tem nomes em vez de números.

**Filtro (máscara booleana)**
Quando você escreve `df["col"] > 10`, o pandas cria uma lista de `True` e `False` para cada linha. Ao passar isso dentro de `df[...]`, ele mantém somente as linhas onde o resultado é `True`. Regra crítica: filtros duplos exigem parênteses em cada condição e o operador `&` (E) ou `|` (OU) entre elas. Exemplo: `df[(df["col1"] == "Brasil") & (df["col2"] > 10)]`.

**GroupBy**
Agrupa as linhas do DataFrame por uma coluna e aplica uma função a cada grupo. Funciona em três etapas: dividir (pelo grupo), aplicar (sum, mean, count...) e combinar (resultado final). Exemplo: `df.groupby("país")["renda"].mean()` divide por país, calcula a média de renda de cada um e retorna o resultado combinado.

**.idxmax() e .idxmin()**
Usados geralmente após um GroupBy. Retornam o nome (índice) do grupo com o maior ou menor valor, e não o valor em si. Exemplo: `resultado.idxmax()` retorna "Brasil" (e não 9500), se Brasil for o grupo com o maior valor.

**.count() vs .nunique()**
`.count()` conta todos os valores não-nulos, incluindo repetidos. `.nunique()` conta apenas os valores únicos, sem repetição. Exemplo com a coluna `["SP", "RJ", "SP", "MG"]`: `.count()` retorna 4, mas `.nunique()` retorna 3, pois "SP" aparece duas vezes.

**NaN (valor nulo)**
Representa a ausência de dado (Not a Number). O pandas ignora NaN automaticamente em cálculos como `.mean()` e `.sum()`. Para checar a quantidade de nulos, use `df.isnull().sum()`. Para tratar, use `.dropna()` para remover linhas ou `.fillna(valor)` para substituir os nulos por um valor.

**Pivot Table**
Cria uma tabela cruzada, como a "tabela dinâmica" do Excel. Você define o que vai nas linhas, nas colunas, quais valores exibir e como agregá-los (soma, média etc.). Células sem dados para aquela combinação aparecem como NaN.

---

## 4. APIs — CONCEITOS

**O que é uma API**
API significa Application Programming Interface. É uma interface que permite que dois sistemas se comuniquem e troquem dados de forma padronizada. Você faz um pedido (requisição) e recebe uma resposta com os dados solicitados. Pense como um garçom: você faz o pedido, ele vai até a cozinha (servidor) e traz o resultado. Você não precisa saber como a cozinha funciona.

**Endpoint**
A URL específica que você acessa para obter um recurso da API. Cada endpoint entrega um tipo diferente de dado. Por exemplo, `https://brasilapi.com.br/api/banks/v1` é o endpoint de bancos, enquanto `https://viacep.com.br/ws/01310100/json/` é o endpoint de CEP. Pense no endpoint como o endereço exato de um produto numa loja: a loja é a API, o produto é o dado, e o endereço é o endpoint.

**Requisição HTTP (request)**
O "pedido" que seu código faz ao servidor. O tipo mais comum é o `GET`, usado para buscar dados. O servidor recebe o pedido, processa e devolve uma resposta. Em Python, fazemos isso com `requests.get(url)`.

**Resposta (response)**
O objeto retornado pela requisição. Contém tudo que o servidor enviou de volta: o status da operação, os dados e os cabeçalhos. Os atributos mais usados são `response.status_code` (código de sucesso ou erro), `response.json()` (os dados convertidos para Python) e `response.text` (os dados em texto bruto).

**Status Code**
Código numérico que indica o resultado da requisição. Os principais são:

- **200 — OK:** Sucesso. Os dados estão disponíveis e podem ser usados.
- **400 — Bad Request:** Requisição errada. Algum parâmetro está inválido ou faltando.
- **401 — Unauthorized:** Token ausente ou inválido. Sem permissão de acesso.
- **404 — Not Found:** O endpoint não existe. A URL está incorreta.
- **500 — Server Error:** Erro interno no servidor da API. Não é um problema do seu código.

**JSON**
JavaScript Object Notation. É um formato de texto leve e padronizado para trocar dados entre sistemas. Parece muito com dicionários e listas do Python. Um objeto JSON como `{"nome": "Ana", "idade": 20}` se torna um `dict` em Python. Uma lista como `[{"nome": "A"}, {"nome": "B"}]` se torna uma `list` de dicts. O método `.json()` faz essa conversão automaticamente.

**Parâmetros (params)**
Filtros enviados junto com a requisição para restringir ou configurar os dados retornados. São representados por um dicionário Python e adicionados à URL automaticamente pelo `requests`. Exemplo: `params = {"dataInicial": "01/01/2024", "formato": "json"}`. A URL final ficará: `.../dados?dataInicial=01/01/2024&formato=json`. O `&` na URL separa os parâmetros, mas você não precisa montar isso na mão — o requests faz por você.

**Headers (cabeçalhos)**
Informações extras enviadas junto com a requisição, mas que não aparecem na URL. São usados principalmente para autenticação com token, mas também para definir o formato esperado da resposta. Diferente dos params, os headers ficam "escondidos" e não aparecem na URL. Exemplo: `headers = {"X-Auth-Token": "meu_token"}`.

**Token**
Uma chave secreta que identifica e autentica quem está fazendo a requisição. Funciona como um crachá digital. APIs protegidas exigem um token válido para liberar o acesso — sem ele, a API retorna o status `401 Unauthorized`. O token é sempre enviado nos `headers` da requisição, nunca exposto diretamente na URL.

**Fluxo completo de uma requisição**
O passo a passo para consumir uma API é: (1) definir a URL do endpoint, (2) enviar a requisição com `requests.get(url)`, (3) verificar se o status code é 200, (4) converter a resposta com `response.json()`, (5) verificar se o resultado é uma lista ou um dicionário, e (6) transformar em DataFrame com `pd.DataFrame()`.

**list vs dict — quando usar [ ] no DataFrame**
Essa é uma das dúvidas mais comuns. Se o JSON retornado começa com `[`, é uma lista de dicionários — use `pd.DataFrame(dados)` diretamente. Se começa com `{`, é um único dicionário — use `pd.DataFrame([dados])`, com colchetes extras. O `[ ]` extra transforma o dicionário numa lista com 1 elemento, permitindo ao pandas criar uma tabela com 1 linha. Sem ele, o pandas não sabe como montar a estrutura e dará erro.
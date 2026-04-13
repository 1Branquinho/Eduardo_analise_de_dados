import pandas as pd

# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
df = pd.read_csv("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/titanic.csv")

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
df[df["Sex"] == "female"]

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
df_survived = df[df["Survived"] == 1]["PassengerId"].nunique()
print(f"{df_survived} passageiros sobreviveram")

# Questão 4: Calcular a média da idade
# Quantos Homens Sobreviveram?
df_male = df[(df["Sex"] == "male") & (df["Survived"] == 1)]["PassengerId"].nunique()
print(f"{df_male} homens sobreviveram")

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
John_count = df[df["Name"].str.contains("John")]["PassengerId"].nunique()
print(f"Existem {John_count} passageiros tem o nome John")

# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
import pandas as pd
df = pd.read_csv('titanic.csv')
print (df)

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")

df_feminino = df[df['Sex'] == 'female']
print(df_feminino)

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")

df_survived = df[df['Survived'] == 1]
survivors_count = len(df_survived)
print(survivors_count)

# Questão 4: Calcular a média da idade
# Quantos Homens Sobreviveram?

df_male_survived = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
male_survivors_count = len(df_male_survived)
print(male_survivors_count)

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")

john_count = df[df['Name'].str.contains('John', case=False)].shape[0]
print(john_count)
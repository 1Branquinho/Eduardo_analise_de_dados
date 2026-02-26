import pandas as pd

df = pd.read_csv(r'C:\Users\202501027245\Documents\Eduardo_analise_de_dados\aula 2\notas.csv')

#1
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df['year'].min(), df['year'].max())
print(df['country'].nunique())

#2
print(df['score'].mean())
print(df['score'].max())
print(df['score'].min())
print(df.groupby('year')['score'].mean())
print(df['score'].std())

#3
print(df.sort_values('world_rank').head(10))
print(df[df['country'] == 'Brazil'].sort_values('world_rank').head(5))
print(df[df['score'] > 90])
print(df[(df['country'] == 'USA') & (df['score'] > 80)])

#4
print(df[['institution', 'country', 'score']])
print(df[df['world_rank'].between(50, 100)])
print(df[df['country'] == 'United Kingdom'])
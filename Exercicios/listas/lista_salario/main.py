import pandas as pd

df = pd.read_csv('salary.xlsx - Sheet1.csv')

# 1
print(df.shape)

# 2
print(df['salary_in_usd'].mean())
print(df['salary_in_usd'].max())
print(df['salary_in_usd'].min())

# 3
df_subset = df[['job_title', 'salary', 'company_location', 'company_size', 'remote_ratio']]
print(df_subset.head())

# 4
ds_filter = df[df['job_title'] == 'Data Scientist']
print(ds_filter['salary_in_usd'].max(), ds_filter['salary_in_usd'].min())
print(ds_filter[ds_filter['salary_in_usd'] == ds_filter['salary_in_usd'].max()]['company_location'].unique())
print(ds_filter[ds_filter['salary_in_usd'] == ds_filter['salary_in_usd'].min()]['company_location'].unique())

# 5
job_means = df.groupby('job_title')['salary_in_usd'].mean()
print(job_means.idxmax(), job_means.idxmin())

# 6
overall_mean = df['salary_in_usd'].mean()
print(job_means[job_means > overall_mean].index.tolist())

# 7
print(df.groupby('company_location')['salary_in_usd'].mean().idxmax())

# 8
print(df[df['company_location'] == 'BR']['job_title'].unique())

# 9
print(df[df['company_location'] == 'BR']['salary_in_usd'].mean())

# 10
print(df[df['company_location'] == 'BR']['job_title'].nunique())

# 11
br_data = df[df['company_location'] == 'BR']
print(br_data[br_data['salary_in_usd'] == br_data['salary_in_usd'].max()]['job_title'].unique())

# 12
print(df[(df['company_location'] == 'US') & (df['company_size'] == 'L')].shape[0])

# 13
print(df[(df['company_location'] == 'CA') & (df['company_size'] == 'M')]['salary_in_usd'].mean())

# 14
counts = df['company_location'].value_counts()
print(counts.idxmax(), counts.idxmin())

# 15
print(df.groupby('remote_ratio')['salary_in_usd'].mean())

# 16
print(df[df['remote_ratio'] == 100]['company_location'].value_counts().idxmax())
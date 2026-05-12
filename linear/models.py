import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.info()

# ----------------------------------------------------------

# Regressão Linear Simples
# x = total_bill
# y = tip

X = df["total_bill"]
Y = df["tip"]

# Adiciona o intercepto

x = sm.add_constant(X)
modelo = sm.OLS(Y, x).fit()
print(modelo.summary())
y_pred = modelo.predict()
print(y_pred)

sns.lmplot(data = df, x = "total_bill", y = "tip")

from statsmodels.tsa.ar_model import AutoReg
import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgxMTc4NzcyLCJpYXQiOjE3Nzg1ODY3NzIsImp0aSI6IjZkZDBmN2U0MzZjZTQ2MDE5NzU2OWJhYTk4M2Y3NzQ1IiwidXNlcl9pZCI6IjExOCJ9.LNq3BW_qTPNiptneU8bXI9Y6-c7yVwcp57EUhizTLLE"
params = {"ticker": "ibov", "data_ini": "2000-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
data = resp.json()
ibov = pd.DataFrame(data)
ibov["fechamento"] = pd.to_numeric(ibov["fechamento"], errors="coerce")
ibov = ibov.dropna(subset=["fechamento"])
x = ibov["fechamento"].reset_index(drop=True)

model = AutoReg(x, lags=1).fit()
print(model.summary())
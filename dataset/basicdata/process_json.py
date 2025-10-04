import pandas as pd

df = pd.read_json("../SalesTransactions/SalesTransactions.json",
                  encoding="utf-8")
print(df.head())

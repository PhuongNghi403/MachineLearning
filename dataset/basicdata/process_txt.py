import pandas as pd

df = pd.read_csv("../SalesTransactions/SalesTransactions.txt",
                 encoding="utf-8",
                 dtype="unicode",
                 low_memory=False)
print(df)

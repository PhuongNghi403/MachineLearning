import pandas as pd

df = pd.read_xml("../SalesTransactions/SalesTransactions.xml", xpath=".//SalesItem")

print(df.head()) 
row0 = df.iloc[0]
print(row0)
print(row0["OrderID"])
print(row0["ProductID"])

import pandas s pd
df=pd.read_csv("alcohol.csv")
print(df[(df["Year"]==1987) | (df["Year"]==1989)])

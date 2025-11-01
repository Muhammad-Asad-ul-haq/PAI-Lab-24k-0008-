import pandas as pd
df=pd.read_csv("movie.csv")
print(df[(df["revenue"]>2000000) & (df["budget"]<1000000)])

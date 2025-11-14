import pandas as pd
df=pd.read_csv("Titanic-Dataset.csv")


report=df.info()
print(report)

df["Age"]=df["Age"].fillna(df.groupby(["Pclass","Sex"])["Age"].transform("median"))
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
df=df.drop("Cabin",axis=1)

df.insert(11,"FamilySize",df["SibSp"] + df["Parch"])

df["IsAlone"] = 0
df.loc[df['FamilySize'] == 0, 'IsAlone'] = 1


df["Age"]=df["Age"].astype(int)
print(df)

df.to_csv("titanic_cleaned.csv",index=False)

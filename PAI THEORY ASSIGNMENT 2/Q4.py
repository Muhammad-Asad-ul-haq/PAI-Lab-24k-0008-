import pandas as pd
import numpy as np

df=pd.read_csv("titanic_cleaned.csv")
dd=pd.read_csv("ticket_fares.csv")

merged=pd.merge(df,dd,on="Ticket",how="inner")

bins=[0,12,19,59,120]
labels=["child","teen","adult","senior"]
merged["AgeGroup"]=pd.cut(merged["Age"],bins=bins,labels=labels,right=True)

mean_survival_rate=merged.groupby(["Sex","AgeGroup"])["Survived"].mean()
print(mean_survival_rate)

Conclusion=" In my opinion and by seeing the data it is visible that the data does support the (woman and children) hypthesis because it can be seen that the mean survival rate of a female of every age group is much more than the mean survival rate of the male of any age group!! "

with open("report.txt","w") as file:
    file.write(Conclusion)

Pclass_survival_rate = merged.groupby("Pclass")['Survived'].mean()
print(Pclass_survival_rate)

fare_labels = ["Low", "Medium", "High", "Very High"]
merged['FareBin'] = pd.qcut(merged["Fare_x"], 4, labels = fare_labels)

fare_survival_rate = merged.groupby("FareBin", observed=True)["Survived"].mean()
print(fare_survival_rate)

Fare_conclusion="The data does support the WEALTH hypthesis as for the top most class the survival rate is 68% and it decreases as we go down in the class. Seeing the trend in the Fares,we can determine that for the very high fares the survival rate was 60.9% and it only decreases when we go down in fares"
with open("report.txt","a") as file:
    file.write("\n" + Fare_conclusion)

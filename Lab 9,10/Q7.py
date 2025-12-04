import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('Mall_Customers.csv')
except:
    np.random.seed(0)
    n=200
    income = np.random.normal(60,30,n).clip(10,150)
    score = np.random.uniform(1,100,n)
    df = pd.DataFrame({'Annual Income (k$)':income,'Spending Score (1–100)':score})

X = df[['Annual Income (k$)','Spending Score (1–100)']]
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
df['cluster'] = kmeans.labels_

plt.scatter(X.iloc[:,0],X.iloc[:,1],c=df['cluster'])
plt.savefig('mall_clusters.png')

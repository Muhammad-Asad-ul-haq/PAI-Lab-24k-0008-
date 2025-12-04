import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('titanic.csv')
except:
    np.random.seed(0)
    n=500
    df = pd.DataFrame({
        'Pclass':np.random.choice([1,2,3],n),
        'Sex':np.random.choice(['male','female'],n, p=[0.6,0.4]),
        'Age':np.random.normal(30,14,n).clip(1,80),
        'Fare':np.random.exponential(50,size=n),
    })
    df['Survived'] = ((df['Pclass']==1).astype(int) + (df['Sex']=='female').astype(int) + (df['Age']<15).astype(int))>1
    df['Survived'] = df['Survived'].astype(int)

df['Sex'] = (df['Sex']=='male').astype(int)
df['Age'] = df['Age'].fillna(df['Age'].median())

X = df[['Pclass','Sex','Age','Fare']]
y = df['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

clf = DecisionTreeClassifier(max_depth=4, random_state=1).fit(X_train,y_train)
y_pred = clf.predict(X_test)

print(accuracy_score(y_test,y_pred))
print(precision_score(y_test,y_pred,zero_division=0))

plt.figure(figsize=(12,8))
plot_tree(clf,feature_names=X.columns,filled=True)
plt.savefig('titanic_tree.png')

import matplotlib.pyplot as plt
import pandas as pd

data = {'Age': [18, 22, 24, 27, 29, 31, 33, 35, 38, 40, 42, 25, 30, 34, 36, 28]}
df = pd.DataFrame(data)

bins = [18, 25, 30, 35, 100]
labels = ['18-25', '26-30', '31-35', '36+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

age_counts = df['Age Group'].value_counts()

plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Student Ages")
plt.show()

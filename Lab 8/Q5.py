import matplotlib.pyplot as plt
import pandas as pd

data = {'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female']}
df = pd.DataFrame(data)

gender_counts = df['Gender'].value_counts()

plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution of Students")
plt.show()

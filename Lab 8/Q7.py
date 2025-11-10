import matplotlib.pyplot as plt
import pandas as pd

data = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020],
        'Sea_Level_Rise_mm': [0, 5, 12, 20, 28, 38, 50, 63, 78, 95, 110]}
df = pd.DataFrame(data)

plt.scatter(df['Year'], df['Sea_Level_Rise_mm'], color='teal', label='Sea Level Rise')
plt.title("Sea Level Rise Over the Past 100 Years")
plt.xlabel("Year")
plt.ylabel("Sea Level Rise (mm)")
plt.legend()
plt.show()

import matplotlib.pyplot as plt

cities = [
    "Tokyo", "Delhi", "Shanghai", "São Paulo", "Mumbai", "Beijing", "Cairo", "Dhaka", "Mexico City", "Osaka"
]
populations = [37400068, 28514000, 25582000, 21650000, 21556000, 20463000, 20076000, 19578000, 21581000, 19281000]

colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow", "pink", "brown"]

plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color=colors)
plt.title("City Populations - Horizontal Bar Graph")
plt.xlabel("Population")
plt.ylabel("City")
plt.tight_layout()
plt.show()

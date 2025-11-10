import matplotlib.pyplot as plt

players = [
    "Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland", "Benzema", "Salah", "De Bruyne", "Modric", "Kane",
    "Lewandowski", "Vinicius", "Griezmann", "Son", "Pedri", "Gavi", "Rashford", "Foden", "Bellingham", "Rodri"
]
heights = [169, 187, 175, 178, 194, 185, 175, 181, 172, 188,
           185, 176, 176, 183, 174, 173, 185, 171, 186, 191]

colors = [
    "red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow", "pink", "brown",
    "grey", "lime", "navy", "violet", "teal", "gold", "coral", "olive", "skyblue", "indigo"
]

plt.figure(figsize=(10, 5))
plt.bar(players, heights, color=colors)
plt.title("Football Players' Heights - Bar Chart")
plt.xlabel("Players")
plt.ylabel("Height (cm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=players, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Football Players' Heights - Pie Chart")
plt.show()

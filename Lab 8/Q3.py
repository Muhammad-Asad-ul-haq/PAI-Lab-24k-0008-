import matplotlib.pyplot as plt

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies & Cream"]
scoops = [120, 90, 60, 40, 70]

plt.pie(scoops, labels=flavors, startangle=90)
plt.title("Ice Cream Sales Distribution")
plt.show()

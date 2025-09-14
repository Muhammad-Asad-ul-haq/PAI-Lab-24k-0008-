n = int(input("How many elements in each list? "))

a = []
b = []

print("Enter elements for first list:")
for i in range(n):
    val = input()
    a.append(val)

print("Enter elements for second list:")
for i in range(n):
    val = input()
    b.append(val)

d = {}
for i in range(n):
    d[a[i]] = b[i]

f = open("output.txt", "w")
f.write(str(d))
f.close()

print(d)

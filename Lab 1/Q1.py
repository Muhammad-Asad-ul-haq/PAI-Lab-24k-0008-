x = input("Enter number: ")
x = int(x)
a = float(x)
b = str(x)
d = complex(x)
print(type(a))
print(type(b))
print(type(d))
if x - (x // 2) * 2 == 0:
    print("Divisible by 2")
else:
    print("Not divisible by 2")

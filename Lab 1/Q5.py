name = input("Enter name: ")
year = input("Enter birth year: ")

a = name[0:3]
b = year[2:4]

f = ord(name[0])
signs = "@#%&*"
c = signs[f % 5]

pw = a + b + c
print(pw)

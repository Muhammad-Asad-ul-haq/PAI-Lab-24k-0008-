
n = input("Enter 4 digit number: ")
n = n[3] + n[2] + n[1] + n[0]
dig = ""
for i in n:
    d = (int(i) + 7) % 10
    dig = dig+str(d)
print(dig)

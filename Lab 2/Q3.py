students = [("Asad", 67), ("Saad", 55), ("Azan", 48), ("Zona", 65), ("Umair", 88)]


length = len(students)
for i in range(length):
    for j in range(0, length-i-1):
        if students[j][1] < students[j+1][1]:   
           students[j], students[j+1] = students[j+1], students[j]


print("Top 3 Students:")
print(students[0])
print(students[1])
print(students[2])

A = [[4, 2],
     [3, 1]]

B = [[3, 5],
     [1, 1]]

c = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        c[i][j] = A[i][j] + B[i][j]

print("Addition:")
print(c[0])
print(c[1])

d = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        d[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j]

print("Multiplication:")
print(d[0])
print(d[1])

mat = [['Este', 'es'],
       ['un', 'mensaje'],
       ['secreto', '!!!']]

for i in range(len(mat[0])):
    for j in range(len(mat)):
        print(mat[j][i], end=' ')


print(mat[0][0])
print(mat[1][0])
print(mat[2][0])
print(mat[0][1])
print(mat[1][1])
print(mat[2][1])

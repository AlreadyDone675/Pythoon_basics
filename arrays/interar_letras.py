palavra = ["banana", "maçã", "laranja", "uva"]
y = []
for i in range(len(palavra)):
    for c in range(len(palavra[i])):
        x = (palavra[i][c])
        y.append(x)
print(y)
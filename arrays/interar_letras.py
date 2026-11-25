def criptografar(entrada):
    x = []
    y = 0
    if type(entrada) != list:
        entrada = entrada.split()
        print(entrada)
        for i in range(len(entrada)):
            for c in range(len(entrada[i])):
                x.append(ord(entrada[i][c]))
                print("x", x)
                y = sum(x)
                print("y", y)
    else:
        for i in range(len(entrada)):
            for c in range(len(entrada[i])):
                x.append(ord(entrada[i][c]))
                y = sum(x)

A = criptografar(input("Digite a mensagemmm: "))
print("A", A)

palavra = ["banana", "maçã", "laranja", "uva"]
y = []
z = []
rchave = []
hold = []
chave = input("Digite a chave: ")
rchave.append(chave)
print(rchave)
for i in range(len(rchave)):
    for c in range(len(rchave[i])):
        hold.append(ord(rchave[i][c]))
        print(f"rchave: {rchave[i][c]}, chave: {chave}, hold: {hold[c]}")
chave = sum(hold)
print(chave)
print(hold)



for i in range(len(palavra)):
    palavra[i] = palavra[i] + " "
    for c in range(len(palavra[i])):
        x = (palavra[i][c])
        y.append(x)
        z.append(ord(x)* chave)
valor = sum(z)
print(y)
print(z)
print(valor)

resposta = input("Deseja descriptografar a mensagem? (s/n): ")
if resposta == "s":
    resposta = input("Qual é a chave?: ")
    for i in range (len(z)):
        print(chr(z[i]//resposta), end="")
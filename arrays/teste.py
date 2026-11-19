#quantidade define a quantidade de itens na lista.
#Ele é usado em alvo_selection() Como tamanho da lista
#alvo é a lista que vai receber os valores digitados pelo usuário.
#precisa de .append mas antes, é necessario o calculo do hash
#1. Calcular o hash, 2. Append na lista, 3. Tratar valores repetidos(mesmo indice) 4. Aplicar dinamica no tamanho da lista, 5. Trocar valores ao final com a lista pronta
quantidade = int(input("Tamanho da lista: "))
alvo = [None] * quantidade
final = [] * quantidade

def alvo_selection():
    elemento = 0 #Elemento é um valor zerado, usado para armazenar temporariamente o valor do hash e depois passar para a lista
    for i in range(quantidade):
        #quebrar o texto em numeros2'
        alvo[i] = input("Valor: ")
        print(f"Valor {alvo[i]} com sucesso")

def hash_valor():
    elemento = 0 #inicia vazio
    for c in range(len(alvo)):
        for i in range(len(alvo[c])): #intera sobre a lista
            elemento += ord(alvo[c][i]) #soma o valor do char e guarda em elemento
        elemento = elemento % quantidade
        final.append(elemento)
    print(final)

def search():
    search_value = int(input("Digite o valor a ser buscado: "))
    if search_value in final:
        print(f"Valor {search_value} encontrado na lista \nValor: {alvo[search_value]}")
    else:
        print(f"Valor {search_value} não encontrado na lista")

print("iniciando alvo selection")
alvo_selection()
print("iniciando hash valor")
hash_valor()
print("iniciando search")
search()
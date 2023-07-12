# Main
nome = input("Por favor digite a frase: ")

for i in range(len(nome)):
    c = nome[len(nome) - 1 - i]
    print(c.upper(), end=" ")

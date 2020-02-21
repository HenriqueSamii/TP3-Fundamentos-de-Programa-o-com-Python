#Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura. (código)
lista = []
for target_list in range(1, 11):
    itemAdd = input("Palavra "+str(target_list)+" - ")
    lista.insert(0, itemAdd)

print(lista)
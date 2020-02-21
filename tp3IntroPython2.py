#Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)
lista = []
for target_list in range(1, 6):
    itemDelet = int(input("Numero "+str(target_list)+" - "))
    lista.append(int(itemDelet))

print(lista)
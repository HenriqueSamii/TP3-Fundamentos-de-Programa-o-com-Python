#Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)
lista = []
numeroDe0 = 0
t = int(input("Tamanho do vector - "))
for target_list in range(1, t+1):
    itemAdd = int(input("Numero "+str(target_list)+" - "))
    lista.append(itemAdd)
    if itemAdd == 0:
        numeroDe0 +=1

"""for target_list in lista:
    if target_list == 0:
        numeroDe0 +=1"""

print("Existem - "+str(numeroDe0)+" Zeros ")
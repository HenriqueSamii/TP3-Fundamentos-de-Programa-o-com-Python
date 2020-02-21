#Faça uma funçãoum programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios, simulando os lançamentos dos dados. (código)

from random import randint
lista = []        

menroNumero = 1
mairoNumero = 6    
def dado_lancado():
    return randint(menroNumero, mairoNumero)

for target_list in range(100):
    lista.append(dado_lancado())

for numero in range(menroNumero, mairoNumero+1):
    vezesQueNApareceu = 0
    for n in lista:
        if numero == n:
            vezesQueNApareceu+=1
    print(str(numero)+" apareceu "+str(vezesQueNApareceu))
    vezesQueNApareceu = 0
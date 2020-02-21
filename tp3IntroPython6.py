#Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)

def eu_aparecer(listaDeFrases):
    frasesQueEuAparece = []
    for a in listaDeFrases:
        palavraParaLista = a.split (' ')
        if "eu" in palavraParaLista:
            frasesQueEuAparece.append(a)

    print("Eu  aparece em "+str(len(frasesQueEuAparece))+" frases:")
    for target_list in frasesQueEuAparece:
        print(target_list)

lista = []

sair = False
while not sair:
    frase = input("Frase (Escreva 'Sair' para terminar) -")
    if frase == "Sair":
        sair=True
    else:
        lista.append(frase)
    
eu_aparecer(lista)
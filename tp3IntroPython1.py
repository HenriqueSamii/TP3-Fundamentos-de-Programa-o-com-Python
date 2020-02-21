"""Usando Python, faça o que se pede (código e printscreen):
Crie uma lista vazia;
X1.Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
X2.Imprima a lista;
X3.Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
X4.Imprima a lista modificada;
5.Imprima também o tamanho da lista usando a função len();
7.Altere o valor do último elemento para 6 e imprima a lista modificada."""

lista = []        
    
def delet_item(item):
    global lista
    if item in lista:
        lista.remove(item)
        print("Item "+str(item)+" removido"+"\nNova Lista: " + str(lista))
    else:
        print(item + " não existe na lista")

def add_item(item):
    global lista
    lista.append(int(item))

def switch_item(item):
    global lista
    lista[len(lista)-1] = item


N = 7

while N != "6":
    N = input("1.Imprimr Lista\n2.Adicionar a lista.\n3.De um elemento para ser eliminado lista.\n4.Ver tamanho da lista.\n5.Alterar ultimo item da lista\n6.Terminar Programa\n")
    if N=="1":
        print(lista)
    elif N=="2":
        itemAdd = input("Elemento a adicionar - ")
        add_item(itemAdd)
    elif N=="3":
        itemDelet = int(input("Elemento a deletar - "))
        delet_item(itemDelet)
    elif N=="4":
        print("Lisra tem "+ str(len(lista)) + " itens")
    elif N=="5":
        itemSwitch = int(input("Elemento para trocar com o ultimo - "))
        switch_item(itemSwitch)
    elif N=="6":
        print("Adeus")
    else:
        print("Essa opção não existe")
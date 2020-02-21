#Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
#Mostrar lista;
#Incluir elemento;
#Remover elemento;
#Apagar todos os elementos da lista.
#Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista. Se a opção for a alternativa (b),
# seu programa deve pedir o valor do elemento a ser incluído. Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido.
#  E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.

lista = []        
    
def delet_item(item):
    global lista
    if item in lista:
        lista.remove(item)
        print("Item "+item+" removido"+"\nNova Lista: " + str(lista))
    else:
        print(item + " não existe na lista")

def add_item(item):
    global lista
    lista.append(item)

def switch_item(item):
    global lista
    lista[len(lista)-1] = item


N = "aba"

while N != "Sair":
    N = input("a.Imprimr Lista\nb.Adicionar a lista.\nc.De um elemento para ser eliminado lista.\nd.Apagar todos os elementos da lista\nSair.Terminar Programa\n")
    if N=="a":
        print(lista)
    elif N=="b":
        itemAdd = input("Elemento a adicionar - ")
        add_item(itemAdd)
        print(lista)
    elif N=="c":
        itemDelet = input("Elemento a deletar - ")
        delet_item(itemDelet)
    elif N=="d": 
        lista = []
        print(lista)
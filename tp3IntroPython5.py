#Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. 
#O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)
class Aluno():
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

def altura_acima_da_media_alunos(listaAlunos):
    somaTodasAlturas = 0
    for a in listaAlunos:
        somaTodasAlturas += a.altura

    print("A media da altura de todos os alunos é "+str(somaTodasAlturas/len(listaAlunos))+" metros\nE os alunos que passam dessa media são:")
    for a in listaAlunos:
        if a.altura>(somaTodasAlturas/len(listaAlunos)):
            print("Nome: "+ a.nome+" - Altura: "+str(a.altura)+" metros")

lista = []

sair = False
while not sair:
    nome = input("Nome do Aluno (Escreva 'Sair' para terminar) ")
    if nome == "Sair":
        sair=True
    else:
        idade = float(input("Altura - "))
        novoAluno = Aluno(nome,idade)
        lista.append(novoAluno)
    
altura_acima_da_media_alunos(lista)
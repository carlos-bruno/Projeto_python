import os
from random import randint
import sys

clear = lambda: os.system('cls')

def titulo():
    print("\n\t\t***********************************")
    print("\t\t******* Jogo da Adivinhação *******")
    print("\t\t***********************************\n")


titulo()

personalize = input("Deseja personalidade a dificildade do jogo [y]/[n]: ")

if personalize == 'n':

    dificuldade = input("\nEscolha a dificuldade entre 1 e 3: ")
    
    if dificuldade.isnumeric():
        dificuldade = int(dificuldade)
        inicio = 1
        tentativa = 5
        if dificuldade == 1:
            print("Dificuldade facil, números entre 1 e 10")
            final = 10
        elif dificuldade == 2:
            print("Dificuldade média, números entre 1 e 50")
            final = 50
        elif dificuldade == 3:
            print("Dificuldade Dificil, números entre 1 e 100")
            final = 100
        else:
            print("Valor informado não identificado, dificuldade surpresa habilitada. \nO número esta entre 1 e 1000")
            final = 1000
    else:
        clear()
        titulo()
        print("Erro, parâmetro informado incorretamente, programa será finalizado")
        sys.exit()

elif personalize == 'y':
    tentativa = int(input("\nDigite a quantidade de tentativas: "))
    inicio = int(input("\nDigite o valor inicial para o range: "))
    final = int(input("\nDigite o final para o range: "))

clear()
titulo()
numSecreto = randint(inicio, final)

chute = 0

while numSecreto != chute and tentativa != 0:
    print("Você possui", tentativa,"Tentativas" )
    chute = input("Informe um valor: ")
    if chute.isnumeric():
        chute = int(chute)
        if chute == numSecreto:
            clear()
            titulo()
            print("Parabens você acertou !!!")
            break
        else:
            clear()
            titulo()
            print("Tente novamente \n")
            tentativa -= 1
    else:
        clear()
        titulo()
        print("#ERROR ??? Caractere incorreto. \n\n ****O Programa será finalizado****")
        break
else:
    clear()
    titulo()
    print("Você Perdeu :( o valor informado era", numSecreto,"\nBoa sorte na proxima")
import forca
import adivinhacao
import jogodavelha

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Jogo da Velha")

    jogo = int(input("Qual jogo?\n"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo==3):
        print("Jogando Tic Tac Toe")
        jogodavelha.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()

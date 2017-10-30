import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}\n".format(rodada, tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou " , chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero
        maior   = chute > numero
        menor   = chute < numero

        if(acertou):
            print("\nVocê acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if (rodada == tentativas):
                print("Você perdeu, o número era {}\n".format(numero))
            elif(maior):
                print("Você chutou muito alto\n")
            elif(menor):
                print("Você chutou muito baixo\n")
            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

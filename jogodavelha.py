def jogar():
    m = ['.','.','.',
         '.','.','.',
         '.','.','.']
    a = 0
    jogando = True

    while(jogando):
        print("\t\t\t      Exemplo")
        print(" {} | {} | {}\t\t 0 | 1 | 2".format(m[0], m[1], m[2]))
        print("---+---+---\t\t---+---+---")
        print(" {} | {} | {}\t\t 3 | 4 | 5 ".format(m[3], m[4], m[5]))
        print("---+---+---\t\t---+---+---")
        print(" {} | {} | {}\t\t 6 | 7 | 8 ".format(m[6], m[7], m[8]))

        if ((m[0] == 'O' and m[1] == 'O' and m[2] == 'O') or
            (m[3] == 'O' and m[4] == 'O' and m[5] == 'O') or
            (m[6] == 'O' and m[7] == 'O' and m[8] == 'O') or
            (m[0] == 'O' and m[3] == 'O' and m[6] == 'O') or
            (m[1] == 'O' and m[4] == 'O' and m[7] == 'O') or
            (m[2] == 'O' and m[5] == 'O' and m[8] == 'O') or
            (m[0] == 'O' and m[4] == 'O' and m[8] == 'O') or
            (m[2] == 'O' and m[4] == 'O' and m[6] == 'O')):
            print("O jogador número 1 ganhou!\n")
            break
        elif ((m[0] == 'X' and m[1] == 'X' and m[2] == 'X') or
              (m[3] == 'X' and m[4] == 'X' and m[5] == 'X') or
              (m[6] == 'X' and m[7] == 'X' and m[8] == 'X') or
              (m[0] == 'X' and m[3] == 'X' and m[6] == 'X') or
              (m[1] == 'X' and m[4] == 'X' and m[7] == 'X') or
              (m[2] == 'X' and m[5] == 'X' and m[8] == 'X') or
              (m[0] == 'X' and m[4] == 'X' and m[8] == 'X') or
              (m[2] == 'X' and m[4] == 'X' and m[6] == 'X')):
            print("O jogador número 2 ganhou!\n")
            break

        if(a==9):
            print("\nEmpate!\n")
            break

        c = int(input("Informe a posição:\n"))
        if (m[c]=='.'):
            if (a%2==0):
                m[c] = 'O'
            else:
                m[c] = 'X'
            a+=1

if(__name__ == "__main__"):
    jogar()
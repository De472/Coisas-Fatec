
#Vareaveis diversas
end = False
empate = 0
dificuldade_easy = False
dificuldade_medium = False
dificuldade_hard = False
easy = ("fácil", "facil", "easy", "1")
medium = ("médio", "medio", "medium", "normal", "2")
hard = ("difícil", "dificil", "hard", "3")
sim = ("sim", "s")
nao = ("não", "nao", "n")
p2 = -1
pos1 = " "
pos2 = " "
pos3 = " "
pos4 = " "
pos5 = " "
pos6 = " "
pos7 = " "
pos8 = " "
pos9 = " "
linha = "-" * 50

#Introdução
print("\n" + linha)
print("Jogo da Velha".center(50,))
print(linha + "\n")

print(" 1 | 2 | 3 ".center(50))
print("-----------".center(50))
print(" 4 | 5 | 6 ".center(50))
print("-----------".center(50))
print(" 7 | 8 | 9 ".center(50) + "\n")

print("Para jogar basta digitar a posição que você deseja".center(50))
print("marcar, o computador irá jogar logo em seguida.".center(50))
print("Também tem a opção de poder jogar com outra pessoa.".center(50))
print("Após o jogo terminar este programa irá fechar.\n".center(50))

input("Digite qualquer coisa para continuar.".center(50) + "\n")

cde = 1
while cde == 1:
    multiplayer = input("Você irá jogar com outra pessoa? (\"Sim\" ou \"Não\")".center(50) + "\n")

    if nao.count(multiplayer.lower()) >= 1:
        multiplayer = False
        cde += 1

    elif sim.count(multiplayer.lower()) >= 1:
        multiplayer = True
        p2 = 0
        cde += 1

    else:
        print("Por favor, digite corretamente.\n")

if multiplayer == False:
    print("\nExite 3 níveis de dificuldade:".center(50))
    print("\"Fácil\", \"Médio\" e \"Difícil\".".center(50))

    abc = 1
    while abc == 1:
        dificuldade = input("Qual nível você escolhe?".center(50) + "\n")

        if easy.count(dificuldade.lower()) >= 1:
            dificuldade_easy = True
            abc += 1

        elif medium.count(dificuldade.lower()) >= 1:
            dificuldade_medium = True
            abc += 1

        elif hard.count(dificuldade.lower()) >= 1:
            dificuldade_hard = True

            abc += 1
        else:
            print("Por favor, digite corretamente.\n")


def vitoria():

    global end
    global empate
    empate += 1

    if pos1 == pos2 == pos3:

        if pos1 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos1 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos4 == pos5 == pos6:

        if pos4 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos4 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos7 == pos8 == pos9:

        if pos7 == "O":
            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos7 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos1 == pos4 == pos7:

        if pos1 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos1 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos2 == pos5 == pos8:

        if pos2 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos2 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos3 == pos6 == pos9:

        if pos3 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos3 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos1 == pos5 == pos9:

        if pos1 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos1 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif pos3 == pos5 == pos7:

        if pos3 == "O":

            if p2 == 0:
                print("Parabéns, o jogador 1 ganhou!!")
                end = True

            else:
                print("Você ganhou, parabéns!!")
                end = True

        elif pos3 == "X":

            if p2 == 1:
                print("Parabéns, o jogador 2 ganhou!!")
                end = True

            else:
                print("Infelizmente você perdeu... mais sorte na próxima vez.")
                end = True

    elif empate >= 9:
        print("O jogo acabou em empate.")
        end = True


def jogador():

    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global pos6
    global pos7
    global pos8
    global pos9
    global p2

    while True:

        jogada = input("Selecione a posição que você quer jogar. (1 - 9)\n")
        print("")

        #Verifica se o local escolhido é vazio e se não tem X ou O
        if jogada == "1" and (pos1 == " " or (not pos1 == "X" and not pos1 == "O")):

            if p2 == 0:
                pos1 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos1 = "X"
                p2 -= 1
                break

            else:
                pos1 = "O"
                break

        elif jogada == "2" and (pos2 == " " or (not pos2 == "X" and not pos2 == "O")):

            if p2 == 0:
                pos2 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos2 = "X"
                p2 -= 1
                break

            else:
                pos2 = "O"
                break

        elif jogada == "3" and (pos3 == " " or (not pos3 == "X" and not pos3 == "O")):

            if p2 == 0:
                pos3 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos3 = "X"
                p2 -= 1
                break

            else:
                pos3 = "O"
                break

        elif jogada == "4" and (pos4 == " " or (not pos4 == "X" and not pos4 == "O")):

            if p2 == 0:
                pos4 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos4 = "X"
                p2 -= 1
                break

            else:
                pos4 = "O"
                break

        elif jogada == "5" and (pos5 == " " or (not pos5 == "X" and not pos5 == "O")):

            if p2 == 0:
                pos5 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos5 = "X"
                p2 -= 1
                break

            else:
                pos5 = "O"
                break

        elif jogada == "6" and (pos6 == " " or (not pos6 == "X" and not pos6 == "O")):

            if p2 == 0:
                pos6 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos6 = "X"
                p2 -= 1
                break

            else:
                pos6 = "O"
                break

        elif jogada == "7" and (pos7 == " " or (not pos7 == "X" and not pos7 == "O")):

            if p2 == 0:
                pos7 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos7 = "X"
                p2 -= 1
                break

            else:
                pos7 = "O"
                break

        elif jogada == "8" and (pos8 == " " or (not pos8 == "X" and not pos8 == "O")):

            if p2 == 0:
                pos8 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos8 = "X"
                p2 -= 1
                break

            else:
                pos8 = "O"
                break

        elif jogada == "9" and (pos9 == " " or (not pos9 == "X" and not pos9 == "O")):

            if p2 == 0:
                pos9 = "O"
                p2 += 1
                break

            elif p2 == 1:
                pos9 = "X"
                p2 -= 1
                break

            else:
                pos9 = "O"
                break

        else:
            print("Por favor, escolha uma posição válida.\n")
            tabuleiro()


def computador():

    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global pos6
    global pos7
    global pos8
    global pos9

    import random

    while True:

        if dificuldade_easy == True:
            jogada_easy = random.randint(1, 10)

            if jogada_easy > 3:
                pos_easy = random.randint(1, 8)

                if pos_easy == 1 and (pos1 == " " or (not pos1 == "X" and not pos1 == "O")):
                    pos1 = "X"
                    break

                elif pos_easy == 2 and (pos2 == " " or (not pos2 == "X" and not pos2 == "O")):
                    pos2 = "X"
                    break

                elif pos_easy == 3 and (pos3 == " " or (not pos3 == "X" and not pos3 == "O")):
                    pos3 = "X"
                    break

                elif pos_easy == 4 and (pos4 == " " or (not pos4 == "X" and not pos4 == "O")):
                    pos4 = "X"
                    break

                elif pos_easy == 5 and (pos6 == " " or (not pos6 == "X" and not pos6 == "O")):
                    pos6 = "X"
                    break

                elif pos_easy == 6 and (pos7 == " " or (not pos7 == "X" and not pos7 == "O")):
                    pos7 = "X"
                    break

                elif pos_easy == 7 and (pos8 == " " or (not pos8 == "X" and not pos8 == "O")):
                    pos8 = "X"
                    break

                elif pos_easy == 8 and (pos9 == " " or (not pos9 == "X" and not pos9 == "O")):
                    pos9 = "X"
                    break

            elif jogada_easy <= 3:
                if pos5 == " " or (not pos5 == "X" and not pos5 == "O"):
                    pos5 = "X"
                    break


        elif dificuldade_medium == True:
            jogada_medium = random.randint(1, 80)

            if jogada_medium >= 4:

                if (pos1 and pos2) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos3 == " ":
                            pos3 = "X"
                            break

                elif (pos2 and pos3) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos1 == " ":
                            pos1 = "X"
                            break

                elif (pos1 and pos3) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos2 == " ":
                            pos2 = "X"
                            break

                elif (pos4 and pos5) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos6 == " ":
                            pos6 = "X"
                            break

                elif (pos5 and pos6) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos4 == " ":
                            pos4 = "X"
                            break

                elif (pos4 and pos6) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos5 == " ":
                            pos5 = "X"
                            break

                elif (pos7 and pos8) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos9 == " ":
                            pos9 = "X"
                            break

                elif (pos8 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos7 == " ":
                            pos7 = "X"
                            break

                elif (pos7 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos8 == " ":
                            pos8 = "X"
                            break

                elif (pos1 and pos4) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos7 == " ":
                            pos7 = "X"
                            break

                elif (pos4 and pos7) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos1 == " ":
                            pos1 = "X"
                            break

                elif (pos1 and pos7) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos4 == " ":
                            pos4 = "X"
                            break

                elif (pos2 and pos5) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos8 == " ":
                            pos8 = "X"
                            break

                elif (pos5 and pos8) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos2 == " ":
                            pos2 = "X"
                            break

                elif (pos2 and pos8) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos5 == " ":
                            pos5 = "X"
                            break

                elif (pos3 and pos6) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos9 == " ":
                            pos9 = "X"
                            break

                elif (pos6 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos3 == " ":
                            pos3 = "X"
                            break

                elif (pos3 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos6 == " ":
                            pos6 = "X"
                            break

                elif (pos1 and pos5) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos9 == " ":
                            pos9 = "X"
                            break

                elif (pos5 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos1 == " ":
                            pos1 = "X"
                            break

                elif (pos1 and pos9) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos5 == " ":
                            pos5 = "X"
                            break

                elif (pos3 and pos5) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos7 == " ":
                            pos7 = "X"
                            break

                elif (pos5 and pos7) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos3 == " ":
                            pos3 = "X"
                            break

                elif (pos3 and pos7) == "O":
                    bloqueio_medium = random.randint(1, 10)

                    if bloqueio_medium > 2:

                        if pos5 == " ":
                            pos5 = "X"
                            break

            elif jogada_medium > 1 and jogada_medium < 4:
                pos_medium = random.randint(1, 8)

                if pos_medium == 1 and (pos1 == " " or (not pos1 == "X" and not pos1 == "O")):
                    pos1 = "X"
                    break

                elif pos_medium == 2 and (pos2 == " " or (not pos2 == "X" and not pos2 == "O")):
                    pos2 = "X"
                    break

                elif pos_medium == 3 and (pos3 == " " or (not pos3 == "X" and not pos3 == "O")):
                    pos3 = "X"
                    break

                elif pos_medium == 4 and (pos4 == " " or (not pos4 == "X" and not pos4 == "O")):
                    pos4 = "X"
                    break

                elif pos_medium == 5 and (pos6 == " " or (not pos6 == "X" and not pos6 == "O")):
                    pos6 = "X"
                    break

                elif pos_medium == 6 and (pos7 == " " or (not pos7 == "X" and not pos7 == "O")):
                    pos7 = "X"
                    break

                elif pos_medium == 7 and (pos8 == " " or (not pos8 == "X" and not pos8 == "O")):
                    pos8 = "X"
                    break

                elif pos_medium == 8 and (pos9 == " " or (not pos9 == "X" and not pos9 == "O")):
                    pos9 = "X"
                    break

            elif jogada_medium == 1:
                if pos5 == " " or (not pos5 == "X" and not pos5 == "O"):
                    pos5 = "X"
                    break


        elif dificuldade_hard == True:
            jogada_hard = random.randint(1, 16)

            if jogada_hard > 1:

                if (pos1 and pos2) == "O":

                    if pos3 == " ":
                        pos3 = "X"
                        break

                elif (pos2 and pos3) == "O":

                    if pos1 == " ":
                        pos1 = "X"
                        break

                elif (pos1 and pos3) == "O":

                    if pos2 == " ":
                        pos2 = "X"
                        break

                elif (pos4 and pos5) == "O":

                    if pos6 == " ":
                        pos6 = "X"
                        break

                elif (pos5 and pos6) == "O":

                    if pos4 == " ":
                        pos4 = "X"
                        break

                elif (pos4 and pos6) == "O":

                    if pos5 == " ":
                        pos5 = "X"
                        break

                elif (pos7 and pos8) == "O":

                    if pos9 == " ":
                        pos9 = "X"
                        break

                elif (pos8 and pos9) == "O":

                    if pos7 == " ":
                        pos7 = "X"
                        break

                elif (pos7 and pos9) == "O":

                    if pos8 == " ":
                        pos8 = "X"
                        break

                elif (pos1 and pos4) == "O":

                    if pos7 == " ":
                        pos7 = "X"
                        break

                elif (pos4 and pos7) == "O":

                    if pos1 == " ":
                        pos1 = "X"
                        break

                elif (pos1 and pos7) == "O":

                    if pos4 == " ":
                        pos4 = "X"
                        break

                elif (pos2 and pos5) == "O":

                    if pos8 == " ":
                        pos8 = "X"
                        break

                elif (pos5 and pos8) == "O":

                    if pos2 == " ":
                        pos2 = "X"
                        break

                elif (pos2 and pos8) == "O":

                    if pos5 == " ":
                        pos5 = "X"
                        break

                elif (pos3 and pos6) == "O":

                    if pos9 == " ":
                        pos9 = "X"
                        break

                elif (pos6 and pos9) == "O":

                    if pos3 == " ":
                        pos3 = "X"
                        break

                elif (pos3 and pos9) == "O":

                    if pos6 == " ":
                        pos6 = "X"
                        break

                elif (pos1 and pos5) == "O":

                    if pos9 == " ":
                        pos9 = "X"
                        break

                elif (pos5 and pos9) == "O":

                    if pos1 == " ":
                        pos1 = "X"
                        break

                elif (pos1 and pos9) == "O":

                    if pos5 == " ":
                        pos5 = "X"
                        break

                elif (pos3 and pos5) == "O":

                    if pos7 == " ":
                        pos7 = "X"
                        break

                elif (pos5 and pos7) == "O":

                    if pos3 == " ":
                        pos3 = "X"
                        break

                elif (pos3 and pos7) == "O":

                    if pos5 == " ":
                        pos5 = "X"
                        break

            elif jogada_hard == 1:
                pos_hard = random.randint(1, 9)

                if pos_hard == 1 and (pos1 == " " or (not pos1 == "X" and not pos1 == "O")):
                    pos1 = "X"
                    break

                elif pos_hard == 2 and (pos2 == " " or (not pos2 == "X" and not pos2 == "O")):
                    pos2 = "X"
                    break

                elif pos_hard == 3 and (pos3 == " " or (not pos3 == "X" and not pos3 == "O")):
                    pos3 = "X"
                    break

                elif pos_hard == 4 and (pos4 == " " or (not pos4 == "X" and not pos4 == "O")):
                    pos4 = "X"
                    break

                elif pos_hard == 5 and (pos5 == " " or (not pos5 == "X" and not pos5 == "O")):
                    pos5 = "X"
                    break

                elif pos_hard == 6 and (pos6 == " " or (not pos6 == "X" and not pos6 == "O")):
                    pos6 = "X"
                    break

                elif pos_hard == 7 and (pos7 == " " or (not pos7 == "X" and not pos7 == "O")):
                    pos7 = "X"
                    break

                elif pos_hard == 8 and (pos8 == " " or (not pos8 == "X" and not pos8 == "O")):
                    pos8 = "X"
                    break

                elif pos_hard == 9 and (pos9 == " " or (not pos9 == "X" and not pos9 == "O")):
                    pos9 = "X"
                    break


def tabuleiro ():

    print(" " + pos1 + " | " + pos2 + " | " + pos3 + " ")
    print("-----------")
    print(" " + pos4 + " | " + pos5 + " | " + pos6 + " ")
    print("-----------")
    print(" " + pos7 + " | " + pos8 + " | " + pos9 + " \n")


while end == False:
    tabuleiro()

    if multiplayer == True:
        p2 = 0

        while end == False:
            jogador()

            tabuleiro()

            vitoria()

            if end == True:
                input("Digite qualquer coisa para sair do programa.")
                break

    elif multiplayer == False:
        jogador()

        tabuleiro()

        vitoria()

        if end == True:
            input("Digite qualquer coisa para sair do programa.")
            break

        computador()

        tabuleiro()

        vitoria()

        if end == True:
            input("Digite qualquer coisa para sair do programa.")
            break




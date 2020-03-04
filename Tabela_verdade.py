
print("")
#Feito para uma aula e treinar python
#Livre para copiar/usar
print("Olá, aqui você pode ter tabelas verdade feitas automátimaticamente!!\n")

print("                        Instruções:\n")
print("Basta apenas digitar quantos números/vareáveis a tabela terá e a")
print("operação lógica que será realizada. OBSERVAÇÃO: Neste programa só é")
print("possível realizar no máximo 8 linhas (3 números/vareáveis) e uma")
print("operação por vez, mas é possível salvar a última tabela para que ela")
print("possa ser reutilizada sem a necessidade de digitar os valores.\n")

começar = input("Digite qualquer coisa para começar\n")

#Vareáveis para confirmar a escolha do layout
layout_A = False
layout_B = False
layout_C = False
layout_D = False

#Escolha do layout
voltar_layout = 1

while voltar_layout > -1:
    print("\nVocê quer que o layout seja como?")
    print("  Opção A        Opção B        Opção C        Opção D  ")
    print("  P  |  Q        P  |  Q        P  |  Q        P  |  Q  ")
    print("     |              |              |              |     ")
    print("  V  |  V        V  |  V        F  |  F        F  |  F  ")
    print("  F  |  V        V  |  F        V  |  F        F  |  V  ")
    print("  V  |  F        F  |  V        F  |  V        V  |  F  ")
    print("  F  |  F        F  |  F        V  |  V        V  |  V  ")
    layout = input("")

    if layout == "A" or layout == "a":
        print("Você selecionou a opção A\n")
        voltar_layout -= 5
        layout_A = True

    elif layout == "B" or layout == "b":
        print("Você selecionou a opção B\n")
        voltar_layout -= 5
        layout_B = True

    elif layout == "C" or layout == "c":
        print("Você selecionou a opção C\n")
        voltar_layout -= 5
        layout_C = True

    elif layout == "D" or layout == "d":
        print("Você selecionou a opção D\n")
        voltar_layout -= 5
        layout_D = True
    else:
        print("\nErro na escolha de layout.")
        print("Digite \"A\", \"B\", \"C\" ou \"D\".\n")

#Vareáveis para a escolha do tamanho, operação e salvar
um = (str(1))
dois = (str(2))
tres = (str(3))
oper_N = ("N", "n", "~", "NOT", "Not", "not")
oper_E = ("E", "e", "^", "AND", "And", "and")
oper_OU = ("OU", "Ou", "ou", "V", "v", "OR", "Or", "or")
oper_ENTAO = ("ENTÃO", "ENTAO", "Então", "Entao", "então", "entao", "→", ">")
oper_SOMENTE = ("SOMENTE", "Somente", "somente", "↔", "<>")
save = ("SIM", "Sim", "sim", "S", "s")
salvando = 0

#Escolha do tamanho e resolução
voltar_tamanho = 1

while voltar_tamanho > -1:
    tamanho = input("\nQual será o tamanho da tabela?\n")
    if tamanho.count(um) == 1:
        if layout_A == True:
            print("\nA tabela verdade é:\n")

            print("  P  ")
            print("     ")
            print("  V  ")
            print("  F  \n")

        elif layout_B == True:
            print("\nA tabela verdade é:\n")

            print("  P  ")
            print("     ")
            print("  V  ")
            print("  F  \n")

        elif layout_C == True:
            print("\nA tabela verdade é:\n")

            print("  P  ")
            print("     ")
            print("  F  ")
            print("  V  \n")

        elif layout_D == True:
            print("\nA tabela verdade é:\n")

            print("  P  ")
            print("     ")
            print("  F  ")
            print("  V  \n")

    elif tamanho.count(dois) == 1:
        operação = input("\nQual a operação que você irá fazer?\n")
        if oper_E.count(operação) >= 1:
            if layout_A == True:
                print("\nA tabela verdade é:\n")

                print("  P  |  Q  |  P^Q")
                print("     |     |    ")
                print("  V  |  V  |   V")
                print("  F  |  V  |   F")
                print("  V  |  V  |   V")
                print("  F  |  V  |   F")
                print("  V  |  F  |   F")
                print("  F  |  F  |   F")
                print("  V  |  F  |   F")
                print("  F  |  F  |   F\n")

                salvar = input("Deseja salvar esta tabela?\n")

                if save.count(salvar) >= 1:
                    salvando += 1

                    while salvando == 1:
                        save_slot = input("Quer salvar como? (A, B, C, D ou E)\n")

                        if save_slot == "A" or save_slot == "a":
                            print("Salvo como \"A\"")
                            salvando -=1

                        elif save_slot == "B" or save_slot == "b":
                            print("Salvo como \"B\"")
                            salvando -= 1

                        elif save_slot == "C" or save_slot == "c":
                            print("Salvo como \"C\"")
                            salvando -= 1

                        elif save_slot == "D" or save_slot == "d":
                            print("Salvo como \"D\"")
                            salvando -= 1

                        elif save_slot == "E" or save_slot == "e":
                            print("Salvo como \"E\"")
                            salvando -= 1

                        else:
                            print("Digite corretamente")


            elif layout_B == True:
                print("\nA tabela verdade é:\n")

                print("  P  |  Q  |  P^Q")
                print("     |     |    ")
                print("  V  |  V  |   V")
                print("  V  |  F  |   F")
                print("  F  |  V  |   F")
                print("  F  |  F  |   F")
                print("  V  |  v  |   V")
                print("  V  |  F  |   F")
                print("  F  |  V  |   F")
                print("  F  |  F  |   F\n")

                salvar = input("Deseja salvar esta tabela?\n")

                if save.count(salvar) >= 1:
                    salvando += 1

                    while salvando == 1:
                        save_slot = input("Quer salvar como? (A, B, C, D ou E)\n")

                        if save_slot == "A" or save_slot == "a":
                            print("Salvo como \"A\"")
                            salvando -= 1

                        elif save_slot == "B" or save_slot == "b":
                            print("Salvo como \"B\"")
                            salvando -= 1

                        elif save_slot == "C" or save_slot == "c":
                            print("Salvo como \"C\"")
                            salvando -= 1

                        elif save_slot == "D" or save_slot == "d":
                            print("Salvo como \"D\"")
                            salvando -= 1

                        elif save_slot == "E" or save_slot == "e":
                            print("Salvo como \"E\"")
                            salvando -= 1

                        else:
                            print("Digite corretamente")


            elif layout_C == True:
                print("\nA tabela verdade é:\n")

                print("  P  |  Q  |  P^Q")
                print("     |     |    ")
                print("  F  |  F  |   F")
                print("  v  |  f  |   F")
                print("  F  |  F  |   F")
                print("  V  |  F  |   V")
                print("  F  |  V  |   F")
                print("  v  |  V  |   V")
                print("  F  |  v  |   F")
                print("  V  |  V  |   F\n")

                salvar = input("Deseja salvar esta tabela?\n")

                if save.count(salvar) >= 1:
                    salvando += 1

                    while salvando == 1:
                        save_slot = input("Quer salvar como? (A, B, C, D ou E)\n")

                        if save_slot == "A" or save_slot == "a":
                            print("Salvo como \"A\"")
                            salvando -= 1

                        elif save_slot == "B" or save_slot == "b":
                            print("Salvo como \"B\"")
                            salvando -= 1

                        elif save_slot == "C" or save_slot == "c":
                            print("Salvo como \"C\"")
                            salvando -= 1

                        elif save_slot == "D" or save_slot == "d":
                            print("Salvo como \"D\"")
                            salvando -= 1

                        elif save_slot == "E" or save_slot == "e":
                            print("Salvo como \"E\"")
                            salvando -= 1

                        else:
                            print("Digite corretamente")


            elif layout_D == True:
                print("\nA tabela verdade é:\n")

                print("  P  |  Q  |  P^Q")
                print("     |     |    ")
                print("  F  |  F  |   F")
                print("  F  |  V  |   F")
                print("  V  |  F  |   F")
                print("  V  |  V  |   V")
                print("  F  |  F  |   F")
                print("  F  |  V  |   F")
                print("  V  |  F  |   F")
                print("  V  |  V  |   V\n")

                salvar = input("Deseja salvar esta tabela?\n")

                if save.count(salvar) >= 1:
                    salvando += 1

                    while salvando == 1:
                        save_slot = input("Quer salvar como? (A, B, C, D ou E)\n")

                        if save_slot == "A" or save_slot == "a":
                            print("Salvo como \"A\"")
                            salvando -= 1

                        elif save_slot == "B" or save_slot == "b":
                            print("Salvo como \"B\"")
                            salvando -= 1

                        elif save_slot == "C" or save_slot == "c":
                            print("Salvo como \"C\"")
                            salvando -= 1

                        elif save_slot == "D" or save_slot == "d":
                            print("Salvo como \"D\"")
                            salvando -= 1

                        elif save_slot == "E" or save_slot == "e":
                            print("Salvo como \"E\"")
                            salvando -= 1

                        else:
                            print("Digite corretamente")


    elif tamanho.count(tres) == 1:
        print("sla v2")

    else:

        print("Digite \"1\", \"2\" ou \"3\".\n")

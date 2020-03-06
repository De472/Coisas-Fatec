
import random

rolar_dnv = 0
end = 1

#Para mudar o dado basta mudar os 'random.randint(1, X)'
#Para acrescentar mais dados basta copiar e colar, mudando os valores 'quantidade == X' e 'rolar_dnv += X'
while end > -1:
    quantidade = input("Escolha a quantidade de d6 (no máximo 6).\n")

    if quantidade == "1":
        rolar_dnv += 1
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    elif quantidade == "2":
        rolar_dnv += 2
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    elif quantidade == "3":
        rolar_dnv += 3
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    elif quantidade == "4":
        rolar_dnv += 4
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    elif quantidade == "5":
        rolar_dnv += 5
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    elif quantidade == "6":
        rolar_dnv += 6
        while rolar_dnv > 0:
            print(random.randint(1, 6))
            rolar_dnv -= 1

    else:
        print("Por favor, digite apenas um número.\n")

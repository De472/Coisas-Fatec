
#criado com base no prgrama de brute force

import itertools
import time
import math

lista_caracteres = open("caracteres_96.txt", "r", encoding= "utf-8")
wordlist = open("wordlist_bruteforce.txt", "a", encoding= "utf-8")
#transforma os caracteres em lista e em seguida uma única string
caracteres_lista = (lista_caracteres.readline()).split(" ")
caracteres = "".join(caracteres_lista)


def wordlist_generator():
    tempo_start = time.time()

    #um tamanho mínimo e máximo de senha para o programa ficar combinando
    for tamanho in range (4,10):

        #aqui é onde ocorre cada combinação. Precisa ser o .product()
        for palavra in itertools.product(caracteres, repeat=tamanho):
            #torna as combinações em uma única string
            combinação = "".join(palavra)
            #escreve nesse arquivo
            wordlist.write(combinação + "\n")

    #no fim será escrito o tempo que demorou para finalizar a lista
    tempo_fim = time.time()
    tempo_raw = tempo_fim - tempo_start
    tempo_min = math.floor(round(tempo_raw) / 60)
    tempo_seg = round((60 * tempo_min + tempo_raw), 4)
    tempo = str(tempo_min) + ":" + str(tempo_seg )

    wordlist.write("\nTempo: " + tempo + " (minutos:segundos)\n\n")
    wordlist.close()


    return

wordlist_generator()

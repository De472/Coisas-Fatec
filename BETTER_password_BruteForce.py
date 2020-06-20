
import itertools
import time
import math

lista_caracteres = open("caracteres.txt", "r", encoding= "utf-8")
#transforma os caracteres em lista e em seguida uma única string
caracteres_lista = (lista_caracteres.readline()).split(" ")
caracteres = "".join(caracteres_lista)

print("-" * 33)
print("DEMONSTRAÇÃO - ATAQUE FORÇA BRUTA")
print("-" * 33)

print("\nDigite sua senha e veja quanto")
print("tempo demora para ser crackeada.")
print("Resultados em \"senhas_crackeadas.txt\"\n")


def brute_force():
    password = input("\nSenha: ")
    tentativa = ""
    tempo_start = time.time()

    #um tamanho mínimo e máximo de senha para o programa ficar testando
    for tamanho in range (5,16):

        #aqui é onde ocorre cada combinação. Precisa ser o .product()
        for resposta_raw in itertools.product(caracteres, repeat=tamanho):
            #torna as combinações em uma única string
            tentativa = "".join(resposta_raw)
            print(tentativa)

            if tentativa == password:
                #quando o tempo passar de 60 segundos ele vira minutos
                tempo_fim = time.time()
                tempo_raw = tempo_fim - tempo_start
                tempo_min = math.floor(round(tempo_raw) / 60)
                tempo_seg = round((60 * tempo_min + tempo_raw), 4)
                tempo = str(tempo_min) + ":" + str(tempo_seg )
                print("\nCrackeado.")
                print("Tempo: " + tempo + " (minutos:segundos)\n")
                #função para salvar os dados em um arquivp separado
                lista_senhas = open("senhas_crackeadas.txt", "a", encoding="utf-8")
                lista_senhas.write("Senha: " + password + " (" + str(len(password)) + ")" + \
                                   "\nCaracteres: " + caracteres + " (" + str(len(caracteres)) + ")" + \
                                   "\nTempo: " + tempo + " (minutos:segundos)\n\n")
                lista_senhas.close()


                return

#programinha
brute_force()
end = False
while end == False:
    dnv = input("Deseja testar outra senha? (s/n)\n")

    if dnv.lower() in "sim":
        brute_force()

    elif dnv.lower() in "nao":
        end = True

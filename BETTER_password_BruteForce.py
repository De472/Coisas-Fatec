
import itertools
import time

lista_caracteres = open("caracteres.txt", "r", encoding= "utf-8")
lista_senhas = open("senhas_crackeadas.txt", "a", encoding= "utf-8")
#transforma os caracteres em lista e em seguida uma única string
caracteres_lista = (lista_caracteres.readline()).split(" ")
caracteres = "".join(caracteres_lista)

print("-" * 33)
print("DEMONSTRAÇÃO - ATAQUE FORÇA BRUTA")
print("-" * 33)

print("\nDigite sua senha e veja quanto")
print("tempo demora para ser crackeada.")
print("Resultados salvos quando você sair ")
print("do programa digitando \"n\" no final.")


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
                tempo_fim = time.time()
                tempo = tempo_fim - tempo_start
                print("\nCrackeado.")
                print("Tempo: " + str(round(tempo, 4)) + " segundos\n")
                #função para salvar os dados em um arquivp separado
                lista_senhas.write("Senha: " + password + \
                                   "\nCaracteres: " + caracteres + " (" + str(len(caracteres)) + ")" + \
                                   "\nTempo: " + str(round(tempo, 4)) + " segundos\n\n")


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

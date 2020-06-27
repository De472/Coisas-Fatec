
#PRIMEIRAS 60 LINHAS É A GERAÇÃO DE UM ARQUIVO TEMPLATE
'''
import random
import names

#para usar valores aleatorios nas notas

#gera uma única nota
def gerar_valor():
    gerar_nota = 1

    for index in range (7):
        gerar_nota = gerar_nota + random.randint(0, 100)

    gerar_nota = round((gerar_nota / 5),1)

    if gerar_nota > 100:
        gerar_nota = 100.0

    return gerar_nota


#gera uma certa quantidade de notas
def gerar_valores(quantidade):
    valores_raw = ""

    for index in range(quantidade):
        valores_raw = valores_raw + str(gerar_valor()) + ","

    valores = valores_raw[0 : len(valores_raw) -1]

    return valores


#gerador de uma lista no arquivo txt
def gerar_txt():
    dados = open("dados.txt", "a", encoding="utf-8")

    for index in range (40):
        #a chancd de ter dois nomes iguais entre os 40 é pouca, então não fiz um filtro
        nome = names.get_first_name()
        dados.write("nome:" + nome + "\n")

        dever = gerar_valores(random.randint(1, 10))
        dados.write("deveres:" + dever + "\n")

        quiz = gerar_valores(3)
        dados.write("quizzes:" + quiz + "\n")

        teste = gerar_valores(2)
        dados.write("testes:" + teste + "\n")

        dados.write("#\n")

    dados.close()

#gerar_txt()
'''


#O PROGRAMA COMEÇA AQUI


dados = open("dados.txt", "r", encoding="utf-8")
estudantes = []
aluno = {}

#essa função apenas cria  a lista "estudantes"
def criar_lista():
    for linha in dados.readlines():
        linha.split("\n")

        if "nome" in linha:
            aluno["nome"] = linha[5: len(linha) - 1]

        elif "deveres" in linha:
            aluno["dever de casa"] = linha[8: len(linha) - 1]

        elif "quizzes" in linha:
            aluno["quizzes"] = linha[8: len(linha) - 1]

        elif "testes" in linha:
            aluno["testes"] = linha[7: len(linha) - 1]
            estudantes.append(aluno.copy())

    return estudantes

#print(criar_lista())


#essa função dá os detalhes de cada aluno individualmente ou toda a sala
def details(nome= ""):
    lista = criar_lista()

    if nome != "":

        for index in range(len(lista)):

            if nome.lower() == lista[index]["nome"].lower():
                print("Nome: " + lista[index]["nome"])
                print("Deveres: " + lista[index]["dever de casa"])
                print("Quizzes: " + lista[index]["quizzes"])
                print("Testes: " + lista[index]["testes"])

    else:

        for index in range (len(lista)):
            print("Nome: " + lista[index]["nome"])
            print("Deveres: " + lista[index]["dever de casa"])
            print("Quizzes: " + lista[index]["quizzes"])
            print("Testes: " + lista[index]["testes"] + "\n")

#details()
#details("julie")


#essa função calcula qualquer média, MAS
#precisa informar o NOME do aluno e o TIPO DE NOTA
#DEVER DE CASA / QUIZZES / TESTES
#fiz individualmente para usar a função com qualquer média individualmente
def calcular_media(nome, notas):
    lista = criar_lista()

    for index in range (len(lista)):

        if nome.lower() == lista[index]["nome"].lower():
            numeros = lista[index][notas].split(",")
            media = 0
            counter = 0

            for index in range (len(numeros)):
                media = media + float(numeros[index])
                counter += 1

            return round(media / counter, 1)

#print(calcular_media("chelsea", "dever de casa"))


#essa função calcula a média pondera, MAS
#precisa informar o NOME
def getAverage(nome):
    lista = criar_lista()

    for index in range (len(lista)):

        if nome.lower() == lista[index]["nome"].lower():
            numeros_deveres = lista[index]["dever de casa"].split(",")
            numeros_quizzes = lista[index]["quizzes"].split(",")
            numeros_testes = lista[index]["testes"].split(",")

            def medias(notas):
                media = 0
                counter = 0

                for index in range(len(notas)):
                    media = media + float(notas[index])
                    counter += 1

                return round(media / counter, 1)

            resultado = medias(numeros_deveres) * 0.1 + medias(numeros_quizzes) * 0.3 + medias(numeros_testes) * 0.6

            return round(resultado, 1)

#print(getAverage("Julie"))


#essa função retorna a nota de cada aluno individual
#como pede especificamente "retorne" fiz para cada aluno individual
def getLetterGrade(nome):
    lista = criar_lista()

    for index in range (len(lista)):

        if nome.lower() == lista[index]["nome"].lower():
            nota = getAverage(lista[index]["nome"])

            if nota >= 90:
                return "A"

            elif nota >= 80:
                return "B"

            elif nota >= 70:
                return "C"

            elif nota >= 60:
                return "D"

            else:
                return "F"

#print(getLetterGrade("chelsea"))


def getClassAverage():
    lista = criar_lista()
    media = 0
    counter = 0

    for index in range(len(lista)):
        nome = lista[index]["nome"]
        details(nome)
        print("Média final: " + str(getAverage(nome)))
        print("Conceito: " + getLetterGrade(nome) + "\n")
        media = media + getAverage(nome)
        counter += 1

    print("Média da classe: " + str(round(media / counter, 1)))

#getClassAverage()

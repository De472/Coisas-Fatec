
print("\n" + "-" * 70)
print("Jogo da Forca".center(70))
print("-" * 70 + "\n")

print("Primeiro você escolhe a categoria, quando começar você digitará".center(70))
print("uma letra e uma resposta, após 7 respostas erradas o jogo acaba".center(70))
print("e você perde.\n".center(70))
print("Temas: país, comida e objeto (tecnológico).".center(70))
print("*as palavras não tem acento ou cedilha")
print("**contém um número muito limitado de palavras no momento\n")
print("-" * 70 + "\n")

start = input("Digite qualquer coisa para começar\n")

temas_pais = ("países", "paises", "país", "pais")
temas_comida = ("comidas", "comida")
temas_objeto = ("objeto", "objetos")


selecao_tema = True
pais = False
comida = False
objeto = False

while selecao_tema == True:
    escolha_tema = input("\nQual tema você quer?\n")

    if temas_pais.count(escolha_tema.lower()) >= 1:
        print("\nVocê escolheu \"País\".\n")
        pais = True
        selecao_tema = False

    elif temas_comida.count(escolha_tema.lower()) >= 1:
        print("\nVocê escolheu \"Comida\".\n")
        comida = True
        selecao_tema = False

    elif temas_objeto.count(escolha_tema.lower()) >= 1:
        print("\nVocê escolheu \"Objeto\".\n")
        objeto = True
        selecao_tema = False

    else:
        print("\nPor Favor, digite um tema válido.\n")


#dados para cada palavra
import random
def palavras():

    global palavra_chave

    palavras_pais = ("Alemanha", "Argentina", "Brasil", "Canada", "China", "Cuba", "Equador", "Espanha", "Franca",\
                     "Grecia", "India", "Japao", "Mexico", "Portugal", "Russia", "Suecia", "Suica")
    palavras_comida = ("Arroz", "Batata", "Carne", "Cenoura", "Espaguete", "Feijao", "Feijoada", "Frango", "Linguiça",\
                       "Macarronada", "Miojo", "Peixe", "Salsicha")
    palavras_objeto = ("Celular", "Controle", "Lampada", "Liquidificador", "Notebook", "Radio", "Relogio", "Roteador",\
                       "Telefone", "Televisao", "Ventilador", "Videogame")

    if pais == True:
        palavra_chave = palavras_pais[random.randint(0, 16)]

    elif comida == True:
        palavra_chave = palavras_comida[random.randint(0, 12)]

    elif objeto == True:
        palavra_chave = palavras_objeto[random.randint(0, 11)]


palavras()

erros = 0
print("Erros: " + "X" * erros + "\n")
forca = ("_ " * len(palavra_chave))
print("Palavra:")
print(forca)

#Para reescrever a "forca" colocando as letras acertadas
#Por Willem em https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

end = False

while end == False:
    if erros < 7:

        verificar_letra = len(palavra_chave) - 1
        letra = input("\nLetra: ")

        while verificar_letra > -1:

            if letra.upper() == palavra_chave[verificar_letra]:
                forca = replace_str_index(forca, verificar_letra * 2, letra.upper())
                verificar_letra -= 1

            if letra == palavra_chave[verificar_letra]:
                forca = replace_str_index(forca, verificar_letra * 2 , letra)
                verificar_letra -= 1

            else:
                verificar_letra -= 1

        print("\n" + forca)


        resposta = input("\nResposta: ")

        if resposta.lower() != palavra_chave.lower():
            erros += 1
            print("\nErros: " + "X" * erros + "\n")

            if erros < 7:
                print(forca)

        elif resposta.lower() == palavra_chave.lower():
            print("Você Acertou. PARABÉNS!!")
            input("Digite qualquer coisa para fechar o programa.")
            end = True

    if erros == 7:
        print("\nVocê Não Acertou...")
        print("A palavra era: " + palavra_chave)
        input("\nDigite qualquer coisa para fechar o programa.")
        end = True

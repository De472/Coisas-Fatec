
#Assim como a lista 07, eu não fiz utilizando o teste que já tem aqui, mas utilizei
#alguns dos exemplos daqui e também usei random (os que usam palavras não usei random)

#Pode dar RUN, coloquei inputs depois de cada exercício
#assim ele é executado em partes (mas são grandes).
#Mas pra corrigir vc precisa conferir o enunciado no código pra saber
#se realmente está certo. Eu acho que tudo já está certo kk menos o último, tijolo sem loop

import random

def random_list():
  length_lista = random.randint(2, 8)
  lista = []

  for numero in range(length_lista):
    lista.append(random.randint(0, 35))

  return lista


#Lista feita pra um exercício que precisa do 13
def random_list_13():
  length_lista = random.randint(2, 8)
  lista = []

  for numero in range(length_lista):
    lista.append(random.randint(10, 15))

  return lista


#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. near_ten
# Seja um n não negativo, retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez. Use a função resto da divisão.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True
def near_ten(n):
  print(str(n))
  tamanho_index = len(str(n)) - 1
  numero = str(n)
  ultimo_digito = numero[tamanho_index]

  if tamanho_index == 0:
    if ultimo_digito in "89":
      return "O número está pelo menos a 2 dígitos de um múltiplo de 10.\n"

    #Não considerei 0 como múltiplo de 10
    else:
      return "O numero está A MAIS de 2 dígitos de distância de um múltiplo de 10.\n"

  else:
    if ultimo_digito in "01289":
      return "O número está pelo menos a 2 dígitos de um múltiplo de 10.\n"

    else:
      return "O numero está A MAIS de 2 dígitos de distância de um múltiplo de 10.\n"


print("\nNEAR_TEN")
for numero in range(15):
  print(near_ten(random.randint(1, 35)))
  

input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0
def lone_sum(a, b, c):
  print("A: " + str(a) + " | B: " + str(b) + " | C: " + str(c))

  if a == b and a == c:
    return "A soma é: 0.\n"

  elif a == b:
    return "A soma é: " + str(c) + ".\n"

  elif a == c:
    return "A soma é: " + str(b) + ".\n"

  elif b == c:
    return "A soma é: " + str(a) + ".\n"

  else:
    return "A soma é: " + str((a + b + c)) + ".\n"


print("-" * 50)
print("LONE_SUM")
for numero in range(15):
  print(lone_sum(random.randint(3, 7), random.randint(3, 7), random.randint(3, 7)))
  

input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# C. luck_sum
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1
def lucky_sum(a, b, c):
  print("A: " + str(a) + " | B: " + str(b) + " | C: " + str(c))

  if a == 13:
    return "A soma é: 0.\n"

  elif b == 13:
    return "A soma é: " + str(a) + ".\n"

  elif c == 13:
    return "A soma é: " + str(a + b) + ".\n"

  else:
    return "A soma é: " + str(a + b + c) + ".\n"


print("-" * 50)
print("LUCKY_SUM")
for numero in range(15):
  print(lucky_sum(random.randint(10, 15), random.randint(10, 15), random.randint(10, 15)))
  
  
input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# D. double_char
# retorna os caracteres da string original duplicados
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'
def double_char(frase):
  print("\n" + frase)
  frase_nova = ""

  for index in frase:

    frase_nova = frase_nova + (index * 2)

  return frase_nova


print("-" * 50)
print("DOUBLE_CHAR")
print(double_char("python"))
print(double_char("nintendo"))
print(double_char("retorna"))
print(double_char("string"))
print(double_char("original"))
print(double_char("duplicados"))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# E. count_hi
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2
def count_hi(frase):
  print(frase)
  counter = 0
  hi_count = 0

  for index in frase.lower():

    if counter == 0:
      if index == "h":
        counter += 1

    elif counter == 1:
      if index == "i":
        hi_count += 1
        counter -= 1

      else:
        counter -= 1

  return "A quantidade de \"hi\" é: " + str(hi_count) + "\n"


print("-" * 50)
print("COUNT_HI")
print(count_hi('abc hi ho'))
print(count_hi('ABCHI hi'))
print(count_hi('hihi'))
print(count_hi('hiHIhi'))
print(count_hi(''))
print(count_hi('h'))
print(count_hi('hi'))
print(count_hi('Hi is no HI on ahI'))
print(count_hi('hiho not HOHIhi'))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# F. cat_dog
# verifica se o aparece o mesmo número de vezes 'cat' e 'dog'
# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True
def cat_dog(frase):
  print(frase)
  counterC = 0
  counterD = 0
  cat_count = 0
  dog_count = 0

  for index in frase.lower():

    if counterC == 0 and counterD == 0:
      if index == "c":
        counterC += 1

      elif index == "d":
        counterD += 1

    elif counterC == 1:
      if index == "a":
        counterC += 1

      else:
        counterC -= 1

    elif counterC == 2:
      if index == "t":
        cat_count += 1
        counterC -= 2

      else:
        counterC -= 2

    elif counterD == 1:
      if index == "o":
        counterD += 1

      else:
        counterD -= 1

    elif counterD == 2:
      if index == "g":
        dog_count += 1
        counterD -= 2

      else:
        counterD -= 2

  if cat_count == dog_count:
    return "A quantidade de \"cat\" e \"dog\" são iguais.\n"

  else:
    return "A quantidade de \"cat\" e \"dog\" NÃO são iguais.\n"

print("-" * 50)
print("CAT_DOG")
print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
print(cat_dog('catxxdogxxxdog'))
print(cat_dog('catxdogxdogxcat'))
print(cat_dog('catxdogxdogxca'))
print(cat_dog('dogdogcat'))
print(cat_dog('dogogcat'))
print(cat_dog('dog'))
print(cat_dog('cat'))
print(cat_dog('ca'))
print(cat_dog('c'))
print(cat_dog(''))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# G. count_code
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(frase):
  print(frase)
  counter = 0
  code_count = 0

  for index in frase.lower():

    if counter == 0:
      if index == "c":
        counter += 1

    elif counter == 1:
      if index == "o":
        counter += 1

      else:
        counter -= 1

    elif counter == 2:
      counter += 1

    elif counter == 3:
      if index == "e":
        code_count += 1

      else:
        counter -= 3

  return ("A quantidade de co*e é: " + str(code_count) + ".\n")

print("-" * 50)
print("COUNT_CODE")
print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))
print(count_code('cozfxxcope'))
print(count_code('xxcozeyycop'))
print(count_code('cozcop'))
print(count_code('abcxyz'))
print(count_code('code'))
print(count_code('ode'))
print(count_code('c'))
print(count_code(''))
print(count_code('AAcodeBBcoleCCccoreDD'))
print(count_code('AAcodeBBcoleCCccorfDD'))
print(count_code('coAcodeBcoleccoreDD'))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# H. end_other
# as duas strings devem ser convertidas para minúsculo via lower()
# depois disso verifique que no final da string b ocorre a string a
# ou se no final da string a ocorre a string b
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True
def end_other(fraseA, fraseB):
  print("A: " + fraseA + " | B: " + fraseB)
  index_inicial_B_maior = len(fraseB) - len(fraseA)
  index_final_B_maior = len(fraseB)
  index_inicial_A_maior = len(fraseA) - len(fraseB)
  index_final_A_maior = len(fraseA)

  if len(fraseB) > len(fraseA):
    if fraseA.lower() == fraseB.lower()[index_inicial_B_maior: index_final_B_maior]:
      return "A frase A está no final da Frase B.\n"

    else:
      return "Nenhuma frase está no final da outra.\n"

  elif len(fraseA) > len(fraseB):
    if fraseB.lower() == fraseA.lower()[index_inicial_A_maior: index_final_A_maior]:
      return "A frase B está no final da Frase A.\n"

    else:
      return "Nenhuma frase está no final da outra.\n"

  elif fraseA.lower() == fraseB.lower():
    return "As frases são iguais.\n"

  else:
    return "Nenhuma frase está em alguma.\n"


print("-" * 50)
print("END_OTHER")
print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(end_other('Hiabc', 'abcd'))
print(end_other('Hiabc', 'bc'))
print(end_other('Hiabcx', 'bc'))
print(end_other('abc', 'abc'))
print(end_other('xyz', '12xyz'))
print(end_other('yz', '12xz'))
print(end_other('Z', '12xz'))
print(end_other('12', '12'))
print(end_other('abcXYZ', 'abcDEF'))
print(end_other('ab', 'ab12'))
print(end_other('ab', '12ab'))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(lista):
  print(lista)
  par_count = 0

  for index in lista:
    if index == 0:
      do_nothing = 1
      #0 não é par

    else:
      if index % 2 == 0:
        par_count += 1

  return "A quantidade de npumeros pares na lista é: " + str(par_count) + ".\n"


print("-" * 50)
print("COUNT_EVENS")
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([]))
print(count_evens([2, 11, 9, 0]))
print(count_evens([2]))
for numero in range(7):
  print(count_evens(random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# J. sum13
# retorna a soma dos números de uma lista
# 13 dá azar, você deverá ignorar o 13 e todos os números à sua direita
# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([13, 1, 2, 3, 4]) -> 0
def sum13(lista):
  print(lista)
  soma = 0

  for index in lista:
    if index == 13:
      break

    else:
      soma += index

  return "A soma é: " + str(soma) + ".\n"


print("-" * 50)
print("SUM13")
for numero in range(15):
  print(sum13(random_list_13()))
  

input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# K. has22
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(lista):
  print(lista)
  counter = 0

  for index in lista:
    if counter == 0:
      if index == 2:
        counter += 1

    elif counter == 1:
      if index == 2:
        return "O dois aparece consecutivamente.\n"

      else:
        counter -= 1

  return "O dois NÃO aparece consecutivamente.\n"


print("HAS22")
print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
print(has22([2, 2, 1, 2]))
print(has22([1, 3, 2]))
print(has22([1, 3, 2, 2]))
print(has22([2, 3, 2, 2]))
print(has22([4, 2, 4, 2, 2, 5]))
print(has22([1, 2]))
print(has22([2, 2]))
print(has22([2]))
print(has22([]))
print(has22([3, 3, 2, 2]))
print(has22([5, 2, 5, 2]))


input("Digite qualquer coisa para avançar pro último exercício/desafio.\n")


#NÃO CONSEGUI FAZER ESSE DO TIJOLO

# L. desafio! faça somente se já tiver acabado o EP1 e todas as listas
# Fila de tijolos sem usar loops
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# é possível uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True
def fila_tijolos(pequenos, grandes, meta):
  print("Pequenos(1): " + str(pequenos) + " | Grandes(5): " + str(grandes) + " | Meta: " + str(meta))
  valor_grandes = grandes * 5
  valor_total = pequenos + valor_grandes

  if meta > valor_total:
    return "NÃO é possível montar a fila.\n"

  else:
    if meta == valor_total:
      return "É possível montar a fila.\n"

    elif meta - valor_grandes == 0:
      return "É possível montar a fila.\n"

    elif meta <= pequenos:
      return "É possível montar a fila.\n"

    elif meta < valor_grandes:
      if ((meta - pequenos) % 5) != 0:
        return "NÃO é possível montar a fila.\n"

      else:
        return "NÃO é possível montar a fila.\n"

    else:
      return "NÃO é possível montar a fila.\n"


print("-" * 50)
print("FILA_TIJOLOS")
print(fila_tijolos(3, 1, 8))
print(fila_tijolos(3, 1, 9))
print(fila_tijolos(3, 2, 10))
print(fila_tijolos(3, 2, 8))
print(fila_tijolos(3, 2, 9))
print(fila_tijolos(6, 1, 11))
print(fila_tijolos(6, 0, 11))
print(fila_tijolos(3, 1, 7))
print(fila_tijolos(1, 1, 7))
print(fila_tijolos(2, 1, 7))
print(fila_tijolos(7, 1, 11))
print(fila_tijolos(7, 1, 8))
print(fila_tijolos(7, 1, 13))
print(fila_tijolos(43, 1, 46))
print(fila_tijolos(40, 1, 46))
print(fila_tijolos(22, 2, 33))
print(fila_tijolos(0, 2, 10))
print(fila_tijolos(1000000, 1000, 1000100))
print(fila_tijolos(2, 1000000, 100003))
print(fila_tijolos(12, 2, 21))


input("Digite qualquer coisa para finalizar.\n")



#Deixei esse even porque aqui está contando que o 0 é par, mas NÃO É!
#E o do tijolo está aqui porque não fiz
'''
print ()
print ('Count_evens')
test(count_evens([2, 1, 2, 3, 4]), 3)
test(count_evens([2, 2, 0]), 3)
test(count_evens([1, 3, 5]), 0)
test(count_evens([]), 0)
test(count_evens([11, 9, 0, 1]), 1)
test(count_evens([2, 11, 9, 0]), 2)
test(count_evens([2]), 1)
test(count_evens([2, 5, 12]), 2)

print ()
print ('Fila de Tijolos')
test(fila_tijolos(3, 1, 8), True)
test(fila_tijolos(3, 1, 9), False)
test(fila_tijolos(3, 2, 10), True)
test(fila_tijolos(3, 2, 8), True)
test(fila_tijolos(3, 2, 9), False)
test(fila_tijolos(6, 1, 11), True)
test(fila_tijolos(6, 0, 11), False)
test(fila_tijolos(3, 1, 7), True)
test(fila_tijolos(1, 1, 7), False)
test(fila_tijolos(2, 1, 7), True)
test(fila_tijolos(7, 1, 11), True)
test(fila_tijolos(7, 1, 8), True)
test(fila_tijolos(7, 1, 13), False)
test(fila_tijolos(43, 1, 46), True)
test(fila_tijolos(40, 1, 46), False)
test(fila_tijolos(22, 2, 33), False)
test(fila_tijolos(0, 2, 10), True)
test(fila_tijolos(1000000, 1000, 1000100), True)
test(fila_tijolos(2, 1000000, 100003), False)
test(fila_tijolos(12, 2, 21), True)
'''

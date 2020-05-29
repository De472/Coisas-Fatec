
#Não utilizei a função de "correção/teste" do final, mas criei exemplos aleatórios
#e utilizei alguns dos exemplos q estavam aqui mesmo

#Pode dar RUN, coloquei inputs depois de cada exercício
#assim ele é executado em partes (mas são grandes).
#Mas pra corrigir vc precisa conferir o enunciado no código pra saber
#se realmente está certo. Eu acho que tudo já está certo kk

import random

def random_True_False():
  valor = random.randint(0, 1)

  if valor == 0:
    return False

  elif valor == 1:
    return True


def random_list():
  length_lista = random.randint(2, 8)
  lista = []

  for numero in range(length_lista):
    lista.append(random.randint(0, 20))

  return lista


#lista com index impar para um exercício específico
def random_list_impar():
  lista = []
  impar = False

  while impar == False:
    length_lista = random.randint(3, 7)

    if (length_lista == 4) or (length_lista == 6):
      impar = False

    else:
      impar = True

  for numero in range(length_lista):
    lista.append(random.randint(0, 20))

  return lista


#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False
def first_last6(lista):
  ultimo_digito = len(lista) - 1
  print(lista)

  if (lista[0] == 6) or (lista[ultimo_digito] == 6):
    return "O primeiro ou último dígito é 6.\n"

  else:
    return "Nem o primeiro nem o último dígito são 6.\n"


print("\nFIRST_LAST6\n")
print(first_last6([0, 5, 4, 3, 5, 6]))
print(first_last6([6, 2]))
print(first_last6([16]))
print(first_last6([4, 9, 6]))
print(first_last6([0, 5, 4, 3, 5, 6]))

#nesse não é interessante ser aleatório pq precisa ser igual a 6
for numero in range(3):
  print(first_last6(random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# B. same_first_last
# retorna True se a lista nums possui pelo menos um elemento
# e o primeiro elemento é igual ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True
def same_first_last(lista):
  ultimo_digito = len(lista) - 1
  print(lista)

  if ultimo_digito == 0:
    return "Só tem 1 dígito\n"

  elif lista[0] == lista[ultimo_digito]:
    return "O primeiro e o último dígito são iguais.\n"

  else:
    return "O primeiro e o último dígito NÃO são iguais.\n"

print("-" * 50)
print("SAME_FIRST_LAST\n")
print(same_first_last([3, 5, 6, 3]))
print(same_first_last([2, 2]))
print(same_first_last([3]))
print(same_first_last([1, 3]))
print(same_first_last([6, 3, 8, 15]))
print(same_first_last([5, 4, 28, 6, 3, 5]))

#Neste tb n é interessante por tb precisa ser igual
for numero in range(2):
  print(same_first_last(random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# C. common_end
# Dada duas listas a e b, verifica se os dois primeiros são
# iguais ou os dois últimos são iguais
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True
def common_end(listaA, listaB):
  ultimo_digito_A = len(listaA) - 1
  ultimo_digito_B = len(listaB) - 1
  print(str(listaA) + " | " + str(listaB))

  if listaA[0] == listaB[0]:
    return "O primeiro dígito de cada lista são iguais.\n"

  elif listaA[ultimo_digito_A] == listaB[ultimo_digito_B]:
    return "O último dígito de cada lista são iguais.\n"

  else:
    return "Nem o primeiro e nem o último dígito das listas são iguais.\n"


print("-" * 50)
print("COMMON_END\n")
print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))
print(common_end([1, 2, 3], [1]))
print(common_end([1, 2, 3], [2]))

#Neste tb n é interessante por tb precisar se igual
for numero in range(2):
  print(common_end(random_list(), random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# D. maior_ponta
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]
def maior_ponta(lista):
  ultimo_digito = len(lista) - 1
  print(lista)

  if lista[0] >= lista[ultimo_digito]:
    lista = [lista[0]] * len(lista)
    return "A lista nova é: " + str(lista) + ".\n"

  elif lista[0] < lista[ultimo_digito]:
    lista = [lista[ultimo_digito]] * len(lista)
    return "A lista nova é: " + str(lista) + ".\n"


print("-" * 50)
print("MAIOR_PONTA\n")
print(maior_ponta([1, 2, 3, 7]))
print(maior_ponta([11, 5, 9]))
print(maior_ponta([2, 11, 3]))
print(maior_ponta([11, 3, 3, 9, 4, 6]))
print(maior_ponta([3, 11, 11]))
print(maior_ponta([2, 2, 2]))
print(maior_ponta([2, 11, 2, 1]))
print(maior_ponta([0, 0, 1]))
for numero in range(6):
  print(maior_ponta(random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# E. sum2
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(lista):
  print(lista)

  if len(lista) == 1:
    return "Só possui um dígito, que é: " + str(lista[0]) + ".\n"

  elif len(lista) == 0:
    return "Não possui nenhum dígito, então é: 0\n"

  else:
    return "A soma dos dois primeiros dígitos é: " + str(lista[0] + lista[1]) + ".\n"


print("-" * 50)
print("SUM2\n")
print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
print(sum2([1, 2]))
print(sum2([1]))
print(sum2([]))
print(sum2([4, 5, 6]))
print(sum2([4]))
for numero in range(10):
  print(sum2(random_list()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# F. middle_way
# sejam duas listas de inteiros a e b
# retorna uma lista de tamanho 2 contendo os elementos do
# meio de a e b, suponha que as listas tem tamanho ímpar
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]
def middle_way(listaA, listaB):
  meio_digito_A = listaA[int(len(listaA) / 2)]
  meio_digito_B = listaB[int(len(listaB) / 2)]
  print(str(listaA) + " | " + str(listaB))

  lista_nova = [meio_digito_A, meio_digito_B]

  return "A lista nova é: " + str(lista_nova) + ".\n"


print("-" * 50)
print("MIDDLE_WAY\n")
print(middle_way([1, 2, 3, 5, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))
print(middle_way([1, 9, 7], [4, 8, 8, 4, 3]))
print(middle_way([1, 2, 3], [3, 1, 4]))
print(middle_way([1, 2, 3], [4, 1, 1]))
for numero in range(10):
  print(middle_way(random_list_impar(), random_list_impar()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# G. date_fashion
# você e sua namorada(o) vão a um restaurante
# eu e par são as notas das suas roupas de 0 a 10
# quanto maior a nota mais chique vocês estão vestidos
# o resultado é se vocês conseguiram uma mesa no restaurante:
# 0=não 1=talvez e 2=sim
# se a nota da roupa de um dos dois for menor ou igual a 2
# vocês não terão direito à uma mesa (0)
# se as notas são maiores, então caso um dos dois esteja
# bem chique (nota >= 8) então a resposta é sim (2)
# caso contrário a resposta é talvez (1)
# date_fashion(5, 10) -> 2
# date_fashion(5, 2) -> 0
# date_fashion(5, 5) -> 1
def date_fashion(eu, par):
  print(str(eu) + " | " + str(par))

  if (eu <= 2) or (par <= 2):
    return "0 = Sem direito a mesa.\n"

  elif (eu >= 8) or (par >= 8):
    return "2 = Tem direito a mesa.\n"

  else:
    return "1 = Talvez tenha direito a uma mesa.\n"


print("-" * 50)
print("DATE_FASHION\n")
print(date_fashion(5, 10))
print(date_fashion(3, 7))
print(date_fashion(5, 2))
print(date_fashion(5, 5))
print(date_fashion(3, 3))
print(date_fashion(10, 2))
print(date_fashion(2, 9))
for numero in range(10):
  print(date_fashion(random.randint(0, 10), random.randint(0, 10)))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  print("Temperatura: " + str(temp) + " | É verão: " + str(is_summer))

  if is_summer == True:
    if temp >= 60 and temp <= 100:
      return "Os esquilos brincam.\n"

    else:
      return "Os esquilos NÃO brincam.\n"

  elif is_summer == False:
    if temp >= 60 and temp <= 90:
      return "Os esquilos brincam.\n"

    else:
      return "Os esquilos NÃO brincam.\n"


print("-" * 50)
print("SQUIRREL_PLAY\n")
print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
print(squirrel_play(90, False))
print(squirrel_play(90, True))
print(squirrel_play(100, False))
print(squirrel_play(100, True))
print(squirrel_play(105, True))
print(squirrel_play(59, False))
print(squirrel_play(60, False))
for numero in range(10):
  print(squirrel_play(random.randint(50, 110), random_True_False()))


input("Digite qualquer coisa para avançar pro próximo exercício.\n")


# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocide <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 
def pego_correndo(speed, is_birthday):
  print("Velocidade: " + str(speed) + " | Aniversário: " + str(is_birthday))

  if is_birthday == True:
    if speed <= 65:
      return "0 = Sem multa.\n"

    elif speed <= 85:
      return "1 = Multa média.\n"

    elif speed > 85:
      return "2 = Multa grave.\n"

  elif is_birthday == False:
    if speed <= 60:
      return "0 = Sem multa.\n"

    elif speed <= 80:
      return "1 = Multa média.\n"

    elif speed > 80:
      return "2 = Multa grave.\n"


print("-" * 50)
print("PEGO_CORRENDO\n")
print(pego_correndo(60, False))
print(pego_correndo(65, False))
print(pego_correndo(65, True))
print(pego_correndo(80, False))
print(pego_correndo(85, False))
print(pego_correndo(85, True))
print(pego_correndo(70, False))
print(pego_correndo(75, False))
print(pego_correndo(75, True))
print(pego_correndo(90, False))
for numero in range(8):
  print(pego_correndo(random.randint(55, 95), random_True_False()))


input("Digite qualquer coisa para avançar pro último exercício.\n")

  
# J. alarm_clock
# day: 0=domingo, 1=segunda, 2=terça, ..., 6=sábado
# vacation = True caso você esteja de férias
# o retorno é uma string que diz quando o despertador tocará
# dias da semana '07:00'
# finais de semana '10:00'
# a menos que você esteja de férias, neste caso:
# dias da semana '10:00'
# finais de semana 'off'
# alarm_clock(1, False) -> '7:00'
# alarm_clock(5, False) -> '7:00'
# alarm_clock(0, False) -> '10:00'
def alarm_clock(day, vacation):
  print("Dia: " + str(day) + " | Férias: " + str(vacation))

  if vacation == True:
    if (day > 0) and (day < 6):
      return "O despertador tocará as 10:00.\n"

    else:
      return "O despertador NÃO tocará.\n"

  elif vacation == False:
    if (day > 0) and (day < 6):
      return "O despertador tocará as 07:00.\n"

    else:
      return "O despertador tocará as 10:00.\n"


print("ALARM_CLOCK\n")
print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
print(alarm_clock(6, False))
print(alarm_clock(0, True))
print(alarm_clock(6, True))
print(alarm_clock(1, True))
print(alarm_clock(3, True))
print(alarm_clock(5, True))
for numero in range(10):
  print(alarm_clock(random.randint(0,6), random_True_False()))


input("Digite qualquer coisa para finalizar.\n")




lista_caracteres = open("caracteres.txt", "r", encoding= "utf-8")
caracteres = (lista_caracteres.readline()).split(" ")

print("-" * 33)
print("DEMONSTRAÇÃO - ATAQUE FORÇA BRUTA")
print("-" * 33)

print("\nDigite sua senha e veja quanto")
print("tempo demora para ser crackeada.\n")

password = input("Senha: ")
tentativa = ""


def brute_force():
    for tamanho in range (6,10):

        for index in range (96):
            tentativa = caracteres[index] * tamanho
            tentativa_raw = [caracteres[index]]
            for valor in range (tamanho):
                tentativa_raw.append(caracteres[index])
            if tentativa == password:
                return "Senha crackeada com sucesso!"

            else:

                for numero in range (0, tamanho + 1):
                    tentativa_raw = [caracteres[index]]
                    for valor in range(tamanho):
                        tentativa_raw.append(caracteres[index])

                    for index0 in range (96):
                        tentativa_raw[tamanho - numero] = caracteres[index0]

                        for numero0 in range (1,numero):

                            for index1 in range (96):
                                tentativa_raw[tamanho - numero - numero0] = caracteres[index1]
                                tentativa = "".join(tentativa_raw)
                                print(tentativa)











print(brute_force())

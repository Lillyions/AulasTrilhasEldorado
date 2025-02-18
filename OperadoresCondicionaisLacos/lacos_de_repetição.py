# lista_de_compras = ["Ovos", "Farinha", "Leite", "Confete", "Cenoura"]
#
# for item in lista_de_compras:
#     print("Comprei o item: ", item)


numero = 0

while True:
    print("Numero", numero)
    numero = numero + 1

    if numero % 2 == 0:
        print(numero, "é par")
        continue

    print(numero, "é ímpar")

    # if numero == 10:
    #     print("Meu número é 10")
    #     break

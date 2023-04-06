#supermercado


lista = []

qtd = int(input())

for i in range(qtd):


    entrada = input().split()
    preco = float(entrada[0])
    kg = float(entrada[1])

    kg = 1000 / kg                    #1kg tem mil gramas

    resultado = round(preco * kg, 3)          #arredondando agora p 3 casas decimais

    lista.append(resultado)                     #apendando


lista = sorted(lista)

print("{}".format(lista[0]))



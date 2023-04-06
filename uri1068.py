#balanço entre parenteses
#se a posição dos parenteses estiver errada, então é para falar que está "incorrect"
#a+(b*c)-2-a está "correct"
# já 2*(3-a)) está "incorrect", pois o último parentese foi colocado a+.


while True:
    try:
        sentenca = input()
        cont_parentese = 0


        for i in range(len(sentenca)):
            if (sentenca[i] == "("):
                cont_parentese += 1     #a cada ( eu somo 1
            elif (sentenca[i] == ")"):
                cont_parentese -= 1    # acada ) eu diminuo 1, logo vai conseguir equilibrar
                #para cada ( eu preciso ter um ), logo se faltar um desses, não vai ser igual a zero.
            if (cont_parentese < 0):
                break
        if (cont_parentese == 0):
            print("correct")       #só vai ser correct se tudo estiver equilibrado
        else:
            print("incorrect")    #senão não for tudo igual, então está "incorrect"

    except EOFError:                #se a entrada for errada, então vai exibir um eoferror e com o break vai fechar.
        break
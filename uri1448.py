#Telefone sem fio

while True:
    try:

        entrada = int(input())
        for i in range((entrada)):            #loop que vai nos ajudar a ler quantas frases
            sentenca = str(input())
            primeiro = str(input())
            segundo = str(input())
            count1 = 0
            count2 = 0

            for letra in range(len(sentenca)):           #iremos percorrer cada letra da frase
                if (letra < len(primeiro)) and (sentenca[letra] == primeiro[letra]):
                    count1  = count1 + 1                                                        #conforme a condicao, o contador vai ganhar +1
                if (letra < len(segundo)) and (sentenca[letra] == segundo[letra]):
                    count2 = count2 + 1

            print("Instancia {}".format(i+1))
            if count1 > count2:
                print("time 1")                                                 #conforme o valor de count 1 e 2, vamos ter uma ganhador
            elif count2 > count1:
                print("time 2")
            elif count1 == count2:
                print("empate")

    except EOFError:
        break
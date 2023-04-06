#soma de fatoriais
while True:
    try:                                        #no except vai ser apenas um break para encerrar o programa
        numero1, numero2 = map(int, input().split())  #com map vamos declarar numero 1 e numero 2 em uma só linha
        cont1 = numero1 - 1      #como o numero1 e o numero2 vão mudar de valor durante o programa, teremos contadores
        cont2 = numero2 - 1
        if numero1 == 0:        #uma regra por definição de fatorial é que o fatorial de zero eh sempre 1...
            numero1 = 1
        if numero2 == 0:
            numero2 = 1

        while cont1 > 0:        #agora vamos fazer algo geral, mas excluindo o zero, pois tem exceçoes
            numero1 = numero1 * cont1

            cont1 -= 1
        while cont2 > 0:        #mesmo processo pro contador 2
            numero2 = numero2 * cont2
            cont2 -= 1
        print(numero1 + numero2)    #agora a soma dos fatoriais
    except EOFError:        #como foi aconselhado na questão, usaremos EOFError no except e break para encerrar
        break
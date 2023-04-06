while True:
    #teremos uma variavel para a maior velocidade e o nível dessa maior velocidade, estão interligados
    #como queremos que uma hora acabe, usaremos while True
    # a questão sugere que usemos a função EOF -EndOfFile
    try:                #para um Try, temos um except, logo vc vai tentar algo.. se der, executa os comandos
                        #se não der, vai pro except, que no caso vai ter um EOFError e um break para parar o programa.

        quantidade = int(input())
        velocidade = input().split()     #temos uma lista de velocidades
        maior = 0
        i = 0
        for i in range(quantidade):      #loop para poder
            if int(velocidade[i]) > maior:
                maior = int(velocidade[i])      #agora sabemos qual a maior velocidade da lista

        if maior < 10:
            nivel = 1
        elif maior >= 10 and maior < 20:
            nivel = 2


        elif maior >= 20:
            nivel = 3
        print(nivel)

    except EOFError:                #quando der EOF(end of file), o programa acaba
                                    #eoferror vai mostrar o erro na tela
        break
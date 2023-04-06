#Emplacando Tuk tuks


while True:
    try:
        qtd = int(input())
        while qtd:


            c, d = map(int,input().split())    #criamos uma lista, digitaremos o c e o d separados por espaço

            #26 consoantes eh o maximo e 10 dígitos eh o maximo
            placas = (pow(26,c)) * (pow(10,d))      #isso implica que sempre que ou c ou d forem zero, logo o resultado vai ser a outra potência
            if placas == 1:     #para isso acontecer, c e d tem que ser iguais a zero simultaneamente
                placas = 0      #logo se na entrada for 0 0, na saída vai ser 0.
            print(placas)   #depois da checagem, imprimir a quantidade de placas calculadas



            qtd = qtd + 1       #aqui vai checando quantidade a quantidade, conforme o valor de quantidade aumenta.
    except EOFError:
        break

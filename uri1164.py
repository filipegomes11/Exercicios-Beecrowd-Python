entradas = int(input())

for i in range(entradas):              #loop para poder ter o numero de entradas digitadas
    numero = int(input())
    soma = 0
    for j in range(1,numero):          #loop que começa no numero um e vai até numero - 1
        if(numero%j == 0):
            soma = soma + j            #se qualquer numero desse loop for divisivel por numero, será adicionado a soma
    if(soma == numero):
        print("{} eh perfeito".format(numero))
    else:
        print("{} nao eh perfeito".format(numero))
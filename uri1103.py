#despertador
while True:
    lista_sono = input().split()    #lista sono vai ser a lista de horas e minutos que daniela vai digitar
    h1 = int(lista_sono[0])
    m1 = int(lista_sono[1])
    h2 = int(lista_sono[2])
    m2 = int(lista_sono[3])
    dormir = 0
    acordar = 0
    if m1+m2+h1+h2 == 0:            #se tudo for zero, então não tem sentido o programa rodar, logo break.
        break
    if h1 == 0:
        dormir = (24*60)+m1         #lembrando que dormir e acordar estarão em minutos, como pede a questão
    else:
        dormir = (h1*60) + m1
    if h2 == 0:
        acordar =(24*60)+m2
    else:
        acordar = (h2*60) + m2
    if acordar > dormir:
        print(acordar-dormir)
    else:
        print((24*60)-(dormir-acordar))
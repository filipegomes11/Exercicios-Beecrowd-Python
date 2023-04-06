from math import sqrt
#Elevador
#se um cilindro tem diametro menor ou igual a altura e menor ou igual a largura, ele cabe separadamenteno elevador


while True:
    try:

        l, c, r1, r2 = map(int,input().split())     #criamos a lista com split
        if (l == 0 and c == 0 and r1 == 0 and r2 == 0):
            break

        diametro_r1 = 2*r1

        if sqrt(pow((l - r2 - r1), 2) + pow(c - r2 - r1, 2)) >= r1 + r2:
            print("S")
        else:
            print("N")


        if c > l:
            if (c >= (diametro_r1) * 2) and ((l >= r1) or (l >= r2)):
                print('S')

            else:
                print('N')


        elif l > c:
            if (l >= diametro_r1 * 2) and ((c >= r1) or (c >= r2)):
                print('S')
            else:
                print('N')



        else:
            if (l >= (diametro_r1) * 2) and ((c >= r1) or (c >= r2)):
                print('S')
            elif (c >= (diametro_r1) * 2) and ((l >= r1) or (l >= r2)):
                print('S')
            else:
                print('N')

    except EOFError:
        break
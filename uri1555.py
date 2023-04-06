#Funcões
import math


i = 0
vezes = int(input())

for i in range(vezes):

    incognita = input().split()
    x = int(incognita[0])
    y = int(incognita[1])


    if x >= 1 and y<=100:
        rafael = math.pow((3 * x), 2) + math.pow(y, 2)
        beto = 2 * math.pow(x, 2) + math.pow(5 * y, 2)
        carlos = (-100 * x) + math.pow(y, 3)


        if rafael>beto and rafael>carlos:
            print("Rafael ganhou")

        if beto>rafael and beto>carlos:
            print("Beto ganhou")

        if carlos>beto and carlos>rafael:
            print("Carlos ganhou")
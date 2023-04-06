# número primo
import math

teste = int(input())
i = 0

for i in range(teste):
    x = int(input())
    if x>1 and x<= pow(10,7):
        primo = True
        for i in range(2,x):
            if x%i == 0:
                primo = False
                break

        if primo:
            print("{} eh primo".format(x))
        else:
            print("{} nao eh primo".format(x))
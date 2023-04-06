from math import sqrt

while True:
    try:
        l, c, r1, r2 = map(int, input().split())

        if l == 0 and c == 0 and r1 == 0 and r2 == 0:
            break

        else:
            if r1 > r2:
                maxCirc = r1 + r1
            else:
                maxCirc = r2 + r2
            if (l >= maxCirc) and (c >= maxCirc):
                if sqrt(pow((l - r2 - r1), 2) + pow(c - r2 - r1, 2)) >= r1 + r2:
                    print('S')
                else:
                    print('N')
            else:
                print("N")
    except EOFError:
        break
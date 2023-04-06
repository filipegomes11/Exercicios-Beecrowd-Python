#Triângulo
#Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
#um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
#e menor que a soma dos outros dois lados.

while True:
    try:
        def entrada():
            a, b, c, d = map(int,input().split())
            return a, b, c, d


        def condicao_triangulo(a,b,c):
            if abs(a - b) < c and c < a+b:
                if abs(a - c) < b and b < a+c:
                    if abs(c - b) < a and a < b+c:
                        return True
            else:
                return False


        def encaixar(a,b,c,d):
            if condicao_triangulo(a, b, c) or condicao_triangulo(a, b, d) or condicao_triangulo(a, c, d) or condicao_triangulo(
                    b, c, d):
                print("S")

            else:
                print("N")

        a, b, c, d = entrada()
        encaixar(a, b, c, d)

    except EOFError:
        break












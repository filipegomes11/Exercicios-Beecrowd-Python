#Enigma




a = str(input())
b = str(input())
quantidade = len(a) - len(b)    #diferença entre o array de a e o de b


def checagem(a, b):
    for i in range(len(a)):     #vamos rodar todo o tamanho de a e nele checar se existe alguma letra repetida entre a e b
        if a[i] == b[i]:        #exemplo: o M de ARMADA
            return False
    return True

posicoes = 0

for j in range(quantidade + 1):         #adicionamos 1 à quantidade, por causa do range que pega sempre menos 1.
    if checagem(a[j:len(b)+j], b) == True:  #se a checagem de a na posicao j(0) até o tamanho de b somado com j existir
        posicoes = posicoes + 1
print(posicoes)


def entrada():
    altura_sapo, n_canos = map(int, input().split())    #criamos uma lista com espaço entre a altura do pulo e Ncanos
    altura_canos = input().split()                      #criei outra lista para poder ter ter a sequencia de alturas de canos
    for i in range(len(altura_canos)):
        altura_canos[i] = int(altura_canos[i])   #quando criamos a lista de altCanos, precisamos fazer um loop do inicio do array
                                                 #até o final do array, para poder também contar os espaços também e transformar tudo em inteiro.
    return altura_sapo, n_canos, altura_canos


                                    #definir os parametros utilizados agora na função
def checagem(cano1, cano2, p):              #função abs vai retornar o valor absoluto: pois como temos uma diferença, então  pode ser que fique negativo
                                    #mas não queremos trabalhar com números negativos, pois logo após temos uma inequação.
    if abs(cano1 - cano2) > p:              #checar as condições do problema:
                                    #O valor absoluto da diferença de altura entre canos consecutivos tem que ser de, no máximo, a altura do pulo do sapo
        return True
    else:
        return False


def main():                         #aqui na main vamos unir todas as funções
    p, n, altura_canos = entrada()
    valor_logico = False
    for i in range(n - 1):
        valor_logico = checagem(altura_canos[i], altura_canos[i + 1], p)
        if valor_logico == True:            #se a linha 13 foi falsa, o comando da linha 26 vai ser feito
            print("GAME OVER")
            break
    if valor_logico == False:               #se a linha 13 foi verdadeira, o comando da linha 29 eh executado
        print("YOU WIN")


main()                              #voltar com a main, senão dá erro






















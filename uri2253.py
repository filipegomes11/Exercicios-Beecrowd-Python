# validador de senhas

while True:
    try:
        senha = input()
        minuscula = False
        maiscula = False  # vamos comecar com os pre requisitos como falsos
        numero = False
        if (len(senha) < 6) or (len(senha) > 32):
            print("Senha invalida.")
        else:
            for i in range(len(senha)):
                #vamos usar a funcao ord que descobre o valor de cada caracter na tabela ASCII
                if (((ord(senha[i])) > 96) and ((ord(senha[i])) < 123)):
                    minuscula = True #se estiver no intervalo aberto (96,123), então é minusculo
                elif(((ord(senha[i])) > 64) and ((ord(senha[i])) < 91)):
                    maiscula = True  # se estiver no intervalo aberto (64,91), então é maiusculo
                elif (((ord(senha[i])) > 47) and ((ord(senha[i])) < 58)):
                    numero = True   #se estiver no intervalo aberto (47,58) então é um número
                else:
                    maiscula, minuscula, numero = False
                    break

            if (maiscula and minuscula and numero):     #se há todos os pre requisitos, então está ok
                print('Senha valida.')
            else:
                print('Senha invalida.')            #se falta pelo menos um, está invalido mesmo assim

    except:
        break

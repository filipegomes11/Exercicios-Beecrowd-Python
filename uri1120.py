#revisao de contrato
#vou digitar o digito que está com problema e um numero em que esse digito está presente
#na saída vai aparecer o número sem o digito que está com defeito


while True:
    digito, numero = input().split()        #estão splitados por um espaço quando forem digitados
    if(digito == "0" and numero == "0"):      #a forma de terminar o programa é com os dois sendo zero
        break



    numero = "0" + numero
    vf = int(numero.replace(digito,'')) #era string, agora é tudo inteiro
    #replace é foi pra substituir o digito quebrado por NADA no array
    print(vf)
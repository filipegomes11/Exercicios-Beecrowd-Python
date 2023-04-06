#tempo de um evento
#se ele quer a diferença entre os dois dias, logo é só transformar tudo em segundo e fazer a subtração





di = int(input().split()[1])               #com o split, criamos uma lista
tempo = input().split(" : ")
hi = int(tempo[0])
mi = int(tempo[1])
si = int(tempo[2])

somatorio_i = si + mi*60 + hi*3600 + di*3600*24     #1 dia tem 86400 segundos, uma hora tem 3600 e um minuto tem 60secs

df = int(input().split()[1])
tempo = input().split(" : ")
hf = int(tempo[0])
mf = int(tempo[1])
sf = int(tempo[2])

somatorio_f = sf + mf*60 + hf*3600 + df*3600*24

#aqui começamos a encaixar pro print, como o programa quer. a variavel diferença vai perdendo valores em forma de
#cascata, então quando chegar na variavel segundos ela não vai precisar de mais nenhuma conta, pois tudo tinha sido
#transformado em forma de segundo

diferenca = somatorio_f - somatorio_i
dias_print = diferenca//(3600*24)

diferenca = diferenca % (3600*24)

horas_print = diferenca//3600
diferenca = diferenca % 3600

minutos_print = diferenca//60
diferenca = diferenca % 60   #vai ser igual a segundos agr

segundos_print = diferenca

print("{}dia(s)".format(dias_print))
print("{} hora(s)".format(horas_print))     #essas variaveis "x_print" são importantes para que nem o inicial e nem o final percam valores
print("{} minuto(s)".format(minutos_print))
print("{} segundo(s)".format(segundos_print))
#frequencia de numeros

numero = int(input())

lista = []

for i in range(numero):
	entrada = int(input())
	lista.append(entrada)


correcao = sorted(set(lista))		#do ingles sort = organizar. A funcao sorted vai organizar
									# a funcao set vai tirar tudo que ta sendo repetido


for j in range(len(correcao)):		#o tamanho de correcao basicamente vai ser quantos elementos tem no vetor
	print("{} aparece {} vez(es)".format(correcao[j], lista.count(correcao[j])))

		#count => quantas vezes corrigiu






























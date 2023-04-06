#cara ou coroa

while True:									#com o while true posso fazer estilo um menu, com ele terminando no 0

	vezes = int(input())

	if (vezes == 0):						#esse teve que ficar aqui no inicio, nao pode ser no final, senao nunca termina
		break

	pontos = list(map(int,input().split()))	#criamos uma lista para todos os resultados



	joao = 0
	#basicamente um contador pra joao e outro pra maria
	maria = 0
	for i in pontos:
		if(i == 0):
			maria = maria+  1			#se o resultado der 0 (cara), aí maria vai somar
		else:
			joao = joao + 1				#resultado deu coroa, joao ganha ponto1
	print("Mary won {} times and John won {} times".format(maria,joao))


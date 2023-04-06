#coleção de pokemon


entrada = int(input())            #número na entrada
string = []                    #vetor para colocar as strings
i = 0

for i in range(entrada):          #loop para adicionar os pokemons com a função append
    string.append(input())     #uma vez digitado, esse nome vai ser adicionado como pokemon

#função set vai nos ajudar a tirar os repetidos
#como no total temos 151 pokemons, após usar a função set e tirar os repetidos, podemos agora subtrair e ver quantos faltam
resposta = 151 - len(set(string))

print("Falta(m) {} pomekon(s).".format(resposta))
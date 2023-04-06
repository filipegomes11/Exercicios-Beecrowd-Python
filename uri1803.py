#matring




f = input()
coluna2 = input()
coluna3 = input()
l = input()


matriz1 = []
matriz2 = []


palavra = ""
for i in range(len(f)):
    matriz1.append(f[i] + coluna2[i] + coluna3[i] + l[i])
for j in range(len(f)):
    if (int(j) != 0) and (int(j) != int(len(matriz1))-1):
        matriz2.append((int(matriz1[0])*int(matriz1[j])+int(matriz1[len(matriz1)-1])) % 257)
for k in range(len(matriz2)):
    palavra += chr(matriz2[int(k)])
print(palavra)





























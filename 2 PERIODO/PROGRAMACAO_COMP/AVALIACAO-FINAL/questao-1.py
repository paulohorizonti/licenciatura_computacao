# Analise o trecho de programa a seguir, e responsa com base na execução
# desse trecho de código em python

#inicializando a matriz M
M=[[0,0,0],
   [0,0,0],
   [0,0,0]]
x=1
for i in range(3):
    for j in range(3):
        M[i][j] = i+2*j+x
        x +=1
print(M)
cont=0 #variavel auxiliar para efetuar contagem
#Considerando a execução desse trecho de programa em python, o numero de posições da matriz M
#que, ao final da execução, apresenta um valor maior ou igual a 10 é qual?

#percorrer a matriz resultante
for i in range(3):
    for j in range(3):
       #verificar cada elemento da matriz e comparar se é maior ou igual a 10
       if M[i][j] >= 10:
           cont+=1 #quando atende ao if ele soma 1

print('REPOSTA DA QUESTÃO\n[ {} ] POSIÇÕES MAIORES OU IGUAIS A 10'.format(cont))


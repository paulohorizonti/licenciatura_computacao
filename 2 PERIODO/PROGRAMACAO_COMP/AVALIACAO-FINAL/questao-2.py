# Dado o seguinte programa

#inicializacao das variaveis
a=2
b=1
c=3
d=0

#Calculo das variaveis lógicas
x = not(a+d>0)and(c-b<=5)
y = not x or(c/a>2)
z = y and x and (c - b - a >=0)

#Se formos exibir o resultado da saida de valores X, Y Z, quais serao
#os resultados respectivamente
print('REPOSTA\n')
print('{}, {}, {}'.format(x,y,z))

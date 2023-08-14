# 9. Escreva um programa em Python que solicite ao usuário dois números inteiros e realize
# as seguintes operações:
# e) Calcule a soma dos dois números.
# f) Calcule a diferença entre o primeiro número e o segundo número.
# g) Calcule o produto dos dois números.
# h) Calcule a divisão inteira do primeiro número pelo segundo número.
# i) Calcule o resto da divisão do primeiro número pelo segundo número.
# j) Calcule o resultado da potenciação do primeiro número elevado ao segundo
# número.
import math
n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
#Soma
soma = n1+n2

#Diferença
if n2<n1:
    dif = n1-n2
else:
    dif = n2-n1
#Produto
mult = n1*n2

#Divisão inteira
if(n2==0):
    print('\033[31mDIVISAO POR "0" IMPOSSIVEL \033[0;0m')
else:
    div = n1//n2

# Resto da divisão
if(n2==0):
    print('\033[31mDIVISAO POR "0" IMPOSSIVEL \033[0;0m')
else:
    rest = n1%n2
# Potencia
pot = math.pow(n1,n2)

print('NÚMEROS DIGITADOS: {} E {}'.format(n1,n2))
print('\n')

print('Soma: {} \nDiferença: {} \nProduto: {} \nDivisão Inteira: {} \nResto Divisão: {}'
          ' \nPotencia: {:.2f}'.format(soma, dif, mult, div, rest, pot))

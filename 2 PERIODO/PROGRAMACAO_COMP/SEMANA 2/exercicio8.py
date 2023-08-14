# 8. Escreva um programa em Python que solicite ao usuário dois números inteiros e
# realize as seguintes operações:
# a) Calcule a soma dos dois números.
# b) Calcule a diferença entre o primeiro número e o segundo número.
# c) Calcule o produto dos dois números.
# d) Calcule a divisão do primeiro número pelo segundo número (certifique-se de
# tratar o caso de divisão por zero).
n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
soma = n1+n2
if n2<n1:
    dif = n1-n2
else:
    dif = n2-n1
mult = n1*n2
if(n2==0):
    print('\033[31mDIVISAO POR "0" IMPOSSIVEL \033[0;0m')
    print('Soma: {}, Subtração: {}, Multiplicação: {}'.format(soma, dif, mult))
else:
    div = n1/n2
    print('Soma: {}, Subtração: {}, Multiplicação: {}, Divisão: {}'.format(soma, dif, mult, div))



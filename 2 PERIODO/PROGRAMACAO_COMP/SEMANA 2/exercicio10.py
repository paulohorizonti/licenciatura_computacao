# 10. Escreva um programa em Python que solicite ao usuário o valor de um ângulo em
# graus e calcule o seno, cosseno e tangente desse ângulo.
import math

angulo=eval(input('DIGITE O ANGULO EM GRAUS: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
print('Para o angulo: {} graus, temos que seu seno: {:.2f}, cosseno: {:.2f}, tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))

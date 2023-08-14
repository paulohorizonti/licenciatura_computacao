# 11. Escreva um programa em Python que solicite ao usuário a quantidade de horas
# trabalhadas por mês e o valor da hora de trabalho, e calcule o salário mensal.
VALOR_HORA = 5.65
horas_trabalhadas = eval(input('DIGITE AS HORAS TRABALHADAS : '))
salario = horas_trabalhadas*VALOR_HORA
print('Seu salario esse mes foi de: {} reais'.format(salario))


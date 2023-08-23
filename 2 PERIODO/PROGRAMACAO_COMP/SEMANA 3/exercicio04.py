"""Desenvolva um algoritmo em Python 
para calcular o índice de massa corporal
(IMC) de uma pessoa. O algoritmo deve 
solicitar ao usuário que digite o peso e a
 altura da pessoa e calcular o IMC usando 
 a fórmula: IMC = peso / (altura * altura). 
 Em seguida, o algoritmo deve verificar em
  qual faixa o IMC se encontra e exibir uma 
  mensagem correspondente.Por exemplo, se o
   IMC for menor que 18.5, o algoritmo
    deve exibir a mensagem "Abaixo do peso"
    . Se o IMC estiver entre 18.5 e 24.9, 
    o algoritmo deve exibir a mensagem 
    "Peso normal". E assim por diante, de 
    acordo com as faixas de IMC 
    estabelecidas."""
peso=eval(input('Digite o peso : '))
altura = eval(input('Digite a altura: '))
imc=peso/(altura*altura)

if imc<=16.9:
    print('IMC: {:.2f} - MUITO ABAIXO DO PESO'.format(imc))
elif imc >17 and imc <18.4:
    print('IMC: {:.2f} - ABAIXO DO PESO'.format(imc))
elif imc >18.5 and imc <24.9:
    print('IMC: {:.2f} - PESO NORMAL'.format(imc))
elif imc >25 and imc <29.9:
    print('IMC: {:.2f} - ACIMA DO PESO'.format(imc))
elif imc >30 and imc <34.9:
    print('IMC: {:.2f} - OBESIDADE GRAU I'.format(imc))
elif imc >35 and imc <=40:
    print('IMC: {:.2f} - OBESIDADE GRAU II'. format(imc))
else:
    print('IMC: {:.2f} - OBESIDADE GRAU III'.format(imc))





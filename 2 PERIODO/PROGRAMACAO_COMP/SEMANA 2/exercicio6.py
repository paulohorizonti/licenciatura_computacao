# 6. Exercícios Combinados:
# a) Escreva um programa que solicite ao usuário um número inteiro, multiplique esse
#    número por 2 e exiba o resultado na tela. Utilize variáveis para armazenar os valores.

# b)Cálculo do Volume de uma Esfera
#   Desenvolva um algoritmo em Python que solicite ao usuário o raio de uma esfera e
#   calcule o seu volume. O volume de uma esfera é dado pela fórmula: V = (4/3) * π * r³,
#   onde V é o volume e r é o raio da esfera.
#   Utilize os conceitos estudados, como declaração de variáveis, atribuição de valores, uso
#   do módulo de matemática (math) e exibição de resultados na tela.
#   Passos do algoritmo:
#     Importe o módulo de matemática utilizando a instrução import math.
#     Solicite ao usuário que digite o raio da esfera.
#     Armazene o valor digitado em uma variável chamada "raio".
#     Calcule o volume utilizando a fórmula: volume = (4/3) * math.pi * raio**3.
#     Exiba na tela uma mensagem informando o volume calculado.
#     Exemplo de saída esperada:
#        Digite o raio da esfera: 5
#          O volume da esfera é: 523.5987755982989
#   Neste exercício, você estará aplicando os conceitos de declaração de variáveis,
#   atribuição de valores, cálculos matemáticos utilizando o módulo de matemática (math) e
#   exibição de resultados na tela. Essa é uma aplicação prática dos conceitos estudados,
#   pois o cálculo do volume de uma esfera é utilizado em diversas áreas, como física e
#   engenharia.
#   Lembre-se de testar seu algoritmo com diferentes valores de raio para garantir que os
#   cálculos estejam corretos.

#   d) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
#      metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
#      para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
#      R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
#      preço total.
import math
print('---------------- EXERCICIO "a" ------------------------------- ')
numero_int = eval(input('DIGITE UM NÚMERO INTEIRO: '))
print('Número inteiro digitado pelo usuário: {}'.format(numero_int))
print('\n')

print('---------------- EXERCICIO "b" ------------------------------- ')
# Formula:  V = (4/3) * π * r³

raio_esfera= eval(input('DIGITE O RAIO DA ESFERA: '))
volume = (4/3)*math.pi * pow(raio_esfera,3)
print('Volume da esfera de raio: {} é {:.2f}'.format(raio_esfera,volume))
print('\n')
print('---------------- EXERCICIO "c" ------------------------------- ')
# 1 litro para cada 3m2
# cada lata tem 18/ l e custa 80 reais
area = eval(input('Digite o tamanho da área em m2, por favor: '))
qtd_litros = area /3
print('Sua área {} m2 vai gastar {:.2f} litros de tinta'.format(area,qtd_litros))
latas = qtd_litros / 18
valor_gasto = latas * 80
print('Vai gastar {:.2f} latas, e R${:.2f} reais para pintar tudo'.format(latas,valor_gasto))

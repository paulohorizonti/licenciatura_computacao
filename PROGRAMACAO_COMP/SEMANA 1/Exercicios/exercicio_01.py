# 1 -Exercício de Cálculo de Média:
#    a. Escreva um programa em Python que solicite ao usuário três notas (de 0 a 10) e
#    calcule a média dessas notas. Em seguida, exiba a média na tela.
nota1 = eval(input('Digite a primeira Nota: '))
nota2 = eval(input('Digite a segunda Nota: '))
nota3 = eval(input('Digite a terceira Nota: '))

media=(nota1+nota2+nota3)/3
print('A media das notas informadas foi : {}'.format(media))
print(type(media))
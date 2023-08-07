#2. Exercício de Conversão de Horas:
#   a. Escreva um programa em Python que solicite ao usuário um número inteiro que
#   a quantidade de horas e converta esse valor para dias e horas. Exiba o
#   resultado na tela.
tempo = int(input('Digite a quantidade de horas : '))
if(tempo <24):
    print('O tempo que informou,  {} hora(s) não chega a ser um dia inteiro'.format(tempo))
else:
    dias = tempo // 24
    horas = (tempo % 24)
    if(horas >0):
        print('{} horas correspondem a {} dia(s) e {} hora(s)'.format(tempo, dias, horas))
    else:
        print('{} horas correspondem a {} dia(s)'.format(tempo, dias))

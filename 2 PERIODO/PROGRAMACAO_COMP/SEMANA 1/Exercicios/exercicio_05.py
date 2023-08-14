# 5. Exercício de Tempo de Vida
# a. Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule
# quantos dias de vida um fumante perderá. Exiba o total em dias.
fumDia = int(input('Quantos cigarros você fuma por dia: '))
tempoFumo = int(input('Quanto tempo, em anos, você ja fumou: '))

#perco esses minutos por dia
tempoPerdidoPorDia = 10*fumDia

diasQueFumou = 365*tempoFumo

print('Eu perco {} min todo dia, pois fumo {} por dia'.format(tempoPerdidoPorDia, fumDia))

porAnoFumo = fumDia*365

print('Eu fumo {} cigarros por ano, fumando {} por dia'.format(porAnoFumo, fumDia))

#vai dar em minutos
x = tempoPerdidoPorDia*diasQueFumou
x=x/60 #minutos para horas
x=x/24 #horas para dias

dias=int(x//1) #somente horas
horas =int((x-dias)*24)
if(horas>0):
    print('Eu ja perdi {} dias e {} horas de vida, pois fumei {} cigarro(s) por dia em {} ano(s)'.format(dias, horas, fumDia, tempoFumo))
else:
    print('Eu ja perdi {} horas dias de vida, pois fumei {} cigarro(s) por dia em {} ano(s)'.format(horas,fumDia, tempoFumo))






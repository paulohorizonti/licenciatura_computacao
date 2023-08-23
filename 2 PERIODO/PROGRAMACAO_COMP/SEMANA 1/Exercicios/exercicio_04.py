# 4. Exercício de Tempo de Viagem
# a. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a
# distância a percorrer e a velocidade média esperada para a viagem.
dist = eval(input('Digite a distância em KM: '))
vel = eval(input('Digite a velocidade média esperada(km/h) : '))
tempoDesloc = dist / vel

tempInt = int(tempoDesloc // 1)
tempQueb = tempoDesloc - tempInt
minT = int(tempQueb * 60)

#print('Parte inteira: ', tempInt, ' - Parte quebrada', tempQueb, ' - Minutos', minT)

if (tempQueb > 0):
    print('O tempo percorrido para a distância de {}km, a uma velocidade de {}km/h \n'
          ' é de: {} horas e {} minutos'.format(dist, vel, tempInt, minT))
else:
    print('O tempo percorrido para a distância de {}km, a uma velocidade de {}km/h \n'
          ' é de: {} hora(s)'.format(dist, vel, int(tempoDesloc)))

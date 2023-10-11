# Dado o programa a seguir
def calcule(aux):
    tst = 1
    if aux == 0:
        return tst
    else:
        return aux + calcule(aux - 1)
entrada = int(input('DIDITE UM VALOR: '))
reposta = calcule(entrada)
print(reposta)

#se for digitado como entrada o valor 14, qual sera o valor impresso na saida
#RESPOSTA: 106
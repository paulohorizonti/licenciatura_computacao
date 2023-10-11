#O programa abaixo realiza a troca dos valores de duas variaveis NORTE e SUL,
# com ajuda de uma variavel AUX. Se os valores iniciais forem 44 para NORTE
# e 19 para SUL, ao final da exeucação das instruções, essas variaveis conterao respectivamente
# os valores 19 e 44
NORTE=155
SUL=15
print('MOSTRANDO VALORES INICIAIS')
print('NORTE: \t[{}]\nSUL: \t[{}]'.format(NORTE, SUL))
print('-----------------------------------------------')
AUX = NORTE
NORTE = SUL
SUL = AUX
print('MOSTRANDO VALORES TROCADOS USANDO VARIAVEL AUX')
print('NORTE: \t[{}]\nSUL: \t[{}]'.format(NORTE, SUL))
print('-----------------------------------------------')
NORTE=155
SUL=15
print('VOLTANDO VALORES INICIAIS')
print('NORTE: \t[{}]\nSUL: \t[{}]'.format(NORTE, SUL))
print('-----------------------------------------------')
NORTE=NORTE+SUL
SUL=NORTE-SUL
NORTE=NORTE-SUL

print('MOSTRANDO VALORES TROCADOS SEM USO DA  VARIAVEL AUX')
print('NORTE: \t[{}]\nSUL: \t[{}]'.format(NORTE, SUL))
print('-----------------------------------------------')
#A estrutra equivalente que gera o mesmo resultado, sem a ajuda de uma variavel auxiliar AUX, está indicada
# na seguinte alternativa
print('RESPOSTA')
print('NORTE = NORTE + SUL\nSUL = NORTE - SUL\nNORTE = NORTE - SUL')
print('-----------------------------------------------')

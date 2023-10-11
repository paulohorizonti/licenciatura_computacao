VET = [3,1,4,1,5,9,2,6,5,3]
for CONTA in range(9):
    for CONTB in range(CONTA + 1,10):
        if VET[CONTA] > VET[CONTB]:
            AUX=VET[CONTB]
            VET[CONTB]=VET[CONTA]
            VET[CONTA] = AUX
print(VET)

#o que o programa acima faz?
# ordena em ordem crescente e imprime o vetor final
print('RESPOSTA: ordena em ordem crescente e imprime o vetor final')
# 12. Escreva um programa em Python que solicite ao usuário se ele deseja ativar o modo
# noturno (sim ou não). O programa deve exibir a mensagem "Modo noturno ativado!" se o usuário
#responder "sim", e a mensagem "Modo noturno desativado!" se o usuário responder "não"
noturno = input('DESEJA ATIVAR MODO NOTURNO (SIM/NÃO): ')

print(noturno)
if (noturno!='SIM') and (noturno!='NÃO'):
    print('ESCREVA SOMENTE SIM OU NÃO')
else:
    if noturno == 'SIM':
        print('MODO NOTURNO ATIVADO')
    else:
        print('MODO NOTURNO DESATIVADO')

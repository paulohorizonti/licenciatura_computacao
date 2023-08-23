"""Desenvolva um algoritmo em Python para determinar se um ano é bissexto. O algoritmo
deve solicitar ao usuário que digite um ano e verificar se o ano é bissexto. Um ano é
bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400. Caso o
ano seja bissexto, o algoritmo deve exibir a mensagem "Ano bissexto". Caso contrário, o
algoritmo deve exibir a mensagem "Ano não bissexto"."""
ano = int(input("DIGITE O ANO, POR FAVOR: "))

if ano % 4 == 0 and ano % 100 != 0:
    if ano % 400 == 0:
        print('NÃO BISEXTO')
    else:
        print('BISEXTO')
else:
    print('NÃO BISEXTO')
"""Desenvolva um algoritmo em Python para determinar se uma pessoa tem direito a
desconto em um ingresso de cinema. O algoritmo deve solicitar ao usuário que digite a
idade da pessoa e verificar se ela tem menos de 12 anos ou mais de 60 anos. Se a idade
estiver dentro dessas faixas, a pessoa terá direito a um desconto de 50% no valor do
ingresso. Caso contrário, não haverá desconto. O algoritmo deve exibir o valor a ser pago
pelo ingresso, considerando o desconto, se aplicável."""
valor = eval(input('DIGITE O VALOR DO INGRESSO : '))
idade = int(input('DIGITE A IDADE DA PESSOA: '))

if idade >=12 and idade <=60:
    print('VALOR DO INGRESSO: {:.2f}'.format(valor))
else:
    valor_c_desc = valor - ((valor * 50) / 100)
    print('CONSIDERANDO SUA IDADE: {}, SEU INGRESSO QUE ERA DE {} VAI TER DESCONTO E VAI CUSTAR: {:.2f}'.format(idade,valor,valor_c_desc))

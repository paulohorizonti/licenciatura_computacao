""" Desenvolva um algoritmo em Python para calcular o preço final de um produto em
uma loja, considerando os seguintes critérios:

Se o preço do produto for maior que R$ 100,00 e o cliente for VIP, aplique um desconto de 10%
no preço final.

Se o preço do produto for maior que R$ 100,00 e o cliente não for VIP, aplique um desconto de
5% no preço final.

 Se o preço do produto for menor ou igual a R$ 100,00, não aplique nenhum desconto.

O algoritmo deve solicitar o preço do produto e se o cliente é VIP ou não. Em seguida, ele deve
calcular e exibir o preço final após aplicar o desconto, se aplicável.

Dica: Utilize a função input() para receber os valores digitados pelo usuário e a função float() para
converter os valores para números decimais. Sua tarefa é escrever o algoritmo completo, incluindo as estruturas
condicionais if e else.
Certifique-se de testar seu algoritmo com diferentes valores de entrada para garantir que ele
esteja funcionando corretamente. Lembre-se de comentar seu código para melhorar a legibilidade e explicar cada etapa do
algoritmo"""
preco_produto = eval(input('DIGITE O PREÇO DO PRODUTO: '))

if preco_produto < 100:
    preco_final = preco_produto
else:
    cliente_Vip = int(input('CLIENTE VIP? [1]-SIM - [2]-NÃO: '))
    if cliente_Vip == 1:
        preco_final = preco_produto - ((preco_produto * 10) / 100)
    else:
        preco_final = preco_produto - ((preco_produto * 5) / 100)

print('Preço final do produto : R${:.2f}'.format(preco_final))
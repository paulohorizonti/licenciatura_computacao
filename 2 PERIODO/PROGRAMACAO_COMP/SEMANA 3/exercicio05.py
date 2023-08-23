""" Desenvolva um algoritmo em Python  para criar um conversor de moedas que   permita ao usuário converter valores
entre diferentes moedas. O algoritmo deve utilizar os conceitos estudados, como declaração de variáveis, atribuição
de valores, operações matemáticas, entrada de dados do usuário e exibição de resultados na tela.
Passos do algoritmo: Declare as variáveis de conversão para cada moeda desejada, por exemplo: taxa_dolar = 5.25 #
Valor da taxa de câmbio do dólar em relação à moeda local taxa_euro = 6.15. Valor da taxa de câmbio do euro em
relação à moeda local Solicite ao usuário o valor a ser convertido e a moeda de origem:
valor_origem = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: BRL, USD, EUR): ")
Solicite ao usuário a moeda de destino:
moeda_destino = input("Digite a moeda de destino (ex: BRL, USD, EUR): ")
Utilize estruturas condicionais (if/elif/else) para realizar a conversão de acordo
com as moedas selecionadas:
Se moeda_origem for igual a "BRL" e  moeda_destino for igual a "USD", o  valor convertido será
valor_origem dividido pela taxa_dolar. Se moeda_origem for igual a "BRL" e moeda_destino for igual a "EUR",
o valor convertido será  valor_origem dividido pela taxa_euro. Adicione outras condições de acordo com
as moedas que deseja incluir. Exiba na tela o valor convertido:
print("Valor convertido:", valor_convertido) 
Exemplo de saída esperada:
Digite o valor a ser convertido: 
100 
Digite a moeda de origem (ex: BRL, USD, EUR):
BRL Digite a moeda de destino (ex: BRL, USD, EUR): USD Valor convertido: 19.05
Neste exercício, você estará aplicando os conceitos estudados para criar um algoritmo  mais complexo,
que envolve declaração de variáveis, atribuição de valores, operações matemáticas e estruturas condicionais.
Essa é uma aplicação prática dos conceitos, já que a conversão de moedas é um problema real que enfrentamos ao
viajar ou fazer transações financeiras internacionais. Lembre-se de testar seu algoritmo com diferentes valores e
moedas para garantir que as conversões estejam corretas."""

tx_dolar=4.94
tx_euro=5.35
tx_ars=0.014

vl_origem=eval(input('Digite o valor de origem: '))
m_origem=int(input('Digite a moeda de ORIGEM: \n1-BRL \n2-USD \n3-EUR \n4-ASR: '))
m_destino=int(input('Digite a moeda de DESTINO: \n1-BRL \n2-USD \n3-EUR \n4-ASR: '))
if m_origem==1 and m_destino==2:
    v_conv=vl_origem/tx_dolar
    print('O valor R${:.2f}  convertido em dolares: ${:.2f}'.format(vl_origem,v_conv))
elif m_origem==2 and m_destino==1:
    v_conv=vl_origem*tx_dolar
    print('O valor USD${:.2f}  convertido em Reais: R${:.2f}'.format(vl_origem,v_conv))
if m_origem==1 and m_destino==3:
    v_conv=vl_origem/tx_euro
    print('O valor R${:.2f}  convertido em EUROS: ${:.2f}'.format(vl_origem,v_conv))
elif m_origem==3 and m_destino==1:
    v_conv=vl_origem*tx_euro
    print('O valor EUR${:.2f}  convertido em REAIS: R${:.2f}'.format(vl_origem,v_conv))
if m_origem==1 and m_destino==4:
    v_conv=vl_origem/tx_ars
    print('O valor R${:.2f}  convertido em PESOS: ${:.2f}'.format(vl_origem,v_conv))
elif m_origem==4 and m_destino==1:
    v_conv=vl_origem*tx_ars
    print('O valor PESOS${:.2f}  convertido em REAIS: R${:.2f}'.format(vl_origem,v_conv))


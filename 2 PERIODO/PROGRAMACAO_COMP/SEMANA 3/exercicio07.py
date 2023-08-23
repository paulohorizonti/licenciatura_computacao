""" Desenvolva um algoritmo em Python para verificar se um número digitado pelo usuário é par ou ímpar.
 O algoritmo deve solicitar ao usuário que digite um número inteiro e, em seguida, verificar se o número
 é par ou ímpar. Caso seja par, o algoritmo deve exibir a mensagem "O número é par".
  Caso seja ímpar, o algoritmo deve exibir a mensagem "O número é ímpar".
Dica:
Utilize a função input() para receber o valor digitado pelo usuário e a função int() para converter
o valor para um número inteiro.
Sua tarefa é escrever o algoritmo completo, incluindo as estruturas condicionais if e else.
Certifique-se de testar seu algoritmo com diferentes valores de entrada para garantir que ele esteja
funcionando corretamente.
Lembre-se de comentar seu código para melhorar a legibilidade e explicar cada etapa do algoritmo."""

try:
    num = int(input('\033[35m DIGITE UM NUMERO INTEIRO \033[0;0m \n'))
    if num % 2 == 0:
        print('\033[36m NUMERO PAR')
    else:
        print('\033[33m NUMERO IMPAR')
except:
    print('\033[31m VERIFIQUE OS DADOS INFORMADOS E TENTE NOVAMENTE')

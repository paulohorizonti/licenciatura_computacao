#3. Exercício de Aumento de Salário
#   a. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor
#   do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo
#   salário.
salario = eval(input('Digite o salário do maganal: '))
aumento = eval(input('Agora a % do aumento: '))
salarioFinal = ((salario*aumento)/100)+salario
print('Para um aumento de {}%, o salario que era de: R${:.2f}, foi para: R${:.2f}'.format(aumento, salario, salarioFinal))
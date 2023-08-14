# 7. Faça um programa em Python que solicite ao usuário o seu nome e idade. Em seguida,
# exiba na tela uma mensagem contendo o nome e a idade informados pelo usuário.
nome=input('DIGITE SEU NOME: ')
idade=int(input('DIGITE SUA IDADE: '))
nome = nome.upper()
print('Nome: {}, idade: {} anos'.format(nome,idade))
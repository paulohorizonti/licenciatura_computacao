#Dada a seguinte função
def verify_var_type(variable):
    if isinstance(variable, str):
        return True
    else:
        return False
#Analisando o bloco de codigo acina, responda. Qual o retorno dessa
#função?

#Neste caso, basta fazer a chamada da funcao passando qq coisa no parametro
print("PASSANDO COMO PARAMETRO A PALAVRA 'todos', TEMOS O RETORNO: ")
print(verify_var_type('todos'))
print("PASSANDO COMO PARAMETRO O NUMERO 10, TEMOS O RETORNO: ")
print(verify_var_type(10))
print('----------------------------------\n')
print('PORTANTO A RESPOSTA É: A função acima verifica o tipo de uma variavel e caso seja do tipo string retorna o valor TRUE')
# Reescreva o código da Atividade 01 utilizando o conceito de
# compreensão de dicionários (dict comprehension).

#relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']

#armazenar numero de letras de cada nome
qtd_letras = {}

# Usando o dict
qtd_letras = {f'{nome.upper()}': f'QtdLetras: {len(nome)}' for nome in nomes }
print(qtd_letras)
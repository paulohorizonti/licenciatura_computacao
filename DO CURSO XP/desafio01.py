#relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']

#armazenar numero de letras de cada nome
qtd_letras = {}

#calcula o tamanho de cada nome (em numero de letras) e armazena o valor na estrutra
for nome in nomes:
    qtd_letras[nome] = len(nome)

print(qtd_letras)

# Usando o dict
qtd_letras = {f'{nome.upper()}': f'QtdLetras: {len(nome)}' for nome in nomes }
print(qtd_letras)
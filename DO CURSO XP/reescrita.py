lista = ['Ferrari', 'Lamborghini', 'Porsche']
dicionario = {
  f'{elemento.lower()}': f'Montadora: {elemento.upper()}' for elemento in lista
}
print(dicionario)
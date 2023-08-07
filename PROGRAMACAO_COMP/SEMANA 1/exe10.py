# Cálculo do desconto em uma compra
valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = valor_compra * desconto / 100
valor_final = valor_compra - valor_desconto
print("O valor do desconto é:", valor_desconto)
print("O valor final da compra com desconto é:", valor_final)
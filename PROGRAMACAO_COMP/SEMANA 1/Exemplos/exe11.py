# Cálculo do IMC (Índice de Massa Corporal)
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / altura**2
print("Seu IMC é:", imc)
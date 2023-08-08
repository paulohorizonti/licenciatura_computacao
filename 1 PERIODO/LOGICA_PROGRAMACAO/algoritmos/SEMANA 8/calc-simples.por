programa
{
	inteiro opcao, num1, num2
	
	funcao inicio()
	{
		escreva("Digite uma opção \n")
		escreva("1 PARA SOMAR - 2 PARA SUBTRAIR - 3 PARA MULTIPLICAR - 4 PARA DIVIDIR \n")
		leia(opcao)

		se(opcao == 1)
		{
			escreva("Digite o primeiro número :")
			leia(num1)
			escreva("Digite o segundo número : ")
			leia(num2)
			escreva("A soma dos dois numeros digitados é : ", num1+num2)
		}
		se(opcao == 2)
		{
			escreva("Digite o primeiro número :")
			leia(num1)
			escreva("Digite o segundo número : ")
			leia(num2)
			escreva("A subtracao dos dois numeros digitados é : ", num1-num2)
		}
		se(opcao == 3)
		{
			escreva("Digite o primeiro número :")
			leia(num1)
			escreva("Digite o segundo número : ")
			leia(num2)
			escreva("A multiplicacao dos dois numeros digitados é : ", num1*num2)
		}
		se(opcao == 4)
		{
			escreva("Digite o primeiro número :")
			leia(num1)
			escreva("Digite o segundo número : ")
			leia(num2)
			escreva("A divisao dos dois numeros digitados é : ", num1/num2)
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1001; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
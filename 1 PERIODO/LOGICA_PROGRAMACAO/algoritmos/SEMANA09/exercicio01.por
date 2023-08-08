programa
{
/*
Escrever um programa no Portugol Studio que possua uma
função que some o valor de duas variáveis do tipo inteiro
lidas do usuário, em seguida atribua zero para o valor
dessas variáveis.*/
	inteiro num1, num2
	funcao inicio()
	{
		escreva("Digite o primeiro número : ")
		leia(num1)
		escreva("Digite o segundo número : ")
		leia(num2)
		soma(num1,num2)
	
	}

	funcao soma(inteiro &a, inteiro &b)
	{
		inteiro resultado = a+b
		num1 = 0
		num2 = 0
		
		escreva("A soma entre ",a," e ", b," é : ",resultado,"\n")
		escreva("Valor de num1 :",num1,"\n")
		escreva("Valor de num2 :",num2,"\n")
		
	
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 415; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
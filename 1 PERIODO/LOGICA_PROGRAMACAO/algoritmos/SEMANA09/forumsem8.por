programa
{
/*
Escreva um programa no Portugol Studio que dada uma cadeia com o nome da pessoa, adicione o sobrenome na cadeia através de uma função. 
Isto pode ser feito de duas formas: 
1 - através da passagem de parâmetro por valor, onde você dá o nome e a cadeia retornada pela função é a cadeia com nome concatenada com sobrenome; 
ou a 
forma 2 - através da passagem de parâmetro por referência, onde a cadeia é modificada dentro da própria função, que possui retorno vazio.

Em ambos os casos, mostre a cadeia antes e depois da alteração. Veja a seguir alguns exemplos. 

Exemplo caso 1: 
cadeia nomeCompleto = "Tanilson"
nomeCompleto = adicionarSobrenome( nomeCompleto)
// após a linha de cima o novo valor da variável nomeCompleto deve ser "Tanilson Dias", por exemplo, isto é o nome concatenado com um sobrenome

Exemplo caso 2: 
cadeia nomeCompleto = "Tanilson"
adicionarSobrenome( nomeCompleto)
// após a linha de cima o novo valor da variável nomeCompleto deve ser "Tanilson Dias", por exemplo, isto é o nome concatenado com um sobrenome

*/
	inclua biblioteca Texto  --> tx
	cadeia nome, sobrenome, nomeCompleto=""
	cadeia nomeSobrenome=""
	
	funcao inicio()
	{
		nome = "ERICA"
		sobrenome = "DE SOUSA"
		escreva("Seu nome é: ", nome," e seu sobrenome é: ",sobrenome,"\n") //aqui mostra as duas variaveis separadas


		escreva("PARAMETROS POR VALOR: \n\n")
		escreva("Valor da variavel nomeCompleto antes da alteração : ",nomeCompleto,"\n")
		nomeCompleto = adicionarSobrenomeValor(nome)

		
		
		escreva("Valor da variavel nomeCompleto depois da alteração : ",nomeCompleto,"\n\n")
		
	}

	funcao cadeia adicionarSobrenomeValor(cadeia a)
	{
		
		
		nomeCompleto=a+" "+sobrenome
		
		retorne  nomeCompleto
	
	}

	
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1598; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */
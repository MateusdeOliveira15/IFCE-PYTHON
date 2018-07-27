#Escrever um programa que leia uma sequência de números positivos calcule e imprima a
#quantidade de valores superior à média aritmética. A sequência termina quando for
#digitado o valor zero.

#OBSERVAÇÃO: o valor zero não é incluso como termo da sequência


numeros = []

i = 1
while i!=0:
	
	num = int(input('Digite um número: '))
	numeros.append(num)
	
	i = int(input('Digite 0 para sair ou digite outro número para continuar: '))
	

soma = 0
for i in range(len(numeros)):
	soma  = soma + numeros[i]

media = soma / len(numeros)


quant = 0
for i in range(len(numeros)):
	if numeros[i]>media:
		quant = quant + 1

print(quant)
	
	
	
	
	
	
	
	

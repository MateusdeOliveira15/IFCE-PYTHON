#Elabore um algoritmo que leia duas listas de dez inteiros e faça a multiplicação dos
#elementos de mesmo índice, colocando o resultado em uma terceira lista, que deve ser
#mostrado como saída.

quant = int(input('Digite o tamanho das listas: '))

lista1 = []
lista2 = []

for i in range(quant):
	x = int(input('Digite um número para a primeira lista: '))
	y = int(input('Digite um número para a segunda lista: '))
	
	lista1.append(x)
	lista2.append(y)

lista_nova = []

for i in range(len(lista1)):
	resultado = lista1[i] * lista2[i]
	lista_nova.append(resultado)

print(lista_nova)


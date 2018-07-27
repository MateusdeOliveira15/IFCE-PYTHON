#Escreva um algoritmo que leia uma lista de 20 inteiros digitado pelo usuário. Em seguida,
#troque o primeiro elemento pelo o último, o segundo com o penúltimo, o terceiro com o
#antepenúltimo e, assim, sucessivamente. Mostre o novo vetor após todas as trocas.


lista = []

for i in range(20):
	num = int(input('Digite um número: '))
	lista.append(num)


lista_nova = []

x = 1
for i in range(0,len(lista)):
	z = lista[len(lista)-x]
	lista_nova.append(z)
	
	x = x + 1
print(lista_nova)
		



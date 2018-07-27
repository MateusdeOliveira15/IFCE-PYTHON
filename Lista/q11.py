#Escreva um programa que leia duas sequências de números ordenadas pelo usuário e
#execute o algoritmo insert sort. O algoritmo insert sort, ou ordenação por inserção, é o
#algoritmo de ordenação que, dado duas listas constrói uma nova lista com um elemento
#de cada vez, uma inserção por vez. Não pode usar o sort na lista final.
#Exemplo:
#lista_1 = [1, 2, 5, 6]
#lista_2 = [1, 2, 3, 4]
#nova_lista = [1, 1, 2, 2, 3, 4, 5, 6]

lista_1 = [1,2,5,6]
lista_2 = [1,2,3,4]

lista_1.sort()
lista_2.sort()

lista_nova = lista_1 + lista_2

for i in range(1,len(lista_nova)):
	x = lista_nova[i]
	j = i-1
	while j>=0 and x<lista_nova[j]:
		lista_nova[j+1] = lista_nova[j]
		j=j-1
		lista_nova[j+1] = x

print(lista_nova)

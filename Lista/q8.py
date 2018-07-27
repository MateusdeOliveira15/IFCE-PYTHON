#Receber uma palavra digitada pelo usuário e calcular quantas vogais (a, e, i, o, u) possui
#essa palavra. Em seguida, o programa deve pedir para o usuário digitar um caractere
#(vogal ou consoante) e substituir todas as vogais da palavra dada por esse caractere.

string = input('Digite uma palavra: ')
lista = list(string)


quant = 0

for i in range(len(lista)):
	if lista[i] == 'a' or lista[i] == 'e' or lista[i] == 'i' or lista[i] == 'o'	or lista[i] == 'u' or lista[i] == 'A' or lista[i] == 'E' or lista[i] == 'I' or lista[i] == 'O' or lista[i] == 'U':
		quant = quant + 1	

print('Quantidades de vogais: {}'.format(quant))

carac = input('Digite um caractere: ')

for i in range(len(lista)):
	if 'a' == lista[i] or 'A' == lista[i]:
		lista[i] = carac
	if 'e' == lista[i] or 'E' == lista[i]:
		lista[i] = carac
	if 'i' == lista[i] or 'I' == lista[i]:
		lista[i] = carac
	if 'o' == lista[i] or 'O' == lista[i]:
		lista[i] = carac
	if 'u' == lista[i] or 'U' == lista[i]:
		lista[i] = carac

string = ''.join(lista)

print(string)
	
	
	
	
	
	

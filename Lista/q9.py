#Faça um programa que receba do usuário uma string e imprima a string sem suas vogais. 

string = input('Digite uma string: ')
lista = list(string)

string_nova = []

for i in range(len(lista)):
	if lista[i] != 'a' and lista[i] != 'e' and lista[i] != 'i' and lista[i] != 'o' and lista[i] != 'u':
		string_nova.append(lista[i])


string_nova = ''.join(string_nova)

print('String sem as vogais: {}'.format(string_nova))

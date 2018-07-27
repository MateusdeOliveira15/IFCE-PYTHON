#Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em
#uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário. 

string = input('Digite uma string: ')
letra1 = input('Digite uma letra: ')
letra2 = input('Digite outra letra: ')

string = list(string)


for i in range(len(string)):
	if letra1 in string:
		cod = string.index(letra1)
		string[cod] = letra2

string = ''.join(string)

print(string)

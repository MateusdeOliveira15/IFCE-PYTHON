#Construa um algoritmo que gere aleatoriamente treze elementos inteiros de 1 até 100,
#que é o gabarito de um teste da loteria esportiva. O programa deve pedir sempre o
#número do cartão de um apostador (usuário) e a lista de palpites com treze valores de 1 e
#até 100. Nem preciso dizer que o usuário e nem a loteria sorteiam números repetidos. Validem.

#Verifique para cada apostador o número de acertos, comparando o gabarito com as
#respostas dele. Escreva o número do apostador e o número de acertos ao final da
#aposta. Se o apostador tiver treze acertos, mostre a mensagem “Ganhador". Caso
#contrário, o programa deve voltar a pedir o número do cartão e a lista de palpites de um
#novo apostador.

import random



numeros = []

i = 1
while i <= 4:
	num = random.randint(1, 4)		
	if num not in numeros:
		numeros.append(num)
		i = i + 1
		
palpite=[]		

pontos = 0

while 1:
	print('################################################################################')
	cartao =  int(input('Digite o número do cartão : '))
	j = 1
	while j <= 3:
		numero = int(input('Digite um palpite: '))
		
		if numero in palpite:
			numero = int(input('Digite um palpite diferente dos outros: '))
			palpite.append(numero)
			j = j + 1
		else:
			palpite.append(numero)
			j = j + 1
	
	
	for i in range(0,3):
		if numeros[i] in palpite:
			pontos = pontos + 1
	
	if pontos == 3:
		print('################################################################################')
		print('GANHAAAAAAAADOOOOORRRRRRRRRRRRRRR!!!!!!!!!!!!!')
		print('Cartão: {}\nPontos: {}'.format(cartao,pontos))
		break
	else: 			
		print('Cartão: {}\nPontos: {}'.format(cartao,pontos))
		palpite = []
		pontos = 0
	
	
	

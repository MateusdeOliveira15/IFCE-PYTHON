#Uma firma quer fazer uma pesquisa de mercado para saber se as pessoas gostaram ou
#não de um novo produto lançado do mercado. Para isso, ela quer reunir informações
#acerca das pessoas, tais como o sexo do entrevistado (1 - Masculino, 2 - Feminino) e a
#resposta (1 - Sim ou 2 - Não). Sabe-se que a pesquisa será feita com 10 pessoas. Faça
#um programa que entreviste, calcule e mostre:
#A. O número de pessoas que respondeu sim;
#B. O número de pessoas que respondeu não;
#C. O número de homens que respondeu sim;
#D. O número de mulheres que respondeu não. 


sim = 0
nao = 0
hSim = 0
mNao = 0

for i in range(5):
	print('RESPONDA AS PERGUNTAS ABAIXO: ')
	print('-------------------------------------------------------------------')
	print('GÊNERO')
	print('1 - Masculino ')
	print('2 - Feminino \n')
	genero = int(input('Resposta -> '))
	print('-------------------------------------------------------------------')
	print('RESPOSTA DA PESQUISA')
	print('1 - Sim ')
	print('2 - Não \n')
	resposta = int(input('Resposta -> '))
	
	
	if resposta == 1:
		sim = sim + 1
	if resposta == 2:
		nao = nao + 1
	if genero == 1 and resposta == 1:
		hSim = hSim + 1
	if genero == 2 and resposta == 2:
		mNao = mNao + 1
print('\n##########################################################\n')
print('Número de pessoas que respondeu sim: {}'.format(sim))
print('Número de pessoas que respondeu não: {}'.format(nao))
print('Número de homens que respondeu sim: {}'.format(hSim))
print('Número de mulheres que respondeu não: {}'.format(mNao))	
print('\n##########################################################')

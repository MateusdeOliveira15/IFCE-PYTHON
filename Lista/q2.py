#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25
#se forem compradas pelo menos doze. Escreva um programa que leia o número de
#maçãs compradas, calcule e escreva o valor total da compra. 

quant = int(input('Digite a quantidades de maçãs compradas: '))

if quant < 12:
	valor = quant * 0.30
	print('Quantidades de maçãs-> {}'.format(quant))
	print('Preço total à pagar pelas %d maçãs -> R$%.2f'%(quant,valor))
else:
	valor = quant * 0.25
	print('Quantidades de maçãs-> {}'.format(quant))
	print('Preço total à pagar pelas %d maçãs -> R$%.2f'%(quant,valor))

#Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o
#triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que: 

#• Triângulo Retângulo: possui um ângulo reto. (igual a 90 graus)
#• Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90 graus)
#• Triângulo Acutângulo: possui três ângulos agudos. (menor que 90 graus)
#OBSERVAÇÃO: O programa deve mostrar que os ângulos são inválidos quando eles
#juntos ultrapassarem 180 graus.

angulo1 = int(input('Digite o primeiro ângulo: '))
angulo2 = int(input('Digite o segundo ângulo: '))
angulo3 = int(input('Digite o terceiro ângulo: '))

soma = angulo1 + angulo2 + angulo3


if soma > 180:
	print('Ângulos são inválidos!!!')
elif soma == 90 :
	print('---------------------------------------------------')
	print('Triângulo Retângulo')
	print('---------------------------------------------------')
elif 90 <= soma <= 180:
	print('---------------------------------------------------')
	print('Triângulo Obtusângulo')
	print('---------------------------------------------------')
else:
	print('---------------------------------------------------')
	print('Triângulo Acutângulo')
	print('---------------------------------------------------')

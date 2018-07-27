#Escreva um algoritmo que leia um conjunto de 12 fichas correspondente aos alunos e
#armazene-as em listas. A ficha contém as seguintes informações: altura e o código do
#sexo de uma pessoa (código = 1 se for masculino e 2 se for feminino), e calcule e
#imprima:
#A. A maior e a menor altura da turma;
#B. As mulheres com altura acima da média da altura das mulheres;
#C. Os homens com altura abaixo da média da altura das mulheres;
#D. As pessoas com altura abaixo da média da turma.


altura = []
aux = []
sexo = []


for i in range(6):
	print('-----------------------------------------------------------')
	h = float(input('Digite a altura: '))
	s = int(input('1 - Masculino / 2 - Feminino: '))
	print('-----------------------------------------------------------')
	
	altura.append(h)
	aux.append(h)
	sexo.append(s)
#Algoritimo de maior e menor valor de uma lista
altura.sort()
maior = altura[-1]
menor = altura[0]

print('############################################################')
print('Maior altura: {} / Menor altura: {}'.format(maior,menor))


somaH = 0
contH = 0
soma = 0
cont = 0
for i in range(len(aux)):
	if sexo[i] == 2:
		somaH = somaH + aux[i]
		contH = contH + 1
	soma = soma + aux[i]
	cont = cont + 1
media = soma / cont
mediaH = somaH / contH

m_acima = 0
h_abaixo = 0
t_abaixo = 0
for i in range(len(aux)):
	if sexo[i] == 2 and aux[i] > mediaH:
		m_acima = m_acima + 1
	if sexo[i] == 1 and aux[i] < mediaH:
		h_abaixo = h_abaixo + 1
	if altura[i]<media:
		t_abaixo = t_abaixo + 1

print('As mulheres com altura acima da média da altura das mulheres: {}'.format(m_acima))
print('Os homens com altura abaixo da média da altura das mulheres: {}'.format(h_abaixo))
print('As pessoas com altura abaixo da média da turma: {}'.format(t_abaixo))
		
		
		
		

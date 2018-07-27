#Receber uma string digitada pelo usuário e imprimi-la de trás pra frente.

string = input('Digite uma string: ')

lista = list(string)
lista.reverse()


var = ''.join(lista)

print(var)


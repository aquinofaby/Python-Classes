
#Pedir um numero inteiro
num = int(input("Digite um numero inteiro:"))

#Unidade é o resto do numero digitado dividido por 10
uni = num % 10

#Numero é o numero menos a unidade do valor dividido por 10
num = (num - uni) /10 

#Dezena é encontrada quanto o resto do numero é dividido por 10
dez = num % 10

#Imprimir na tela
print("O dígito das dezenas é", int(dez))

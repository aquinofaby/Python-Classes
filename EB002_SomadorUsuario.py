
#Associar variaveis = input de usuario para A e B 
#Input como comando tras saída do tipo string
#Mudar para tipo Int - só assim é capaz de fazer operações matematicas 

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))

#Associar as variaveis novamente
aux = a
a = b
b = aux

#Imprimir na tela resultados
print(a)
print(b)

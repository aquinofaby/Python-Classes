
#Criar um contador que quebre os segundos inseridos em > HORAS, MINUTOS E SEGUNDOS 

#atrelar a variavel = input de numero
segundos_str = input ("Por favor, entre com o número de segundos que deseja converter: ")

#Atrelando a outra variavel = numero transformando em inteiro 
total_segs = int(segundos_str)

#Converter horas em segundos, dividir por 3600 (equivalente a 1 hora)
horas = total_segs // 3600

#Converter a quant de segundos restantes (restante dos segundos divididos por 3600)
segs_restantes = total_segs % 3600

#Converter minutos (segundos restantes dividido por 60)
minutos = segs_restantes // 60

#dividir os seguntos restantes por 60
segs_restantes_final= segs_restantes % 60

#Operador (simbolo) //  da como resultado o inteiro da divisão 
#Operador (simbolo) % da como resultado o resto da divisão > 13 % 2 ( dentro 13/2 = 12 + 1) > 1

#Imprimir na tela 
print(horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")


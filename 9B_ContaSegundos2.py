#Criar um contador que quebre os segundos inseridos em > HORAS, MINUTOS E SEGUNDOS 
#Atrelar a variavel = input de numero e transformando em inteiro
segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

#Converter segundos em horas, dividir por 86400 (equivalente a 1 dia)
dias = segundos // 86400

#Converter a quant de segundos restantes
segs_restantes = segundos % 86400

#Converter horas em segundos, dividir por 3600 (equivalente a 1 hora)
horas = segs_restantes // 3600
segs_restantes = segs_restantes % 3600

#Converter minutos (segundos restantes dividido por 60)
minutos = segs_restantes // 60

#dividir os seguntos restantes por 60
segs_restantes_final= segs_restantes % 60


#Imprimir na tela 
print(dias, "dias,",horas, "horas, ", minutos, "minutos e", segs_restantes_final, "segundos.")


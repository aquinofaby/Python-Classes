
#Usuario ira fazer input da temperatura
temperaturaFahrenheit = input ("Digite uma temperatura em Fahrenheit: ")

#Float é numero flutuante ex> fraçoes ou numeros com ponto e casas decimais.
temp = float(temperaturaFahrenheit)

#Incluir numa variavel ( Subtrair 32 da Temp Fahrenheit) multiplicar por 5 e dividir por 9 
temperaturaCelsius = (temp - 32) * 5/9

#Imprimir a temperatura.
print ("A temperatura atual é", temperaturaCelsius)


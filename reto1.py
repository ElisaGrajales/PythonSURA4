#Entradas = Variables = Referencias en memoria
nivelAgua = int(input("Digite el nivel de agua: "))

#Proceso

if(nivelAgua >= 0 and nivelAgua <20): 
    print(f'el nivel de agua es: {nivelAgua} y este es bajo')
elif (nivelAgua >= 20 and nivelAgua <400):
    print(f'el nivel de agua es: {nivelAgua} y está operando normalmente')
elif (nivelAgua >= 400):
    print(f'el nivel de agua es: {nivelAgua} y este es alto')
else: 
    print(f'el nivel de agua no es váildo')

#Salida

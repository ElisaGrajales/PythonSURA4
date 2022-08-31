##Entradas
## Ene-feb-mar == invierno
## abril-may-jun == primavera
##jul-agosto-sept
## 

##Establecer un programa donde la entrada sea el mes del año

mes = (input("Digite el mes del año que desea clasifificar: "))
mes = mes.lower()

#Proceso

if(mes == 'enero' or 'febrero' or 'marzo'): 
    print(f'el mes del año es: {mes} y este es invierno')
elif (mes == 'abril' or 'mayo' or 'junio'): 
    print(f'el mes del año es: {mes} y este es primavera')
elif (mes == 'julio' or 'agosto' or 'septiembre'): 
    print(f'el mes del año es: {mes} y este es verano')
elif (mes == 'octubre' or 'noviembre' or 'diciembre'): 
    print(f'el mes del año es: {mes} y este es otoño')
else: 
    print(f'el mes ingresado no es váildo')

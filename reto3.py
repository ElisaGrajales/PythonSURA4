
edad = int(input("Digite la edad: "))

if(edad >= 0 and edad <14): 
    print(f'la edad es: {edad} y es un niño')
elif (edad >= 14 and edad <28):
    print(f'la edad es: {edad} y es un joven')
elif (edad >= 28 and edad <60):
    print(f'la edad es: {edad} y es un adulto')
elif (edad >= 60 and edad <150):
    print(f'la edad es: {edad} y es un adulto mayor')
else: 
    print(f'el rango de edad es inválido')
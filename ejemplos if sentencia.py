#Operadores Relacionales
'''los operadores relacionales en python son
    Operador        Nombre                   Ejemplo            Significado
     <          Menor que                     5<4          5 es menor que 4
     >          Mayor que                     7>4          7 es mayor que 4
     ==         Igual que                     4==4         4 es igual a 4
     !=         No Igual a (Diferente)        4!=5         4 no es igual a 5
     <=         Menor o igual que             6<=6         6 es menor o igual a 6
     >=         Mayor o igual que             9>=5         9 es mayor o igual a 5
     
operadores Logicos 
  
operador logico                 simbolo
conjuncion                        and  
disyuncion                         or
negacion                          not
'''

# Ejemplo de if sentencia con operadores relacionales


pre=int(input("Señor usuario porfabor ingrese su edad: "))
if pre>=18:
    print("Usted es mayor de edad")
print("fin")

x=int(input("Ingrese un numero: "))
if x>10:
    print("El numero esta por encima que diez")
    if x>20:
        print("El numero esta por debajo de 20")
    else: print("Pero no por encima de 20")
print("fin")

#CONTINUACION TEMA EJEMPLOS
print()
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un numero: "))

op=n1+n2
print(op)

if op<=30:
    print("El resultado es menor o igual a 30")
elif op>30:
    print("El resultado es mayor a 30")
else:
    print("Su Numero se paso de lo permitido")
print("fin")

#OTRO EJEMPLO RELACIONADO AL TEMA
print("GENERACIONES DIGITALES")

Generacion_Silenciosa=1920 #debe ser menor a esta fecha
Año_Nacimiento=int(input("Ingrese su año de nacimiento: "))

if Año_Nacimiento>=1964:
    print("Usted pertenece a la Generacion Baby Boomer")
elif Año_Nacimiento>=1979:
    print("Usted pertenece a la Generacion X")
elif Año_Nacimiento>=2000:
    print("Usted pertenece a la Generacion Y")
elif Año_Nacimiento<=2010:
    print("Usted pertenece a la Generacion Z")
else:
    print("El Dato ingresado no es ningun año de nacimiento por lo tanto no esta clasificado")
print("FIN")
    
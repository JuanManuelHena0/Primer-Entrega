#EJERCICIOS CON WHILE,CONDICIONALES Y ESTRUCTURAS.
print("EJERCICIO 1 suma hasta cero")
suma = 0
numero = int(input("Ingrese un numero entero :"))
numero1 = int(input("Ingrese otro numero entero: "))
numero2 = int(input("Ingrese otro numero entero: "))
while numero != 0:
    suma += numero
print("La suma total es:", suma)

print("EJERCICIO 2  contraseña secreta")

contraseña=1223
while True:
    prueba = int(input("Ingres contra "))
    if prueba == contraseña:
        print("Contraseña correcta papacho")
        break
    else:
        print("Contraseña incorrecta")

print("EJERCICIO 3  LISTA DE COMPRAS")
lista=[]
compra1=input("ingrese un producto a la lista(ingrese 'fin' para salir): ")
while True:
    if compra1.lower() == 'fin':
        break
    else:
        lista.append(compra1)
        compra1 = input("ingrese otro producto a la lista(ingrese 'fin' para salir): ")
print("La lista de compras es:", lista)

print("JERCICIO 4 CONTADOR DE PARES E IMPARES")
nu1=int(input("Ingrese el primer numero: "))
nu2=int(input("Ingrese el segundo numero: "))
nu3=int(input("Ingrese el tercer numero: "))
nu4=int(input("Ingrese el cuarto numero: "))
nu5=int(input("Ingrese el quinto numero: "))
nu6=int(input("Ingrese el sexto numero: "))
nu7=int(input("Ingrese el septimo numero: "))
nu8=int(input("Ingrese el octavo numero: "))
nu9=int(input("Ingrese el noveno numero: "))
nu10=int(input("Ingrese el decimo numero: "))
numeros = [nu1, nu2, nu3, nu4, nu5, nu6, nu7, nu8, nu9, nu10]
contador_pares = 0
contador_impares = 0
for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print("Cantidad de numeros pares:", contador_pares)
print("Cantidad de numeros impares:", contador_impares)

print("EJERCICIO 5 PROMEDIO DE  CALIFICACIONES")
calificaciones=[]
calificacion1=input("Ingrese una calificacion de 0 a 5 (ingrese 'salir' para terminar): ")
while  calificacion1.lower() != "salir":
    if calificacion1.lower() == 'salir':
        break
    elif 0 <= int(calificacion1) <= 5:
        calificaciones.append(float(calificacion1))
        calificacion1 = input("Ingrese otra calificacion de 0 a 5 (ingrese 'salir' para terminar): ")
        
    else:
        print("La calificación debe estar entre 0 y 5. Intente de nuevo.")
    
promedio=sum(calificaciones) / len(calificaciones) if calificaciones else 0
print("El promedio de las calificaciones es:", promedio)

print("EJERCICIO 6")

numero_tabla=int(input("Ingrese un numero para ver su tabla de multiplicar: "))
contador=1
while contador <= 10:
    resultado = numero_tabla * contador
    print(f"{numero_tabla}*{contador} = resultado")
#     contador += 1
print("Fin del ejercicio 6")

print("EJERCICIO 7")
secret=int(input("Sr Usuario a continuacion se eligio un numero secreto del 1 al 10 trate de adivinarlo: "))
numero_secreto=7
while secret != numero_secreto:
    if secret not in range(1, 11):
        print("El numero debe estar entre 1 y 10. Intente de nuevo.")
    else:
        print("Numero incorrecto, intente de nuevo.")
    secret = int(input("Ingrese un numero del 1 al 10: "))
print("Felicidades, adivinaste el numero secreto:", numero_secreto)
print("Fin del ejercicio 7")

print("EJERCICIO 8")
tupla_frutas = ("manzana", "banana", "naranja", "uva", "pera")
adiv=input("Sr Usuario a continuacion hay unas series de frutas, trate de adivinar una de ellas: ")
while adiv not in tupla_frutas:
    print("Fruta incorrecta, intente de nuevo.")
    adiv = input("Ingrese una fruta denuevo: ")
print("Felicidades, adivinaste la fruta:", adiv)
print("Fin del ejercicio 8")

print("EJERCICIO 9")
diccionario_español = {
     "uno": "one",
     "dos": "two", 
     "tres": "three",
     "cuatro": "four",
     "cinco": "five"}
ing=input("Sr.Usuario a continucacion ingrese un numero en palabras en español del 1 al 5 para que veas la traduccion")
while ing not in diccionario_español:
    print("El numero ingresado no esta en el rango que se le pidio, intente de nuevo.")
    ing = input("Ingrese un numero en palabras del 1 al 5: ")
print("El numero en inglés es:", diccionario_español[ing])
print("Fin del ejercicio 9")

print("EJERCICIO 10.")
while True:
    print("Menu de operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")    
    opcion = input("seleccione una opcion (1-5): 1.Sumar, 2.Restar, 3.Multiplicar, 4.Dividir, 5.Salir: ")
    
    if opcion == '5':
        print("saliendo del pgrama")
        break
    
    elif opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        
        if opcion == '1':
            resultado = num1 + num2
            print(f"La suma de {num1} y {num2} es: {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"La resta de {num1} y {num2} es: {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"La multiplicacion de {num1} y {num2} es: {resultado}")
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"La divion de {num1} y {num2} es: {resultado}")
            else:
                print("Division entre cero no permitida")
    else:
        print("opcion invalida, intente otra vez")
print("Fin del ejercicio 10")

print("Ejercicio 11")
Nombres_Edades={}
while True:
    nombre = input("Ingrese el nombre del estudiant (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    Nombres_Edades[nombre] = edad
print(Nombres_Edades)
print("Fin del ejercicio 11")

print("Ejercicio 12")
lista_colores = ("zapote", "rosado", "plateado", "amarillo", "verde")
adiv1=input("Sr Usuario a continuacion hay unas series de colores, trate de adivinar una de ellas: ")
while adiv1 not in lista_colores:
    print("color incorrecto, intente de nuevo.")
    adiv1 = input("Ingrese un color de la lista: ")
print("Felicidades, adivinaste el color:", adiv1)
print("Fin del ejercicio 12")

print("Ejercicio 13")
nume=int(input("Sr Usuario a continuacion ingrese un numero para potenciarlo de 1 a 5 :"))
contador1=1
while contador1 <= 5:
    potenci = nume ** contador1
    print(f"{nume} elevado a {contador1} es: {potenci}")
    contador1 += 1
print("Fin del ejercicio 13")

print("Ejercicio 14")
numelo=int(input("Sr Usuario a continuacion ingrese un numero que desea elevar al cuadrado es decir el doble de ese numero:"))
contador2=1
while contador2 <= 2:
    cuadrado = numelo ** contador2
    print(f"{numelo} elevado a {contador2} es: {cuadrado}")
    contador2 += 1
print("Fin del ejercicio 14")

print("Ejercicio 15")
estudiantes_notas = {}
while True:
    nombre_estudiante = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre_estudiante.lower() == 'salir':
        break
    nota_estudiante = float(input(f"Ingrese la nota de {nombre_estudiante} (0-5): "))
    if 0 <= nota_estudiante <= 5:
        estudiantes_notas[nombre_estudiante] = nota_estudiante
    else:
        print("Nota inválida. Debe estar entre 0 y 5.")
print(estudiantes_notas)
print("Fin del ejercicio 15")






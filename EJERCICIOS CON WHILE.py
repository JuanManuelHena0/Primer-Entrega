#EJERCICIOS CON WHILE,CONDICIONALES Y ESTRUCTURAS.
# print("EJERCICIO 1 suma hasta cero")
#pide al usuario  numeros enteros y sumalos hasta que ingrese 0.Luego muestra el total
# suma = 0
# numero = int(input("Ingrese un numero entero :"))
# numero1 = int(input("Ingrese otro numero entero: "))
# numero2 = int(input("Ingrese otro numero entero: "))
# while numero != 0:
#     suma += numero
# print("La suma total es:", suma)

# print("EJERCICIO 2  contraseña secreta")

# contraseña=1223
# while True:
#     prueba = int(input("Ingres contra "))
#     if prueba == contraseña:
#         print("Contraseña correcta papacho")
#         break
#     else:
#         print("Contraseña incorrecta")

# print("EJERCICIO 3  LISTA DE COMPRAS")
# lista=[]
# compra1=input("ingrese un producto a la lista(ingrese 'fin' para salir): ")
# while True:
#     if compra1.lower() == 'fin':
#         break
#     else:
#         lista.append(compra1)
#         compra1 = input("ingrese otro producto a la lista(ingrese 'fin' para salir): ")
# print("La lista de compras es:", lista)

# print("JERCICIO 4 CONTADOR DE PARES E IMPARES")
# nu1=int(input("Ingrese el primer numero: "))
# nu2=int(input("Ingrese el segundo numero: "))
# nu3=int(input("Ingrese el tercer numero: "))
# nu4=int(input("Ingrese el cuarto numero: "))
# nu5=int(input("Ingrese el quinto numero: "))
# nu6=int(input("Ingrese el sexto numero: "))
# nu7=int(input("Ingrese el septimo numero: "))
# nu8=int(input("Ingrese el octavo numero: "))
# nu9=int(input("Ingrese el noveno numero: "))
# nu10=int(input("Ingrese el decimo numero: "))
# numeros = [nu1, nu2, nu3, nu4, nu5, nu6, nu7, nu8, nu9, nu10]
# contador_pares = 0
# contador_impares = 0
# for numero in numeros:
#     if numero % 2 == 0:
#         contador_pares += 1
#     else:
#         contador_impares += 1
# print("Cantidad de numeros pares:", contador_pares)
# print("Cantidad de numeros impares:", contador_impares)

print("EJERCICIO 5 PROMEDIO DE  CALIFICACIONES")
calificaciones=[]
calificacion1=float(input("Ingrese la primera calificacion:('de 0 a 5' ) "))
while True:
    if calificacion1 == 'salir':
        break
    elif calificacion1 <=0 or calificacion1 >5:
        print("Calificación inválida. Debe estar entre 0 y 5.")
        calificacion1 = int(input("Ingrese la primera calificacion:('de 0 a 5'o ingrese salir para finalizar ) "))
    else:
        calificaciones.append(calificacion1)
        calificacion1 = float(input("Ingrese la siguiente calificacion:('de 0 a 5' o ingrese salir para finalizar ) "))
promedio=sum(calificaciones) / len(calificaciones) if calificaciones else 0
print("El promedio de las calificaciones es:", promedio)







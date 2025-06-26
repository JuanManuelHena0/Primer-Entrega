#OLIMPIADAS PRIMERA RONDA EJERCICIO 2 CON  SU RESPECTIVO DIAGRAMA DE FLUJO

print("Numeros en palabras 0-9")
#imprime el nombre del numero (ej: "tres") si esta entre 0 a 9.
Numeros=["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
numero=int(input("Sr.ingrese un numero en palabras del 0 al 9:"))
if 0 <= numero <= 9:
    print(f"Sr.Usuario El numero en palabras es: {Numeros[numero]}")
else:
    print("Sr.Usuario El numero no es valido, por favor ingrese un numero entre 0 y 9")


#EJERCICIO 18 DEL TALLER OLIMPIADAS 2
print("Comparador de letras,pide dos letras y determina:")
# - Si son iguales
# - Si estan en orden alfabético
# - Si una es vocal y la otra consonante
le1 = input("Ingrese la primera letra: ").lower()
le2 = input("Ingrese la segunda letra: ").lower()
print("Señor.Usuario a continuacion se creara una lista de las vocales")
v="aeiou"
if le1 == le2:
    print("Las letras son iguales.")
else:
    print("Las letras son diferentes.")
    if le1 < le2:
        print("Las letras están en orden alfabético.")
    else:
        print("Las letras no están en orden alfabético.")
    vocales1= le1 in v
    vocales2= le2 in v
    if vocales1 and not vocales2:
        print(f"La letra {le1} es una vocal y la letra {le2} es una consonante.")
    elif not vocales1 and vocales2:
        print(f"La letra {le1} es una consonante y la letra {le2} es una vocal.")
    else:
        print("Ambas letras son vocales o ambas son consonantes.")
    





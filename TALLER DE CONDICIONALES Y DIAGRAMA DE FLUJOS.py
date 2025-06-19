# #EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS
# #1. Solicitar un número al usuario y determinar si es positivo, negativo o cero.
nume=int(input("ingrese un numero:"))
if nume>0:
    print("el numero es positivo")
elif nume==0:
    print("el numero es cero")
elif nume<0:
    print("El numero es negativo")
else:
     print("El numero no es valido")
print("fin")
    
# #2.Calcula el mayor de dos numeros ingresados

num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
if num1>num2:
    print("el numero mayor es:", num1)
elif num2<num1:
    print("el numero mayor es:", num2)
    
else:
    print("los numeros son iguales")
print("fin")

# #3.Determina si el numero es par o impar
num3=int(input("ingrese un numero:"))
if num3%2==0:
    print("el numero es par")
elif num3%2!=0:  
    print("el numero es impar")

# #4.Dado un numero verifiva si esta entre 10 y 20
num4=int(input("ingrese un numero:"))
if num4>=10 and num4<=20:
    print("el numero esta entre 10 y 20")
else:
    print("el numero no esta entre 10 y 20")
print("fin")

# #5.Dado tres numeros,encuentra el mayor usando condicionales
num5=int(input("ingrese el primer numero:"))
num6=int(input("ingrese el segundo numero:"))
num7=int(input("ingrese el tercer numero:"))
if num5>num6 and num5>num7:
    print("el numero mayor es:", num5)
elif num6>num5 and num6>num7:
    print("el numero mayor es:", num6)
elif num7>num5 and num7>num6:
    print("el numero mayor es:", num7)
else:
    print("los numeros son iguales")
print("fin")

# #6.Calcula el precio final con un 10% de descuento si el total es mayor a $100.
precio_producto=float(input("ingrese el precio del producto:"))
if precio_producto>100:
    descuento=precio_producto*0.10
    precio_final=precio_producto-descuento
    print("el precio final con descuento es:", precio_final)
print("fin")

# #7.verifica si una persona puede votar (mayor o igual a 18 años)
edad=int(input("ingrese su edad:"))
if edad==18:
    print("puede votar")
elif edad>18:
    print("puede votar")
else:
    print("no puede votar")
print("fin")

#8.Dado el precio y tipo de cliente (VIP,NORMAL),aplica un descuento del 2O% solo a VIP.
precio=float(input("ingrese el precio del producto:"))
tipo=input("ingrese el tipo de cliente:")
if tipo == "vip":
    descuento = precio * 0.20
    precio_final = precio - descuento
    print("El precio final para cliente VIP es:", precio_final)
elif tipo == "normal":
    print("El precio para cliente normal es:", precio)
print("fin")

#9.Determina si un numero es multiplonden5 y 3 al mismo tiempo.

numero1=int(input("ingrese un numero:"))
if numero1%5==0 and numero1%3==0:
    print("el numero es multiplo de 5 y 3")
else:
    print("el numero no es multiplo de 5 y 3")
print("fin")

#10.Dado un numero,verifica si es divisible entre dos o mas datos.

numero2=int(input("ingrese un numero:"))
divisor1=int(input("ingrese el primer divisor:"))
divisor2=int(input("ingrese el segundo divisor:"))
if numero2%divisor1==0 and numero2%divisor2==0:
    print("el numero es divisible entre", divisor1, "y", divisor2)
else:
    print("el numero no es divisible entre", divisor1, "y", divisor2)
print("fin")

# #EJERCICIOS CON LISTAS (con condicionales)

#11.Crea una lista con 5 numeros.Si el tercer numero es mayor que 10,muestra "Mayor a 10",de lo contrario muestra "Menor o igual a 10".
list=[]
list.append=int(input("ingrese el primer numero:"))
list.append=int(input("ingrese el segundo numero:"))
list.append=int(input("ingrese el tercer numero:"))
list.append=int(input("ingrese el cuarto numero:"))
list.append=int(input("ingrese el quinto numero:"))
print(list)
if list[2] > 10:
    print("Mayor a 10")
else:
    print("menor o igual a 10")
print("fin")    

#12.verifica si el numero 7 esta en la lista [3,5,7,9] si esta muestra,muestra "esta en la lista,de lo contrario muestra "No esta en la lista"

listaa=[]
listaa.append=int(input("Ingrese el primer numero"))
listaa.append=int(input("Ingrese el segundo numero"))
listaa.append=int(input("Ingrese el tercer numero"))
listaa.append=int(input("Ingrese el cuarto numero"))
print("Esta en la lista"if 7 in listaa else "No esta en la lista")

#13.Suma los dos primeros elementos de la lista [4,6,2,8].Si la suma es mayor que 10,muestra la suma es alta de lo contrario la suma es baja
list12=[]
list12.append=int(input("Ingrese el primer numero"))
list12.append=int(input("Ingrese el segundo numero"))
list12.append=int(input("Ingrese el tercer numero"))
list12.append=int(input("Ingrese el cuarto numero"))
ope=list12[0]+list12[1]
print("El resultado de la suma es:", ope , "por lo tanto")
if ope > 10:
    print("la suma es alta")
else:
    print("la suma es baja")
print

#14.Dada la lista ("ana","luis","pedro","marta"),muestra el ultimo nombre si ese nombre es "marta",muestra "Nombre correcto"

nombres10=["ana","luis","pedro","marta"]
if nombres10[-1] == "marta":
    print("Nombre correcto")
else:
    print("Nombre incorrecto")
print("fin")

#15.Crea una lista con tres colores.Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
colores=["rojo","azul","verde"]
if colores[1] == "azul":
    colores[1]="amarillo"
print(colores)
print("fin")

#EJERCICIOS CON TUPLAS (CON CONDICIONALES) 

#16.Crea una tupla con los valores (5, 8, 12, 20) si el primer valor es menor que el ultimo,muestra "orden ascendente",de lo contrario muestra "orden descendente".

tupli=(5, 8, 12, 20)
if tupli[0] < tupli[-1]:
    print("orden ascendente")
else:
    print("orden descendente")
print("fin")

#17.Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor que 30,si es asi muestra " edad mayor que 30",de lo contrario muestra "edad menor o igual a 30".

tupla2=(25, 32, 28)
if tupla2[1] > 30:
    print("edad mayor que 30")
else:
    print("edad menor o igual a 30")
print("FIN")

#18.Convierte una tupla (1, 2 , 3)a lista,cmabia el segundo valor a 10 solo si es igual a 2,luego conviertela en tupla y muestrela

tupla3=(1, 2, 3)
lista3=list(tupla3)
if lista3[1] == 2:
    lista3[1] = 10
tupla3=tuple(lista3)
print(tupla3)
print("FIN")

#19.Dada la tupla (4, 9),accede al segundo valor.Si es mayor que 5.Muestra "Coordenada Alta",de lo contrario muestra "Coordenada Baja".

tupla4=(4, 9)
if tupla4[1] > 5:
    print("Coordenada Alta")
else:
    print("Coordenada Baja")
print("FIN")

#20.Compara si las tuplas (3,4) y (3,5) son iguales,si lo son,muestra "tuplas iguales",de lo contrario muestra "tuplas diferentes".
tupla5=(3,4)
tupla6=(3,5)
if tupla5 == tupla6:
    print("tuplas iguales")
else:
    print("tuplas diferentes")
print("FIN")

#EJERCICIOS CON DICCIONARIOS (con condicionales)

#21.Crea un diccionario con ("nombre": "Juan", "edad": 17) si la edad es mayor que 18,muestra "Mayor de edad",de lo contrario muestra "Menor de edad".

diccionary={"nombre": "Juan", "edad": 17}
if diccionary["edad"] > 18:
    print("Mayor de edad")
elif diccionary["edad"] == 18:
    print("Tiene 18 años, es mayor de edad")
else:
    print("Menor de edad")
print("FIN")

#22.Crea un diccionario("nombre": "Lucia", "Edad": 20).Si la edad es mayor a 18,cambia el valor de la "edad" a 21.Luego muestra el diccinario.

Diccio={"nombre": "Lucia", "Edad": 20}
if Diccio["Edad"] > 18:
    Diccio["Edad"] = 21
print("Diccio")
print("FIN")

#23.Crea un diccionario con ("nombre": "Carlos", "edad").Si la clave "ciudad" no existe,agregale con el valor "Bogota" y muestralo en diccionario.

diccionario_numero8000={"nombre": "Carlos", "edad": 20}
if "ciudad" not in diccionario_numero8000:
    diccionario_numero8000["ciudad"] = "Bogota"
print(diccionario_numero8000)
print("FIN")

#24.Dado el diccionario ("producto": "pan", "precio":$1200),verifica si la clave "precio" existe.Si existe,muestra su valor,si no muestra "no hay precio".

diccionario_producto={"producto": "pan", "precio": 1200}
if "precio" in diccionario_producto:
    print("el precio es $1200 por un  de pan")
else:
    print("no hay precio")
print("FIN")

#25.Crea un diccionario con ("pan": 1200,"leche: 2000".  Si "pan"esta en el diccionario,muestra su precio;si no muestra "producto no disponible"
 
diccio_numero7123={"pan": 1200, "leche": 2000}
if "pan" in diccio_numero7123:
    print("el precio del pan es $1200")
else:
    print("producto no disponible")
print("FIN") #el mejor programador

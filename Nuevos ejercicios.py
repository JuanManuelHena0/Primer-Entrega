print("EJEMPLO 1 append")
f=[]
f.append("manzana")
f.append("pera")
f.append("naranja")
print("La lista de frutas",f) 

print("EJEMPLO 2 INSERT")

numeros=[3,8,1,6]
numeros.insert(2,4)
print("despues de insertar el 4 en la posicion 2",numeros)

print("EJEMPLO 3 EXTEND")

numeros=[3,8,1,6]
numeros.extend([4,5,6])
print("despues de extender la lista",numeros)

print("EJEMPLO 4 REMOVE")

numeros=(8,1)
numeros.remove(8)
print("despues de eliminar el 8",numeros)

print("EJEMPLO 5 max")

numeros=[5,2,3,6,9]
maximo=max(numeros)
print("el numero mayor es",maximo)

print("EJEMPLO 6 min")

numeros=[7,1,5,2,3,6,9]
minimo=min(numeros)
print("el numero menor es",minimo)

print("EJEMPLO 7 sort")

numeros=[5,2,1,3,6,9]
numeros.sort()
print("el numero en orden es",numeros)

print("BIENVENIDO Sr.Usuario AL SISTEMA DE CALIFIACION CALIFICAMEYA,PARA INGRESAR NECESITA COMPLETAR UNOS REQUISITOS")
print("EL SISTEMA DE CALIFICACION MANEJA NOTAS COMO LAS SIGUIENTES:")
N1=int(1.0)
N2=int(2.0)
N3=int(3.0)
N4=int(4.0)
N5=int(5.0)
print(N1,"NOTA MUY BAJA",N2,"NOTA BAJA",N3,"NOTA MEDIA",N4,"NOTA ALTA",N5,"NOTA MUY ALTA")
print("Sr.Usuario PARA INGRESAR AL SISTEMA DEBE INGRESAR SU NOMBRE Y APELLIDO")
nombre=input("INGRESE SU NOMBRE")
apellido=input("INGRESE SU APELLIDO")
print("BIENVENIDO SR",nombre,apellido,"A CALIFICAMEYA")
print("Sr.Usuario POR ULTIMO PARA INGRESAR AL SISTEMA DEBE INGRESAR EL NOMBRE DE INSTITUCION Y EL GRUPO EN EL QUE ESTAS:")
print("Sr.Usuario INGRESE EL NOMBRE DE LA INSTITUCION")
institucion=input("INGRESE EL NOMBRE DE LA INSTITUCION")
print("Sr.Usuario INGRESE EL GRUPO AL QUE PERTENECE")
grupo=input("INGRESE EL GRUPO AL QUE PERTENECE")
print("Sr.Usuario BIENVENIDO A CALIFICAMEYA")
print("Sr.Usuario A CONTINUACION INGRESE SU NOTA RESPECTIVA A LAS 5 MATERIAS CUYO NUMERO DE NOTAS SON 3 EN CADA UNA")
materias=int(input("INGRESE LA PRIMERA MATERIA QUE QUIERE SACAR EL PROMEDIO DE NOTAS"))
notad=int(input("INGRESE LA PRIMERA NOTA DE LA MATERIA"))
notad1=int(input("INGRESE LA SEGUNDA NOTA DE LA MATERIA"))
notad2=int(input("INGRESE LA TERCERA NOTA DE LA MATERIA"))
promedio=(notad+notad1+notad2)/3
print("EL PROMEDIO DE LA PRIMERA MATERIA ES:",promedio)
materias1=int(input("INGRESE LA SEGUNDA MATERIA QUE QUIERE SACAR EL PROMEDIO DE NOTAS"))
notad3=int(input("INGRESE LA PRIMERA NOTA DE LA MATERIA"))
notad4=int(input("INGRESE LA SEGUNDA NOTA DE LA MATERIA"))
notad5=int(input("INGRESE LA TERCERA NOTA DE LA MATERIA"))
promedio1=(notad3+notad4+notad5)/3
print("EL PROMEDIO DE LA SEGUNDA MATERIA ES:",promedio1)
materias2=int(input("INGRESE LA TERCERA MATERIA QUE QUIERE SACAR EL PROMEDIO DE NOTAS"))
notad6=int(input("INGRESE LA PRIMERA NOTA DE LA MATERIA"))
notad7=int(input("INGRESE LA SEGUNDA NOTA DE LA MATERIA"))
notad8=int(input("INGRESE LA TERCERA NOTA DE LA MATERIA"))
promedio2=(notad6+notad7+notad8)/3
print("EL PROMEDIO DE LA TERCERA MATERIA ES:",promedio2)
print("Hola Sr.Usuario con el nombre",nombre,apellido,"de la institucion",institucion,"del grupo",grupo,"su promedio de la primera materia es:",materias,promedio,"su promedio de la segunda materia es:",materias1,promedio1,"su promedio de la tercera materia es:",materias2,promedio2)
print("muchas gracias por usar el sistema de calificacion CALIFICAMEYA")

print("EJERCICIO TABLERO")

clientes=["ana," "mario", "juliana", "carlos", "ana", "mario", "lucia", "jose"]

clientes.append("JULIANA")
print("Lista despues de agregar a JULIANA:", clientes)
cantidad=len(clientes)
print("Cantidad de clientes:", cantidad)
menor="El nombre menor es:", min(clientes)
mayor="El nombre mayor es:", max(clientes)
print("El nombre menor alfabeticamente es:", menor)
print("El nombre mayor alfabeticamente es:", mayor)
nombreordenado=sorted(clientes)
remover="Se ha eliminado el nombre de la lista:", clientes.remove("mario")
mayus="El nombre en mayusculas es:", clientes.upper()
indice="El indice de juliana es:", clientes.index("juliana")
print("El nombre en mayusculas es:", mayus)
print("El indice de juliana es:", indice)



numero=[1,2,3,2]
numero.remove(2)
numero.remove(2)
print("Lista de numeros:", numero)

numero1=[1,2,3,2]
numero1[3]=4
numero1.remove(4)
print("Lista de numeros:", numero1)
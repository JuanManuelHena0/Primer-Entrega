print("EJERCICIO TALLER DICCIONARIO,TUPLAS,LISTAS")

producto=input("ingrese el nombre de su producto:")
precio=int(input("ingrese el precio del producto:"))
cantidad=int(input("ingrese la cantidad de productos:"))
tupla=(producto,precio)
lista=[tupla,cantidad]
diccionario1={
    producto:lista,   
}
total=precio*cantidad
print()
print("RESUMEN DE LA COMPRA")
print("nombre del producto:",producto)
print("PRECIO UNITARIO:",precio)
print("CANTIDAD DE PRODUCTOS:",cantidad)
print("TOTAL A PAGAR:",total)
print("gracias por su compra")

print("EJERCICIO TALLER 2 DICCIONARIO,TUPLAS,LISTAS")
nombre1=input("ingrese nombre del primer producto:") 
precio1=int(input("ingrese el precio del producto:"))
cantidad1=int(input("ingrese la cantidad de productos:"))


nombre2=input("ingrese nombre del segundo producto:")
precio2=int(input("ingrese el precio del producto:"))
cantidad2=int(input("ingrese la cantidad de productos:"))

nombre3=input("ingrese nombre del tercer producto:")
precio3=int(input("ingrese el precio del producto:"))
cantidad3=int(input("ingrese la cantidad de productos:"))

producto1=[(nombre1,precio1),cantidad1]
producto2=[(nombre2,precio2),cantidad2]
producto3=[(nombre3,precio3),cantidad3]

print("GUARDADO DICCIONARIO")
diccionario={"producto1":producto1,"producto2":producto2,"producto3":producto3}
print(diccionario)

print("RESUMEN DE LA COMPRA")
print("producto1:",diccionario["producto1"])
print("producto2:",diccionario["producto2"])
print("producto3:",diccionario["producto3"])
print("GRACIAS POR SU COMPRA")

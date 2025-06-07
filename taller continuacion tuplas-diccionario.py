print("TALLER REGISTRO SIMPLE DE PRODUCTO Y CALCULO DE DATOS")
Entrada="Señor Usuario porfavor para continuar ingrese la serie de datos que se le preguntan"
print(Entrada)
Nombre_produc=input("Señor Usuario porfavor proceda a Ingresar el nombre del producto: ")
Precio_Unitario=float(input("Señor Usuario porfavor proceda a Ingresar el precio del producto: "))
Cantidad_Producto=int(input("Señor Usuario porfavor proceda a Ingresar la cantidad del producto: "))

estructura_Tuplistica=(Nombre_produc,
                       Precio_Unitario
)
lista=(estructura_Tuplistica,Cantidad_Producto,)

Diccionario={"Producto:",lista}

Operacion_Total=Precio_Unitario*Cantidad_Producto
print=("El total de la compra es:",Operacion_Total)

print("TALLER #2 FACTURA DE MULTIPLIPLESVPRODUCTOS")

Entrada="Señor Usuario porfavor para continuar ingrese la serie de datos que se le preguntan"
print(Entrada)
Nombre_produc=input("Señor Usuario porfavor proceda a Ingresar el nombre del producto: ")
Precio_Unitario=float(input("Señor Usuario porfavor proceda a Ingresar el precio del producto: "))
Cantidad_Producto=int(input("Señor Usuario porfavor proceda a Ingresar la cantidad del producto: "))

print("PORFAVOR INGRESE EL SEGUNDO PRODUCTO DIFERENTE AL ANTERIOR")

Nombre_produc2=input("Señor Usuario porfavor proceda a Ingresar el nombre del producto: ")
Precio_Unitario2=float(input("Señor Usuario porfavor proceda a Ingresar el precio del producto: "))
Cantidad_Producto2=int(input("Señor Usuario porfavor proceda a Ingresar la cantidad del producto: "))

print("PORFAVOR INGRESE EL TERCER PRODUCTO DIFERENTE AL ANTERIOR")

Nombre_produc3=input("Señor Usuario porfavor proceda a Ingresar el nombre del producto: ")
Precio_Unitario3=float(input("Señor Usuario porfavor proceda a Ingresar el precio del producto: "))
Cantidad_Producto3=int(input("Señor Usuario porfavor proceda a Ingresar la cantidad del producto: "))

tupla_producto1 = [(Nombre_produc,Precio_Unitario)]
tupla_producto2 = [(Nombre_produc2,Precio_Unitario2)]
tupla_producto3 = [(Nombre_produc3,Precio_Unitario3)]

list = ([tupla_producto1 , Cantidad_Producto])
list2 = ([tupla_producto2, Cantidad_Producto2])
list3 = ([tupla_producto3,Cantidad_Producto3])

factura={"Producto1:", list,
         "Producto2:",list2,
         "Producto3:",list3
         }
total_De_Cada_Producto1=Precio_Unitario*Cantidad_Producto
total_De_Cada_Producto2=Precio_Unitario2*Cantidad_Producto2
total_De_Cada_Producto3=Precio_Unitario3*Cantidad_Producto3







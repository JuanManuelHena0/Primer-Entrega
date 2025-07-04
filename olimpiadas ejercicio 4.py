#**************INICIO DEL PROGRAMA****************
#Se dara las listas iniciales
print("productos = [Manzana , Banano ,Pera]")
#Para seguir con la programacion debida ingresar los productos en el orden correcto

pro1=input("Sr.Usuario ingrese el nombre del primer producto:")
pro2=input("Sr.Usuario ingrese el nombre del segundo producto:")
pro3=input("Sr.Usuario ingrese el nombre del tercer producto:")
productos = [pro1, pro2, pro3]
if "Pera" in productos:
    print("Sr.Usuario la pera esta en la lista de productos por lo tanto se agregara mango a la lista")
    productos.append("Mango")

#Como Pera esta en la lista de productos, se agregara Mango a la lista de productos

print("---------------------------------------------------------------------------------------")

print("precios = [1500, 1000, 1800] ")

#Para seguir con la programacion debida ingresar los precio en el orden correcto
pre1=int(input("Sr.Usuario ingrese el precio del primer producto:"))
pre2=int(input("Sr.Usuario ingrese el precio del segundo producto:"))
pre3=int(input("Sr.Usuario ingrese el precio del tercer producto:"))
precios = [pre1, pre2, pre3]
#Como 1800 esta en la lista de precios, se agregara el precio 2000 a la lista de precios
if 1800 in precios:
    print("Sr.Usuario el precio 1800 esta en la lista de precios por lo tanto se agregara el precio 2000 a la lista")
    precios.append(2000)
print("Se han ingresado los productos y precios correctamente.")

print("---------------------------------------------------------------------------------------")

#Al tener la variable banano en la lista de productos, se eliminara de la lista
if "Banano" in productos:
    print("Sr.Usuario el producto Banano esta en la lista de productos se eliminara de la lista")
    productos.remove("Banano")
print("Se ha eliminado el producto Banano de la lista de productos.")
#ahora s epone la lista actualizada de productos con el precio actualizado
print("Lista de productos actualizada:", productos)
print("Lista de precios actualizada:", precios)
print("---------------------------------------------------------------------------------------")

#Se elimina el primer elemento de la lista productos si esta tiene 4 elementos

if len(productos) == 4:
    print("la lista de productos tiene 4 elementos por lo tanto se eliminara el primero")
    productos.pop(0)
elif len(productos) < 4:
    print("La lista de productos no tiene 4 elementos, por lo tanto no se eliminara el primer elemento")
print("Lista de productos despues de la posible eliminacion:", productos)


print("---------------------------------------------------------------------------------------")

#Se reemplaza el precio 1500 por 1600 si este existe en la lista de precios

if 1500 in precios:
    print("El precio 1500 esta en precios por lo tanto se remplazara por 1600")
    precios.remove(1500)
    precios.append(1600)
    print("Se ha reemplazado el precio 1500 por 1600.")
print("Lista de precios despues del posible reemplazo:", precios)

print("---------------------------------------------------------------------------------------")


#Se crea una lista llamada oferta que contiene los dos primeros productos de la lista productos
oferta = productos[:2]
print("Se ha creado la lista oferta con los dos primeros productos:", oferta)

print("---------------------------------------------------------------------------------------")


#Crea una lista llamada altos_precios que contiene los dos ultimos precios de la lista precios
altos_precios = precios[-2:]
print("Se ha creado la lista altos_precios con los dos ultimos precios:", altos_precios)

print("---------------------------------------------------------------------------------------")

#Al mango estar en las lista de productos, se crea una tupla con el nombre mango y el precio 2000
if "Mango" in productos:
    tupla_mango = ("Mango", 2000)
    print("Se ha creado la tupla:", tupla_mango)

print("---------------------------------------------------------------------------------------")

#Manzana esta en oferta, se agrega "descuento" a la lista oferta
if "Manzana" in oferta:
    oferta.append("descuento")
    print("Se ha agregado 'descuento' a la lista oferta:", oferta)
    
print("---------------------------------------------------------------------------------------")


#"descuento" esta en oferta,se crea un diccionario llamado informe con las claves:
#  "producto": "Manzana")
#   "precio_original": 1600
#   "descuento": True
print("Se verificara si 'descuento' esta en oferta para crear el diccionario informe.")
if "descuento" in oferta:
    informe = {
        "producto": "Manzana",
        "precio_original": 1600,
        "descuento": True
    }
    print("Se ha creado el diccionario informe:", informe)
    
print("---------------------------------------------------------------------------------------")


#Como el diccionario informe fue creado, se añade la clave "vigencia" con el valor "30 dias"
if "informe" in locals():
    informe["vigencia"] = "30 dias"
    print("Se ha añadido la clave 'vigencia' al diccionario informe:", informe)
    
print("---------------------------------------------------------------------------------------")


#como hay mas de 3 elementos en precios, se elimina el ultimo elemento de precios
if len(precios) > 3:
    precios.pop()
    print("Se ha eliminado el ultimo elemento de precios:", precios)
    
print("---------------------------------------------------------------------------------------")

#Piña no esta en productos, se agrega a la lista de productos
if "Piña" not in productos:
    productos.append("Piña")
    print("Se ha agregado 'Piña' a la lista de productos:", productos)
    
print("---------------------------------------------------------------------------------------")



#se imprimira las listas,cualquier tupla y el diccionario informe si fue creado
print("Lista de productos:", productos)
print("Lista de precios:", precios)
print("Lista de oferta:", oferta)
print("Lista de altos precios:", altos_precios)
if "informe" in locals():
    print("Diccionario informe:", informe)

#******************FIN DEL PROGRAMA****************
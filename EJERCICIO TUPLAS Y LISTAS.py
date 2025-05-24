N1= int(input("Ingrese el primer numero"))
N2= int(input("Ingrese el segudno numero"))
N3= int(input("Ingrese el tercer numero"))
N4= int(input("Ingrese el cuarto numero"))
N5= int(input("Ingrese el quinto numero"))
N6= int(input("Ingrese el sexto numero"))
N7= int(input("Ingrese el septimo numero"))
N8= int(input("Ingrese el octavo numero"))
N9= int(input("Ingrese el noveno numero"))
N10= int(input("Ingrese el decimo numero")) 
numeros=[N1,N2,N3,N4,N5,N6,N7,N8,N9,N10]
tuplas1=(N1,N1**2)
tuplas2=(N2,N2**2)
tuplas3=(N3,N3**2)
tuplas4=(N4,N4**2)
tuplas5=(N5,N5**2)
tuplas6=(N6,N6**2)
tuplas7=(N7,N7**2)
tuplas8=(N8,N8**2)
tuplas9=(N9,N9**2)
tuplas10=(N10,N10**2)
suma=N1+N2+N3+N4+N5+N6+N7+N8+N9+N10
promedio=suma/10
doble=suma*2
mitad_promedio=promedio/2
Operaciones_diversas=[
N1+N2,
N3-N4,
N5*N2,
N7**2,
N8%3,
N10//2,
N5-N1,
]
print("lista de numeros:",numeros)
print("Tuplas(numeros,cuadrado):",tuplas1,tuplas2,tuplas3,tuplas4,tuplas5,tuplas6,tuplas7,tuplas8,tuplas9,tuplas10)
print("Suma de todos los numeros:",suma)
print("Promedio de todos los numeros:",promedio)
print("Doble de la suma de todos los numeros:",doble)
print("Mitad del promedio de todos los numeros:",mitad_promedio)
print("Operaciones diversas:",Operaciones_diversas)



# ActividadAvanzada2
#Lista

Compras = ["Leche", "Arroz", "Aceite", "Lentejas"]
#Paso 1
Compras.append("Zumo")
Compras.append("Galletas")
#Paso 2
print(Compras)
#Paso 3
print(Compras[1:3])
#Paso 4
print(Compras[4:6])
#Paso 5
Compras[4]= "ZUMO DE NARANJA"
#Paso 6
Compras.pop()
# #Paso 7
Compras.append("Limones")
Compras.append("Naranjas")
Compras.append("Macarrones")
Compras.append("Café")
Compras.append("Pipas")
Compras.append("Colacao")
#Paso 8
Compras.sort() 

#Tuple

 #Paso 1
Estaciones=("Primavera","Verano","Otoño","Invierno")
print(Estaciones[1:2])
#Paso 2
print(Estaciones)

#Actividad avanzada
nombres = ["Arturo","Julio","Dani"]
for i in nombres:
    Estudiantes= input(f"Ha venido {i} a clase? y/n")
Readme cambio
segundo cambio
name = input("¿Cual es tu nombre?")
print(f"Tu nombre es {name}")
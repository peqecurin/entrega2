#10) Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:

nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David','Diego', 
           'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 'FEDERICO', 'Fernanda',
           'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' ,
           'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 
            'Matias',  'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina']


#nombres_lista = nombres.split()    --> Modifiqué directamente la lista
#print(nombres_lista)
cant_alumnos = len(nombres)    #--> Identifico cuantos alumnos hay
#print(cant_alumnos)

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#________________________________________________________________________________________
           
#A, B, C) Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. 
#Utilizar esta estructura para la resolución de los siguientes items.
#B) Calcular el promedio de notas de cada estudiante.
#C) Calcular el promedio general del curso.

lista = list(zip(nombres, notas_1, notas_2))  #Zipeo para q me junten las listas --> OBtengo una lista de tupls
#print (lista)

prom_total = 0         #Doy el primer valor al promedio total ara q vaya sumandolo en la iteración
dic_listas = {}        #Creo un dicccionario para tener los datos juntos
promedios = []         #Creo una lista para guardar los promedios d cada alumno

print("Los promedios de los alumnos:")
for nombre, nota_1, nota_2 in lista:
    dic_listas[nombre] = [nota_1, nota_2] 

    prom = (nota_1 + nota_2)/2                   #Calculo el promedio de notas de cada estudiante
    promedios.append((nota_1 + nota_2)/2)        #Agrego dicho promedio a una lista para usarla luego
    
    print(f"Alumno: {nombre}, Promedio: {prom}")

    prom_total = prom_total + prom       

#Para obtener el promedio del curso, sumo los promedios y los dividio por la cantidad de alumnos
prom_total = prom_total/cant_alumnos
print(f"El promedio total del curso es: {prom_total}")

#print(dic_listas)    #Chequeo que el diccionario funcione

#________________________________________________________________________________________

#D) Identificar al estudiante con la nota promedio más alta.
#E) Identificar al estudiante con la nota más baja.
#Voy a buscar el mayor/menor promedio usando las funciones max y min.

mayor_prom = max(promedios)
menor_prom = min(promedios)

for elem in promedios:
    if elem == mayor_prom:
        indice_mayor = promedios.index(elem)
        print(f"El alumno con mayor promedio es {nombres[indice_mayor]} con un promedio de {mayor_prom}")
    elif elem == menor_prom:
        indice_menor = promedios.index(elem)
        print(f"El alumno con menor promedio es {nombres[indice_menor]} con un promedio de {menor_prom}")

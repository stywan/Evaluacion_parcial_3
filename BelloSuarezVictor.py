Lista_Curso = []
import csv  
#1Procesar lista de estudiantes
def Procesar_lista_estudiantes():
    with open('listaCurso5B.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for x in lector_csv:
            Lista_Curso.append(archivo_csv)
            print(x)
        

#2 Registrar estudiante
def Registrar_estudiantes():
    RUT = input(str("Ingresa el rut: "))
    NOMBRE = input("Ingresa el nombre: ")
    NOTA_1 = float(input("Ingrese la nota 1: "))
    NOTA_2 = float(input("Ingrese la nota 2: "))
   
    estudiantes = {
        "rut": RUT ,
        "nombre":NOMBRE,
        "not_1":NOTA_1,
        "nota_2":NOTA_2,
       
    }
    Lista_Curso.append(estudiantes)
    print(f"Estudiante {NOMBRE} fue registrado con exito.")  
    print(Lista_Curso)


#3 Modificar nota
def Modificar_nota():
    modificar = input("Ingresa el Rut del estudiante: ")
    for estudiante in Lista_Curso:
        pass








#4 Eliminar estudiante
def Eliminar_estudiantes():
    eliminar = input("Ingrese el Rut del estudiantes: ")
    pass
        







#5 Generar promedio de notas
def Generar_promedio_notas():
    pass








#6 Generar acta de cierre de curso
def Generar_acta_cierre_notas():
    with open("Acta_cierre_5B.csv", "w", newline='', encoding='UTF-8') as archivo_csv:
        pass








def Salir_programa():
    print("Saliendo del programa...")
    
#Funcion principal
def Funcion_principal():
    opciones = {
        "1": Procesar_lista_estudiantes,
        "2": Registrar_estudiantes,
        "3": Modificar_nota,
        "4": Eliminar_estudiantes,
        "5": Generar_promedio_notas,
        "6": Generar_acta_cierre_notas,
    }
    while True:
        opcion = input("\n   Menu \n1. Procesar lista de estudiantes \n2. Registrar estudiante \n3. Modificar nota. \n4. Eliminar estudiante. \n5. Generar promedio de notas. \n6. Generar acta de cierre de curso. \n7. Salir del programa \nSelecciona una opcion: ")
        if opcion == "7":
            Salir_programa()
            break
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opcion no valida, intente nuevamente.")
    pass
Funcion_principal()



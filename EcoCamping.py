print("Gestion de Eco-Camping 'Bosque Vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENU DE CONTROL DE REGISTROS===")
    print("1.- ver sitios disponibles")
    print("2.- Registro de nuevos vehiculos en el sitio(Entrada)")
    print("3.- Registro de salida de vehiculos(Salida)")
    print("4.- Estado actual del camping")
    print("5.- Salir")
    try:
        opcion = int(input("seleccione una opcion (1-5):   "))
    except ValueError:
        print("Opcion no valida, seleccione una opcion entre 1 y 5") 
        continue 
    #Despliegue de opciones
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] sitios libres para recibir vehiculos:  {disponibles}")
    else:
        print("opcion fuera de rango") 
          
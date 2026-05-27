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
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if sitios_libres == 0:
            print("lo sentimos, no quedan espacios en el camping")
        else:
            try:
                ingreso = int(input("¿Cuantos sitios o vehiculos van a ingresar?"))
                if ingreso <= 0:
                    print("Error: la cantidad de ingresos debe ser mayor a 0") 
                elif ingreso > sitios_libres:
                    print(f"solo pueden ingresar un maximo de {sitios_libres} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                    print("Error: Debe ingresar un numero valido")
    else:
        print("opcion fuera de rango") 

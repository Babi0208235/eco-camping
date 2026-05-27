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
    elif opcion == 3:
        print(f"\n-- Registrar (vehiculos o sitios ocupados:  {sitios_ocupados})")
        if sitios_ocupados == 0:
            print("no hay vehiculos registrados en el camping actualmente")
        else:
            try: 
                salida = int(input("¿Cuantos vehiculos se retiran?:   "))
                if salida <= 0:
                    print(f"Error: la cantidad a retirar debe ser mayor a 0 ")
                elif salida > sitios_ocupados:
                    print(f"Error: no se pueden retirar mas de {sitios_ocupados} vehiculos")
                else:
                    sitios_ocupados -= salida 
                    print(f" salida registrada, se han liberado {salida} vehiculos")
            except ValueError:
                print("Error: debe ingresar un numero entero valido")
    elif opcion == 4:
        porcentaje_ocupacion = (sitios_ocupados / capacidad_maxima) * 100
        print(f"\n[ESTADO] ocupacion actual:  {sitios_ocupados}/{capacidad_maxima} sitios")
        print(f"[ESTADO] El camping esta al {porcentaje_ocupacion:.1f}% de su capacidad")
    elif opcion == 5:
        print("cerrando el sistema")
        ejecutando = False 
    else:
        print("opcion fuera de rango")
        

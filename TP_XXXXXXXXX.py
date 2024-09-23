##########################
######     MENU     ######
##########################

def mostrar_menu(inventario):
    while True:
        print("  MENU DE OPCIONES")
        print("====================")
        print("(1) Inventario")
        print("(2) Reportes")
        print("(3) Salir")
        print("====================")
        try:
            opcion = int(input("Opción: "))
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número.\n")
            continue

        if opcion == 1:
            print("\n==================================================================================================")
            print("\t\t\t\t   LISTA DE LIBROS DISPONIBLES")
            print("--------------------------------------------------------------------------------------------------")
            print(f"{'Código':<9} {'Título':<29} {'Autor':<22} {'Año':<7} {'Género':<16} {'Cantidad':<8}")
            print("--------------------------------------------------------------------------------------------------")
            for valor in inventario.values():
                print(f"{valor['Código']:<9} {valor['Titulo']:<29} {valor['Autor']:<22} {valor['Año']:<7} {valor['Género']:<16} {valor['Cantidad']:<8}")
            while True:
                print("==================================================================================================")
                print("1 -> Registrar nuevo libro")
                print("2 -> Eliminar un libro")
                print("3 -> Actualizar los datos del libro")
                print("4 -> Listar todos los libros")
                print("5 -> Buscar libros")
                print("0 -> Regresar al menu")
                print("==================================================================================================")
                try:
                    accion = int(input("Ingrese su opción: "))
                except ValueError:
                    print("Opción no válida. Por favor, ingrese un número.\n")
                    continue

                if accion == 1:
                    Registrar_Libro(inventario)
                elif accion == 2:
                    Eliminar_Libro(inventario)
                elif accion == 3:
                    Actualizar_Libro(inventario)
                elif accion == 4:
                    Listar_Libro(inventario)
                elif accion == 5:
                    Buscar_Libro(inventario)
                elif accion == 0:
                    print("")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.\n")

        elif opcion == 2:
            reportes(inventario)

        elif opcion == 3:
            print("\nSaliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.\n")

##########################
######   OPCIONES   ######
##########################

def Registrar_Libro(inventario):
    print("==================================================================================================")
    codigo = sorted(inventario.keys())[-1] + 1 #Una vez ordenado las claves, el -1 toma el ultimo elemento y le aumenta en 1
    titulo = input("\nIngrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")

    while True:
        try:
            año = int(input("Ingrese el año de publicación: "))
            break
        except ValueError:
            print("Año no válido. Por favor, ingrese un número.")

    genero = input("Ingrese el género del libro: ")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Cantidad no válida. Por favor, ingrese un número.")
    
    inventario[codigo] = {"Código": codigo, "Titulo": titulo, "Autor": autor, "Año": año, "Género": genero, "Cantidad": cantidad}
    print("Libro registrado exitosamente.\n") #Se asignan los valores al nuevo libro con la variable "codigo" como numero de libro

def Eliminar_Libro(inventario):
    print("==================================================================================================")
    
    while True:
        try:
            codigo = int(input("\nIngrese el código del libro a eliminar: "))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")
    
    libro_eliminado = inventario.pop(codigo, None) #None es valor opcional
    
    if libro_eliminado is not None:
        print("Libro eliminado exitosamente.\n")
    else:
        print("Código no encontrado.\n")

def Actualizar_Libro(inventario):
    print("==================================================================================================")
    
    while True:
        try:
            codigo = int(input("\nIngrese el código del libro a actualizar: "))
            break
        except ValueError:
            print("Código no válido. Por favor, ingrese un número.")

    if codigo in inventario:
        print("Ingrese los nuevos datos (deje vacío para no cambiar)")
        titulo = input(f"Título ({inventario[codigo]['Titulo']}): ") or inventario[codigo]['Titulo'] 
        autor = input(f"Autor ({inventario[codigo]['Autor']}): ") or inventario[codigo]['Autor']
        año = input(f"Año ({inventario[codigo]['Año']}): ") or inventario[codigo]['Año']
        genero = input(f"Género ({inventario[codigo]['Género']}): ") or inventario[codigo]['Género']
        
        while True:
            cantidad_input = input(f"Cantidad ({inventario[codigo]['Cantidad']}): ")
            if cantidad_input == "":
                cantidad = inventario[codigo]['Cantidad'] #Mantener la cantidad existente
                break
            try:
                cantidad = int(cantidad_input) #Convertir a entero
                break
            except ValueError:
                print("Cantidad no válida. Por favor, ingrese un número.")

        inventario[codigo].update({
            "Titulo": titulo,
            "Autor": autor,
            "Año": año,
            "Género": genero,
            "Cantidad": cantidad
        })
        print("Libro actualizado exitosamente.\n")
    else:
        print("Código no encontrado.\n")

def Listar_Libro(inventario):
        print(" ")
        print(f"{'Código':<9} {'Título':<29} {'Autor':<22} {'Año':<7} {'Género':<16} {'Cantidad':<8}")
        print("--------------------------------------------------------------------------------------------------")
        
        for valor in inventario.values():
            print(f"{valor['Código']:<9} {valor['Titulo']:<29} {valor['Autor']:<22} {valor['Año']:<7} {valor['Género']:<16} {valor['Cantidad']:<8}")

        print(" ")

def Buscar_Libro(inventario):
    print("==================================================================================================")
    print("\nBUSCAR LIBRO POR:")
    print("-------------------------")
    print("(1) Título")
    print("(2) Autor")
    print("(3) Género")
    print("=========================")

    while True:
        try:
            busqueda = int(input("Seleccione una opción: "))
            break
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número.")
    
    if busqueda == 1:  #Buscar libro por título
        print("=========================")
        Disponibles_1 = {valor['Titulo'] for valor in inventario.values()}
        print("\nSeleccione un título disponible:")
        print("--------------------------------------")
        for titulo in Disponibles_1:
            print(titulo)
        print("======================================")
        busqueda_titulo = input("Ingrese el título del libro: ")
        resultados = []
        for libro in inventario.values():
            if libro['Titulo'].lower() == busqueda_titulo.lower():
                resultados.append(libro)

    elif busqueda == 2:  #Buscar libro por autor
        print("=========================")
        Disponibles_2 = {valor['Autor'] for valor in inventario.values()}
        print("\nSeleccione un autor disponible:")
        print("--------------------------------------")
        for autor in Disponibles_2:
            print(autor)
        print("======================================")
        busqueda_autor = input("Ingrese el autor del libro: ")
        resultados = []
        for libro in inventario.values():
            if libro['Autor'].lower() == busqueda_autor.lower():
                resultados.append(libro)

    elif busqueda == 3:  #Buscar libro por género
        print("=========================")
        Disponibles_3 = {valor['Género'] for valor in inventario.values()}
        print("\nSeleccione un genero disponible:")
        print("--------------------------------------")
        for genero in Disponibles_3:
            print(genero)
        print("======================================")
        busqueda_genero = input("Ingrese el género del libro: ")
        resultados = []
        for libro in inventario.values():
            if libro['Género'].lower() == busqueda_genero.lower():
                resultados.append(libro)

    else:
        print("Opción no válida.\n")
        return

    if resultados:
        print("\nLibros encontrados:")
        for libro in resultados:
            print(f"{libro['Código']}: {libro['Titulo']} por {libro['Autor']}, Año: {libro['Año']}, Género: {libro['Género']}, Cantidad: {libro['Cantidad']}")
        print("")
    else:
        print("No se encontraron libros con esa búsqueda.\n")

##########################
######   REPORTES   ######
##########################

def reportes(inventario):
    while True:
        print("\n==================================================================================================")
        print("1 -> Ver total de libros en inventario")
        print("2 -> Ver cantidad de libros por género")
        print("3 -> Ver autor con más libros en inventario")
        print("0 -> Regresar al menú")
        print("==================================================================================================")
        
        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número.")
            continue

        if opcion == 1: #Ver total de libros en el inventario
            total_libros = 0
            for libro in inventario.values():
                total_libros += libro['Cantidad']
            print(f"\nTotal de libros en inventario: {total_libros}")
            
            
        elif opcion == 2:  #Ver la cantidad de libros por género
            generos = {}
            for libro in inventario.values():
                genero = libro['Género']
                cantidad = libro['Cantidad']
                if genero in generos:
                    generos[genero] += cantidad #Se le suma a un genero ya registrado
                else:
                    generos[genero] = cantidad #Se registra nuevo genero
                    
            print("\nCantidad de libros por género:")
            for genero, cantidad in generos.items():
                print(f"{genero}: {cantidad}")

        elif opcion == 3: #Ver autor con mas libros en el inventario
            autores = {}
            for libro in inventario.values():
                autores[libro['Autor']] = autores.get(libro['Autor'], 0) + libro['Cantidad']
            
            autor_maslibros = None
            max_libros = 0

            for autor, cantidad in autores.items():
                if cantidad > max_libros:
                    max_libros = cantidad
                    autor_maslibros = autor

            if autor_maslibros:
                print(f"\nEl autor con más libros en el inventario es: {autor_maslibros} con {max_libros} libros")
            else:
                print("No hay autores en el inventario.\n")

        elif opcion == 0:
            print("")
            mostrar_menu(inventario)
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

##########################
######  INVENTARIO  ######
##########################

inventario = {
    1: {"Código": 1, "Titulo": "Matemática Discreta", "Autor": "Perez Rimualdo", "Año": 2021, "Género": "Informatica", "Cantidad": 3},
    2: {"Código": 2, "Titulo": "Los perros hambrientos", "Autor": "Ciro Alegria", "Año": 1970, "Género": "Literatura", "Cantidad": 10},
    3: {"Código": 3, "Titulo": "Drácula", "Autor": "Bram Stoker", "Año": 1970, "Género": "Literatura", "Cantidad": 4},
    4: {"Código": 4, "Titulo": "Java", "Autor": "Victor Balta", "Año": 2009, "Género": "Informatica", "Cantidad": 2},
}

mostrar_menu(inventario)
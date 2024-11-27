import csv
import os

# Nombre del archivo CSV
archivo_csv = "productos.csv"

# Variable para almacenar el criterio de ordenamiento global
criterio_ordenamiento = "5"  # Sin orden específico por defecto

# Función para inicializar el archivo CSV si no existe
def inicializar_csv():
    try:
        with open(archivo_csv, mode='x', newline='') as file:
            writer = csv.writer(file)
            # Escribe la cabecera
            writer.writerow(["ID", "Nombre", "Precio", "Cantidad"])
    except FileExistsError:
        pass  # Si el archivo ya existe, no hace nada

# Función para agregar un producto al archivo CSV
def agregar_producto(id, nombre, precio, cantidad):
    with open(archivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nombre, precio, cantidad])
    print("Producto agregado exitosamente.")

# Función para seleccionar criterio de ordenamiento
def seleccionar_ordenamiento():
    print("\n--- Seleccionar criterio de ordenamiento ---")
    print("1. Ordenar por ID (de menor a mayor)")
    print("2. Ordenar por Nombre (alfabéticamente)")
    print("3. Ordenar por Precio (de menor a mayor)")
    print("4. Ordenar por Cantidad de stock (de menor a mayor)")
    print("5. Sin orden específico")
    opcion = input("Elige una opción: ")
    global criterio_ordenamiento
    if opcion in ["1", "2", "3", "4", "5"]:
        criterio_ordenamiento = opcion
        print("Criterio de ordenamiento actualizado.")
    else:
        print("Opción inválida. El criterio no ha sido cambiado.")

# Función para listar productos
def listar_productos():
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            productos = list(reader)  # Convierte el contenido a una lista

            if len(productos) < 2:  # Si solo tiene encabezado o está vacío
                print("No hay productos para mostrar.")
                return

            # Ordenar según el criterio guardado
            global criterio_ordenamiento
            if criterio_ordenamiento == "1":
                productos = [productos[0]] + sorted(productos[1:], key=lambda x: int(x[0]))  # Ordena por ID
            elif criterio_ordenamiento == "2":
                productos = [productos[0]] + sorted(productos[1:], key=lambda x: x[1].lower())  # Ordena por Nombre
            elif criterio_ordenamiento == "3":
                productos = [productos[0]] + sorted(productos[1:], key=lambda x: float(x[2]))  # Ordena por Precio
            elif criterio_ordenamiento == "4":
                productos = [productos[0]] + sorted(productos[1:], key=lambda x: int(x[3]))  # Ordena por Cantidad

            # Mostrar encabezados y productos en formato tabla
            encabezados = productos[0]
            print("\nLista de productos:")
            print("-" * 60)
            print(f"{encabezados[0]:<10} | {encabezados[1]:<20} | {encabezados[2]:<10} | {encabezados[3]:<10}")
            print("-" * 60)
            for row in productos[1:]:
                print(f"{row[0]:<10} | {row[1]:<20} | {row[2]:<10} | {row[3]:<10}")
            print("-" * 60)

    except FileNotFoundError:
        print("El archivo no existe. Por favor, inicializa el sistema.")

# Función para buscar un producto por ID
def buscar_producto(id):
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            productos = list(reader)  # Convierte todo el contenido en una lista

            if len(productos) < 2:  # Si solo tiene encabezado o está vacío
                print("No hay productos en la base de datos.")
                return

            # Encabezados de la tabla
            encabezados = productos[0]

            # Buscar el producto
            for row in productos[1:]:
                if row[0] == id:
                    # Mostrar encabezados y producto encontrado
                    print("\nProducto encontrado:")
                    print("-" * 60)
                    print(f"{encabezados[0]:<10} | {encabezados[1]:<20} | {encabezados[2]:<10} | {encabezados[3]:<10}")
                    print("-" * 60)
                    print(f"{row[0]:<10} | {row[1]:<20} | {row[2]:<10} | {row[3]:<10}")
                    print("-" * 60)
                    return
            
            print(f"No se encontró un producto con ID {id}.")
    except FileNotFoundError:
        print("El archivo no existe. Por favor, inicializa el sistema.")

# Función para modificar un producto
def modificar_producto(id):
    try:
        productos = []
        modificado = False
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    print("Producto encontrado:", row)
                    nombre = input("Nuevo nombre (deja vacío para no cambiar): ") or row[1]
                    precio = input("Nuevo precio (deja vacío para no cambiar): ") or row[2]
                    cantidad = input("Nueva cantidad (deja vacío para no cambiar): ") or row[3]
                    productos.append([id, nombre, precio, cantidad])
                    modificado = True
                else:
                    productos.append(row)

        if modificado:
            with open(archivo_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(productos)
            print("Producto modificado exitosamente.")
        else:
            print("Producto con ID", id, "no encontrado.")

    except FileNotFoundError:
        print("El archivo no existe. Por favor, inicializa el sistema.")

# Función para eliminar un producto
def eliminar_producto(id):
    try:
        productos = []
        eliminado = False
        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == id:
                    eliminado = True
                else:
                    productos.append(row)

        if eliminado:
            with open(archivo_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(productos)
            print("Producto eliminado exitosamente.")
        else:
            print("Producto con ID", id, "no encontrado.")

    except FileNotFoundError:
        print("El archivo no existe. Por favor, inicializa el sistema.")

# Menú principal
def menu():
    inicializar_csv()
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto")
        print("2. Buscar producto por ID")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Ordenar listado")
        print("6. Listado de productos")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            precio = input("Ingresa el precio del producto: ")
            cantidad = input("Ingresa la cantidad del producto: ")
            agregar_producto(id, nombre, precio, cantidad)
        elif opcion == "2":
            id = input("Ingresa el ID del producto a buscar: ")
            producto = buscar_producto(id)
        elif opcion == "3":
            id = input("Ingresa el ID del producto a modificar: ")
            modificar_producto(id)
        elif opcion == "4":
            id = input("Ingresa el ID del producto a eliminar: ")
            eliminar_producto(id)
        elif opcion == "5":
            seleccionar_ordenamiento()
        elif opcion == "6":
            listar_productos()
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()

nombreDelArticulo = ""
descripcionDelArticulo = ""
codigoDeBarras = ""
categoriaDelArticulo = ""
precioDelArticulo = 0.0
cantidadEnStock = 0
sucursal = ""

print("Bienvenido al sistema de inventario de artículos")
print("-------------INVENTARIO DE ARTÍCULOS-------------")
print("1. Agregar un nuevo artículo")
print("2. Mostrar artículos")
print("3. Buscar artículo")
print("4. Actualizar artículo")
print("5. Eliminar artículo")
print("6. Salir")
print("-------------------------------------------------")
opcion = int(input("Seleccione una opción: "))

match opcion:
    case 1:
        nombreDelArticulo = input("Ingrese el nombre del artículo: ")
        descripcionDelArticulo = input("Ingrese la descripción del artículo: ")
        codigoDeBarras = input("Ingrese el código de barras: ")
        categoriaDelArticulo = input("Ingrese la categoría del artículo: ")
        precioDelArticulo = float(input("Ingrese el precio del artículo: "))
        cantidadEnStock = int(input("Ingrese la cantidad en stock: "))
        sucursal = input("Ingrese la sucursal donde se encuentra el artículo: ")
        print("Artículo agregado exitosamente.")
    case 2:
        print("Nombre del artículo:", nombreDelArticulo, "Descripción del artículo:", descripcionDelArticulo, "Código de barras:", codigoDeBarras, "Categoría del artículo:", categoriaDelArticulo, "Precio del artículo:", precioDelArticulo, "Cantidad en stock:", cantidadEnStock, "Sucursal:", sucursal)
    case 3:
        nombreDelArticulo = ""
        descripcionDelArticulo = ""
        codigoDeBarras = ""
        categoriaDelArticulo = ""
        precioDelArticulo = 0.0
        cantidadEnStock = 0
        sucursal = ""
        print("Artículo buscado.")
    case 4:
        nombreDelArticulo = input("Ingrese el nuevo nombre del artículo: ")
        descripcionDelArticulo = input("Ingrese la nueva descripción del artículo: ")
        codigoDeBarras = input("Ingrese el nuevo código de barras: ")
        categoriaDelArticulo = input("Ingrese la nueva categoría del artículo: ")
        precioDelArticulo = float(input("Ingrese el nuevo precio del artículo: "))
        cantidadEnStock = int(input("Ingrese la nueva cantidad en stock: "))
        sucursal = input("Ingrese la nueva sucursal donde se encuentra el artículo: ")
    case 5:
        print("¡Guardado exitosamente! Hasta luego!")
    case 6:
        print("¡Opción no válida!")
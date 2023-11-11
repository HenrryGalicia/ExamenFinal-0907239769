def registrar_datos(codigo, marca, modelo, precio, kilometraje ):
    return f"{codigo}: {marca}: {modelo}: {precio}: {kilometraje: }"

def generar_reporte_datos(datos):
    reporte = "\n".join ([datos['registro'] for datos]);
    return reporte

def guardar_reporte_en_archivo(reporte, nombre_archivo="vehiculos.xlsx"):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(reporte)
    print(f"El reporte de datos ha sido guardado en {nombre_archivo}")


ventas = []

while True:
    dato = input("Ingrese el nombre del dato ('fin' para salir): ")
    if dato.lower() == 'fin':
        break

    codigo = int(input("Ingrese el codigo: "))
    marca = float(input("Ingrese la marca: "))
    modelo = float(input("Ingrese el modelo: "))
    precio = float(input("Ingrese el precio: "))
    kilometraje = float(input("Ingrese el kilometraje: "))

    registro_datos = registrar_datos(codigo , marca, modelo, precio, kilometraje)
    ventas.append({'registro': registro_datos, 'codigo': codigo, 'marca': marca, 'modelo': modelo, 'precio': precio, 'kilometraje': kilometraje, })

reporte = generar_reporte_datos(dato)
guardar_reporte_en_archivo(reporte)

def listar_datos():
    with open('vehiculos.xlsx', 'r') as archivo:
        lineas = archivo.readlines()
        
    if not lineas:
        print("No hay datos registrados.")
    else:
        print("Listado de datos:")
        for linea in lineas:
            elementos = linea.strip().split(',')
            codigo, marca, modelo, precio, kilometraje = elementos
            print(f"Código: {codigo}")
            print(f"marca: {marca}")
            print(f"modelo: {modelo}")
            print(f"precio: {precio}")
            print(f"kilometraje: {kilometraje}")
            print("------------------------------")


def anular_dato():
    codigo = input("Ingrese el código del dato: ")
    
    dato_encontrado = False

    datos_actualizados = []

    with open('vehiculos.xlsx', 'r') as archivo:
        for linea in archivo:
            elementos = linea.strip().split(',')
            if elementos[0] == codigo:
                venta_encontrada = True
                print("dato anulado.")
                
                marca = int(elementos[2])
                if codigo in dato:
                    dato[codigo] = (dato[codigo][0], dato[codigo][1] + marca, dato[marca][2])
                else:
                    print(f"ADVERTENCIA: El dato con código '{codigo}' no está en el dato, pero se ha anulado un dato.")
            else:
                datos_actualizados.append(linea)

    if venta_encontrada:
        with open('vehiculos.xlsx', 'w') as archivo:
            archivo.writelines(datos_actualizados)
    else:
        print(f"No se encontró ninguna venta con el código del dato '{codigo}'.")

while True:
    print("\nMenú:")
    print("1. CrearVehiculos")
    print("2. Listar vehiculos")
    print("3. editar vehiculos")
    print("4. Eliminar vehiculos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        crear_vehiculos()
    elif opcion == '2':
        Listar_vehiculos()
    elif opcion == '3':
        Editar_vehiculos()
    elif opcion == '4':
        Eliminar_vehiculos()
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Nombre del estudiante: Brayan Steven Morales Gutiérrez
# Grupo: 844
# Programa: Ingenieria Multimedia
# Codigo fuente: Autoria propia

# Crear matriz de datos
inventario = [
["A001", "Computadora", 14, 18],
["A002", "Impresora", 20, 8],
["A003", "Escaner", 10, 10],
["A004", "Pantalla", 0, 25],
["A005", "Parlante", 7, 18],
["A006", "Teclado", 5, 10],
["A007", "Router", 12, 15]
]
# Funcion para calcular el total y la cantidad exacta a pedir
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    # Si el stock actual es menor al mínimo, se debe pedir la diferencia
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
    # Si es mayor o igual a cero, no se necesita pedir nada
    else:
        cantidad_a_pedir = 0

    return cantidad_a_pedir

# Procesa inventario y muestra resultados
# Imprimir encabezado de la tabla
print("-"*70)
print("Informe de pedidos de restablecimiento de articulos Tecno Innovation.")
print("-"*70)

# Recorrer fila por fila de la matriz
for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # LLamar y sumar la funcion para calcular la cantidad a pedir
    cantidad_final = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

    # Imprimir resultados
    print(f"Articulo: {nombre:<12} |  Cantidad a pedir: {cantidad_final}")

print("-"*70)
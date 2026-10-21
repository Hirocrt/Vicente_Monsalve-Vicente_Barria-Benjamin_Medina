import oracledb
from models.proyecto import Proyecto


def mostrar(id_proyecto, nombre, descripcion, fecha):
    texto_descripcion = descripcion if descripcion is not None else "Sin descripción"
    texto_fecha = fecha.strftime("%d-%m-%Y")
    print(f"ID: {id_proyecto} | Proyecto: {nombre} | Inicio: {texto_fecha}")
    print(f"    Descripción: {texto_descripcion}")


print("1. Listar todos los proyectos")
print("2. Buscar un proyecto por ID")
opcion = input("Elige una opción: ").strip()

proy = Proyecto()

try:
    if opcion == "1":
        lista = proy.obtenerTodos()
        if len(lista) == 0:
            print("No hay proyectos registrados.")
        else:
            for fila in lista:
                mostrar(fila[0], fila[1], fila[2], fila[3])

    elif opcion == "2":
        texto = input("Ingresa el ID del proyecto: ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        elif proy.cargarPorID(int(texto)):
            mostrar(proy.id_proyecto, proy.nombre, proy.descripcion, proy.fecha_inicio)
        else:
            print(f"No existe un proyecto con ID {texto}.")

    else:
        print("Opción no válida.")
except oracledb.Error as error:
    print("Error de base de datos:", error)
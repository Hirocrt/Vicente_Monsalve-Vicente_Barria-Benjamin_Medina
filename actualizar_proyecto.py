import oracledb
from models.proyecto import Proyecto

proy = Proyecto()

try:
    lista = proy.obtenerTodos()
    if len(lista) == 0:
        print("No hay proyectos registrados.")
    else:
        print("Ingresa el ID del proyecto que quieres actualizar...")
        for fila in lista:
            print(f"ID: {fila[0]} | Proyecto: {fila[1]}")

        texto = input("ID ----> ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        elif not proy.cargarPorID(int(texto)):
            print(f"No existe un proyecto con ID {texto}.")
        else:
            nuevoNombre = input(f"Nuevo nombre [{proy.nombre}] (ENTER para no cambiarlo): ")
            if nuevoNombre.strip() != "":
                proy.nombre = nuevoNombre

            actual = proy.descripcion if proy.descripcion is not None else "sin descripción"
            nuevaDescripcion = input(f"Nueva descripción [{actual}] (ENTER = no cambiar, 'ninguna' = borrarla): ").strip()
            if nuevaDescripcion.lower() == "ninguna":
                proy.descripcion = None
            elif nuevaDescripcion != "":
                proy.descripcion = nuevaDescripcion

            fechaActual = proy.fecha_inicio.strftime("%d-%m-%Y")
            nuevaFecha = input(f"Nueva fecha de inicio [{fechaActual}] (día-mes-año, ENTER para no cambiarla): ").strip()
            if nuevaFecha != "":
                proy.fecha_inicio = nuevaFecha

            proy.actualizar()
            print("Proyecto actualizado correctamente.")
except ValueError as error:
    print("Error:", error)
except oracledb.Error as error:
    print("Error de base de datos:", error)
import oracledb
from models.proyecto import Proyecto

proy = Proyecto()

try:
    lista = proy.obtenerTodos()
    if len(lista) == 0:
        print("No hay proyectos registrados.")
    else:
        print("Ingresa el ID del proyecto que quieres eliminar...")
        for fila in lista:
            print(f"ID: {fila[0]} | Proyecto: {fila[1]}")

        texto = input("ID ----> ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        elif not proy.cargarPorID(int(texto)):
            print(f"No existe un proyecto con ID {texto}.")
        else:
            registros, asignaciones = proy.contarAsociados(proy.id_proyecto)
            print(f"Vas a eliminar el proyecto '{proy.nombre}'.")
            if registros > 0 or asignaciones > 0:
                print("Atención: también se borrarán de forma permanente:")
                print(f"  - {registros} registro(s) de tiempo")
                print(f"  - {asignaciones} asignación(es) de empleados")
            respuesta = input("¿Confirmas la eliminación? (s/n): ").strip().lower()
            if respuesta == "s":
                proy.eliminar(proy.id_proyecto)
                print("Proyecto eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
except ValueError as error:
    print("Error:", error)
except oracledb.Error as error:
    print("Error de base de datos:", error)
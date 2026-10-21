import oracledb
from models.departamento import Departamento

dep = Departamento()

try:
    lista = dep.obtenerTodos()
    if len(lista) == 0:
        print("No hay departamentos registrados.")
    else:
        print("Ingresa el ID del departamento que quieres eliminar...")
        for fila in lista:
            gerente = fila[3] if fila[3] is not None else "Sin gerente"
            print(f"ID: {fila[0]} | Departamento: {fila[1]} | Gerente: {gerente}")

        texto = input("ID ----> ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        elif not dep.cargarPorID(int(texto)):
            print(f"No existe un departamento con ID {texto}.")
        else:
            cantidad = dep.contarEmpleados(dep.id_departamento)
            print(f"Vas a eliminar el departamento '{dep.nombre_departamento}'.")
            if cantidad > 0:
                print(f"Atención: {cantidad} empleado(s) quedarán sin departamento.")
            respuesta = input("¿Confirmas la eliminación? (s/n): ").strip().lower()

            if respuesta == "s":
                dep.eliminar(dep.id_departamento)
                print("Departamento eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
except ValueError as error:
    print("Error:", error)
except oracledb.Error as error:
    print("Error de base de datos:", error)
import oracledb
from models.departamento import Departamento

print("1. Listar todos los departamentos")
print("2. Buscar un departamento por ID")
opcion = input("Elige una opción: ").strip()

dep = Departamento()

try:
    if opcion == "1":
        lista = dep.obtenerTodos()
        if len(lista) == 0:
            print("No hay departamentos registrados.")
        else:
            for fila in lista:
                gerente = fila[3] if fila[3] is not None else "Sin gerente"
                print(f"ID: {fila[0]} | Departamento: {fila[1]} | Gerente: {gerente}")

    elif opcion == "2":
        texto = input("Ingresa el ID del departamento: ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        elif dep.cargarPorID(int(texto)):
            gerente = dep.nombre_gerente if dep.nombre_gerente is not None else "Sin gerente"
            print(f"ID: {dep.id_departamento} | Departamento: {dep.nombre_departamento} | Gerente: {gerente}")
        else:
            print(f"No existe un departamento con ID {texto}.")

    else:
        print("Opción no válida.")
except oracledb.Error as error:
    print("Error de base de datos:", error)

import oracledb
from models.departamento import Departamento

dep = Departamento()

try:
    # PASO 1: mostrar la lista de departamentos
    lista = dep.obtenerTodos()
    if len(lista) == 0:
        print("No hay departamentos registrados.")
    else:
        print("Ingresa el ID del departamento que quieres actualizar...")
        for fila in lista:
            gerente = fila[3] if fila[3] is not None else "Sin gerente"
            print(f"ID: {fila[0]} | Departamento: {fila[1]} | Gerente: {gerente}")

        # PASO 2: pedir el ID y validarlo
        texto = input("ID ----> ").strip()
        if not texto.isdigit():
            print("Error: el ID debe ser un número entero.")
        # PASO 3: cargar el departamento en el objeto
        elif not dep.cargarPorID(int(texto)):
            print(f"No existe un departamento con ID {texto}.")
        else:
            # PASO 4: pedir los nuevos valores (ENTER = mantener el actual)
            nuevoNombre = input(f"Nuevo nombre [{dep.nombre_departamento}] (ENTER para no cambiarlo): ")
            if nuevoNombre.strip() != "":
                dep.nombre_departamento = nuevoNombre

            actual = dep.id_gerente if dep.id_gerente is not None else "sin gerente"
            nuevoGerente = input(f"Nuevo ID de gerente [{actual}] (ENTER = no cambiar, 'ninguno' = quitar gerente): ").strip()
            datosValidos = True
            if nuevoGerente.lower() == "ninguno":
                dep.id_gerente = None
            elif nuevoGerente != "":
                if nuevoGerente.isdigit():
                    dep.id_gerente = int(nuevoGerente)
                else:
                    print("Error: el ID del gerente debe ser un número entero.")
                    datosValidos = False

            # PASO 5: llamar a actualizar()
            if datosValidos:
                dep.actualizar()
                print("Departamento actualizado correctamente.")
except ValueError as error:
    print("Error:", error)
except oracledb.Error as error:
    print("Error de base de datos:", error)
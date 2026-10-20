import oracledb
from models.departamento import Departamento

nuevo = Departamento()
nuevo.nombre_departamento = input("Ingresa el nombre del departamento: ")
textoGerente = input("Ingresa el ID del gerente (ENTER si aún no tiene): ").strip()

if textoGerente != "" and not textoGerente.isdigit():
    print("Error: el ID del gerente debe ser un número entero.")
else:
    if textoGerente != "":
        nuevo.id_gerente = int(textoGerente)
    try:
        nuevo.insertar()
        print(f"Departamento creado con ID {nuevo.id_departamento}")
    except ValueError as error:
        print("Error:", error)
    except oracledb.Error as error:
        print("Error de base de datos:", error)
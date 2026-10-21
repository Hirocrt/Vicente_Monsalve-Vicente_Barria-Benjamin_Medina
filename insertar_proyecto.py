import oracledb
from models.proyecto import Proyecto

nuevo = Proyecto()
nuevo.nombre = input("Ingresa el nombre del proyecto: ")
nuevo.descripcion = input("Ingresa la descripción (ENTER si no tiene): ")
nuevo.fecha_inicio = input("Fecha de inicio (día-mes-año): ")

try:
    nuevo.insertar()
    print(f"Proyecto creado con ID {nuevo.id_proyecto}")
except ValueError as error:
    print("Error:", error)
except oracledb.Error as error:
    print("Error de base de datos:", error)
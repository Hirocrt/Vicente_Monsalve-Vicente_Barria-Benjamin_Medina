from models.conexion import ConexionDB

def registrar_empleado_proyecto():
    print("--- ASIGNAR EMPLEADO A PROYECTO ---")
    id_empleado=input("Ingrese el ID del Empleado: ")
    id_proyecto=input("Ingrese el ID del Proyecto: ")
    rol=input("Ingrese el rol del empleado de este proyecto: ")
    fecha=input("Ingrese la fecha de asignación: ")
    
    bd = ConexionDB()
    if bd.conexion is None:
        print("No se pudo establecer la conexion con la base de datos.")
        return
    
    try:
        sql = """INSERT INTO empleado_proyecto (id_empleado, id_proyecto, rol, fecha_asignacion)
        VALUES (:1, :2, :3, :4)"""
        
        valores = (id_empleado, id_proyecto, rol, fecha)
        
        bd.cursor.execute(sql, valores)
        bd.conexion.commit()
        print("\n¡Empleado asignado al proyecto con exito!")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al registrar la asignación: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    registrar_empleado_proyecto()
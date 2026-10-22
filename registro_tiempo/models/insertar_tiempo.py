from models.conexion import ConexionDB

def registrar_horas():
    print("--- REGISTRAR HORAS TRABAJADAS ---")
    id_asignacion = input("Ingrese el ID de su asignacion (empleado_proyecto): ")
    fecha = input("Ingrese la fecha del trabajo: ")
    horas = input("Ingrese la cantidad de horas trabajadas: ")
    descripcion = input("Ingrese una breve descripcion de la tarea: ")
    
    bd = ConexionDB()
    if bd.conexion is None:
        print("No se pudo establecer conexion con la base de datos.")
        return
    
    try:
        sql = """INSERT INTO registro_tiempo (id_asignacion, fecha, horas_trabajadas, descripcion) 
        VALUES (:1, :2, :3, :4)"""
        
        valores = (id_asignacion, fecha, horas, descripcion)
        
        bd.cursor.execute(sql, valores)
        bd.conexion.commit()
        print("\n¡Horas registradas con exito!")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al registrar el tiempo: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    registrar_horas()
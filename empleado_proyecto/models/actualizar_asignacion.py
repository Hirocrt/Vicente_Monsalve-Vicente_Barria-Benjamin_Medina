from models.conexion import ConexionDB

def modificar_rol_asignacion():
    print("--- ACTUALIZAR ROL EN PROYECTO ---")
    id_asignacion = input("Ingrese el ID de la asignacion que desea modificar: ")
    nuevo_rol = input("Ingrese el nuevo rol del empleado: ")
    
    bd = ConexionDB
    if bd.conexion is None:
        return
    
    try:
        sql = "UPDATE empleado_proyecto SET rol = :1 WHERE id_asignacion = :2"
        bd.cursor.execute(sql, (nuevo_rol, id_asignacion))
        bd.conexion.commit()
        
        if bd.cursor.rowcount > 0:
            print("\n¡El rol ha sido actualizado correctamente!")
        else:
            print("\nNo se encontro ninguna asignacion con ese ID.")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al actualizar: {e}")
    finally:
        bd.cursor.close
        bd.conexion.close
if __name__ == "__main__":
    modificar_rol_asignacion()
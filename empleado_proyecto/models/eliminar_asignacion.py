from models.conexion import ConexionDB

def desasignar_empleado():
    print("--- ELIMINAR EMPLEADO DE UN PROYECTO ---")
    id_asignacion = input("Ingrese el ID de la asignacion que desea eliminar: ")
    
    bd = ConexionDB
    if bd.conexion is None:
        return
    
    try:
        sql = "DELETE FROM empleado_proyecto WHERE id_asignacion = :1"
        bd.cursor.execute(sql, (id_asignacion))
        bd.conexion.commit()
        
        if bd.cursor.rowcount > 0:
            print("\n¡El empleado ha sido removido del proyecto con exito!")
        else:
            print("\nNo se encontro ninguna asignacion con ese ID.")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al eliminar la asignacion: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    desasignar_empleado()
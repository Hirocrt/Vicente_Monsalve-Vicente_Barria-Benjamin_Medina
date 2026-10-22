from models.conexion import ConexionDB

def borrar_tiempo():
    print("--- ELIMINAR REGISTRO DE TIEMPO ---")
    id_registro = input("Ingrese el ID del registro de tiempo que desea eliminar: ")
    
    bd = ConexionDB
    if bd.conexion is None:
        return
    
    try:
        sql = "DELETE FROM registro_tiempo WHERE id_registro = :1"
        bd.cursor.execute(sql, (id_registro))
        bd.conexion.commit()
        
        if bd.cursor.rowcount > 0:
            print("\n¡El registro de tiempo ha sido eliminado con exito!")
        else:
            print("\nNo se encontro ningun registro con ese ID.")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al eliminar el registro: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    borrar_tiempo()
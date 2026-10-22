from models.conexion import ConexionDB

def modificar_tiempo():
    print("--- ACTUALIZAR REGISTRO DE TIEMPO ---")
    id_registro = input("Ingrese el ID del registro de tiempo que desea modificar: ")
    nuevas_horas = input("Ingrese la cantidad corregida de horas: ")
    nueva_descripcion = input("Ingrese la nueva descripcion: ")
    
    bd = ConexionDB
    if bd.conexion is None:
        return
    
    try:
        sql = "UPDATE registro_tiempo SET horas_trabajadas = :1, descripcion = :2 WHERE id_registro = :3"
        bd.cursor.execute(sql, (nuevas_horas, nueva_descripcion, id_registro))
        bd.conexion.commit()
        
        if bd.cursor.rowcount > 0:
            print("\n¡El registro de tiempo ha sido actualizado correctamente!")
        else:
            print("\nNo se encontro ningun registro con ese ID.")
    except Exception as e:
        bd.conexion.rollback()
        print(f"\nError al actualizar el registro: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    modificar_tiempo()
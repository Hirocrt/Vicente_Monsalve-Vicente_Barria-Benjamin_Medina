from models.conexion import ConexionDB

def listar_asignaciones():
    print("--- LISTADO DE EMPLEADOS POR PROYECTO ---")
    
    bd = ConexionDB()
    if bd.conexion is None:
        return
    
    try:
        sql = """
            SELECT ep.id_asignacion, e.nombre, p.nombre, ep.rol, ep.fecha_asignacion
            FROM empleado_proyecto ep
            JOIN empleado e ON ep.id_empleado = e.id
            JOIN proyecto p ON ep.id_proyecto = p.id
        """
        bd.cursor.execute(sql)
        resultados = bd.cursor.fechall()
    
        if not resultados:
            print("No hay empleados asignados a ningun proyecto actualmente.")
        else:
            print(f"{'ID':<5} | {'Empleado':<20} | {'Proyecto':<20} | {'Rol':<20} | {'Fecha':<12}")
            print("-" * 85)
        for fila in resultados:
            print(f"{fila[0]:<5} | {fila[1]:<20} | {fila[2]:<20} | {fila[3]:<20} | {str(fila[4]):<12}")
    
    except Exception as e:
        print(f"Error al consultar las asignaciones: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    listar_asignaciones()
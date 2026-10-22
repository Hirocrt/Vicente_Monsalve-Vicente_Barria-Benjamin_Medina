from models.conexion import ConexionDB

def listar_tiempos():
    print("--- HISTORIAL DE TIEMPO REGISTRADO ---")
    
    bd = ConexionDB()
    if bd.conexion is None:
        return
    
    try:
        sql = """
            SELECT rt.id_registro, e.nombre, p.nombre, rt.fecha, rt.horas_trabajadas, rt.descripcion
            FROM registro_tiempo rt
            JOIN empleado_proyecto ep ON rt.id_asignacion = ep.id_asignacion
            JOIN empleado e ON ep.id_empleado = e.id
            JOIN proyecto p ON ep.id_proyecto = p.id
            ORDER BY rt.fecha DESC
        """
        bd.cursor.execute(sql)
        resultados = bd.cursor.fetchall()
        
        if not resultados:
            print("No hay registros de tiempo cargados en el sistema.")
        else:
            print(f"{'ID':<5} | {'Empleado':<15} | {'Proyecto':<15} | {'Fecha':<12} | {'Horas':<6} | {'Descripción':<25}")
            print("-" * 90)
            for fila in resultados:
                print(f"{fila[0]:<5} | {fila[1]:<15} | {fila[2]:<15} | {str(fila[3]):<12} | {fila[4]:<6} | {fila[5]:<25}")
                
    except Exception as e:
        print(f"Error al consultar el historial de tiempos: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
    if __name__ == "__main__":
        listar_tiempos()
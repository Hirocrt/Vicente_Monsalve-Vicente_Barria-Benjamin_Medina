from conexion import ConexionDB

def generar_informe_proyecto():
    print("--- INFORME DE HORAS POR PROYECTO ---")
    id_proyecto = input("Ingrese el ID del Proyecto que desea consultar: ")
    
    bd = ConexionDB()
    if bd.conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    try:
        sql = """
            SELECT p.nombre, SUM(rt.horas_trabajadas) as total_horas
            FROM proyecto p
            JOIN empleado_proyecto ep ON p.id = ep.id_proyecto
            JOIN registro_tiempo rt ON ep.id_asignacion = rt.id_asignacion
            WHERE p.id = :1
            GROUP BY p.nombre
        """
        bd.cursor.execute(sql, (id_proyecto))
        resultado = bd.cursor.fetchone()
        
        print("\n========================================")
        if resultado:
            nombre_proyecto = resultado[0]
            total_horas = resultado[1] if resultado[1] is not None else 0
            print(f" PROYECTO: {nombre_proyecto}")
            print(f" TOTAL DE HORAS INVERTIDAS: {total_horas} hrs")
        else:
            print(" No se encontraron registros de tiempo para este proyecto.")
            print(" Verifique que el ID sea correcto o que ya tenga horas asignadas")
        print("========================================\n")
        
    except Exception as e:
        print(f"Error al generar el informe del proyecto: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()
        
if __name__ == "__main__":
    generar_informe_proyecto()
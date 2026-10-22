from conexion import ConexionDB

def generar_informe_empleado():
    print("--- INFORME DE HORAS POR EMPLEADO ---")
    id_empleado = input("Ingrese el ID del Empleado que desea consultar: ")

    bd = ConexionDB()
    if bd.conexion is None:
        return

    try:
        sql = """
            SELECT e.nombre, SUM(rt.horas_trabajadas) as total_horas
            FROM empleado e
            JOIN empleado_proyecto ep ON e.id = ep.id_empleado
            JOIN registro_tiempo rt ON ep.id_asignacion = rt.id_asignacion
            WHERE e.id = :1
            GROUP BY e.nombre
        """
        bd.cursor.execute(sql, (id_empleado,))
        resultado = bd.cursor.fetchone()

        print("\n========================================")
        if resultado:
            nombre_empleado = resultado[0]
            total_horas = resultado[1]
            print(f" EMPLEADO: {nombre_empleado}")
            print(f" TOTAL DE HORAS TRABAJADAS: {total_horas} hrs")
        else:
            print(" No se encontraron registros de horas para este empleado.")
        print("========================================\n")
                
    except Exception as e:
        print(f"Error al generar el informe del empleado: {e}")
    finally:
        bd.cursor.close()
        bd.conexion.close()

if __name__ == "__main__":
    generar_informe_empleado()
from models.conexion import ConexionDB


class Informe:
    def obtenerInformeEmpleados(self):
        try:
            c = ConexionDB()
            sql = """SELECT e.id_empleado, u.nombre, u.correo, u.telefono,
                            d.nombre_departamento, u.inicio_contrato, u.salario
                    FROM empleados e
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    LEFT JOIN departamentos d ON e.id_departamento = d.id_departamento
                    ORDER BY e.id_empleado"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al generar el informe de empleados: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerInformeDepartamentos(self):
        try:
            c = ConexionDB()
            sql = """SELECT d.id_departamento, d.nombre_departamento,
                            (SELECT COUNT(*) FROM empleados e
                            WHERE e.id_departamento = d.id_departamento)
                    FROM departamentos d
                    ORDER BY d.id_departamento"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al generar el informe de departamentos: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
             pass

    def obtenerInformeProyectos(self):
        try:
            c = ConexionDB()
            sql = """SELECT p.id_proyecto, p.nombre, p.descripcion, p.fecha_inicio,
                            (SELECT COUNT(*) FROM empleado_proyecto ep
                             WHERE ep.id_proyecto = p.id_proyecto),
                            (SELECT NVL(SUM(rt.horas_trabajadas), 0) FROM registro_tiempo rt
                             WHERE rt.id_proyecto = p.id_proyecto)
                    FROM proyectos p
                    ORDER BY p.id_proyecto"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al generar el informe de proyectos: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerInformeRegistros(self):
        try:
            c = ConexionDB()
            sql = """SELECT rt.id_registro, u.nombre, d.nombre_departamento, p.nombre,
                            rt.fecha, rt.horas_trabajadas, rt.tareas
                    FROM registro_tiempo rt
                    JOIN empleados e ON rt.id_empleado = e.id_empleado
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    JOIN proyectos p ON rt.id_proyecto = p.id_proyecto
                    LEFT JOIN departamentos d ON e.id_departamento = d.id_departamento
                    ORDER BY rt.fecha, rt.id_registro"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al generar el informe de registros de tiempo: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass
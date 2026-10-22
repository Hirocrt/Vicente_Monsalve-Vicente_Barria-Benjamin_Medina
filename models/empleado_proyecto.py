from models.conexion import ConexionDB


class EmpleadoProyecto:
    id_asignacion: int
    id_empleado: int
    id_proyecto: int

    def __init__(self, id_asignacion: int = 0, id_empleado: int = 0, id_proyecto: int = 0):
        self.id_asignacion = id_asignacion
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    def __str__(self):
        return f"ID asignación: {self.id_asignacion} | ID empleado: {self.id_empleado} | ID proyecto: {self.id_proyecto}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            sql = """SELECT ep.id_asignacion, e.id_empleado, u.nombre, p.id_proyecto, p.nombre
                    FROM empleado_proyecto ep
                    JOIN empleados e ON ep.id_empleado = e.id_empleado
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    JOIN proyectos p ON ep.id_proyecto = p.id_proyecto
                    ORDER BY ep.id_asignacion"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener las asignaciones: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerPorProyecto(self, idProyecto):
        try:
            c = ConexionDB()
            sql = """SELECT ep.id_asignacion, e.id_empleado, u.nombre
                    FROM empleado_proyecto ep
                    JOIN empleados e ON ep.id_empleado = e.id_empleado
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    WHERE ep.id_proyecto = :id
                    ORDER BY ep.id_asignacion"""
            c.cursor.execute(sql, id=idProyecto)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los empleados del proyecto: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def insertar(self):
        try:
            c = ConexionDB()
            sql = "INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES (:ide, :idp)"
            c.cursor.execute(sql, ide=self.id_empleado, idp=self.id_proyecto)
            c.conexion.commit()
            print("Empleado asignado al proyecto")
        except Exception as e:
            print(f"ERROR al insertar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def actualizar(self):
        try:
            c = ConexionDB()
            sql = """UPDATE empleado_proyecto SET id_empleado=:ide, id_proyecto=:idp
                    WHERE id_asignacion=:id"""
            c.cursor.execute(sql, id=self.id_asignacion, ide=self.id_empleado, idp=self.id_proyecto)
            c.conexion.commit()
            print("Asignación actualizada")
        except Exception as e:
            print(f"ERROR al actualizar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def cargarPorID(self, idBuscado):
        try:
            c = ConexionDB()
            sql = "SELECT id_asignacion, id_empleado, id_proyecto FROM empleado_proyecto WHERE id_asignacion = :id"
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_asignacion = fila[0]
                self.id_empleado = fila[1]
                self.id_proyecto = fila[2]
                return True
            else:
                print("No se encontró una asignación con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar la asignación por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM empleado_proyecto WHERE id_asignacion = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("Empleado removido del proyecto")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerEmpleados(self):
        try:
            c = ConexionDB()
            sql = """SELECT e.id_empleado, u.nombre
                    FROM empleados e
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    ORDER BY e.id_empleado"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los empleados: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerProyectos(self):
        try:
            c = ConexionDB()
            c.cursor.execute("SELECT id_proyecto, nombre FROM proyectos ORDER BY id_proyecto")
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los proyectos: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass
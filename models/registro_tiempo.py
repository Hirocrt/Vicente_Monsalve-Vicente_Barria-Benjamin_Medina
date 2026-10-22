from models.conexion import ConexionDB


class RegistroTiempo:
    id_registro: int
    id_empleado: int
    id_proyecto: int
    fecha: str
    horas_trabajadas: float
    tareas: str

    def __init__(self, id_registro: int = 0, id_empleado: int = 0, id_proyecto: int = 0,
                 fecha: str = "", horas_trabajadas: float = 0, tareas: str = ""):
        self.id_registro = id_registro
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.tareas = tareas

    def __str__(self):
        return f"ID registro: {self.id_registro} | Empleado: {self.id_empleado} | Proyecto: {self.id_proyecto} | Fecha: {self.fecha} | Horas: {self.horas_trabajadas}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            sql = """SELECT rt.id_registro, u.nombre, p.nombre, rt.fecha, rt.horas_trabajadas, rt.tareas
                    FROM registro_tiempo rt
                    JOIN empleados e ON rt.id_empleado = e.id_empleado
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    JOIN proyectos p ON rt.id_proyecto = p.id_proyecto
                    ORDER BY rt.fecha DESC, rt.id_registro DESC"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los registros de tiempo: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerPorEmpleado(self, idEmpleado):
        try:
            c = ConexionDB()
            sql = """SELECT rt.id_registro, p.nombre, rt.fecha, rt.horas_trabajadas, rt.tareas
                    FROM registro_tiempo rt
                    JOIN proyectos p ON rt.id_proyecto = p.id_proyecto
                    WHERE rt.id_empleado = :id
                    ORDER BY rt.fecha DESC, rt.id_registro DESC"""
            c.cursor.execute(sql, id=idEmpleado)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los registros del empleado: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def obtenerPorProyecto(self, idProyecto):
        try:
            c = ConexionDB()
            sql = """SELECT rt.id_registro, u.nombre, rt.fecha, rt.horas_trabajadas, rt.tareas
                    FROM registro_tiempo rt
                    JOIN empleados e ON rt.id_empleado = e.id_empleado
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    WHERE rt.id_proyecto = :id
                    ORDER BY rt.fecha DESC, rt.id_registro DESC"""
            c.cursor.execute(sql, id=idProyecto)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los registros del proyecto: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def insertar(self):
        try:
            c = ConexionDB()
            sql = """INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, tareas)
                    VALUES (:ide, :idp, TO_DATE(:fec, 'DD-MM-YYYY'), :horas, :tareas)"""
            c.cursor.execute(sql, ide=self.id_empleado, idp=self.id_proyecto, fec=self.fecha,
                             horas=self.horas_trabajadas, tareas=self.tareas)
            c.conexion.commit()
            print("Registro de tiempo insertado")
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
            sql = """UPDATE registro_tiempo SET id_empleado=:ide, id_proyecto=:idp,
                    fecha=TO_DATE(:fec, 'DD-MM-YYYY'), horas_trabajadas=:horas, tareas=:tareas
                    WHERE id_registro=:id"""
            c.cursor.execute(sql, id=self.id_registro, ide=self.id_empleado, idp=self.id_proyecto,
                             fec=self.fecha, horas=self.horas_trabajadas, tareas=self.tareas)
            c.conexion.commit()
            print("Registro de tiempo actualizado")
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
            sql = """SELECT id_registro, id_empleado, id_proyecto, fecha, horas_trabajadas, tareas
                    FROM registro_tiempo WHERE id_registro = :id"""
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_registro = fila[0]
                self.id_empleado = fila[1]
                self.id_proyecto = fila[2]
                self.fecha = fila[3].strftime('%d-%m-%Y') if fila[3] else ""
                self.horas_trabajadas = fila[4]
                self.tareas = fila[5]
                return True
            else:
                print("No se encontró un registro de tiempo con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar el registro de tiempo por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM registro_tiempo WHERE id_registro = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("Registro de tiempo eliminado")
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
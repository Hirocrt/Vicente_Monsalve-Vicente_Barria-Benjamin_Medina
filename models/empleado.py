from models.conexion import ConexionDB


class Empleado:
    id_empleado: int
    id_usuario: int
    id_departamento: int

    def __init__(self, id_empleado: int = 0, id_usuario: int = 0, id_departamento: int = None):
        self.id_empleado = id_empleado
        self.id_usuario = id_usuario
        self.id_departamento = id_departamento

    def __str__(self):
        return f"ID empleado: {self.id_empleado} | ID usuario: {self.id_usuario} | ID departamento: {self.id_departamento}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            sql = """SELECT e.id_empleado, u.nombre, d.nombre_departamento
                    FROM empleados e
                    JOIN usuarios u ON e.id_usuario = u.id_usuario
                    LEFT JOIN departamentos d ON e.id_departamento = d.id_departamento
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

    def insertar(self):
        try:
            c = ConexionDB()
            sql = "INSERT INTO empleados (id_usuario, id_departamento) VALUES (:idu, :idd)"
            c.cursor.execute(sql, idu=self.id_usuario, idd=self.id_departamento)
            c.conexion.commit()
            print("Empleado insertado ")
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
            sql = "UPDATE empleados SET id_usuario=:idu, id_departamento=:idd WHERE id_empleado=:id"
            c.cursor.execute(sql, id=self.id_empleado, idu=self.id_usuario, idd=self.id_departamento)
            c.conexion.commit()
            print("Empleado actualizado ")
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
            sql = "SELECT id_empleado, id_usuario, id_departamento FROM empleados WHERE id_empleado = :id"
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_empleado = fila[0]
                self.id_usuario = fila[1]
                self.id_departamento = fila[2]
                return True
            else:
                print("No se encontró un empleado con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar empleado por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM empleados WHERE id_empleado = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("Empleado eliminado")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass
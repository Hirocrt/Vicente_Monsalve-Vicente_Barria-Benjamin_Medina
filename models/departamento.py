from models.conexion import ConexionDB


class Departamento:
    id_departamento: int
    nombre_departamento: str

    def __init__(self, id_departamento: int = 0, nombre_departamento: str = ""):
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

    def __str__(self):
        return f"ID: {self.id_departamento} | Departamento: {self.nombre_departamento}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            sql = """SELECT id_departamento, nombre_departamento
                    FROM departamentos
                    ORDER BY id_departamento"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los departamentos: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def insertar(self):
        try:
            c = ConexionDB()
            sql = "INSERT INTO departamentos (nombre_departamento) VALUES (:nom)"
            c.cursor.execute(sql, nom=self.nombre_departamento)
            c.conexion.commit()
            print("Departamento insertado")
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
            sql = """UPDATE departamentos SET nombre_departamento = :nom
                    WHERE id_departamento = :id"""
            c.cursor.execute(sql, id=self.id_departamento, nom=self.nombre_departamento)
            c.conexion.commit()
            print("Departamento actualizado")
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
            sql = """SELECT id_departamento, nombre_departamento
                    FROM departamentos
                    WHERE id_departamento = :id"""
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_departamento = fila[0]
                self.nombre_departamento = fila[1]
                return True
            else:
                print("No se encontró un departamento con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar departamento por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def contarEmpleados(self, idDepartamento):
        try:
            c = ConexionDB()
            sql = "SELECT COUNT(*) FROM empleados WHERE id_departamento = :id"
            c.cursor.execute(sql, id=idDepartamento)
            return c.cursor.fetchone()[0]
        except Exception as e:
            print(f"ERROR al contar los empleados: {e}")
            return 0
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM departamentos WHERE id_departamento = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("Departamento eliminado")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass
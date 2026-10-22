from models.conexion import ConexionDB


class Administrador:
    id_administrador: int
    id_usuario: int
    rol: str

    def __init__(self, id_administrador: int = 0, id_usuario: int = 0, rol: str = ""):
        self.id_administrador = id_administrador
        self.id_usuario = id_usuario
        self.rol = rol

    def __str__(self):
        return f"ID admin: {self.id_administrador} | ID usuario: {self.id_usuario} | Rol: {self.rol}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            sql = """SELECT a.id_administrador, u.nombre, a.rol
                    FROM administradores a
                    JOIN usuarios u ON a.id_usuario = u.id_usuario
                    ORDER BY a.id_administrador"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los administradores: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def insertar(self):
        try:
            c = ConexionDB()
            sql = "INSERT INTO administradores (id_usuario, rol) VALUES (:idu, :rol)"
            c.cursor.execute(sql, idu=self.id_usuario, rol=self.rol)
            c.conexion.commit()
            print("Administrador insertado ")
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
            sql = "UPDATE administradores SET id_usuario=:idu, rol=:rol WHERE id_administrador=:id"
            c.cursor.execute(sql, id=self.id_administrador, idu=self.id_usuario, rol=self.rol)
            c.conexion.commit()
            print("Administrador actualizado ")
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
            sql = "SELECT id_administrador, id_usuario, rol FROM administradores WHERE id_administrador = :id"
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_administrador = fila[0]
                self.id_usuario = fila[1]
                self.rol = fila[2]
                return True
            else:
                print("No se encontró un administrador con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar administrador por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM administradores WHERE id_administrador = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("Administrador eliminado")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass
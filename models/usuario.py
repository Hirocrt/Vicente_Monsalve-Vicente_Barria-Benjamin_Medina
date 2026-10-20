from models.conexion import ConexionDB


class Usuario:
    id_usuario: int
    nombre: str
    contrasena: str
    direccion: str
    telefono: str
    correo: str
    inicio_contrato: str
    salario: int

    def __init__(self, id_usuario: int = 0, nombre: str = "", contrasena: str = "", direccion: str = "",
                 telefono: str = "", correo: str = "", inicio_contrato: str = "", salario: int = 0):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.contrasena = contrasena
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.inicio_contrato = inicio_contrato
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id_usuario} | Nombre: {self.nombre} | Correo: {self.correo}"

    def obtenerTodos(self):
        try:
            c = ConexionDB()
            c.cursor.execute("SELECT id_usuario, nombre, correo, salario FROM usuarios ORDER BY id_usuario")
            return c.cursor.fetchall()
        except Exception as e:
            print(f"ERROR al obtener los usuarios: {e}")
            return []
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def insertar(self):
        try:
            c = ConexionDB()
            sql = """INSERT INTO usuarios (nombre, contrasena_hash, direccion, telefono, correo,
                    inicio_contrato, salario)
                    VALUES (:nom, :clave, :direc, :tel, :correo, TO_DATE(:fec, 'DD-MM-YYYY'), :salario)"""
            c.cursor.execute(sql, nom=self.nombre, clave=self.contrasena, direc=self.direccion,
                             tel=self.telefono, correo=self.correo, fec=self.inicio_contrato,
                             salario=self.salario)
            c.conexion.commit()
            print("¡Usuario insertado correctamente!")
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
            sql = """UPDATE usuarios SET nombre=:nom, contrasena_hash=:clave, direccion=:direc,
                    telefono=:tel, correo=:correo, inicio_contrato=TO_DATE(:fec, 'DD-MM-YYYY'),
                    salario=:salario WHERE id_usuario=:id"""
            c.cursor.execute(sql, id=self.id_usuario, nom=self.nombre, clave=self.contrasena,
                             direc=self.direccion, tel=self.telefono, correo=self.correo,
                             fec=self.inicio_contrato, salario=self.salario)
            c.conexion.commit()
            print("¡Usuario actualizado correctamente!")
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
            sql = """SELECT id_usuario, nombre, contrasena_hash, direccion, telefono, correo,
                    inicio_contrato, salario FROM usuarios WHERE id_usuario = :id"""
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()

            if fila:
                self.id_usuario = fila[0]
                self.nombre = fila[1]
                self.contrasena = fila[2]
                self.direccion = fila[3]
                self.telefono = fila[4]
                self.correo = fila[5]
                self.inicio_contrato = fila[6].strftime('%d-%m-%Y') if fila[6] else ""
                self.salario = fila[7]
                return True
            else:
                print("No se encontró un usuario con ese ID.")
                return False
        except Exception as e:
            print(f"ERROR al cargar usuario por ID: {e}")
            return False
        finally:
            try:
                c.conexion.close()
            except:
                pass

    def eliminar(self, idEliminar):
        try:
            c = ConexionDB()
            sql = "DELETE FROM usuarios WHERE id_usuario = :id"
            c.cursor.execute(sql, id=idEliminar)
            c.conexion.commit()
            print("¡Usuario eliminado correctamente!")
        except Exception as e:
            print(f"ERROR al eliminar en la Base de Datos: {e}")
        finally:
            try:
                c.conexion.close()
            except:
                pass
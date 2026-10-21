import oracledb
from models.conexion import ConexionDB


class Departamento:
    id_departamento: int
    nombre_departamento: str
    id_gerente: int 

    def __init__(self):
        self.id_departamento = None
        self.nombre_departamento = ""
        self.id_gerente = None
        self.nombre_gerente = None

    def __str__(self):
        return f"ID: {self.id_departamento} | Departamento: {self.nombre_departamento}"

    def existeEmpleado(self, idEmpleado):
        c = ConexionDB()
        try:
            sql = "SELECT 1 FROM empleados WHERE id_empleado = :id"
            c.cursor.execute(sql, id=idEmpleado)
            return c.cursor.fetchone() is not None
        finally:
            c.conexion.close()

    def validar(self):
        nombre = (self.nombre_departamento or "").strip()
        if nombre == "":
            raise ValueError("El nombre del departamento es obligatorio.")
        if len(nombre) > 100:
            raise ValueError("El nombre no puede superar los 100 caracteres.")
        self.nombre_departamento = nombre

        if self.id_gerente is not None:
            if self.id_gerente <= 0:
                raise ValueError("El ID del gerente debe ser un número positivo.")
            if not self.existeEmpleado(self.id_gerente):
                raise ValueError(f"No existe un empleado con ID {self.id_gerente}.")

    def insertar(self):
        self.validar()
        c = ConexionDB()
        try:
            sql = """INSERT INTO departamentos (nombre_departamento, id_gerente)
                     VALUES (:nom, :gerente)
                     RETURNING id_departamento INTO :id_nuevo"""
            id_nuevo = c.cursor.var(int)
            c.cursor.execute(sql, nom=self.nombre_departamento,
                             gerente=self.id_gerente, id_nuevo=id_nuevo)
            c.conexion.commit()
            self.id_departamento = id_nuevo.getvalue()[0]
        except oracledb.IntegrityError as error:
            c.conexion.rollback()
            if error.args[0].code == 1:
                raise ValueError("Ya existe un departamento con ese nombre.") from error
            raise
        finally:
            c.conexion.close()


    def obtenerTodos(self):
        c = ConexionDB()
        try:
            sql = """SELECT d.id_departamento, d.nombre_departamento, d.id_gerente, u.nombre
                     FROM departamentos d
                     LEFT JOIN empleados e ON d.id_gerente = e.id_empleado
                     LEFT JOIN usuarios u ON e.id_usuario = u.id_usuario
                     ORDER BY d.id_departamento"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        finally:
            c.conexion.close()


    def cargarPorID(self, idBuscado):
        c = ConexionDB()
        try:
            sql = """SELECT d.id_departamento, d.nombre_departamento, d.id_gerente, u.nombre
                     FROM departamentos d
                     LEFT JOIN empleados e ON d.id_gerente = e.id_empleado
                     LEFT JOIN usuarios u ON e.id_usuario = u.id_usuario
                     WHERE d.id_departamento = :id"""
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()
            if fila is None:
                return False
            self.id_departamento = fila[0]
            self.nombre_departamento = fila[1]
            self.id_gerente = fila[2]
            self.nombre_gerente = fila[3]
            return True
        finally:
            c.conexion.close()



    def actualizar(self):
        self.validar()
        c = ConexionDB()
        try:
            sql = """UPDATE departamentos
                     SET nombre_departamento = :nom, id_gerente = :gerente
                     WHERE id_departamento = :id"""
            c.cursor.execute(sql, nom=self.nombre_departamento,
                             gerente=self.id_gerente, id=self.id_departamento)
            
            if c.cursor.rowcount == 0:
                raise ValueError("No existe un departamento con ese ID.")
            c.conexion.commit()
        except oracledb.IntegrityError as error:
            c.conexion.rollback()

            if error.args[0].code == 1:
                raise ValueError("Ya existe un departamento con ese nombre.") from error
            raise
        finally:
            c.conexion.close()


    def contarEmpleados(self, idDepartamento):
  
        c = ConexionDB()
        try:
            sql = "SELECT COUNT(*) FROM empleados WHERE id_departamento = :id"
            c.cursor.execute(sql, id=idDepartamento)
            return c.cursor.fetchone()[0]
        finally:
            c.conexion.close()


    def eliminar(self, idEliminar):
        c = ConexionDB()
        try:
            sql = "DELETE FROM departamentos WHERE id_departamento = :id"
            c.cursor.execute(sql, id=idEliminar)
       
            if c.cursor.rowcount == 0:
                raise ValueError("No existe un departamento con ese ID.")
            c.conexion.commit()
        except oracledb.Error:
            c.conexion.rollback()
            raise
        finally:
            c.conexion.close()
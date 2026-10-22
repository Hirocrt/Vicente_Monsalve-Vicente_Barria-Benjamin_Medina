from datetime import datetime
import oracledb
from models.conexion import ConexionDB


class Proyecto:
    id_proyecto: int
    nombre: str
    descripcion: str
    fecha_inicio: datetime

    def __init__(self):
        self.id_proyecto = None
        self.nombre = ""
        self.descripcion = None
        self.fecha_inicio = None

    def __str__(self):
        return f"ID: {self.id_proyecto} | Proyecto: {self.nombre}"

    def validar(self):
        nombre = (self.nombre or "").strip()
        if nombre == "":
            raise ValueError("El nombre del proyecto es obligatorio.")
        if len(nombre) > 100:
            raise ValueError("El nombre no puede superar los 100 caracteres.")
        self.nombre = nombre

        descripcion = (self.descripcion or "").strip()
        if len(descripcion) > 500:
            raise ValueError("La descripción no puede superar los 500 caracteres.")
        self.descripcion = descripcion if descripcion != "" else None

        if self.fecha_inicio is None or self.fecha_inicio == "":
            raise ValueError("La fecha de inicio es obligatoria.")
        if isinstance(self.fecha_inicio, str):
            try:
                self.fecha_inicio = datetime.strptime(self.fecha_inicio.strip(), "%d-%m-%Y")
            except ValueError:
                raise ValueError("La fecha debe tener el formato día-mes-año, por ejemplo 25-03-2026.")

    
    def insertar(self):
        self.validar()
        c = ConexionDB()
        try:
            sql = """INSERT INTO proyectos (nombre, descripcion, fecha_inicio)
                     VALUES (:nom, :descr, :fec)
                     RETURNING id_proyecto INTO :id_nuevo"""
            id_nuevo = c.cursor.var(int)
            c.cursor.execute(sql, nom=self.nombre, descr=self.descripcion,
                             fec=self.fecha_inicio, id_nuevo=id_nuevo)
            c.conexion.commit()
            self.id_proyecto = id_nuevo.getvalue()[0]
        except oracledb.Error:
            c.conexion.rollback()
            raise
        finally:
            c.conexion.close()

    def obtenerTodos(self):
        c = ConexionDB()
        try:
            sql = """SELECT id_proyecto, nombre, descripcion, fecha_inicio
                     FROM proyectos
                     ORDER BY id_proyecto"""
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        finally:
            c.conexion.close()


    
    def cargarPorID(self, idBuscado):
        c = ConexionDB()
        try:
            sql = """SELECT id_proyecto, nombre, descripcion, fecha_inicio
                     FROM proyectos
                     WHERE id_proyecto = :id"""
            c.cursor.execute(sql, id=idBuscado)
            fila = c.cursor.fetchone()
            
            if fila is None:
                return False
            self.id_proyecto = fila[0]
            self.nombre = fila[1]
            self.descripcion = fila[2]
            self.fecha_inicio = fila[3]
            return True
        finally:
            c.conexion.close()


        
    def actualizar(self):
        self.validar()
        c = ConexionDB()
        try:
            sql = """UPDATE proyectos
                     SET nombre = :nom, descripcion = :descr, fecha_inicio = :fec
                     WHERE id_proyecto = :id"""
            c.cursor.execute(sql, nom=self.nombre, descr=self.descripcion,
                             fec=self.fecha_inicio, id=self.id_proyecto)
            
            if c.cursor.rowcount == 0:
                raise ValueError("No existe un proyecto con ese ID.")
            c.conexion.commit()
        except oracledb.Error:
            c.conexion.rollback()
            raise
        finally:
            c.conexion.close()  


    def contarAsociados(self, idProyecto):
        c = ConexionDB()
        try:
            c.cursor.execute(
                "SELECT COUNT(*) FROM registro_tiempo WHERE id_proyecto = :id",
                id=idProyecto)
            registros = c.cursor.fetchone()[0]

            c.cursor.execute(
                "SELECT COUNT(*) FROM empleado_proyecto WHERE id_proyecto = :id",
                id=idProyecto)
            asignaciones = c.cursor.fetchone()[0]
            return registros, asignaciones
        finally:
            c.conexion.close()

    def eliminar(self, idEliminar):
        c = ConexionDB()
        try:
            sql = "DELETE FROM proyectos WHERE id_proyecto = :id"
            c.cursor.execute(sql, id=idEliminar)
            # rowcount indica cuántas filas borró el DELETE
            if c.cursor.rowcount == 0:
                raise ValueError("No existe un proyecto con ese ID.")
            c.conexion.commit()
        except oracledb.Error:
            c.conexion.rollback()
            raise
        finally:
            c.conexion.close()    
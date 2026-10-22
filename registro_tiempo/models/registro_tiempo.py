class RegistroTiempo:
    def __init__(self, id_registro=None, id_asignacion=None, fecha=None, horas_trabajadas=None, descripcion=None):
        self.id_registro = id_registro
        self.id_asignacion = id_asignacion
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
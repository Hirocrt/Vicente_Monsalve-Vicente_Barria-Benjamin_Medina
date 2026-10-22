import oracledb

class ConexionDB:

    def __init__(self):
        try:
            # Conexión apuntando explícitamente a localhost
            self.conexion = oracledb.connect(
                user="  PRUEBAECO", 
                password="inacap", 
                host="localhost",
                port=1521,          
                service_name="xe"   
            )
            self.cursor = self.conexion.cursor()
            print("Conexión exitosa a localhost.")
            
        except Exception as e:
            print(f"ERROR CRÍTICO DE CONEXIÓN: Detalle: {e}")
            self.conexion = None
            self.cursor = None
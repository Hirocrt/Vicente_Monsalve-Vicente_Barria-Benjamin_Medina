from models.conexion import ConexionDB
from models.usuario import Usuario
from models.empleado import Empleado
from models.administrador import Administrador
from models.departamento import Departamento
from models.proyecto import Proyecto
from models.empleado_proyecto import EmpleadoProyecto
from models.registro_tiempo import RegistroTiempo
from models.informe import Informe



# para mostrar los datos de las tablas antes de hacer operaciones

def formatearFecha(fecha):
    if fecha is None or fecha == "":
        return ""
    if isinstance(fecha, str):
        return fecha
    return fecha.strftime("%d-%m-%Y")

def mostrarUsuarios():
    print("\nUsuarios disponibles:")
    for fila in Usuario().obtenerTodos():
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Correo: {fila[2]}")


def mostrarEmpleados():
    print("\nEmpleados disponibles:")
    for fila in Empleado().obtenerTodos():
        print(f"ID: {fila[0]} | Nombre: {fila[1]}")


def mostrarDepartamentos():
    print("\nDepartamentos disponibles:")
    for fila in Departamento().obtenerTodos():
        print(f"ID: {fila[0]} | Departamento: {fila[1]}")


def mostrarProyectos():
    print("\nProyectos disponibles:")
    for fila in Proyecto().obtenerTodos():
        print(f"ID: {fila[0]} | Proyecto: {fila[1]}")


#usuarios


def imprimirMenuUsuarios():
    print(" MENÚ USUARIOS ")
    print("1. Ver todos los usuarios")
    print("2. Agregar usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("0. Volver")
    print()


def menuUsuarios():
    usr = Usuario()

    while True:
        imprimirMenuUsuarios()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            listaUsuarios = usr.obtenerTodos()
            if listaUsuarios:
                print(" LISTA DE USUARIOS ")
                for fila in listaUsuarios:
                    print(f"ID: {fila[0]} | {fila[1]} | {fila[2]} | Salario: {fila[3]}")
            else:
                print("No hay usuarios registrados.")
            print()

        elif opcion == "2":
            try:
                print(" AGREGAR USUARIO ")
                usr.nombre = input("Nombre: ")
                usr.contrasena = input("Contraseña: ")
                usr.direccion = input("Dirección: ")
                usr.telefono = input("Teléfono: ")
                usr.correo = input("Correo: ")
                usr.inicio_contrato = input("Inicio de contrato (DD-MM-YYYY): ")
                usr.salario = int(input("Salario: "))

                usr.insertar()

            except ValueError:
                print("Error: El salario debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "3":
            listaUsuarios = usr.obtenerTodos()
            if not listaUsuarios:
                print("No hay usuarios para actualizar.\n")
                continue

            print(" ACTUALIZAR USUARIO ")
            for fila in listaUsuarios:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Correo: {fila[2]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del usuario a actualizar: "))

                if usr.cargarPorID(idSeleccionado):
                    print("\n(Presiona ENTER si no deseas modificar un campo)")

                    nuevoNombre = input(f"Nuevo nombre [{usr.nombre}]: ")
                    if nuevoNombre != "":
                        usr.nombre = nuevoNombre

                    nuevaContrasena = input("Nueva contraseña [no mostrar]: ")
                    if nuevaContrasena != "":
                        usr.contrasena = nuevaContrasena

                    nuevaDireccion = input(f"Nueva dirección [{usr.direccion}]: ")
                    if nuevaDireccion != "":
                        usr.direccion = nuevaDireccion

                    nuevoTelefono = input(f"Nuevo teléfono [{usr.telefono}]: ")
                    if nuevoTelefono != "":
                        usr.telefono = nuevoTelefono

                    nuevoCorreo = input(f"Nuevo correo [{usr.correo}]: ")
                    if nuevoCorreo != "":
                        usr.correo = nuevoCorreo

                    nuevoInicio = input(f"Nuevo inicio de contrato (DD-MM-YYYY) [{usr.inicio_contrato}]: ")
                    if nuevoInicio != "":
                        usr.inicio_contrato = nuevoInicio

                    nuevoSalario = input(f"Nuevo salario [{usr.salario}]: ")
                    if nuevoSalario != "":
                        usr.salario = int(nuevoSalario)

                    usr.actualizar()
            except ValueError:
                print("Error: Ingresaste un valor inválido para el ID o el salario.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "4":
            listaUsuarios = usr.obtenerTodos()
            if not listaUsuarios:
                print("No hay usuarios para eliminar.\n")
                continue

            print(" ELIMINAR USUARIO ")
            for fila in listaUsuarios:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Correo: {fila[2]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del usuario a eliminar: "))
                respuesta = input("Esto también elimina su empleado/administrador. ¿Seguro? (s/n): ")
                if respuesta.lower() == "s":
                    usr.eliminar(idSeleccionado)
                else:
                    print("Eliminación cancelada.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")


# EMPLEADOS

def imprimirMenuEmpleados():
    print(" MENÚ EMPLEADOS ")
    print("1. Ver todos los empleados")
    print("2. Agregar empleado")
    print("3. Actualizar empleado")
    print("4. Eliminar empleado")
    print("0. Volver")
    print()


def menuEmpleados():
    emp = Empleado()

    while True:
        imprimirMenuEmpleados()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            listaEmpleados = emp.obtenerTodos()
            if listaEmpleados:
                print(" LISTA DE EMPLEADOS ")
                for fila in listaEmpleados:
                    departamento = fila[2] if fila[2] else "Sin departamento"
                    print(f"ID: {fila[0]} | {fila[1]} | Departamento: {departamento}")
            else:
                print("No hay empleados registrados.")
            print()

        elif opcion == "2":
            try:
                print(" AGREGAR EMPLEADO ")
                mostrarUsuarios()
                emp.id_usuario = int(input("ID del usuario (debe existir): "))

                mostrarDepartamentos()
                textoDepartamento = input("ID del departamento (ENTER si no tiene): ")
                if textoDepartamento != "":
                    emp.id_departamento = int(textoDepartamento)
                else:
                    emp.id_departamento = None

                emp.insertar()

            except ValueError:
                print("Error: Los IDs deben ser números enteros.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "3":
            listaEmpleados = emp.obtenerTodos()
            if not listaEmpleados:
                print("No hay empleados para actualizar.\n")
                continue

            print(" ACTUALIZAR EMPLEADO ")
            for fila in listaEmpleados:
                print(f"ID: {fila[0]} | Nombre: {fila[1]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del empleado a actualizar: "))

                if emp.cargarPorID(idSeleccionado):
                    print("\n(Presiona ENTER si no deseas modificar un campo)")

                    nuevoUsuario = input(f"Nuevo ID de usuario [{emp.id_usuario}]: ")
                    if nuevoUsuario != "":
                        emp.id_usuario = int(nuevoUsuario)

                    mostrarDepartamentos()
                    nuevoDepartamento = input(f"Nuevo ID de departamento [{emp.id_departamento}] (escribe 'ninguno' para quitarlo): ")
                    if nuevoDepartamento.lower() == "ninguno":
                        emp.id_departamento = None
                    elif nuevoDepartamento != "":
                        emp.id_departamento = int(nuevoDepartamento)

                    emp.actualizar()
            except ValueError:
                print("Error: Ingresaste un valor inválido, los IDs deben ser números enteros.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "4":
            listaEmpleados = emp.obtenerTodos()
            if not listaEmpleados:
                print("No hay empleados para eliminar.\n")
                continue

            print(" ELIMINAR EMPLEADO ")
            for fila in listaEmpleados:
                print(f"ID: {fila[0]} | Nombre: {fila[1]}")

            try:
                idSeleccionado = int(input("Ingresa el ID a eliminar: "))
                emp.eliminar(idSeleccionado)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")


# ADMINISTRADORES

def imprimirMenuAdministradores():
    print(" MENÚ ADMINISTRADORES ")
    print("1. Ver todos los administradores")
    print("2. Agregar administrador")
    print("3. Actualizar administrador")
    print("4. Eliminar administrador")
    print("0. Volver")
    print()


def menuAdministradores():
    adm = Administrador()

    while True:
        imprimirMenuAdministradores()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            listaAdmins = adm.obtenerTodos()
            if listaAdmins:
                print(" LISTA DE ADMINISTRADORES ")
                for fila in listaAdmins:
                    print(f"ID: {fila[0]} | {fila[1]} | Rol: {fila[2]}")
            else:
                print("No hay administradores registrados.")
            print()

        elif opcion == "2":
            try:
                print(" AGREGAR ADMINISTRADOR ")
                mostrarUsuarios()
                adm.id_usuario = int(input("ID del usuario (debe existir): "))
                adm.rol = input("Rol: ")

                adm.insertar()

            except ValueError:
                print("Error: El ID del usuario debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "3":
            listaAdmins = adm.obtenerTodos()
            if not listaAdmins:
                print("No hay administradores para actualizar.\n")
                continue

            print(" ACTUALIZAR ADMINISTRADOR ")
            for fila in listaAdmins:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Rol: {fila[2]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del administrador a actualizar: "))

                if adm.cargarPorID(idSeleccionado):
                    print("\n(Presiona ENTER si no deseas modificar un campo)")

                    nuevoUsuario = input(f"Nuevo ID de usuario [{adm.id_usuario}]: ")
                    if nuevoUsuario != "":
                        adm.id_usuario = int(nuevoUsuario)

                    nuevoRol = input(f"Nuevo rol [{adm.rol}]: ")
                    if nuevoRol != "":
                        adm.rol = nuevoRol

                    adm.actualizar()
            except ValueError:
                print("Error: Ingresaste un valor inválido, los IDs deben ser números enteros.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "4":
            listaAdmins = adm.obtenerTodos()
            if not listaAdmins:
                print("No hay administradores para eliminar.\n")
                continue

            print(" ELIMINAR ADMINISTRADOR ")
            for fila in listaAdmins:
                print(f"ID: {fila[0]} | Nombre: {fila[1]} | Rol: {fila[2]}")

            try:
                idSeleccionado = int(input("Ingresa el ID a eliminar: "))
                adm.eliminar(idSeleccionado)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")


# DEPARTAMENTOS

def imprimirMenuDepartamentos():
    print(" MENÚ DEPARTAMENTOS ")
    print("1. Ver todos los departamentos")
    print("2. Buscar departamento por ID")
    print("3. Agregar departamento")
    print("4. Actualizar departamento")
    print("5. Eliminar departamento")
    print("0. Volver")
    print()


def menuDepartamentos():
    dep = Departamento()

    while True:
        imprimirMenuDepartamentos()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            listaDepartamentos = dep.obtenerTodos()
            if listaDepartamentos:
                print(" LISTA DE DEPARTAMENTOS ")
                for fila in listaDepartamentos:
                    print(f"ID: {fila[0]} | {fila[1]}")
            else:
                print("No hay departamentos registrados.")
            print()

        elif opcion == "2":
            try:
                idSeleccionado = int(input("Ingresa el ID del departamento: "))
                if dep.cargarPorID(idSeleccionado):
                    print(f"ID: {dep.id_departamento} | {dep.nombre_departamento}")
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "3":
            try:
                print(" AGREGAR DEPARTAMENTO ")
                dep.nombre_departamento = input("Nombre del departamento: ")
                dep.insertar()

            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "4":
            listaDepartamentos = dep.obtenerTodos()
            if not listaDepartamentos:
                print("No hay departamentos para actualizar.\n")
                continue

            print(" ACTUALIZAR DEPARTAMENTO ")
            for fila in listaDepartamentos:
                print(f"ID: {fila[0]} | Departamento: {fila[1]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del departamento a actualizar: "))

                if dep.cargarPorID(idSeleccionado):
                    print("\n(Presiona ENTER si no deseas modificar un campo)")

                    nuevoNombre = input(f"Nuevo nombre [{dep.nombre_departamento}]: ")
                    if nuevoNombre != "":
                        dep.nombre_departamento = nuevoNombre

                    dep.actualizar()
            except ValueError:
                print("Error: Ingresaste un valor inválido para el ID.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "5":
            listaDepartamentos = dep.obtenerTodos()
            if not listaDepartamentos:
                print("No hay departamentos para eliminar.\n")
                continue

            print(" ELIMINAR DEPARTAMENTO ")
            for fila in listaDepartamentos:
                print(f"ID: {fila[0]} | Departamento: {fila[1]}")

            try:
                idSeleccionado = int(input("Ingresa el ID a eliminar: "))

                if dep.cargarPorID(idSeleccionado):
                    cantidad = dep.contarEmpleados(dep.id_departamento)
                    print(f"Vas a eliminar el departamento '{dep.nombre_departamento}'.")
                    if cantidad > 0:
                        print(f"Atención: {cantidad} empleado(s) quedarán sin departamento.")
                    respuesta = input("¿Confirmas la eliminación? (s/n): ")
                    if respuesta.lower() == "s":
                        dep.eliminar(dep.id_departamento)
                    else:
                        print("Eliminación cancelada.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")


# PROYECTOS


def imprimirMenuProyectos():
    print(" MENÚ PROYECTOS ")
    print("1. Ver todos los proyectos")
    print("2. Buscar proyecto por ID")
    print("3. Agregar proyecto")
    print("4. Actualizar proyecto")
    print("5. Eliminar proyecto")
    print("0. Volver")
    print()


def menuProyectos():
    pro = Proyecto()

    while True:
        imprimirMenuProyectos()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "0":
            break

        try:
            if opcion == "1":
                listaProyectos = pro.obtenerTodos()
                if listaProyectos:
                    print(" LISTA DE PROYECTOS ")
                    for fila in listaProyectos:
                        descripcion = fila[2] if fila[2] else "Sin descripción"
                        print(f"ID: {fila[0]} | {fila[1]} | {descripcion} | Inicio: {formatearFecha(fila[3])}")
                else:
                    print("No hay proyectos registrados.")

            elif opcion == "2":
                texto = input("Ingresa el ID del proyecto: ").strip()
                if not texto.isdigit():
                    print("Error: El ID debe ser un número entero.")
                elif pro.cargarPorID(int(texto)):
                    descripcion = pro.descripcion if pro.descripcion else "Sin descripción"
                    print(f"ID: {pro.id_proyecto} | {pro.nombre} | {descripcion} | Inicio: {formatearFecha(pro.fecha_inicio)}")
                else:
                    print(f"No existe un proyecto con ID {texto}.")

            elif opcion == "3":
                print(" AGREGAR PROYECTO ")
                pro.nombre = input("Nombre: ")
                pro.descripcion = input("Descripción (ENTER si no tiene): ")
                pro.fecha_inicio = input("Fecha de inicio (DD-MM-YYYY): ")

                pro.insertar()
                print(f"Proyecto creado con ID {pro.id_proyecto}")

            elif opcion == "4":
                listaProyectos = pro.obtenerTodos()
                if not listaProyectos:
                    print("No hay proyectos para actualizar.")
                else:
                    print(" ACTUALIZAR PROYECTO ")
                    for fila in listaProyectos:
                        print(f"ID: {fila[0]} | Nombre: {fila[1]}")

                    texto = input("Ingresa el ID del proyecto a actualizar: ").strip()
                    if not texto.isdigit():
                        print("Error: El ID debe ser un número entero.")
                    elif pro.cargarPorID(int(texto)):
                        print("\n(Presiona ENTER si no deseas modificar un campo)")

                        nuevoNombre = input(f"Nuevo nombre [{pro.nombre}]: ")
                        if nuevoNombre != "":
                            pro.nombre = nuevoNombre

                        descripcionActual = pro.descripcion if pro.descripcion else ""
                        nuevaDescripcion = input(f"Nueva descripción [{descripcionActual}]: ")
                        if nuevaDescripcion != "":
                            pro.descripcion = nuevaDescripcion

                        nuevaFecha = input(f"Nueva fecha de inicio (DD-MM-YYYY) [{formatearFecha(pro.fecha_inicio)}]: ")
                        if nuevaFecha != "":
                            pro.fecha_inicio = nuevaFecha

                        pro.actualizar()
                        print("Proyecto actualizado")
                    else:
                        print(f"No existe un proyecto con ID {texto}.")

            elif opcion == "5":
                listaProyectos = pro.obtenerTodos()
                if not listaProyectos:
                    print("No hay proyectos para eliminar.")
                else:
                    print(" ELIMINAR PROYECTO ")
                    for fila in listaProyectos:
                        print(f"ID: {fila[0]} | Nombre: {fila[1]}")

                    texto = input("Ingresa el ID del proyecto a eliminar: ").strip()
                    if not texto.isdigit():
                        print("Error: El ID debe ser un número entero.")
                    elif pro.cargarPorID(int(texto)):
                        registros, asignaciones = pro.contarAsociados(pro.id_proyecto)
                        print(f"Vas a eliminar el proyecto '{pro.nombre}'.")
                        if registros > 0 or asignaciones > 0:
                            print(f"Atención: también se borrarán {registros} registro(s) de tiempo y {asignaciones} asignación(es) de empleados.")
                        respuesta = input("¿Confirmas la eliminación? (s/n): ")
                        if respuesta.lower() == "s":
                            pro.eliminar(pro.id_proyecto)
                            print("Proyecto eliminado")
                        else:
                            print("Eliminación cancelada.")
                    else:
                        print(f"No existe un proyecto con ID {texto}.")

            else:
                print("Opción no válida. Intenta nuevamente.")

        except ValueError as error:
            print("Error:", error)
        except Exception as e:
            print(f"Hubo un error inesperado: {e}")
        finally:
            print()



# EMPLEADOS EN PROYECTOS

def imprimirMenuAsignaciones():
    print(" MENÚ EMPLEADOS EN PROYECTOS ")
    print("1. Ver empleados de un proyecto")
    print("2. Ver todas las asignaciones")
    print("3. Asignar empleado a un proyecto")
    print("4. Mover empleado a otro proyecto")
    print("5. Quitar empleado de un proyecto")
    print("0. Volver")
    print()


def menuAsignaciones():
    asi = EmpleadoProyecto()

    while True:
        imprimirMenuAsignaciones()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            try:
                mostrarProyectos()
                idProyecto = int(input("Ingresa el ID del proyecto: "))
                listaEmpleados = asi.obtenerPorProyecto(idProyecto)
                if listaEmpleados:
                    print(" EMPLEADOS DEL PROYECTO ")
                    for fila in listaEmpleados:
                        print(f"Asignación: {fila[0]} | Empleado ID: {fila[1]} | Nombre: {fila[2]}")
                else:
                    print("Ese proyecto no tiene empleados asignados.")
            except ValueError:
                print("Error: El ID del proyecto debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "2":
            listaAsignaciones = asi.obtenerTodos()
            if listaAsignaciones:
                print(" LISTA DE ASIGNACIONES ")
                for fila in listaAsignaciones:
                    print(f"Asignación: {fila[0]} | Empleado: {fila[2]} (ID {fila[1]}) | Proyecto: {fila[4]} (ID {fila[3]})")
            else:
                print("No hay asignaciones registradas.")
            print()

        elif opcion == "3":
            try:
                print(" ASIGNAR EMPLEADO A PROYECTO ")
                mostrarProyectos()
                asi.id_proyecto = int(input("ID del proyecto: "))

                mostrarEmpleados()
                asi.id_empleado = int(input("ID del empleado: "))

                asi.insertar()

            except ValueError:
                print("Error: Los IDs deben ser números enteros.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "4":
            listaAsignaciones = asi.obtenerTodos()
            if not listaAsignaciones:
                print("No hay asignaciones para mover.\n")
                continue

            print(" MOVER EMPLEADO A OTRO PROYECTO ")
            for fila in listaAsignaciones:
                print(f"Asignación: {fila[0]} | Empleado: {fila[2]} | Proyecto: {fila[4]} (ID {fila[3]})")

            try:
                idSeleccionado = int(input("Ingresa el ID de la asignación a mover: "))

                if asi.cargarPorID(idSeleccionado):
                    mostrarProyectos()
                    asi.id_proyecto = int(input("Ingresa el ID del nuevo proyecto: "))
                    asi.actualizar()
            except ValueError:
                print("Error: Los IDs deben ser números enteros.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "5":
            listaAsignaciones = asi.obtenerTodos()
            if not listaAsignaciones:
                print("No hay asignaciones para eliminar.\n")
                continue

            print(" QUITAR EMPLEADO DE UN PROYECTO ")
            for fila in listaAsignaciones:
                print(f"Asignación: {fila[0]} | Empleado: {fila[2]} | Proyecto: {fila[4]}")

            try:
                idSeleccionado = int(input("Ingresa el ID de la asignación a eliminar: "))
                respuesta = input("¿Confirmas que quieres quitar al empleado del proyecto? (s/n): ")
                if respuesta.lower() == "s":
                    asi.eliminar(idSeleccionado)
                else:
                    print("Eliminación cancelada.")
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")



# REGISTRO DE TIEMPO


def imprimirMenuRegistroTiempo():
    print(" MENÚ REGISTRO DE TIEMPO ")
    print("1. Ver todos los registros")
    print("2. Ver registros de un empleado")
    print("3. Ver registros de un proyecto")
    print("4. Agregar registro")
    print("5. Actualizar registro")
    print("6. Eliminar registro")
    print("0. Volver")
    print()


def menuRegistroTiempo():
    reg = RegistroTiempo()

    while True:
        imprimirMenuRegistroTiempo()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            listaRegistros = reg.obtenerTodos()
            if listaRegistros:
                print(" LISTA DE REGISTROS DE TIEMPO ")
                for fila in listaRegistros:
                    print(f"Registro: {fila[0]} | Empleado: {fila[1]} | Proyecto: {fila[2]} | Fecha: {formatearFecha(fila[3])} | Horas: {fila[4]} | Tareas: {fila[5]}")
            else:
                print("No hay registros de tiempo.")
            print()

        elif opcion == "2":
            try:
                mostrarEmpleados()
                idEmpleado = int(input("Ingresa el ID del empleado: "))
                listaRegistros = reg.obtenerPorEmpleado(idEmpleado)
                if listaRegistros:
                    print(" REGISTROS DEL EMPLEADO ")
                    for fila in listaRegistros:
                        print(f"Registro: {fila[0]} | Proyecto: {fila[1]} | Fecha: {formatearFecha(fila[2])} | Horas: {fila[3]} | Tareas: {fila[4]}")
                else:
                    print("Ese empleado no tiene registros de tiempo.")
            except ValueError:
                print("Error: El ID del empleado debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "3":
            try:
                mostrarProyectos()
                idProyecto = int(input("Ingresa el ID del proyecto: "))
                listaRegistros = reg.obtenerPorProyecto(idProyecto)
                if listaRegistros:
                    print(" REGISTROS DEL PROYECTO ")
                    for fila in listaRegistros:
                        print(f"Registro: {fila[0]} | Empleado: {fila[1]} | Fecha: {formatearFecha(fila[2])} | Horas: {fila[3]} | Tareas: {fila[4]}")
                else:
                    print("Ese proyecto no tiene registros de tiempo.")
            except ValueError:
                print("Error: El ID del proyecto debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "4":
            try:
                print(" AGREGAR REGISTRO DE TIEMPO ")
                mostrarEmpleados()
                reg.id_empleado = int(input("ID del empleado: "))

                mostrarProyectos()
                reg.id_proyecto = int(input("ID del proyecto: "))

                reg.fecha = input("Fecha (DD-MM-YYYY): ")
                reg.horas_trabajadas = float(input("Horas trabajadas (ingresar con punto): ").replace(",", "."))
                reg.tareas = input("Tareas realizadas: ")

                reg.insertar()

            except ValueError:
                print("Error: Los IDs deben ser números enteros y las horas un número, por ejemplo 7.5")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            finally:
                print()

        elif opcion == "5":
            listaRegistros = reg.obtenerTodos()
            if not listaRegistros:
                print("No hay registros para actualizar.\n")
                continue

            print(" ACTUALIZAR REGISTRO DE TIEMPO ")
            for fila in listaRegistros:
                print(f"Registro: {fila[0]} | Empleado: {fila[1]} | Proyecto: {fila[2]} | Fecha: {formatearFecha(fila[3])} | Horas: {fila[4]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del registro a actualizar: "))

                if reg.cargarPorID(idSeleccionado):
                    print("\n(Presiona ENTER si no deseas modificar un campo)")

                    nuevaFecha = input(f"Nueva fecha (DD-MM-YYYY) [{reg.fecha}]: ")
                    if nuevaFecha != "":
                        reg.fecha = nuevaFecha

                    nuevasHoras = input(f"Nuevas horas trabajadas [{reg.horas_trabajadas}]: ")
                    if nuevasHoras != "":
                        reg.horas_trabajadas = float(nuevasHoras.replace(",", "."))

                    nuevasTareas = input(f"Nuevas tareas [{reg.tareas}]: ")
                    if nuevasTareas != "":
                        reg.tareas = nuevasTareas

                    reg.actualizar()
            except ValueError:
                print("Error: Ingresaste un valor inválido para el ID o las horas.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "6":
            listaRegistros = reg.obtenerTodos()
            if not listaRegistros:
                print("No hay registros para eliminar.\n")
                continue

            print(" ELIMINAR REGISTRO DE TIEMPO ")
            for fila in listaRegistros:
                print(f"Registro: {fila[0]} | Empleado: {fila[1]} | Proyecto: {fila[2]} | Fecha: {formatearFecha(fila[3])} | Horas: {fila[4]}")

            try:
                idSeleccionado = int(input("Ingresa el ID del registro a eliminar: "))
                reg.eliminar(idSeleccionado)
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Hubo un error inesperado: {e}")
            print()

        elif opcion == "0":
            break

        else:
            print("Opción no válida. Intenta nuevamente.\n")




# INFORMES


def cortar(texto, ancho):
    if texto is None:
        return ""
    return str(texto)[:ancho]


def mostrarInformeEmpleados():
    lista = Informe().obtenerInformeEmpleados()
    print("=== INFORME DE EMPLEADOS ===")
    if not lista:
        print("No hay empleados registrados.")
        return

    print(f"{'ID':<4} | {'Nombre':<20} | {'Correo':<24} | {'Teléfono':<12} | {'Departamento':<20} | {'Inicio':<10} | {'Salario':<10}")
    print("-" * 118)
    for fila in lista:
        departamento = fila[4] if fila[4] else "Sin departamento"
        salario = f"${fila[6]:,.0f}".replace(",", ".")
        print(f"{fila[0]:<4} | {cortar(fila[1], 20):<20} | {cortar(fila[2], 24):<24} | {cortar(fila[3], 12):<12} | {cortar(departamento, 20):<20} | {formatearFecha(fila[5]):<10} | {salario:<10}")
    print("-" * 118)
    print(f"Total de empleados: {len(lista)}")


def mostrarInformeDepartamentos():
    lista = Informe().obtenerInformeDepartamentos()
    print("=== INFORME DE DEPARTAMENTOS ===")
    if not lista:
        print("No hay departamentos registrados.")
        return

    print(f"{'ID':<4} | {'Departamento':<28} | {'Empleados':<9}")
    print("-" * 50)
    for fila in lista:
        print(f"{fila[0]:<4} | {cortar(fila[1], 28):<28} | {fila[2]:<9}")
    print("-" * 50)
    print(f"Total de departamentos: {len(lista)}")


def mostrarInformeProyectos():
    lista = Informe().obtenerInformeProyectos()
    print("=== INFORME DE PROYECTOS ===")
    if not lista:
        print("No hay proyectos registrados.")
        return

    print(f"{'ID':<4} | {'Proyecto':<25} | {'Inicio':<10} | {'Empleados':<9} | {'Horas':<8} | {'Descripción':<30}")
    print("-" * 101)
    totalHoras = 0
    for fila in lista:
        descripcion = fila[2] if fila[2] else "Sin descripción"
        totalHoras = totalHoras + float(fila[5])
        print(f"{fila[0]:<4} | {cortar(fila[1], 25):<25} | {formatearFecha(fila[3]):<10} | {fila[4]:<9} | {str(fila[5]):<8} | {cortar(descripcion, 30):<30}")
    print("-" * 101)
    print(f"Total de proyectos: {len(lista)} | Horas trabajadas en total: {round(totalHoras, 2)}")


def mostrarInformeRegistros():
    lista = Informe().obtenerInformeRegistros()
    print("=== INFORME DE REGISTROS DE TIEMPO ===")
    if not lista:
        print("No hay registros de tiempo.")
        return

    print(f"{'ID':<4} | {'Empleado':<20} | {'Departamento':<16} | {'Proyecto':<20} | {'Fecha':<10} | {'Horas':<6} | {'Tareas':<25}")
    print("-" * 119)
    totalHoras = 0
    for fila in lista:
        departamento = fila[2] if fila[2] else "Sin departamento"
        totalHoras = totalHoras + float(fila[5])
        print(f"{fila[0]:<4} | {cortar(fila[1], 20):<20} | {cortar(departamento, 16):<16} | {cortar(fila[3], 20):<20} | {formatearFecha(fila[4]):<10} | {str(fila[5]):<6} | {cortar(fila[6], 25):<25}")
    print("-" * 119)
    print(f"Total de registros: {len(lista)} | Horas trabajadas en total: {round(totalHoras, 2)}")


def imprimirMenuInformes():
    print(" MENÚ INFORMES ")
    print("1. Informe de empleados")
    print("2. Informe de departamentos")
    print("3. Informe de proyectos")
    print("4. Informe de registros de tiempo")
    print("5. Informe completo (los cuatro)")
    print("0. Volver")
    print()


def menuInformes():
    while True:
        imprimirMenuInformes()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "0":
            break

        try:
            if opcion == "1":
                mostrarInformeEmpleados()

            elif opcion == "2":
                mostrarInformeDepartamentos()

            elif opcion == "3":
                mostrarInformeProyectos()

            elif opcion == "4":
                mostrarInformeRegistros()

            elif opcion == "5":
                mostrarInformeEmpleados()
                print()
                mostrarInformeDepartamentos()
                print()
                mostrarInformeProyectos()
                print()
                mostrarInformeRegistros()

            else:
                print("Opción no válida. Intenta nuevamente.")

        except Exception as e:
            print(f"Hubo un error inesperado: {e}")
        finally:
            print()

# MENÚ PRINCIPAL


# ---------------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------------

def imprimirMenuPrincipal():
    print(" Sistema de gestión ")
    print("1. Usuarios")
    print("2. Empleados")
    print("3. Administradores")
    print("4. Departamentos")
    print("5. Proyectos")
    print("6. Empleados en proyectos")
    print("7. Registro de tiempo")
    print("8. Informes")
    print("0. Salir")
    print()


def probarConexion():
    try:
        c = ConexionDB()
        if c.conexion is None:
            return False
        c.conexion.close()
        return True
    except Exception as e:
        print(f"Hubo un error inesperado: {e}")
        return False


if probarConexion():
    while True:
        imprimirMenuPrincipal()
        opcion = input("Ingresa una opción: ")
        print()

        if opcion == "1":
            menuUsuarios()
        elif opcion == "2":
            menuEmpleados()
        elif opcion == "3":
            menuAdministradores()
        elif opcion == "4":
            menuDepartamentos()
        elif opcion == "5":
            menuProyectos()
        elif opcion == "6":
            menuAsignaciones()
        elif opcion == "7":
            menuRegistroTiempo()
        elif opcion == "8":
            menuInformes()
        elif opcion == "0":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Intenta nuevamente.\n")
else:
    print("No se pudo conectar a la base de datos. Revisa que Oracle esté encendido y los datos de models/conexion.py.")
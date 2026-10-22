Actúa como un desarrollador de Python especializado en programación orientada a objetos, Oracle y trabajo colaborativo con GitHub. Soy estudiante y necesito implementar mi parte de un proyecto grupal llamado EcoTech Solutions.

## Mi responsabilidad
Me tocó hacer el CRUD completo (CREATE, READ, UPDATE y DELETE) de dos tablas: DEPARTAMENTOS y PROYECTOS, según un diagrama UML.
- UML de Departamentos: atributos nombreDepartamento y gerente; métodos crear(), editar(), buscar() y eliminar().
- UML de Proyectos: atributos nombre, descripción y fecha_inicio; métodos Crear(), Editar() y Eliminar().
- No debo implementar las tablas de mis compañeros (usuarios, empleados, administradores, registro_tiempo).


## Qué debe hacer el código
CREATE: validar antes de guardar, hacer INSERT con RETURNING ... INTO para obtener el ID generado, y commit.
READ: obtenerTodos() y cargarPorID() (este es el buscar del UML). En Departamentos, usar LEFT JOIN con empleados y usuarios para mostrar el nombre del gerente. Mensajes claros cuando no hay resultados.
UPDATE: seguir el patrón de clase (mostrar lista, elegir ID, cargar el objeto, ENTER mantiene el valor actual). Reutilizar validar() y revisar rowcount.
DELETE: pedir confirmación (solo "s" borra) y avisar el efecto. En Departamentos, cuántos empleados quedarán sin departamento. En Proyectos, cuántos registros de tiempo y asignaciones se borrarán por el CASCADE.

## Validaciones
- Departamentos: nombre obligatorio y de máximo 100 caracteres, nombre único, y gerente opcional que debe existir en empleados (solo leer esa tabla).
- Proyectos: nombre obligatorio y de máximo 100 caracteres, descripción opcional de máximo 500 (vacía se guarda como NULL), y fecha obligatoria en formato día-mes-año, convertida con datetime.strptime para rechazar fechas imposibles.



## Forma de trabajar
Avanzamos paso a paso: primero el CREATE, luego READ, UPDATE y DELETE, de Departamentos y después de Proyectos. En cada paso indícame en qué archivo va cada fragmento, cómo probarlo (caso correcto, datos inválidos y consulta sin resultados) y cómo explicarlo.

## GitHub
Explícame cómo trabajar en ramas propias (departamentos y proyectos), agregar los archivos por nombre con git add (sin incluir models/conexion.py), hacer commits claros, subir con git push y crear un Pull Request hacia main sin pisar el trabajo de mis compañeros. Incluye .gitignore con _pycache_/ y *.pyc.







## Prompt principal para contextualizar
Soy un estudiante de primer año de ingenieria informatica y ahora estoy empezando un proyecto principalmente centrado en el CRUD sobre la empresa EcoTech Solutions la cual tiene problema sobre su base de datos y como se ordenan las tablas de usuario-empleado-administrador-proyecto-departamento lo que te voy a pedir principalmente es ayuda y que des ideas sobre que cosas agreagar a la estructura base de las funciones del crud

## Base de datos

Basandote en la problematica de ecotech y en el uml que te pase antes quiero que me ayudes a complementar la base de datos que estoy creando siendo que al tratar de ejecutarla me esta dando problemas y que tambien me des sugerencias de como poder mejorar la base de datos pero que antes de mandarme el codigo de la base de datos me digas los errores y las sugerencias que propones para que la base de datos sea más eficiente

## Prompt usuario
En base al codigo que tengo sobre la clase usuario busca errores que pueda tener y tambien propone sugerencias primero sin devolverme el codigo si no que dime que cosas tengo mal y las propuestas tuyas por escrito para poder ver que puedo tomar en cuenta y que no es tan necesario utilizar 


## Prompt empleado y administrador 
Teniendo en cuanta que los "roles" de empleado y administrador van directamente ligados a usuario necesito que veas si es correcta la manera en la que los uni y si no ocurriria algun error en las tablas al registrar a los usuarios con las tablas de los roles de empleado y administrador y que tambien se va a usar la tabla departamento en la clase usuario como estaba en la base de datos.

## Prompt para el main
Teniendo en cuanta que el main va a ser bastante extenso tanto como por las diferentes clases que hay en el proyecto y sus diferentes funciones primero vamos a empezar una clase a la vez como seria primero la de usuario, despues empleado, etc. Ya empece un poco el main pero es bastante rustico y estoy dejando bastantes cosas sin visualizarlas y que me pueden tirar errores a futuro como pueden ser los errores al eliminar un proyecto que este ligado a un usuario pero primero empecemos por los usuarios y asi consevutivamente al igual que antes quiero que primero me muestres mis errores en el codigo y que me des propuestas o soluciones (en texto, no escribas el codigo completo arreglando errores y con sugerencias sin que yo te diga) con la primera cosa que quiero comenzar es agregando una funciones que al inicio de cada operacion para asignar empleados a ciertos departamentos o departamentos disponibles se muestren las entidades disponibles para no tener que estas buscando todo el tiempo las entidades que existen.


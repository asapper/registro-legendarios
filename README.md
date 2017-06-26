# Registro de Legendarios
Proyecto hecho para Casa de Dios. Mantiene el registro de todos los Legendarios.

## Instrucciones de Uso
Para correr este proyecto localmente sigue las siguientes instrucciones.

1.  Clona este proyecto localmente.
2. Asegúrate de tener Python >=3.6-32 instalado.
3. (Recomendado) Crea un *virtual environment* para este proyecto.
4. Instala los paquetes requeridos por este proyecto, usando el siguiente comando:

`pip install -r requirements.txt`

**NOTA:** el archivo *requirements.txt* es parte de este proyecto.

5. Crea un usuario y una base de datos en Postgresql usando los siguientes comandos:

`CREATE USER <name>`
Si este comando es ejecutado correctamente deberías ver una respuesta que dice `CREATE ROLE` en tu Terminal.

`CREATE DATABASE <database_name> OWNER <name>`
En <name> usa el nombre que usaste para crear un usuario anteriormente. Si este comando es ejecutado correctamente deberías ver una respuesta que dice `CREATE DATABASE` en tu Terminal.

6. Modifica la configuración de la base de datos en el archivo *Legendarios/settings.py*. Cambia los siguientes datos a los datos de la basa de datos creada anteriormente:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name>',
        'USER': '<name>',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
`

7. Inicializa tu base de datos usando el siguiente comando:

`python manage.py migrate`

**NOTA:** al momento de escritura de este archivo, el proyecto usa Postgresql como base de datos para development.

8. Corre el proyecto usando el siguiente comando:

`python manage.py runserver`

Ve a `localhost:8000` para ver el proyecto corriendo.


## Usando el programa
Para usar el programa necesitarás hacer un par de cosas más.

1. Crear un super usuario:

`python manage.py createsuperuser`

**NOTA:** este superusuario tiene acceso al dashboard de Administrador en `localhost:8000/admin`, pero no tiene acceso al registro de Legendarios.

2. Crear usuarios en el sistema: lo puedes hacer al registrarte en la página de inicio del programa.

**NOTA:** cualquier usuario que registres manualmente tiene acceso al registro de Legendarios, pero no tiene acceso al dashboard de Administrador.

## Comentarios/Preguntas
Si tienes algún comentario o pregunta, envíame un correo a andysapper1@gmail.com

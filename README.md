# Registro de Legendarios
Proyecto hecho para Casa de Dios. Mantiene el registro de todos los Legendarios.

## Instrucciones de Uso

### Uso en Docker
Para correr este proyecto en contenedores de Docker sigue las siguientes intrucciones.

1. Clona este proyecto.
2. Inicia Docker en tu ordenador.
3. Corre el siguiente comando para iniciar los contenedores:

```./startup_scipt.sh```

Esto habrá creado el proyecto. Puedes accederlo en `localhost:8000`. Este script ha creado un super-usuario en la base de datos. Los datos de ese usuario son:

**Usuario:** legendario_1

**Contraseña:** legendarios_gt1

Con estos datos puedes acceder la página de administracion (`localhost:8000/admin`) y la página de registros (`localhost:8000/registros`).


**NOTA:** existen varios campos que debes configurar de acuerdo a tu servidor. A continuación encontrarás una lista con información de configuración que debes hacer.

1. La configuración de tu base de datos debes hacerla en el archivo *.env*. Allí debes cambiar la información necesaria para tu 'Name', 'User', 'Host', 'Port' de la base de datos.

2. Debes cambiar los hosts que aceptes en tu servidor en el archivo *Legendarios/settings.py*. En ALLOWED_HOSTS debes incluir los URLs de tu página que accesa este proyecto. Puedes encontrar más información acerca de este tema [aquí](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-ALLOWED_HOSTS).

3. Debes cambiar la variable SECURE_HSTS_SECONDS en el archivo *Legendarios/settings.py*. Para cambiar esta variable debes hacer pruebas en base a tu servidor. Puedes encontrar más información acerca de este tema [aquí](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECURE_HSTS_SECONDS).

4. Debes cambiar la variable STATIC_ROOT en el archivo *Legendarios/settings.py*. Aquí debes especificar el path en tu servidor donde tus archivos serán guardados. [Sigue las instrucciones para hacer esto](https://docs.djangoproject.com/en/1.11/howto/static-files/#deployment). Para una configuración más extensiva, [sigue estas instrucciones](https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/).


### Uso local
Para correr este proyecto localmente sigue las siguientes instrucciones.

1. Clona este proyecto localmente.
2. Asegúrate de tener Python >=3.6-32 instalado.
3. (Recomendado) Crea un *virtual environment* para este proyecto.
4. Instala los paquetes requeridos por este proyecto, usando el siguiente comando:

```pip install -r requirements.txt```

**NOTA:** el archivo *requirements.txt* es parte de este proyecto.

5. Crea un usuario y una base de datos en Postgresql usando los siguientes comandos:

```CREATE USER <name>```

Si este comando es ejecutado correctamente deberías ver una respuesta que dice `CREATE ROLE` en tu Terminal.

```CREATE DATABASE <database_name> OWNER <name>```

En <name> usa el nombre que usaste para crear un usuario anteriormente. Si este comando es ejecutado correctamente deberías ver una respuesta que dice `CREATE DATABASE` en tu Terminal.

6. Modifica la configuración de la base de datos en el archivo *Legendarios/local_settings.py*. Cambia los siguientes datos a los datos de la basa de datos creada anteriormente:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name>',
        'USER': '<name>',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

7. Inicializa tu base de datos usando el siguiente comando:

```python manage.py migrate```

**NOTA:** al momento de escritura de este archivo, el proyecto usa Postgresql como base de datos para development.

8. Ejecuta el siguiente comando para crear diferentes permisos y un superusuario:

```python manage.py shell < init_script.py```

Este script ha creado un super-usuario en la base de datos. Los datos de ese usuario son:

**Usuario:** legendario_1

**Contraseña:** legendarios_gt1

9. Corre el proyecto usando el siguiente comando:

```python manage.py runserver```

Ve a `127.0.0.1:8000/registros` para ver el proyecto corriendo.


## Usando el programa
Usando el programa puedes hacer un par de cosas más.

1. Crear un super usuario:

```python manage.py createsuperuser```

**NOTA:** este superusuario tiene acceso al dashboard de Administrador en `localhost:8000/admin`, pero no tiene acceso al registro de Legendarios.

2. Crear usuarios en el sistema: lo puedes hacer al registrarte en la página de inicio del programa.

**NOTA:** cualquier usuario que registres manualmente tiene acceso al registro de Legendarios, pero no tiene acceso al dashboard de Administrador.

## Comentarios/Preguntas
Si tienes algún comentario o pregunta, envíame un correo a andysapper1@gmail.com

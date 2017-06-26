# Registro de Legendarios
Proyecto hecho para Casa de Dios. Mantiene el registro de todos los Legendarios.

## Instrucciones de Uso
Para correr este proyecto localmente sigue las siguientes instrucciones.

1.  Clona este proyecto localmente.
2. Asegúrate de tener Python instalado.
3. (Recomendado) Crea un *virtual environment* para este proyecto.
4. Instala los paquetes requeridos por este proyecto, usando el siguiente comando:

`pip install -r requirements.txt`

**NOTA:** el archivo *requirements.txt* es parte de este proyecto.

5. Inicializa tu base de datos usando el siguiente comando:

`python manage.py migrate`

**NOTA:** al momento de escritura de este archivo, el proyecto usa SQLite como base de datos para development.

6. Corre el proyecto usando el siguiente comando:

`python manage.py runserver`

Ve a `localhost:8000` para ver el proyecto corriendo.


## Usando el programa
Para usar el programa necesitarás hacer un par de cosas más.

1. Crear un super usuario:

`python manage.py createsuperuser`

2. Crear usuarios en el sistema: lo puedes hacer al registrarte en la página de inicio del programa.

## Comentarios/Preguntas
Si tienes algún comentario o pregunta, envíame un correo a andysapper1@gmail.com

este es el primer proyecto en si el cualintentare crear una web que me ayude a entender mejor lo de ermua.

1. Cree la carpeta scrapin1 
2. el entorno virtual
3. Instalar las dependencias[
    comienzo por el back:
    pip install django instaloader django-cors-headers
    //django-cors-headers (para permitir la comunicación entre el frontend y el backend).
]
4. creo mi app de django: django-admin startproject backend

5. Creo una app para gestionar las publicaciones de Instagram: 
cd backend 
python manage.py startapp instagram_posts

  
  #  settings.py
6. 
Cuando creas un proyecto en Django, el archivo settings.py actúa como el cerebro de tu aplicación. Aquí se configuran todas las opciones y ajustes que definirán cómo se comporta tu aplicación.

INSTALLED_APPS = [
    'etc',
    'corsheaders',
    'instagram_posts'
]
Es una lista de aplicaciones que forman parte de mi proyecto Django. Cada aplicación es un módulo de Python que contiene modelos, vistas, plantillas y otros componentes específicos de una funcionalidad particular. Al agregar una aplicación a esta lista, le decimos a Django que debe cargar esa aplicación y hacer que sus funcionalidades estén disponibles en el proyecto.

corsheaders:Es crucial cuando tienes un frontend (como Angular) y un backend (Django) separados, y ambos se ejecutan en diferentes dominios. Al agregarla, permites que tu frontend pueda hacer solicitudes a tu backend, evitando problemas de seguridad relacionados con el origen de las solicitudes (CORS, Cross-Origin Resource Sharing). Al agregarla, se habilita el mecanismo CORS, que permite que el backend envíe los encabezados necesarios para que el frontend pueda realizar las solicitudes.

instagram_posts: Es la aplicación que hemos creado para manejar los posts de Instagram. Al agregar tu aplicación personalizada, le estás diciendo a Django que debe buscar los modelos, vistas y URL patterns definidos en esa aplicación. Esto es fundamental para que puedas acceder a las funcionalidades que has creado para manejar los posts de Instagram.

7.  MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ## otros middlewares
    El middleware de CORS debe estar antes de otros middlewares como el de CommonMiddleware para que funcione correctamente
]

Un middleware es una pieza de software que intercepta las solicitudes HTTP entrantes y las respuestas salientes.Es un filtro que modifica la solicitud o la respuesta antes de que llegue a la vista o después de que se haya generado.

 ## Intercepta solicitudes: Cuando una solicitud HTTP llega a tu servidor Django, CorsMiddleware la intercepta antes de que llegue a tu vista.
## Verifica el origen: Comprueba si la solicitud proviene de un origen autorizado (es decir, si el dominio desde el que se realiza la solicitud está permitido).
## Agrega encabezados CORS: Si el origen es válido, añade los encabezados CORS necesarios a la respuesta. Estos encabezados le indican al navegador del cliente que permita la solicitud, a pesar de que proviene de un dominio diferente.

##  Aseguramos que la aplicación Django pueda manejar correctamente las solicitudes que provienen del frontend (Angular), que probablemente se ejecute en un dominio diferente. Esto es esencial para evitar errores de CORS que podrían impedir que tu aplicación funcione correctamente.

8. CORS_ORIGIN_WHITELIST = [
    'http://localhost:4200',  # El puerto donde Angular servirá la app
]
Indicamos a Django qué dominios están autorizados a realizar solicitudes a la API.
    Explicación detallada:
        CORS_ORIGIN_WHITELIST: Es una lista de URLs que Django considerará seguras para recibir solicitudes.
        'http://localhost:4200': En este caso se especifica que solo las solicitudes provenientes de mi aplicación Angular, que probablemente estés ejecutando localmente en el puerto 4200, serán permitidas.

9. MEDIA_URL = '/media/'  es la dirección web que se mostrará en el navegador para acceder a los archivos multimedia.
   MEDIA_ROOT = BASE_DIR / 'media' es la ruta real en tu servidor donde se almacenarán físicamente esos archivos.
   

MEDIA_URL = '/media/' => Define la URL base que se utilizará para acceder a los archivos multimedia que se suban  a la aplicación (imágenes, videos, documentos, etc.). Imagina que subes una imagen llamada "mi_imagen.jpg" y la guardas en la carpeta "media" de tu proyecto. Para acceder a esta imagen desde tu navegador, utilizarás la siguiente URL: http://tudominio.com/media/mi_imagen.jpg. La parte /media/ es la que está definida en MEDIA_URL.

MEDIA_ROOT = BASE_DIR / 'media'=>Especifica la ubicación física en tu servidor donde se almacenarán los archivos multimedia que subas, BASE_DIR se refiere al directorio raíz del proyecto.Indicamos que los archivos multimedia se guardarán en una subcarpeta llamada "media" dentro de ese directorio raíz. Por ejemplo, si tu proyecto está en /var/www/miproyecto, los archivos se guardarán en /var/www/miproyecto/media.Si la carpeta no existe, Django intentará crear los archivos multimedia en esa ruta y, al no encontrarla, generará un error.

# Agrego bloque de configuración LOGGING en settin.py
* version: 1: Esto simplemente indica que estás utilizando la versión 1 del sistema de logging en Python, 
que es la versión estándar y actual.
* disable_existing_loggers: False: Con esto le dices a Django que no deshabilite los loggers existentes, 
lo que permite que los loggers predeterminados sigan funcionando junto con los que definas.
* Un "handler" define cómo y dónde se almacenarán los logs. En este caso, tienes uno que guarda los errores en un archivo:
file: Especificas un manejador que guarda los errores en un archivo.
        level: 'ERROR': Solo se registran mensajes de nivel de error o superior (advertencias no se guardan, solo errores).
        class: 'logging.FileHandler': El tipo de manejador que escribe los logs en un archivo.
        filename: La ubicación del archivo de logs. En este caso, los errores se almacenarán en BASE_DIR/logs/django_errors.log. Si el directorio logs no existe, tendrás que crearlo manualmente.

* Aquí defines los loggers, que son los que efectivamente registran los eventos:
 'django': Este es el logger predeterminado de Django.
        handlers: ['file']: Indica que utilizará el manejador que acabas de definir.
        level: 'ERROR': Solo los eventos de nivel ERROR se registrarán.
        propagate: True: Esto permite que el evento también se registre en cualquier otro logger superior que haya sido definido. 
* La configuración define un manejador (file) que guarda los errores (nivel ERROR) en un archivo llamado django_errors.log dentro del directorio logs.
### mkdir logs

### mkdir media
En muchos entornos de producción, las aplicaciones web necesitan escribir en directorios específicos, como media para archivos cargados. Si los permisos de las carpetas no están configurados correctamente, la aplicación puede fallar al intentar escribir o acceder a esos archivos.
Por ejemplo, si el usuario bajo el cual corre tu servidor web (como www-data en servidores con Nginx o Apache) no tiene permisos de escritura en la carpeta media, la aplicación no podrá descargar ni guardar las imágenes.
Configuración de permisos en sistemas operativos:

    Es recomendable asegurarse de que el sistema de archivos permita que la aplicación escriba en la carpeta media sin comprometer la seguridad general. En Linux, esto puede manejarse con comandos como chmod y chown.
    Ejemplo: sudo chown -R www-data:www-data /ruta/a/tu/proyecto/media y sudo chmod -R 755 /ruta/a/tu/proyecto/media permiten que el servidor web tenga control sobre esa carpeta.

    ¿estás desplegando la aplicación en un servidor o piensas hacerlo, esta es una observación importante a tener en cuenta.?
### 

10. logica de views.py (pongo comentarios, documentacion etc ... )
###
pathlib.Path es una herramienta poderosa y versátil que ayuda a escribir código más limpio y seguro en proyectos Django. Al utilizar pathlib,se adopta una de las mejores prácticas de desarrollo en Python.
-- Mayor legibilidad
-- Reduce la posibilidad de errores comunes al trabajar con rutas.
-- Integración con Django, se alinea perfectamente con la filosofía y facilita la configuración de rutas en el proyecto.
-- Funcionalidades avanzadas: Ofrece métodos para crear directorios, resolver rutas absolutas, comprobar existencia de archivos, etc.

11. Configurar URLs en Django
-- instagram_posts/urls.py, define la URL para acceder a la API que descargará las publicaciones:
* Establece que cuando un usuario escriba una URL como http://tudominio/get-posts/instagram, Django buscará en esta lista de patrones de URL y encontrará una coincidencia con el patrón que acabamos de definir. A continuación, llamará a la función get_instagram_posts y le pasará el valor de account (en este caso, "instagram") como argumento.
* La función get_instagram_posts es la encargada de realizar la lógica de la aplicación, es decir, descargar las publicaciones de Instagram para la cuenta especificada en la URL. Esta función interactúa con la API de Instagram utilizando la librería instaloader y devuelve una respuesta en formato JSON con la información de las publicaciones.

-- backend/urls.py Incluye las URLs en el archivo principal de URLs:
* Acceder al panel de administración de Django en la ruta /admin/.
* Acceder a las funcionalidades de la aplicación instagram_posts usando el prefijo /api/. Por ejemplo, si tienes una URL definida en instagram_posts/urls.py como path('get-posts/<str:account>/', get_instagram_posts), la ruta completa para acceder a esa funcionalidad sería /api/get-posts/<str:account>/.
* Servir archivos estáticos de la aplicación (por ejemplo, imágenes descargadas de Instagram) desde la ubicación especificada en settings.MEDIA_ROOT.

12. Probar que esto funciona
por si acaso hago: y no da error.
python manage.py makemigrations
python manage.py migrate

# Test 
* pruebas unitarias => python manage.py test
Mocking (unittest.mock): Se usa para simular el comportamiento de instaloader.Profile.from_username y generar un error específico (en este caso, una excepción que simula un perfil inexistente).
Captura de logs (assertLogs): Esto captura los logs de nivel ERROR y verifica que el mensaje de error se haya registrado correctamente.
Verificación: Finalmente, comprueba que el error se haya registrado en el logger correctamente.
 # hago dos veo funciona (lo doy por hecho)
* pruebas postman => python manage.py runserver y funciona.

13. Me pongo a mejorar el codigo con cosas que me pide el cliente, por ahora trabajo en views.py
* Verificación de la foto de perfil: Se verifica la última actualización de la foto de perfil antes de descargarla nuevamente.
* Manejo de errores en get_instagram_posts: Ahora se devuelve un código de estado HTTP 500 con un mensaje genérico en caso de error.
* Limpieza de archivos antiguos: Se ha creado una nueva tarea asíncrona clean_old_files para eliminar archivos de publicaciones que ya no existen en la base de datos.

# configuramos celery => pip install celery
*La tarea de descargar las imágenes de Instagram se ejecuta en segundo plano, lo que evita que los usuarios tengan que esperar a que se complete la descarga.
Actualizar la base de datos: Los datos de las publicaciones de Instagram se guardan en la base de datos de forma asíncrona.
La tarea de eliminar archivos antiguos se ejecuta de forma periódica, lo que ayuda a mantener limpio el almacenamiento.

### paro con lo de celery porque nome dara el tiempo

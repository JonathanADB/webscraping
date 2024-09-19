"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importa el panel de administración de Django.
from django.conf import settings # Importa la variable settings que contiene la configuración de tu proyecto.
from django.conf.urls.static import static #Importa la función static para servir archivos estáticos.
from django.urls import path, include #Importa las funciones path e include para definir patrones de URL e incluir rutas de otras aplicaciones.


#Define una lista donde se almacenan todos los patrones de URL principales del proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram-posts/', include('instagram_posts.urls')),
    #path('api/', include('instagram_posts.urls')),
    #estamos agregando un nuevo patrón de URL a la lista urlpatterns que se 
    # encarga de servir los archivos estáticos de nuestra aplicación. 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # función de Django que se utiliza para servir archivos estáticos 




#settings.MEDIA_URL: Es la URL base para acceder a los archivos estáticos.
#settings.MEDIA_ROOT: Es el directorio en el sistema de archivos donde se almacenan los archivos estáticos.

""" ¿Siguiente paso?

Seguridad: Revisar la seguridad de la API para protegerla de accesos no autorizados.
    Optimización: Optimizar el rendimiento de la API para manejar eficientemente las solicitudes.
   ** Documentación: Agregar documentación al código para facilitar su comprensión por otros desarrolladores.
"""

   

